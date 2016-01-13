#!/usr/bin/env python3

from multiprocessing import Process, Queue
from time import sleep


def myFunc(name):
    for i in range(10):
        print("process ",name)
        sleep(1)


if __name__ == "__main__":
    proc_array =[]

    for i in range(5):
        proc_array.append(Process(target=myFunc,args=("test" + str(i),)) )

    [i.start() for i in proc_array]

    [i.join() for i in proc_array]
