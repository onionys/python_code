#!/usr/bin/env python3

import subprocess

def get_ip_rpi():
    msg = subprocess.check_output("ifconfig".split()).decode()
    data = [line for line in msg.split('\n') if 'inet addr' in line]
    ip_list = [line.split()[1][5:] for line in data]
    return ip_list

# please run this function in windows
def get_ip_win():
    msg = subprocess.check_output("ipconfig".split())
    msg = msg.decode('big5')
    data = [line.strip() for line in msg.split('\n') if "IPv4" in line]
    return [i.split()[-1] for i in data]

print(get_ip_rpi())

