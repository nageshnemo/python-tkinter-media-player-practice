import tkinter
tw = tkinter.Tk()
lbl = tkinter.Label(tw,text = "welcome to python !",bg = "red",fg = "blue",font= "Chillar 22 bold")
lbl.pack()

lbl.configure(bg = "orange", fg = "green")# if we write this the previous one is replaced
# we can also write background in place of bg
tw.configure(bg = "black")
lb2 = tkinter.Label(tw,text = "i am enjoying it man!",font = "verdana 34 italic")
lb2.pack()
lb2.configure(bg = "black", fg = "green")
tw.geometry("600x200")
tw.mainloop()
# geometry and main loop is basically a method