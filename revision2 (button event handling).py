# on clicking the Button our app displays the text Welcome User in a Label the this behaviour is called event handling
# we can do two things
# 1. using command attribute
# 2. using bind() method
from tkinter import *

def showmsg():
    print("i appears because u click the button")
    print("hey! nagesh")
    l1.configure(text = "hey now i am in a label ")



root = Tk() # Tk is the class and root is object or instance
root.geometry('600x200')
l1 = Label(root)
b1 = Button(root , text = "click! me",command = showmsg)
b1.pack()
l1.pack()
root.mainloop()