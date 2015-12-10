#!/usr/bin/env python3

import socket
from threading import Thread


## socket.AF_INET --> internet ipv4
## socket.SOCK_STREAM -> TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

## ("IP", PORT)
sock.bind(('192.168.0.4',8001))
sock.listen(1)


def handle_socket(sock):
    count = 0

    while(True):
        try:
            msg = sock.recv(1024)
            if(msg):
                print("client: ", msg.decode())
                count += 1
                msg = "%d\n" % count
                sock.send(msg.encode())
            else:
                break
        except:
            break


    sock.close()



while True:
    s, addr = sock.accept()
    print("accept a connection.")
    th = Thread(target=handle_socket,args=(s,))
    th.start()
