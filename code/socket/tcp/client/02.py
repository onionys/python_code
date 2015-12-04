#!/usr/bin/env python3

import socket
from time import sleep
count = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect( ("192.168.0.4", 8001) )

sock.send("Hi".encode())
while(True):
    if(count <= 50): 
        msg = sock.recv(1024)
        print("from server: ", msg.decode())
        sleep(1)
        
        sock.send("Hi".encode())
        count += 1
    else:
        break

sock.close()
