#!/usr/bin/env python3
import tkinter as tk

if __name__=="__main__":
    root = tk.Tk()


    label01 = tk.Label(master=root, text = "Hello", font=("Times",36) )
    label01.grid(row=0,column=0)

    label02  = tk.Label(master=root,text="0",font=("Times",36))
    label02.grid(row=0,column=1)
    label02.config(text='TEST')


    root.mainloop()
