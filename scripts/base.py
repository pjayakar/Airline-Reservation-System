import tkinter as tk
from tkinter import *
from fullScreen import FullScreenApp
from bookTicket import Booking
from webcheckin import WebCheckin
from login import Login
import datetime


class Main:
    def __init__(self):
        root = Tk()
        root.title("Udan Khatola")
        app = FullScreenApp(root)
        background_image = PhotoImage(file="src/bkg.png")
        background_label = Label(root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.buttons(root)
        root.mainloop()

    def userLogin(self):
        Login()

    def bookTicket(self):
        Booking()

    def checkin(self):
        WebCheckin()

    def buttons(self, root):
        but1 = Button(
            root,
            bd=0,
            relief="groove",
            compound=tk.CENTER,
            bg="white",
            fg="black",
            activeforeground="pink",
            activebackground="white",
            font="arial 12",
            text="Login/Register",
            pady=10,
            borderwidth=10,
            height=1,
            width=30,
            command=self.userLogin
        )

        but1.place(x=100, y=100)
        but2 = Button(
            root,
            bd=0,
            relief="groove",
            compound=tk.CENTER,
            bg="white",
            fg="black",
            activeforeground="pink",
            activebackground="white",
            font="arial 12",
            text="Book a ticket",
            pady=10,
            borderwidth=10,
            height=1,
            width=30,
            command=self.bookTicket
        )

        but2.place(x=100, y=200)

        but3 = Button(
            root,
            bd=0,
            relief="groove",
            compound=tk.CENTER,
            bg="white",
            fg="black",
            activeforeground="pink",
            activebackground="white",
            font="arial 12",
            text="Web Checkin",
            pady=10,
            borderwidth=10,
            height=1,
            width=30,
            command = self.checkin
        )

        but3.place(x=100, y=300)


Main()
