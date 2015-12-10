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

    vv['btn_img_on'] = tk.PhotoImage(file='./pic/btn_sw_on.gif')
    vv['btn_img_off']= tk.PhotoImage(file='./pic/btn_sw_off.gif')

    vv['btn'] = tk.Button(master=root,text="hello")
    vv['btn'].config(command=btn_call_back)
    vv['btn'].config(image=vv['btn_img_on'])
    vv['btn'].sw = 'on'
    vv['btn'].grid(row=0,column=0)

    root.mainloop()
