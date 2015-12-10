#!/usr/bin/env python3

import socket


## socket.AF_INET --> internet ipv4
## socket.SOCK_STREAM -> TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

## ("IP", PORT)
sock.bind(('192.168.0.4',8001))
sock.listen(5)

while(True):
    s, addr = sock.accept()
    s.send("wellcome".encode())
    while(True):
        try:
            msg = s.recv(1024)
            if(not msg):
                s.close()
                break
            print(msg.decode())
            s.send("hi.".encode())
        except:
            s.close()
            break
    
## close
s.close()
