#!/usr/bin/env python3
import time
import tkinter as tk
from threading import Thread


vv = {}
vv["system_run"] = True


def myloop():
    count = 0
    while(True):
        time.sleep(1)
        if(vv['system_run']):
            count += 1
            vv['label02'].config(text="%d" % count)


def stop_count():
    if(vv["system_run"]):
        vv["system_run"] = False 
        vv['btn01'].config(text="RUN")
    else:
        vv["system_run"] = True
        vv['btn01'].config(text="STOP")


if __name__=="__main__":
    root = tk.Tk()

    label01 = tk.Label(master=root, text = "Hello", font=("Times",36) )
    label01.grid(row=0,column=0)

    label02  = tk.Label(master=root, text= "0", width=5, font=("Times",36))
    label02.grid(row=0,column=1)
    vv['label02'] = label02
    th = Thread(target=myloop)
    th.start()

    btn01 = tk.Button(master=root,text="STOP",font=("Time",36), command=stop_count)
    btn01.grid(row=2,column=0)
    vv['btn01'] = btn01

    root.mainloop()
