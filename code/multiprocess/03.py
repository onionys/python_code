#!/usr/bin/env python3

from multiprocessing import Process, Queue
from time import sleep

def num_put(q):
    for i in range(10):
        print("process num_put: put ", i)
        q.put("num:" + str(i))
        sleep(0.2)

def num_get(q):
    for i in range(10):
        print("process num_get: get ", q.get())
        sleep(0.5)

def main():
    q = Queue()
    p1 = Process(target=num_put,args=(q,))
    p2 = Process(target=num_get,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == "__main__":
    main()
