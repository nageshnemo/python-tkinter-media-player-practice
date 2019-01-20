from tkinter import *
counter = 0
def do_something():
    global counter
    counter =  counter +1
    l1.configure(text = str(counter))
root = Tk()
root.geometry("200x200")

b1 = Button(root,relief = "solid" ,text = "click me yar ",bg = "red",command = do_something)
b1.pack()
l1 = Label(root)
l1.configure(text = str(counter))
l1.pack()

root.mainloop()