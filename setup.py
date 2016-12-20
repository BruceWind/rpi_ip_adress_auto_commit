#!/usr/bin/env python3
# @weizongwei5
# Launch python script on startup
###############################################################################

import getpass
import os


username = getpass.getuser()
config=".config"
autostart="autostart"

sp="/"

userhome = "/home/"+ username 
config_dir = userhome + sp + config
autostart_dir = config_dir + sp + autostart

os.chdir(home)

os.system("mkdir "+config)
os.system("mkdir "+autostart)



