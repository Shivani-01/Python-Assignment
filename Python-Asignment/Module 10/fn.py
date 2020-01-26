import tkinter
window=tkinter.Tk()
window.title("GUI")
def Tuto():
    tkinter.Label(window,text="Hello I'm function").pack()
tkinter.Button(window,text="Click me",command=Tuto).pack()
window.mainloop()
