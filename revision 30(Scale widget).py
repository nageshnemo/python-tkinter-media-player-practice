# scale widget is used
# syntax === sb = Scale(master,from --,to,options)
# two methods -- get() set(value)
# Scale also have a event handling and command attribute which calls the event handler function
# but when python calls the event pass command attribute

from tkinter import *
def set_red_color(val):
    a = hex(val)
    if len()
    root.configure()

root = Tk()
root.geometry('200x200')

sc = Scale(root,from_= 0 ,to = 255,orient = HORIZONTAL,command = set_red_color)
sc.pack()
root.configure(bg = "#000000")
root.mainloop()