#!/usr/bin/env python3
# @weizongwei5
# Launch python script on startup
###############################################################################

import getpass
import os
import string
import time

sp="/"
etc_dir="/etc"
rclocal="rc.local"

username = raw_input("Please input your name:\n")
userhome = "/home/"+ username


git_file_path=userhome + sp + "git" + sp + "rpi_ip_adress_auto_commit/autogetip_and_commit.py"
line_str="python "+git_file_path +" &"


os.chdir(etc_dir)

if os.geteuid() == 0:
    # print (len(ainfo)-1)
    for line in open(rclocal):
        if(line == line_str):
            is_contain=True;

        #
        #     print "+++++++"+line_str+"\n"+line
        # else:
        #     print (line.__len__()+" "+line_str.__len__())
        #     print line_str + "\n" + line

    if(not is_contain):
        pass # TODO write rclocal file




else:
    print ("\n\tOnly root can run this script\n")

