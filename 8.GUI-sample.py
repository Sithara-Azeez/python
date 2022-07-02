from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Sithara")
window.configure(bg="#79D02D")
def hello():
    print("button clicked")
button1 = Button(text="ok",command=hello)

button2 = Button(text="ok",command=hello)

button1.grid(row=0,column=0)
button2.grid(row=0,column=1)

label = Label(window,text="welcome")




window.mainloop()
print("hai")