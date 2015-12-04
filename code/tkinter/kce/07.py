#!/usr/bin/env python
import Tkinter as tk
from threading import Thread
from time import sleep
import random

var = {}

def kce_loop():
    while(var["run"]):
        sleep(1)
        var["PV"].set(int(random.randint(1,100)))

def button_stop():
    var["run"] = False

if __name__=="__main__":
    root = tk.Tk()
    PV_tag_label = tk.Label(master=root,text="PV",width=6,fg='red',bg='black',font=("Times",36)).grid(row=0,column=0)
    SV_tag_label = tk.Label(master=root,text="SV",width=6,fg='red',bg='black',font=("Times",36)).grid(row=1,column=0)
    var["PV"] = tk.StringVar()
    PV_val_label = tk.Label(master=root,textvariable=var["PV"],width=6,fg='red',bg='black',font=("Times",36)).grid(row=0,column=1)
    var["SV"] = tk.StringVar()
    PV_val_label = tk.Label(master=root,textvariable=var["SV"],width=6,fg='red',bg='black',font=("Times",36)).grid(row=1,column=1)
    var["PV"].set("0")
    var["SV"].set("0")
    var["run"] = True
    STOP_btn = tk.Button(master=root,text="STOP",font=("Time",36),command=button_stop).grid(row=2,column=0)

    th = Thread(target=kce_loop,args=())
    th.start()

    root.mainloop()
