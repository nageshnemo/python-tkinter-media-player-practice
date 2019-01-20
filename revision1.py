# buttons
# event handling
from tkinter import *
root = Tk() # Tk is the class and root is object or instance
root.geometry('600x200')
b1 = Button(root , text = "click!me")
b1.pack()
root.mainloop()