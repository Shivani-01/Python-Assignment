import tkinter
window=tkinter.Tk()
#to rename the title of the window
window.title("GUI")
#to get button
button=tkinter.Button(window,text="Button").pack()

label=tkinter.Label(window,text="Welcome to gui tutorial").pack()

tkinter.mainloop()
window.mainloop()
