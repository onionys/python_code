#!/usr/bin/env python3

import socket
from time import sleep
from threading import Thread

target_ip = "192.168.0.4"
target_port = 8001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
system_run = True

def handle_recv():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("192.168.0.7",8001))
    while(system_run):
        msg,addr = s.recvfrom(1024)
        print("from:",addr, ":msg:", msg.decode())

th = Thread(target=handle_recv)
th.start()


print("input message:")
msg = input()
sock.sendto( msg.encode(), (target_ip, target_port) )

for i in range(10):
    sleep(1)
    sock.sendto( "hi".encode(), (target_ip, target_port) )

system_run = False
