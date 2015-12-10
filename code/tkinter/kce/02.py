#!/usr/bin/env python
import Tkinter as tk

if __name__=="__main__":
    root = tk.Tk()
    PV_tag_label = tk.Label(master=root, text = "PV", fg='red',bg='black',font=("Times",36)).grid(row=0,column=0)
    root.mainloop()
