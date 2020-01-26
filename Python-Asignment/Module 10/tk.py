import tkinter
window=tkinter.Tk()
#to rename the title of the window
window.title("GUI")
#to divide single screen into frame
top_frame=tkinter.Frame(window).pack()
bottom_frame=tkinter.Frame(window).pack(side="bottom")
#pack is used to show the object in the window
btn1=tkinter.Button(top_frame,text="Button1",fg="red").pack()
btn2=tkinter.Button(top_frame,text="Button2",fg="green").pack()
btn3=tkinter.Button(bottom_frame,text="Button3",fg="purple").pack()
btn4=tkinter.Button(bottom_frame,text="Button4",fg="orange").pack()
window.mainloop()
