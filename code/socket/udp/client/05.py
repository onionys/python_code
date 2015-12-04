#!/usr/bin/env python3

import socket
from time import sleep

host_ip = "192.168.0.7"
host_port = 8001

target_ip = "192.168.0.4"
target_port = 8001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host_ip, host_port))

for i in range(10):
    msg = input("input message: ")
    sock.sendto( msg.encode(), (target_ip, target_port) )

    msg,addr = sock.recvfrom(1024)
    print("recv from ", addr, " : ", msg.decode())

