#!/usr/bin/env python3
import tkinter as tk

def btn_call_back():
    print("Hello World.")

if __name__ == "__main__":
    root = tk.Tk()
    button = tk.Button(master=root,text="hello", command=btn_call_back)
    button.pack()
    root.mainloop()
