# filedialog.askopenfilename[options]
# [("txtfiles",".txt")]
from tkinter import *
from tkinter import filedialog,messagebox

def showopen():
    file_names = filedialog.askopenfilenames(title = "select your favourite song",filetypes=[("mp4 file","*.mp4"),("mp3 file","*.mp3")])
    #askopenfilenames is basically a method of class filedialog present in tkinter module
    print(type(file_names))
    print((file_names))
    str = ""
    for x in file_names:
        str+=x + "\n"
    lbl.configure(text = str)



root = Tk()
root.geometry("200x200")

btn = Button(root,text = "click me",command = showopen)
lbl = Label(root,text = "your selected file names will appear here")
print(type(filedialog))
print(type(filedialog.askopenfilename()))
btn.pack()
lbl.pack()
root.mainloop()
