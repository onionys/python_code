#!/usr/bin/env python
import Tkinter as tk

var = {}

if __name__=="__main__":
    root = tk.Tk()
    PV_tag_label = tk.Label(master=root,text="PV",width=6,fg='red',bg='black',font=("Times",36)).grid(row=0,column=0)
    SV_tag_label = tk.Label(master=root,text="SV",width=6,fg='red',bg='black',font=("Times",36)).grid(row=1,column=0)
    var["PV"] = tk.StringVar()
    PV_val_label = tk.Label(master=root,textvariable=var["PV"],width=6,fg='red',bg='black',font=("Times",36)).grid(row=0,column=1)
    var["SV"] = tk.StringVar()
    PV_val_label = tk.Label(master=root,textvariable=var["SV"],width=6,fg='red',bg='black',font=("Times",36)).grid(row=1,column=1)
    var["PV"].set("0")
    var["SV"].set("0")

    root.mainloop()
