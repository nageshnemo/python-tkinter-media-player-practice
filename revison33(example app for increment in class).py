# frm now we can convert procedure gui to object oriented

import tkinter
from tkinter import messagebox
class MyGUI:
    def __init__(self,root):
        self.root = root
        self.root.title("MY OOP GUI")
        self.root.geometry("200x200")
        self.lbl= tkinter.Label(self.root,text= "0")
        self.btn1 = tkinter.Button(self.root, text="Click me",command = self.incr_count)



        self.btn1.pack()
        self.lbl.pack()
        self.count = 0

    def incr_count(self):
        self.count = self.count+1
        self.lbl.configure(text = str(self.count))



root = tkinter.Tk()
obj = MyGUI(root)
root.mainloop()