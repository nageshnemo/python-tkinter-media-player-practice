from tkinter import *
oldcolor=""

def enterkey(e):
    root.config(bg="red")

def escapekey(e):
    root.config(bg=oldcolor)

root = Tk()
root.geometry('200x200')
root.bind("<Return>",enterkey)
root.bind("<Escape>",escapekey)
oldcolor=root["bg"]
root.mainloop()
