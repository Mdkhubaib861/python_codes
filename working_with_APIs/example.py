from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
w=Tk()
w.geometry("600x600")
w.title("Matplotlib inside tkinter")
l1=Label(text="This is tkinter and matplotlib Graph")
l1.grid(row=0,column=0)

l2=Label(text="This is tkinter another matplotlib Graph")
l2.grid(row=1,column=0)

myfig=Figure(figsize=(2,4),dpi=100)

mygraph1=myfig.add_subplot(211)
mygraph1.tick_params(axis='x', labelsize=5)

x=["Jan","Feb","March","April","May"]
y=[25,44,41,75,20]
mygraph1.plot(x,y)

mygraph2=myfig.add_subplot(212)
x=["Jan","Feb","March","April","May"]
y=[25,44,41,75,20]
mygraph2.bar(x,y)

canvas=FigureCanvasTkAgg(myfig,master=w)
canvas.draw()
canvas.get_tk_widget().grid(row=2,column=0)

w.mainloop()

def show_graph():
















