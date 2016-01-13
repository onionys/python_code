#!/usr/bin/env python3

from threading import Thread
from time import sleep

# Simple Thread Example 

# the function you want to run as a thread...
def gpi(n):
    for i in range(n):
        print("雞排攤:炸好第{}份雞排".format(i+1))
        sleep(1)

## make 
gpi_th = Thread(target=gpi, args=(10,))

## start 
gpi_th.start()

## join
gpi_th.join()
