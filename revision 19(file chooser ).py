# filedialog.askopenfilename[options]
# [("txtfiles",".txt")]
from tkinter import *
from tkinter import filedialog,messagebox

def showopen():
    file_name = filedialog.askopenfilename(title = "select your favourite song",filetypes=[("mp4 file","*.mp4"),("mp3 file","*.mp3")])
    #askopenfilename is basically a method of class filedialog present in tkinter module
    if len(file_name)!=0:
        messagebox.showinfo("your selection",file_name)

root = Tk()
root.geometry("200x200")
btn = Button(root,text = "click me",command = showopen)
print(type(filedialog))
btn.pack()
root.mainloop()
