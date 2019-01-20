# syntax of bind method
"""
<obj.name>.bind("<event",handler)
this is the widget for which event handling needs to be done
"""
from tkinter import *
def changecolor(e):
    root.configure(bg = "black")
root = Tk()
root.geometry('200x200')
b1 = Button(root,text = "click me yaar")
b1.bind("<Button>",changecolor)
"""
using lambda
b1.bind("<Button>",lambda e:root.configure(bg="yellow"))
"""
b1.pack()
root.mainloop()