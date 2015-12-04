#!/usr/bin/env python3

import tkinter

if __name__ == "__main__":
    print("Hello World. This is the first example of Tkinter.")
    root = tkinter.Tk()
    label = tkinter.Label(master=root,text="hello label").pack()
    #label.grid(row=0,column=0)
    root.mainloop()
