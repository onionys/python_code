#!/usr/bin/env python3
import time
import tkinter as tk
from threading import Thread


vv = {}


def myloop():
    count = 0
    for i in range(10):
        time.sleep(1)
        count += 1
        vv['label02'].config(text= str(count) )



if __name__=="__main__":
    root = tk.Tk()

    label01 = tk.Label(master=root, text = "Hello", font=("Times",36) )
    label01.grid(row=0,column=0)

    label02  = tk.Label(master=root,text="TEST",width=5,font=("Times",36))
    label02.grid(row=0,column=1)
    vv['label02'] = label02

    th = Thread(target=myloop)
    th.start()

    root.mainloop()
