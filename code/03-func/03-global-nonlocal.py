#!/usr/bin/env python3

x = "hello"
def fun(z=10):
    x = z

    def getX():
        return x

    def setX(n):
        nonlocal x
        x = n

    def setX_(n):
        global x
        x = n
    return(getX,setX)

getX, setX = fun()
getX1, setX1 = fun(1000000)

print(getX())
print(getX1())
setX(200)
setX1(500)
print(getX())
print(getX1())
