#!/usr/bin/env python3
import tkinter as tk

if __name__=="__main__":
    root = tk.Tk()

    mylabel = tk.Label(master=root, text = "Hello", font=("Times",36) )
    mylabel.grid(row=0,column=0)

    root.mainloop()
