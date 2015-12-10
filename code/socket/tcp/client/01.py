#!/usr/bin/env python3

import socket
from time import sleep

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect( ("192.168.0.4", 8001) )


msg = sock.recv(1024)
print("from server: ", msg.decode())

print("wait to close")
sleep(10)
print("close")
sock.close()
