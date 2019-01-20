import tkinter
root = tkinter.Tk()
l1=tkinter.Label(root, text="Red Sun", bg="red", fg="white")
l2=tkinter.Label(root, text="Green Grass", bg="green", fg="black")
l3=tkinter.Label(root, text="Blue Sky", bg="blue", fg="white")
l1.pack(fill=tkinter.X)
l2.pack(fill=tkinter.X)
l3.pack(fill=tkinter.X)
root.mainloop()
