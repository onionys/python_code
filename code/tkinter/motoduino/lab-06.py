#!/usr/bin/env python3
import socket


def pack_to_data(data):
    dev_id = (data[0] & 0b01111000) >> 3
    dev_val = ((data[0] & 0b00000111 ) << 7) | (data[1] & 0b01111111)
    return (dev_id, dev_val)


def handle_data(data):
    i= 0
    length = len(data)
    if(data[i] & 0b10000000):
        pass
    else:
        i+=1
    while(i<length):
        try:
            print(pack_to_data(data[i:i+2]))
            i+=2
        except:
            break



address = ('',12345)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)

while(True):
    print('--')
    data, addr = s.recvfrom(1024)
    handle_data(data)
