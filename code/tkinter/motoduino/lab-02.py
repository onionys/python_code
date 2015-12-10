#!/usr/bin/env python3

import serial

def pack_to_data(data):
    dev_id = (data[0] & 0b01111000) >> 3
    dev_val = ((data[0] & 0b00000111 ) << 7) | (data[1] & 0b01111111)
    return (dev_id, dev_val)

def data_to_pack(dev_id,dev_val):
    data[0] = 0b10000000|( dev_id<<3)|((dev_val>>7)&0b00000111)
    data[1] = (0b0001111111&dev_val) 
    return bytes([data[0],data[1]])


ser = serial.Serial('/dev/ttyUSB0',38400,8,'N',1)
inputs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

while(True):
    data = ser.read(2)
    if data[0] & 0b10000000:
        dev_id, dev_val = pack_to_data(data)
        inputs[dev_id] = dev_val
        print(inputs)
    else:
        data = ser.read()
