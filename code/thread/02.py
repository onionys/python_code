#!/usr/bin/env python3

from threading import Thread
from time import sleep

# Simple Thread Example 

def gpi(n):
    for i in range(n):
        print("雞排攤:炸好第{}份雞排".format(i+1))
        sleep(1)
# 
def main():

    n_gpi = input("先生您要幾份雞排?")
    n_gpi = int(n_gpi)

    gpi_th = Thread(target=gpi, args=(n_gpi,))
    gpi_th.start()
    gpi_th.join()


if __name__ == "__main__":
    main()
