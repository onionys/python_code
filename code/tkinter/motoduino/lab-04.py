#!/usr/bin/env python3

import tkinter as tk
import s4a

system_run = True
cars=[]

def up_btn_callback():
    cars[0].up()
    
def stop_btn_callback():
    cars[0].stop()

def turn_left_btn_callback():
    cars[0].turn_left()

def turn_right_btn_callback():
    cars[0].turn_right()

def down_btn_callback():
    cars[0].down()

def offline():
    cars[0].shutdown()

if __name__=="__main__":
    car = s4a.s4a('/dev/ttyUSB0')
    car.start()
    cars.append(car)

    root = tk.Tk()
    up_btn =    tk.Button(master=root, text='UP', command=up_btn_callback,width=10,height=5,font=('Time',15))
    down_btn =  tk.Button(master=root, text='DOWN', command=down_btn_callback,width=10,height=5,font=('Time',15))
    left_btn =  tk.Button(master=root, text='TURN LEFT', command=turn_left_btn_callback,width=10,height=5,font=('Time',15))
    right_btn = tk.Button(master=root, text='TURN RIGHT', command=turn_right_btn_callback,width=10,height=5,font=('Time',15))
    stop_btn = tk.Button(master=root, text='STOP', command=stop_btn_callback,width=10,height=5,font=('Time',15))
    system_off = tk.Button(master=root, text='disconnect', command=offline,width=10,height=5,font=('Time',15))

    up_btn.grid(row=0,column= 1, sticky=tk.W + tk.E + tk.S + tk.N)
    down_btn.grid(row=2,column=1, sticky=tk.W + tk.E + tk.S + tk.N)
    left_btn.grid(row=1,column=0, sticky=tk.W + tk.E + tk.S + tk.N)
    right_btn.grid(row=1,column=2, sticky=tk.W + tk.E + tk.S + tk.N)
    stop_btn.grid(row=1,column=1, sticky=tk.W + tk.E + tk.S + tk.N)
    system_off.grid(row=2,column=2, sticky=tk.W + tk.E + tk.S + tk.N)

    root.mainloop()
