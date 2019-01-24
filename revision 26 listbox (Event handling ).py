from tkinter import *
from tkinter import messagebox
def showitem():
    index_tuple = lb1.curselection()
    if len(index_tuple)!=0:
        str = ""
        for x in index_tuple:
            item = lb.get(x)
            str += item + "\n"

        lb1.configure(text = "you selected \n"+str)


    else:
        messagebox.showerror("no selection","please select an item frst")

root = Tk()
root.geometry("200x200")
lb1 = Listbox(root,selectmode = )

sports = ["cricket","football","badminton","wresrling","chess","pubg","wwe"]
for i in sports:
    lb1.insert(END,i)


lb1.grid(row = 1,column = 1,sticky = W)
root.mainloop()