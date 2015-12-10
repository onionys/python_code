#!/usr/bin/env python3

import socket
from time import sleep

target_ip = "192.168.0.4"
target_port = 8001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


print("input message:")
msg = input()
sock.sendto( msg.encode(), (target_ip, target_port) )
