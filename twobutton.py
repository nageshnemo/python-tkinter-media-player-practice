from tkinter import *
root = Tk()
root.geometry('200x200')
b1 = Button(root,text = "click me yaar")
b1.bind("<Button-1>",lambda self:root.configure(bg="red"))
b1.bind("<Button-3>",lambda self:root.configure(bg="blue"))
b1.pack()
root.mainloop()