import tkinter as tk
from tkinter import Tk, Label, messagebox, StringVar, IntVar, Entry, Radiobutton, Button, Listbox
from configure import user, password
import MySQLdb

class WebCheckin:
    def __init__(self):
        top = Tk()
        top.title("Airline Reservation System")
        top.geometry("500x300")

        self.pnr_value = StringVar()
        self.buttons(top)
        top.mainloop()

    def checkPNR(self):
        pnr = self.pnr_value.get()

    def buttons(self,top):
        label_1 = Label(top, text="Enter PNR number:",textvar=self.pnr_value, width=20, font=("bold", 10))
        label_1.place(x=50, y=100)
        entry_1 = Entry(top, width=30)
        entry_1.place(x=210, y=100)

        Button(top, text='Submit', width=20, bg='brown',
               fg='white', command=self.checkPNR).place(x=180, y=150)

WebCheckin()