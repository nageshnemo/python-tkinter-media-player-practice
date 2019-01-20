from tkinter import *
def clrred(e):
    root.configure(bg = "red")
def clrdefault(e):
    root.configure(bg = oldcolor)
root = Tk()
root.geometry('200x200')
root.bind("<Return>",clrred)
root.bind("<Escape>",clrdefault)
oldcolor = root["bg"]
root.mainloop()