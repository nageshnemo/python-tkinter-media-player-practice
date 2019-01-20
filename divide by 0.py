from tkinter import *
import sys
def finish():
    root.destroy()
def clear():
    e1.delete(0,END)
    e2.delete(0, END)
    e3.delete(0, END)
    e1.focus()
def divide():
    try:
        e3.delete(0,END)
        a = int(e1.get())
        b = int(e2.get())
        c = a/b
        e3.insert(0,str(c))
        e3.config(fg = "green")

    except ZeroDivisionError:
        e3.insert(0,"DENOMINATOR not 0!")
    except ValueError:
        e3.insert(0,"only integers allowed!")

root = Tk()
root.geometry("400x200+100+200")
l1 = Label(root,text = "number division program")
l2 = Label(root,text = "first no")
l3 = Label(root,text = "second no")
l4 = Label(root,text = "result")

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
b1 = Button(root , text = "Divide",command = divide)
b2 = Button(root , text = "Clear",command = clear)
b3 = Button(root , text = "Quit",command = finish)
l1.grid(row = 0,column = 0,columnspan = 4)
e1.grid(row = 1,column = 1)
l2.grid(row = 1,column = 0,sticky = E)
e2.grid(row = 2,column = 1)
l3.grid(row = 2,column = 0,sticky = E)
l4.grid(row = 3,column = 0,sticky = E)
e3.grid(row = 3,column = 1)
b1.grid(row = 4,column = 0)
b2.grid(row = 4,column = 1)
b3.grid(row = 4,column = 2)


root.mainloop()