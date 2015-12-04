#!/usr/bin/env python3

import tkinter as tk

vv = {}

def btn_call_back():
    btn = vv['btn']
    if(btn.sw == 'on'):
        btn.sw = 'off'
        btn.config(image=vv['btn_img_off'])
    else:
        btn.sw = 'on'
        btn.config(image=vv['btn_img_on'])

if __name__ == "__main__":
    root = tk.Tk()

    button_img_on = tk.PhotoImage(file='./btn_sw_on.gif')
    button_img_off = tk.PhotoImage(file='./btn_sw_off.gif')
    vv['btn_img_on'] = button_img_on
    vv['btn_img_off'] = button_img_off

    button = tk.Button(master=root,text="hello", command=btn_call_back, image=vv['btn_img_on'])
    button.sw = "on"
    button.grid(row=0,column=0)
    vv['btn']= button

    root.mainloop()
