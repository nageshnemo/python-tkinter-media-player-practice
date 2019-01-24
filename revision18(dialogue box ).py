from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

def accept():
    num = simpledialog.askinteger("Input","enter voters age",minvalue = 18,maxvalue = 122)
    if num is not None:
        messagebox.showinfo("hello","you entered "+str(num))

root = Tk()
root.geometry("200x200")
btn = Button(root,text = "click me ",command = accept)
btn.pack()
root.mainloop()
