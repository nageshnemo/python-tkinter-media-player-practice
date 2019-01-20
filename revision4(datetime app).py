from tkinter import *
from datetime import *
def showdatetime():
    today = datetime.now()
    fmtdatetime = today.strftime("%d-%B-%Y %H:%M:%S %p")
    l1.config(text=fmtdatetime)
root = Tk()
root.geometry('200x200')
b1=Button(root,text="Click Me",command=showdatetime)
l1=Label(root,text="Click the button for date and time")
b1.pack()
l1.pack()
root.mainloop()
