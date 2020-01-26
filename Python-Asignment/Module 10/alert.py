import tkinter.messagebox
window=tkinter.Tk()
window.title("GUI")
tkinter.messagebox.showinfo("Alert Message","This is just an alert message")
response=tkinter.messagebox.askquestion("Tricky Question","Do you love deep learning?")
if response=="yes":
    tkinter.Label(window,text="Yes").pack()
else:
    tkinter.Label(window,text="No").pack()
window.mainloop()
