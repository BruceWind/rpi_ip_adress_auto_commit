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





