import tkinter
window=tkinter.Tk()
#to rename the title of the window
window.title("GUI")
a="C:\\Users\\Student\\Pictures\\logo.png"
icon=tkinter.PhotoImage(file=a)
label=tkinter.Label(window,image=icon).pack()
label1=tkinter.Label(window,image=icon).pack()
window.mainloop()
