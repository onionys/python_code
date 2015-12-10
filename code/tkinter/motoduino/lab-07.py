#!/usr/bin/env python3

import socket
import threading
from time import sleep




class s4aWeb(object):
    def __init__(self):
        self.pin_outputs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # dev id : 4 ~ 13
        self.pin_inputs =  [0,0,0,0,0,0,0,0,0,0,0] # analog 0 ~ 5
        self.count = 0
        self.system_run = True

    def pack_to_data(self,data):
        dev_id = (data[0] & 0b01111000) >> 3
        dev_val = ((data[0] & 0b00000111 ) << 7) | (data[1] & 0b01111111)
        return (dev_id, dev_val)

    def data_to_pack(self,dev_id,dev_val):
        data = [0,0]
        data[0] = 0b10000000 | ((dev_id & 0b00001111) << 3) | ( ( dev_val >> 7 ) & 0b00000111 )
        data[1] = ( 0b0001111111 & dev_val ) 
        return bytes([data[0],data[1]])

    def set_dev(self,dev_id,dev_val):
        if((dev_val >= 0) and (dev_val < 1024)):
            self.pin_outputs[dev_id] = int(dev_val)
    
    def handle_data(self,data):
        i= 0
        length = len(data)
        if(data[i] & 0b10000000):
            pass
        else:
            i+=1
        while(i<length):
            try:
                dev_id , dev_val = pack_to_data(data[i:i+2])
                self.pin_inputs[dev_id] = dev_val
                i+=2
            except:
                break

    def sock_loop(self):
        address = ('',12345)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(address)
        while(True):
            data, addr = s.recvfrom(80)
            self.handle_data(data)
            data = b''
            for i in range(4,14):
                data += self.data_to_pack( i , self.pin_outputs[i] )
            s.sendto(data, addr)

    def start(self):
        self.th = threading.Thread(target=self.sock_loop,args=())
        self.th.start()

    def up(self):
        self.set_dev(5,255)
        self.set_dev(6,255)
        self.set_dev(7,0)
        self.set_dev(8,0)
        
    def stop(self):
        self.set_dev(5,0)
        self.set_dev(6,0)
        self.set_dev(7,0)
        self.set_dev(8,0)
    
    def turn_left(self):
        self.set_dev(5,255)
        self.set_dev(6,255)
        self.set_dev(7,0)
        self.set_dev(8,1)
    
    def turn_right(self):
        self.set_dev(5,255)
        self.set_dev(6,255)
        self.set_dev(7,1)
        self.set_dev(8,0)
    
    def down(self):
        self.set_dev(5,255)
        self.set_dev(6,255)
        self.set_dev(7,1)
        self.set_dev(8,1)




if __name__ == "__main__":
    ss = s4aWeb()
    ss.start()

    while(True):
        cmd = input().split()
        ss.set_dev(int(cmd[0]), int(cmd[1]))
