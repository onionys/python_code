#!/usr/bin/env python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("192.168.0.4",8001))

while(True):
    msg, addr = sock.recvfrom(1024)
    print("addr: ", addr)
    print("msg: ", msg.decode())

    msg = "I received your msg: " + msg.decode()
    sock.sendto(msg.encode(),addr)
