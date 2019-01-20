from tkinter import *
def do_something():
    #print(" i am the output of your click me welcome")
    l2 = Label(root, text = "welcome to python")
    l2.pack()
    # we can also make here but the problem here is this label will run everytime when we call a function through command


    l1.configure(text = "welcome to python")
root = Tk()
root.geometry("200x200")
b1 = Button(root,relief = "solid" ,text = "click me yar ",bg = "red",command = do_something)
b1.pack()
l1 = Label(root)
l1.pack()

root.mainloop()