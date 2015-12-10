#!/usr/bin/env python

import Tkinter as tk
from random import randint

_x = 0
_y = 0

can = ""

def pressed():
    global _x,_y
    can.create_line(_x,_y, _x + 100, _y + 100)
    can.create_polygon(_x,_y,_x+10,_y,_x+10,_y+10,_x+50,_y+10)
    _x = randint(1,200)
    _y = randint(1,200)


if __name__=="__main__":
    root = tk.Tk()
    can = tk.Canvas(root, bg="blue", height=300, width=300)
    can.grid(row=0,column=0)
    btn = tk.Button(master=root, text="press me",width=5,height=3,font=("Times",35),command=pressed)
    btn.grid(row=1,column=0,sticky=tk.W+tk.E+tk.N+tk.S)
    root.mainloop()
