# scale widget is used
# syntax === sb = Scale(master,from --,to,options)
# two methods -- get() set(value)
# Scale also have a event handling and command attribute which calls the event handler function
# but when python calls the event pass command attribute

from tkinter import *
def set_red_color(val):
    print(val)
    print(type(val))

    red = hex(int(val))
    print (red)

    red = red[2:]
    if len(red) == 1:
        red = "0" + red
    color = "#" + red + "0000"
    print(color)
    root.configure(bg = color)
root = Tk()
root.geometry('200x200')

sc = Scale(root,from_= 0 ,to = 255,orient = HORIZONTAL,command = set_red_color)
sc.pack()
root.configure(bg = "#000000")
root.mainloop()


# modify the previus app so that the  gui contains hree scale widget representing intensities of rd green and blue an
# and the user slides their nobs the color of the root window should cahnge accordingluy