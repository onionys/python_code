#!/usr/bin/env python3

from threading import Thread
from time import sleep

system_run = True

def run1():
    i=0
    while(system_run):
        i+= 1
        sleep(1.2)
        print("run1", i)

def run2():
    i = 0
    while(system_run):
        i+= 1
        sleep(1)
        print("run2", i)

th1 = Thread(target=run1)
th2 = Thread(target=run2)

th1.start()
th2.start()

print("000")
sleep(10)
system_run = False

th1.join()
th2.join()

