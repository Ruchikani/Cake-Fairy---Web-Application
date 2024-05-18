from tkinter import *
import time

window = Tk()
window.title("My First GUI Form")
#window.geometry("400x600")

time_format = time.strftime("%I:%M:%S %p")

#lb1 = Label(window,text="Hello World",font=("Calibri",30))
#lb1.pack()

#lb2 = Label(window,text="Welcome to World of PYTHON",font=20)
#lb2.pack()

lb3 = Label(window,text=time_format,font=("Calibri",60))
lb3.pack()

window.mainloop()
