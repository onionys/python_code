#!/usr/bin/env python3

import tkinter as tk

vv={}

def ok():
    strVar = vv['opt']
    print( "you now select : %s" % strVar.get() )


if __name__ == "__main__":
    root = tk.Tk()

    vv['opt']= tk.StringVar(root)
    vv['opt'].set('one')

    options = ("one","two","three", "four","five")
    opMenu = tk.OptionMenu(root, vv['opt'], *options)

    opMenu.config(font=("Times",36))
    opMenu['menu'].config(font=("Times",36))
    opMenu.grid(row=0,column=0)
    
    button = tk.Button(master=root, text="ok",command=ok,font=("Times",36))
    button.grid(row=1,column=0)
    vv['button']= button
    
    tk.mainloop()
