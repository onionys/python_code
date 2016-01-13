#!/usr/bin/env python3

from threading import Thread
from time import sleep


def gpi(name,n):
    for i in range(n):

        # make your program looked friendly.
        print("雞排攤{0}:炸好第{1}份{0}雞排\n".format(name,i+1))
        sleep(1)


def main():
    n_gpi = input("先生您要幾份雞排?")
    n_gpi = int(n_gpi)

    a = n_gpi // 2
    b = n_gpi - a

    # two different thread , the same function
    gpi_a_th = Thread(target=gpi, args=("號大",a))
    gpi_b_th = Thread(target=gpi, args=("開元社",b))

    gpi_a_th.start()
    gpi_b_th.start()

    gpi_a_th.join()
    gpi_b_th.join()


if __name__ == "__main__":
    main()
