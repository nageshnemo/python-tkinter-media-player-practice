# Listbox = inserting elements in the list
# insert() method for inserting data having two arguments
from tkinter import *
root = Tk()
root.geometry("200x200")
lb1 = Listbox(root)

sports = ["cricket","football","badminton","wresrling","chess","pubg","wwe"]
for i in sports:
    lb1.insert(END,i)
    # END helps us in avoiding incremention count


lb1.grid(row = 1,column = 1,sticky = W)
root.mainloop()