import tkinter
tw = tkinter.Tk()
# img = tkinter.PhotoImage(location of image which is only gif and png not jpeg)
tw.title("my gui app")

sw = tw.winfo_screenheight()
sh = tw.winfo_screenwidth()
print(sh,sw)
xco = sw // 4
yco = sh // 4
rw = sw // 2
rh = sh // 2
tw.geometry(f"{rw}x{rh}+{xco}+{yco}")
tw.mainloop()
