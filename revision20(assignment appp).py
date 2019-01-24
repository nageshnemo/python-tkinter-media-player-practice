from tkinter import *
from tkinter import colorchooser,messagebox

def showpass():
    color = colorchooser.askcolor()
    print(color)

    root_color = color[1]
    if color[1] is not None:
        root.configure(bg = root_color)


    else:
        messagebox.showerror("no color choosen!","color should be choosed")




root = Tk()
root.geometry("200x200")
btn = Button(root,text = "click me",command = showpass)
btn.pack()
root.mainloop()
