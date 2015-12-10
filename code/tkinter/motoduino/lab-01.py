#!/usr/bin/env python3

import serial

ser = serial.Serial("/dev/ttyUSB0",38400,8,'N',1)

while(True):
    print(ser.read(16))

