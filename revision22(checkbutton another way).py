# choice controls allow user to select an option from the available list of choices
"""
== Radiobutton
"""
from tkinter import *
from tkinter import messagebox
def showgender():
    messagebox.showinfo("gender","you selected"+x.get())
root = Tk()
root.geometry("200x200")

l1 = Label(root,text = "select your gender")
x = StringVar()
rb1 = Radiobutton(root,text = "Male",command = showgender,variable = x,value = "Male",tristatevlue = "x" )
# if we set the value other than numeric we also have to set the other state of checkbutton that is trystate
rb2 = Radiobutton(root,text = "Female",command = showgender,variable = x,value = "Female",tristatevalue = "xv")
l1.grid(row = 0,column = 0)
rb1.grid(row = 1,column = 0,sticky = W)
rb2.grid(row = 2,column = 0,sticky = W)
root.mainloop()