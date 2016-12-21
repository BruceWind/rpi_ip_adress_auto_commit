# -*- coding: utf-8 -*-
# @weizongwei5
###############################################################################


import socket
import os
import getpass
import time
import urllib2


def clear_all_cache_file():
    os.system("rm *~")


### ping 的过程仅仅为了解决 偶现的 github 域名解析问题的情况
def ping_githost():
    os.system("ping -c 2 -w 3 github.com")  # ping github count = 2 ,timeout = 3


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def get_current_time():
    ISOTIMEFORMAT = '%Y-%m-%d %X'
    return time.strftime(ISOTIMEFORMAT, time.localtime())


def internet_on():
    try:
        urllib2.urlopen('http://baidu.com', timeout=1)
        return True
    except urllib2.URLError as err:
        print "\tnetwork not connected!!\n\t网络没连接！！\n"
        return False


# one minute countdown....
i = 1
while (i <= 15):
    is_valid = (internet_on())
    if (is_valid):
        i = 15
    time.sleep(4)
    i += 1

# need some field
username = getpass.getuser()
separator = "/"

if (is_valid):
    print "start ping ....."
    ping_githost()
    # time.sleep(2)
    print "get ip......"
    ip_adress = get_ip_address()  # current ip
    # time.sleep(2)
    cur_dir = os.getcwd()  # current dir
    git_dir = "/home/" + username + "/git"

    print("\t IP and Time:" + ip_adress + " " + get_current_time() + "\n")
    print "move dir to gitdir ....."
    os.chdir(git_dir + separator + "rpi_ip_adress_auto_commit")  # change dir
    # time.sleep(2)

    print "git pull....."
    os.system('git pull')
    # time.sleep(2)


    print "clear cache file....."
    clear_all_cache_file()

    print "write ip to ip.txt"
    fp = open('ip.txt', 'w')
    fp.write(ip_adress + " " + get_current_time() + "\n")
    fp.close()
    time.sleep(1)

    print "git commit  push...."
    os.system('git add -A')

    os.system("git commit -m \'ip commit on " + socket.gethostname() + "\'")

    time.sleep(2)
    os.system('git push')

    print "git push finish!!\n\t next seond is will exit!"
    time.sleep(8)
else:
    print('can\'t be  commit to github!\n\t无法提交到github!')
