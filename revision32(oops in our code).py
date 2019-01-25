# frm now we can convert procedure gui to object oriented

import tkinter
from tkinter import messagebox
class MyGUI:
    def __init__(self,root):
        self.root = root
        self.root.title("MY OOP GUI")
        self.root.geometry("200x200")
        self.lbl= tkinter.Label(self.root,text= "click me")
        self.btn1 = tkinter.Button(self.root, text="Greet",command = self.showmsg)
        self.btn2 = tkinter.Button(self.root, text="Quit",command = self.finish)

        self.lbl.pack()
        self.btn1.pack()
        self.btn2.pack()

    def showmsg(self):
        messagebox.showinfo("Greetings","welcome to world")

    def finish(self):
        self.root.destroy()


root = tkinter.Tk()
obj = MyGUI(root)
root.mainloop()