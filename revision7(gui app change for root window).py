from tkinter import *

def fnRed():
    l1["bg"]="red"

def fnGreen():
    l1["bg"]="green"

def fnBlue():
    l1["bg"] = "blue"

root = Tk()
l1=Label(root,height=3,width=20,bg="white")
b1=Button(root,text="Red",width=6,command=fnRed)
b2=Button(root,text="Green",width=6,command=fnGreen)
b3=Button(root,text="Blue",width=6,command=fnBlue)
l1.grid(row=0,column=1)
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)
root.mainloop()