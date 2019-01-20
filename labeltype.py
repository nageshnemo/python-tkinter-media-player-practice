import tkinter
root = tkinter.Tk()
lbl = tkinter.Label(root,text = "red sun" ,relief = "solid" , bg ="red",fg = "white")
lbl1 = tkinter.Label(root,text = "hey bro" ,relief = "solid" , bg ="orange",fg = "blue")
lbl2 = tkinter.Label(root,text = "red sun" ,relief = "solid" , bg ="blue",fg = "yellow")
lbl.pack(fill = tkinter.X)
lbl1.pack(fill = tkinter.X,padx=(300,0),ipadx = 1000,pady = (20,0))
lbl2.pack(fill = tkinter.X,padx=(0,300),ipadx = 10,pady = (20,0))
# this will fill the whole horizontal line

lbl3 = tkinter.Label(root,text = "red sun" ,relief = "solid" , bg ="red",fg = "white")
lbl4 = tkinter.Label(root,text = "hey bro" ,relief = "solid" , bg ="orange",fg = "blue")
lbl5 = tkinter.Label(root,text = "red sun" ,relief = "solid" , bg ="blue",fg = "yellow")

lbl3.pack(padx = 5 , pady = 5 , side = tkinter.LEFT)
lbl4.pack(padx = 5 , pady = 5 , side = tkinter.LEFT)
lbl5.pack(padx = 5 , pady = 5 , side = tkinter.LEFT)


lbl6 = tkinter.Label(root,text = "red sun" ,relief = "solid" , bg ="red",fg = "white")
lbl7 = tkinter.Label(root,text = "hey bro" ,relief = "solid" , bg ="orange",fg = "blue")
lbl8 = tkinter.Label(root,text = "red sun" ,relief = "solid" , bg ="blue",fg = "yellow")

lbl6.place(x=0,y=0)
lbl7.place(x=50 , y = 40)
lbl8.place(x = 26 , y = 4)
# grid


lbl9 = tkinter.Label(root,text = "red sun" ,relief = "solid" , bg ="red",fg = "white")
lbl10 = tkinter.Label(root,text = "hey bro" ,relief = "solid" , bg ="orange",fg = "blue")
lbl11 = tkinter.Label(root,text = "red sun" ,relief = "solid" , bg ="blue",fg = "yellow")


lbl6.place(x=0,y=0)
lbl7.place(x=50 , y = 40)
lbl8.place(x = 26 , y = 4)





root.geometry("600x200")
root.mainloop()
