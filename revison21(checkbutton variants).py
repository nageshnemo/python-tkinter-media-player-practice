# choice controls allow user to select an option from the available list of choices
"""
== Checkbutton
"""
from tkinter import *

def show():
    print(x.get())
root = Tk()
root.geometry("200x200")
old_color = root["bg"]
x = StringVar()
cb = Checkbutton(root,text = "Click me",command = show,variable = x , onvalue = "h1" , offvalue = "bye")
cb.deselect()
cb.pack()

root.mainloop()
