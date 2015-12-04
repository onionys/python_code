#!/usr/bin/env python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

sock.bind(('192.168.0.4',8001))
sock.listen(5)

s, addr = sock.accept()

##
s.send("wellcome.".encode())

msg = s.recv(1024)
print("client: ", msg.decode())

s.close()
