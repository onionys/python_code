#!/usr/bin/env python3

from threading import Thread
from multiprocessing import Process, Queue
from time import sleep

system_run = True

def run1():
    global system_run
    i=0
    while(system_run):
        i+= 1
        sleep(1.2)
        print("run1", i)
        if i >= 5:
            system_run = False
    print("run1 stop")

def run2():
    global system_run
    i = 0
    while(system_run):
        i+= 1
        sleep(1)
        print("\t\trun2", i)
        if i >= 10:
            system_run = False
    print("run2 stop")

p1 = Process(target=run1)
p2 = Process(target=run2)

p1.start()
p2.start()

#sleep(10)

#p1.join()
#p2.join()

