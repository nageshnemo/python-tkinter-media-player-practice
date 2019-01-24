# choice controls allow user to select an option from the available list of choices
"""
== Checkbutton
"""
from tkinter import *

def changecolor():
    root.configure(bg = x.get())
    # through this we can minimise the code by setting the onvlaue and offvalue by red and old color itself
    
root = Tk()
root.geometry("200x200")
old_color = root["bg"]
x = StringVar()
cb = Checkbutton(root,text = "Red",command = changecolor,variable = x,onvalue = "red",offvalue = old_color)
cb.deselect()
cb.pack()
root.mainloop()


