import tkinter
tw = tkinter.Tk()
s = tkinter.StringVar()
lbl = tkinter.Label(tw,borderwidth = 2 ,relief = "solid" , textvariable = s)
lbl.pack()
s.set("welcome nagesh")
# set is basically used to change the label text
# we use three things to do this 
tw.geometry("600x200")
tw.mainloop()
