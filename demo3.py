import tkinter
import tkinter.font
tw = tkinter.Tk()
myfont = tkinter.font.Font(weight = "bold")
lbl = tkinter.Label(tw,text = "welcome to python !")
lbl.configure(font = myfont,borderwidth = 2,relief = "raised",width = 30,height = 4,anchor = "w")
lbl.pack()
print(lbl.keys())
print(lbl['text'])
(lbl['bg']) = "yellow"
tw.geometry("600x200")
tw.mainloop()
