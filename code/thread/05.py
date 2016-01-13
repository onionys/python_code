#!/usr/bin/env python3

from threading import Thread
from time import sleep
from time import time


class Gpi:
    def __init__(self,name,count=0):
        self.name = name
        self.order = count

    def run(self):
        while(True):
            if(self.order):
                print("{0}雞排攤:炸好1份{0}雞排\n".format(self.name))
                self.order -= 1
            else:
                break
            sleep(len(self.name)/2)

        print("生意冷清{}雞排攤老闆抱怨沒訂單...".format(self.name))


    def start(self):
        self.th = Thread(target=self.run)
        self.th.start()

    def join(self):
        self.th.join()
        print("{}雞排攤因為沒訂單收攤了".format(self.name))




def main():
    n_gpi = input("先生您要幾份雞排?")
    n_gpi = int(n_gpi)

    a = n_gpi // 2
    b = n_gpi - a

    gpi1= Gpi("開元社",a)
    gpi2= Gpi("號大",b)

    gpi1.start()
    gpi2.start()

    gpi1.join()
    gpi2.join()


if __name__ == "__main__":
    main()
