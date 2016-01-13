#!/usr/bin/env python3

from threading import Thread
from time import sleep
from time import time
from queue import Queue


class Gpi:

    def __init__(self,name):
        self.name = name
        self.system_run = True
        self.order = Queue()
        self.output = Queue()
        self.busy = False

    def run(self):
        while(self.system_run):
            if(not self.order.empty()):
                self.order.get()
                print("{0}雞排攤得到一份訂單\n".format(self.name))
                self.busy = True
                sleep(1)
                self.busy = False
                print("{0}雞排攤:炸好1份{0}雞排\n".format(self.name))
                self.output.put("{}雞排".format(self.name))
            else:
                print(self.name,"雞排攤,正在休息....")
            sleep(1)

        print("生意冷清{}雞排攤老闆抱怨沒訂單...".format(self.name))


    def start(self):
        self.th = Thread(target=self.run)
        self.th.start()

    def stop(self):
        self.system_run = False

    def join(self):
        self.th.join()
        print("{}雞排攤因為沒訂單收攤了".format(self.name))




def main():
    n_gpi = input("先生您要幾份雞排?")
    n_gpi = int(n_gpi)
    n_order = n_gpi
    gpi_array = []

    gpi1= Gpi("開元社")
    gpi1.start()

    while True:
        if(not gpi1.busy):
            n_order -= 1
            gpi1.order.put("訂單")

        if(not gpi1.output.empty()):
            gpi_array.append(gpi1.output.get())

        if(len(gpi_array) == n_gpi):
            print(gpi_array)
            break


    gpi1.stop()


if __name__ == "__main__":
    main()
