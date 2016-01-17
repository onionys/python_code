#!/usr/bin/env python3


x = 1

def func():
    global x
    x = 100
    print(x)

def func_():
    print(x)


def error_func():
    print(x)
    x = 100



x = 1
#def mk_func_in_func(opt):
#    x = 10
#
#    def func1():
#        global x
#        print(x)
#        x = 100
#
#    def func2():
#        nonlocal x
#        print(x)
#        x = 10000
#
#    def get_X():
#        nonlocal x
#        print(x)
#
#    return func1 if opt else (func2,get_X)

def mk_func(opt):
    x = 10

    def func():
        nonlocal x
        print(x)
        x = 10000

    def getx():
        nonlocal x
        print(x)

    def getx2():
        print(x)

    return func,getx2

if __name__ == "__main__":
    t,getx = mk_func(False)
    t()
    getx()
    print(x)
    
