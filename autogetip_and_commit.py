#!/usr/bin/env python3
# @weizongwei5
###############################################################################


import socket
import os
import getpass
import time
import urllib2


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def get_current_time():
    ISOTIMEFORMAT ='%Y-%m-%d %X'
    return time.strftime(ISOTIMEFORMAT, time.localtime())

def is_connected_network():
    return  os.system('ping 8.8.8.8 -c 2')


def internet_on():
    try:
        urllib2.urlopen('http://baidu.com', timeout=1)
        return True
    except urllib2.URLError as err:
        return False

i = 1
while(i <= 10):
    # if(is_connected_network()==1):
    #     i=11
    is_valid=(internet_on())
    print (returns)
    print i
    time.sleep(3)
    i += 1

username = getpass.getuser()
separator = "/"

ip_adress = get_ip_address()  # current ip
cur_dir = os.getcwd()  # current dir
git_dir = "/home/" + username + "/git"

print(ip_adress+" "+ get_current_time()+"\n")
os.chdir(git_dir + separator + "rpi_ip_adress_auto_commit")  # change dir

os.system('git pull')

fp = open('ip.txt', 'w')
fp.write(ip_adress +" "+ get_current_time()+"\n")
fp.close()

os.system('git add -A')

os.system("git commit -m \'ip commit on " + socket.gethostname() + "\'")

os.system('git push')
