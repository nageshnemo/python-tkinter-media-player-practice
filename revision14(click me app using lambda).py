from tkinter import *
root = Tk()
root.geometry('200x200')
b1 = Button(root,text = "click me bro")
b1.pack()
b1.bind("<Button-1>",lambda e:root.config(bg = "blue"))
b1.bind("<Button-2>",lambda e:root.config(bg = "black"))
b1.bind("<Button-3>",lambda e:root.config(bg = "red"))
root.mainloop()