from tkinter import *

def clickme():
    count.set(count.get()+1)


root = Tk()
root.geometry('600x200')
count = IntVar()

# IntVar is basically a class and count is object
# IntVar have two functions get() and set()

b1 = Button(root,text = "click me yaar",command = clickme)

l1 = Label(root,textvariable = count)

b1.pack()
l1.pack()
print(type(count))
print(type(IntVar))
root.mainloop()