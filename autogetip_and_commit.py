#!/usr/bin/env python3
# @weizongwei5
###############################################################################


import socket
import os
import getpass

import time


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

time.sleep(5)

username=getpass.getuser()
separator="/"

ip_adress = get_ip_address() # current ip 
cur_dir=os.getcwd() # current dir 
git_dir="/home/"+ username +"/git"

print(ip_adress)
os.chdir(git_dir+separator+"rpi_ip_adress_auto_commit") # change dir


os.system('git pull')

fp = open('ip.txt', 'w') 
fp.write(ip_adress+"\n") 
fp.close()

os.system('git add -A')

os.system('git commit -m \'ip commit on raspberry"+socket.gethostname()+"\'')

os.system('git push')




