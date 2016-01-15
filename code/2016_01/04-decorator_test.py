#!/usr/bin/env python3

def mk_func(fn):

    def _f():
        fn()
        print("World")
    return _f


def mk_div(fn):

    def _f(*arg,**args):
        print("<div>")
        fn(*arg,**args)
        print("</div>")
    return _f


from time import time
from time import sleep

def show_time_cost(fn):
    def _f(*args,**dict):
        time_stamp = time()
        fn(*args,**dict)
        now = time()
        print("---------------------------")
        print("function name: ",fn.__name__)
        print("time cost: {:.5}sec".format(now - time_stamp))
        print("---------------------------")
    return _f

@show_time_cost
def hello():
    print("hello")
    sleep(1)
    print("world")

hello()
#hello = mk_div(hello)

