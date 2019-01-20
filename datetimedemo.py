from datetime import *
obj = datetime.now()
from tkinter import *
def do_something():
    today = datetime.now()
    s = today.strftime("%d-%B-%Y %I: %M: %S %p")
    l1.configure(text = s)


root = Tk()
root.geometry("200x200")
b1 = Button(root,relief = "solid" ,text = "click me yar ",bg = "red",command = do_something)
b1.pack()
l1 = Label(root)
l1.pack()

root.mainloop()

