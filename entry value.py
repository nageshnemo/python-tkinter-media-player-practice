from tkinter import *
import sys
def finish():
    sys.exit(0)
def show():
    fname = e1.get()
    lname = e2.get()
    e3.delete(0,END)
    e3.insert(0,fname+" "+ lname)


root = Tk()
l1 = Label(root,text = "first name")
l2 = Label(root,text = "Last name")
l3 = Label(root,text = "you typed")
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
b1 = Button(root , text = "Show",command = show)
b2 = Button(root , text = "Quit",command = finish)
l1.grid(row = 0,column = 0)
e1.grid(row = 0,column = 1)
l2.grid(row = 1,column = 0)
e2.grid(row = 1,column = 1)
l3.grid(row = 2,column = 0)
e3.grid(row = 2,column = 1)
b1.grid(row = 3,column = 0)
b2.grid(row = 3,column = 1)



root.mainloop()