#!/usr/bin/env python
import Tkinter as tk
from threading import Thread
from time import sleep, time
import minimalmodbus
from tk_plot import tk_plot
import random

var = {}

def kce_loop():
    while(var["run"]):
        sleep(1)
        try:
            _pv = random.randint(1,100)
            _sp = 25
            var["PV"].set(_pv)
            var["SP"].set(_sp)
            var["plot"].add_data(time(),_pv)
        except:
            print "ERROR"
            var["PV"].set("ERROR")
            var["SP"].set("ERROR")

def button_stop():
    var["run"] = False

if __name__=="__main__":
    root = tk.Tk()
    PV_tag_label = tk.Label(master=root,text="PV",width=6,fg='red',bg='black',font=("Times",36)).grid(row=0,column=0)
    SP_tag_label = tk.Label(master=root,text="SP",width=6,fg='red',bg='black',font=("Times",36)).grid(row=1,column=0)
    var["PV"] = tk.StringVar()
    PV_val_label = tk.Label(master=root,textvariable=var["PV"],width=6,fg='red',bg='black',font=("Times",36)).grid(row=0,column=1)
    var["SP"] = tk.StringVar()
    SP_val_label = tk.Label(master=root,textvariable=var["SP"],width=6,fg='red',bg='black',font=("Times",36)).grid(row=1,column=1)
    var["PV"].set("0")
    var["SP"].set("0")
    var["run"] = True
    STOP_btn = tk.Button(master=root,text="STOP",font=("Time",36),command=button_stop).grid(row=2,column=0)
    kce_plot = tk_plot(master=root,row=0,col=2,rowspan=6,colspan=6,size=(6,6),dpi=100,interval=1000)
    var["plot"] = kce_plot

    th = Thread(target=kce_loop,args=())
    th.start()

    root.mainloop()
