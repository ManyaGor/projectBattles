from tkinter import *
import calendar
from PIL import ImageTk, Image

root = Tk()
root.title("Calendar")
root.geometry("400x350")
root.resizable(0,0)

icon=ImageTk.PhotoImage(Image.open("C:/Users/THIS P-C/Desktop/calendar.png"))
iconLabel= Label(image=icon)
iconLabel.pack()

def show():
    a = int(monthBox.get())
    b = int(yearBox.get())

    cal = calendar.month(b,a)
    textBox.insert(INSERT,cal)

def clear():
    textBox.delete(0.0,END)

month = Label(root, text="Month", font=('calibri',13,"bold")).place(x=50, y=128)
monthBox = Spinbox(root,values = (1,2,3,4,5,6,7,8,9,10,11,12), width = 7)
monthBox.place(x=120,y=130)

year = Label(root, text="Year", font=('calibri',13,'bold')).place(x=240, y=128)
yearBox = Spinbox(root,from_= 1999, to_=2100, width = 7)
yearBox.place(x=290,y=130)

showButton = Button(root, text="Show", font=('calibri',13,"bold"), command=show).place(x=120,y=290)
clearButton = Button(root, text="Clear", font=('calibri',13,"bold"), command=clear).place(x=180,y=290)
exitButton = Button(root, text="Exit", font=('calibri',13,"bold"), command=root.destroy).place(x=240,y=290)

textBox = Text(root,width=34,height=7)
textBox.place(x=60,y=160)

root.mainloop()