from tkinter import *
root = Tk()
l1 = Label(root,height = 3,width = 20,bg = "white")
b1 = button(root,text ="red",width = 6, command = changecolor("red"))
l1.grid(row = 0,column = 1)
b1.grid(row = 1 ,column = 0)