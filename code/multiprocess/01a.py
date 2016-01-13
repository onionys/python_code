#!/usr/bin/env python3

from multiprocessing import Pool
from time import sleep


def hand_func(x):
    sleep(0.01)
    return x*x





def main():
    data = [i for i in range(1000)]
    p = Pool(4)
    res = p.map(hand_func,data)
    print(res)


def main2():
    data = [i for i in range(1000)]
    with Pool(4) as p:
        res = p.map(hand_func,data)
    print(res)


if __name__ == "__main__":
    main()
