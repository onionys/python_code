#!/usr/bin/env python3
import tkinter as tk


vv = {}

def show_select():
    print("%d" % vv['r_opt_val'].get())

if __name__ == "__main__":
    root = tk.Tk()
    vv['label'] = tk.Label(master=root,text="test01")
    vv['label'].grid(row=0,column=0)
    vv['label'].config(font=('Times',28))

    vv['r_opt_val'] = tk.IntVar()
    
    vv['rbtn1'] = tk.Radiobutton(master=root,text="option 1", value=10)
    vv['rbtn1'].config(variable= vv['r_opt_val']) 
    vv['rbtn1'].config(command=show_select)
    vv['rbtn1'].config(font=("Times",28))
    vv['rbtn1'].grid(row=1,column=0)

    vv['rbtn2'] = tk.Radiobutton(master=root,text="option 2", value=20, command=show_select)
    vv['rbtn2'].config(variable= vv['r_opt_val']) 
    vv['rbtn2'].config(command=show_select)
    vv['rbtn2'].config(font=("Times",28))
    vv['rbtn2'].grid(row=2,column=0)

    vv['rbtn3'] = tk.Radiobutton(master=root,text="option 3", value=30, command=show_select)
    vv['rbtn3'].config(variable= vv['r_opt_val']) 
    vv['rbtn3'].config(command=show_select)
    vv['rbtn3'].config(font=("Times",28))
    vv['rbtn3'].grid(row=3,column=0)

    root.mainloop()
