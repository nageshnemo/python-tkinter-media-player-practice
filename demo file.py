import tkinter
import tkinter.font
tw = tkinter.Tk()
# img = tkinter.PhotoImage(file = location of file)
# we have to use gif file or png file in place of the location
lbl = tkinter.Label(tw.image=img,text = "welcome to python !",compound = tkiner.left)
lbl.pack()
tw.geometry("600x200")
tw.mainloop()
