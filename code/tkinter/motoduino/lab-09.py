#!/usr/bin/env python3

import tkinter as tk
import socket
import threading
from time import sleep


s4a_list = []




class s4aWeb(object):

    def __init__(self):
        self.pin_outputs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # dev id : 4 ~ 13
        self.pin_inputs = [0,0,0,0,0,0,0,0,0,0,0] # analog 0 ~ 5
        self.count = 0
        self.ip = ''
        self.system_run = True

    def pack_to_data(self,data):
        dev_id  = (data[0] & 0b01111000) >> 3
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



    def main_loop(self):
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
        self.th = threading.Thread(target=self.main_loop,args=())
        self.th.start()


    def up(self):
        self.set_dev(5,200)
        self.set_dev(6,200)
        self.set_dev(7,0)
        self.set_dev(8,0)
        
    def stop(self):
        self.set_dev(5,0)
        self.set_dev(6,0)
        self.set_dev(7,0)
        self.set_dev(8,0)
    
    def turn_left(self):
        self.set_dev(5,155)
        self.set_dev(6,155)
        self.set_dev(7,0)
        self.set_dev(8,1)
    
    def turn_right(self):
        self.set_dev(5,155)
        self.set_dev(6,155)
        self.set_dev(7,1)
        self.set_dev(8,0)
    
    def down(self):
        self.set_dev(5,200)
        self.set_dev(6,200)
        self.set_dev(7,1)
        self.set_dev(8,1)





def main_loop():
    address = ("",12345)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(address)

    s1 = s4a_list[0]
    s2 = s4a_list[1]

    while(True):
        data, addr = sock.recvfrom(80)


        if addr[0] == s1.ip:
            s1.handle_data(data)
            data = b''
            for i in range(4,14):
                data += s1.data_to_pack(i,s1.pin_outputs[i])
            sock.sendto(data,addr)

        elif addr[0] == s2.ip:
            s2.handle_data(data)
            data = b''
            for i in range(4,14):
                data += s2.data_to_pack(i,s2.pin_outputs[i])
            sock.sendto(data,addr)

        elif (addr[0] != s1.ip) and (not s1.ip) :
            print('s1 ip',addr[0])
            s1.ip = addr[0]

        elif (addr[0] != s2.ip) and (not s2.ip) :
            print('s2 ip', addr[0])
            s2.ip = addr[0]



if __name__ == "__main__" :

    s1 = s4aWeb()
    s2 = s4aWeb()
    s4a_list.append(s1)
    s4a_list.append(s2)
    th = threading.Thread(target=main_loop,args=())
    th.start()

    root = tk.Tk()

    ## 
    ## define button panel 1
    ##
    up_btn = tk.Button(master=root, text='UP',   command=s1.down,width=10,height=5,font=('Time',15))
    down_btn = tk.Button(master=root, text='DOWN', command=s1.up,width=10,height=5,font=('Time',15))
    left_btn =  tk.Button(master=root, text='TURN LEFT', command=s1.turn_left,width=10,height=5,font=('Time',15))
    right_btn = tk.Button(master=root, text='TURN RIGHT', command=s1.turn_right,width=10,height=5,font=('Time',15))
    stop_btn =  tk.Button(master=root, text='STOP', command=s1.stop,width=10,height=5,font=('Time',15))

    up_btn.grid(row=0,column= 1, sticky=tk.W + tk.E + tk.S + tk.N)
    down_btn.grid(row=2,column=1, sticky=tk.W + tk.E + tk.S + tk.N)
    left_btn.grid(row=1,column=0, sticky=tk.W + tk.E + tk.S + tk.N)
    right_btn.grid(row=1,column=2, sticky=tk.W + tk.E + tk.S + tk.N)
    stop_btn.grid(row=1,column=1, sticky=tk.W + tk.E + tk.S + tk.N)

    ## 
    ## define button panel 2
    ##
    up_btn =    tk.Button(master=root, text='UP',   command=s2.down,width=10,height=5,font=('Time',15))
    down_btn =  tk.Button(master=root, text='DOWN', command=s2.up,width=10,height=5,font=('Time',15))
    left_btn =  tk.Button(master=root, text='TURN LEFT', command=s2.turn_left,width=10,height=5,font=('Time',15))
    right_btn = tk.Button(master=root, text='TURN RIGHT', command=s2.turn_right,width=10,height=5,font=('Time',15))
    stop_btn =  tk.Button(master=root, text='STOP', command=s2.stop,width=10,height=5,font=('Time',15))

    up_btn.grid(row=0,column= 3+1, sticky=tk.W + tk.E + tk.S + tk.N)
    down_btn.grid(row=2,column=3+1, sticky=tk.W + tk.E + tk.S + tk.N)
    left_btn.grid(row=1,column=3+0, sticky=tk.W + tk.E + tk.S + tk.N)
    right_btn.grid(row=1,column=3+2, sticky=tk.W + tk.E + tk.S + tk.N)
    stop_btn.grid(row=1,column=3+1, sticky=tk.W + tk.E + tk.S + tk.N)

    root.mainloop()
