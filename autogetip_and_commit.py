
#!/usr/bin/env python3
# Note:
#   Please save this as diagnostic_firstname.txt
#       (replace firstname w/ yours)
#   Do not edit lines that say: "# Last line in ____"
###############################################################################
# Imports  # there will only be two imports added here.

import socket
import os


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

ip_adress = get_ip_address() # current ip 
cur_dir=os.getcwd() # current dir 

print(ip_adress)
os.chdir("/home/wei/git/rpi_ip_adress_auto_commit") # change dir

fp = open('ip.txt', 'w') 
fp.write(ip_adress) 
fp.close()

os.system('git add -A')
os.system('git commit -m \'ip commit\'')
os.system('git push')




