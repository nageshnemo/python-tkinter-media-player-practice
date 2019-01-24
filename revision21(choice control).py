# choice controls allow user to select an option from the available list of choices
"""
== Checkbutton
"""
from tkinter import *

def changecolor():
    if x.get() == 1:
        root.configure(bg = "red")
    else:
        root.configure(bg = old_color)

root = Tk()
root.geometry("200x200")
old_color = root["bg"]
x = IntVar()
#x is object of Intvar we make a object of this because checkbutton doesnt have any method to get the value
cb = Checkbutton(root,text = "Red",command = changecolor,variable = x)
cb.pack()
root.mainloop()

root.mainloop()
