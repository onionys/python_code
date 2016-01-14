#!/usr/bin/env python3

from time import sleep

def g_pi_tain(n):
    g_pi = []

    for i in range(n):
        sleep(1)
        g_pi.append("gpi")
        print("gpi ok.", i)

    return g_pi


def g_pi_tain2(n):
    for i in range(n):
        sleep(1)
        print("gpi ok.", i)
        yield "gpi" + str(i)
        print("start another gpi")


a = g_pi_tain2(10)







print("===="*20)
a = g_pi_tain2(10)
b = g_pi_tain2(10)

for i in range(10):
    print(next(a))
    print(next(a))
    print(next(b))

