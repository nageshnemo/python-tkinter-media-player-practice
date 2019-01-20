from tkinter import *

def do_something():
    count.set(count.get() + 1)
root = Tk()
root.geometry("200x200")

b1 = Button(root,relief = "solid" ,text = "click me yar ",bg = "red",command = do_something)
count = IntVar()
b1.pack()
l1 = Label(root,textvariable = count )
l1.pack()

root.mainloop()