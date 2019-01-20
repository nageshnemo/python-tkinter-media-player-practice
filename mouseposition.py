from tkinter import *
def changecolor(e):
    print(e)
    print(type(e))
    ch = e.char
    if ch == "r":
        root.configure(bg = "red")
    elif ch == "g":
        root.configure(bg = "green")
    elif ch == "b":
        root.configure(bg = "blue")

root = Tk()
root.geometry('200x200')
root.bind("<Key>",changecolor)
root.mainloop()