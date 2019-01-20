from tkinter import *
count = 0
def clickme():
    global count
    count+=1
    l1.configure(text = str(count))
root = Tk()
b1 = Button(root,text = "click me yaar",command = clickme)
l1 = Label(root,text = "0")
b1.pack()
l1.pack()
root.mainloop()