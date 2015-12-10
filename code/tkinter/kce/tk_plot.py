#!/usr/bin/env python
import Tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation



class tk_plot:
    def __init__(self,master,row=0,col=0,rowspan=1,colspan=1,size=(6,6),dpi=100,interval=1000):
        self.xdata = []
        self.ydata = []
        self.fig = Figure(figsize=size, dpi=dpi)
        self.ax = self.fig.add_subplot(111)
        self.ax.plot(self.xdata,self.ydata)
        self.canvas = FigureCanvasTkAgg(self.fig, master = master)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=row,column=col,rowspan=rowspan,columnspan=colspan,sticky=tk.N+tk.S+tk.E+tk.W)
        self.ani = animation.FuncAnimation(self.fig, self.plot_loop , interval=interval)

    def plot_loop(self,i):
        self.ax.plot(self.xdata, self.ydata)

    def add_data(self,x,y):
        self.xdata.append(float(x))
        self.ydata.append(float(y))

    def get_tk_widget(self):
        return self.canvas.get_tk_widget()

    def get_x_data(self):
        return self.xdata

    def get_y_data(self):
        return self.ydata
