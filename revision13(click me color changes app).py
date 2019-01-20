from tkinter import *
count = 0
def changecolor(e):
    global count
    count+=1
    if count % 2 == 0:
        root.config(bg="red")
    else:
        root.config(bg="blue")
root = Tk()
root.geometry('200x200')
b1 = Button(root,text = "click me")
b1.pack()
b1.bind("<Button>",changecolor)
root.mainloop()