import json
from tkinter import Entry, Label, Listbox, Scrollbar, StringVar, Toplevel, ttk, Button
from tkcalendar import Calendar, DateEntry
import datetime


class Booking:
    def __init__(self):
        top = Toplevel()
        top.title("Book a Ticket")
        top.geometry("800x350")

        self.airport_names = []
        self.airport_code = []
        self.source = StringVar()
        self.destination = StringVar()
        self.number = StringVar()
        self.calendar = StringVar()
        self.time = StringVar()
        self.travel_class = StringVar()

        self.loadJson()
        self.widgets(top)
        top.mainloop()

    def loadJson(self):
        data = open('json_data/airports.json',)
        json_data = json.load(data)
        airport_data = json_data["airports"]
        for airports in airport_data:
            self.airport_names.append(airports["airport_name"])
        data.close()

    def widgets(self, top):
        label = Label(top, text="Flight Booking", padx="3",
                      pady="3", font=("Times New Roman", 25)).pack()

        Label(top, text="Source Location: ", font=(
            "Times New Roman", 15)).place(x=180, y=60)
        source_chosen = ttk.Combobox(top, width=38, textvariable=self.source)
        source_chosen['values'] = self.airport_names
        source_chosen.place(x=375, y=65)
        source_chosen.current()

        Label(top, text="Destination Location: ", font=(
            "Times New Roman", 15)).place(x=180, y=100)
        destination_chosen = ttk.Combobox(
            top, width=38, textvariable=self.destination)
        destination_chosen['values'] = self.airport_names
        destination_chosen.place(x=375, y=105)
        destination_chosen.current()

        # Label(top, text = "Phone Number: ", font=("Times New Roman", 15)).place(x = 180, y = 140)
        # phone = Entry(top, width=30, textvar=self.number)
        # phone.place(x=375, y=145)

        today = datetime.date.today()
        Label(top, text="Date of Journey: ", font=(
            "Times New Roman", 15)).place(x=180, y=140)
        cal = DateEntry(top, selectmode="day", width=15, year=today.year, month=today.month, day=today.day,
                        background='darkblue', foreground='white', borderwidth=2, textvariable=self.calendar)
        cal.place(x=375, y=145)

        Label(top, text="Time of Journey: ", font=(
            "Times New Roman", 15)).place(x=180, y=180)
        time_chosen = ttk.Combobox(top, width=10, textvariable=self.time)
        time_chosen['values'] = ['7:30', '9:30', '11:30',
                                 '13:30', '15:30', '17:30', '19:30', '21:30', '23:30']
        time_chosen.place(x=375, y=185)
        time_chosen.current()

        Label(top, text="Class of Travel: ", font=(
            "Times New Roman", 15)).place(x=180, y=220)
        class_chosen = ttk.Combobox(
            top, width=20, textvariable=self.travel_class)
        class_chosen['values'] = ['First Class',
                                  'Business Class', 'Economy Class']
        class_chosen.place(x=375, y=225)
        class_chosen.current()

        Button(top, text='Submit', width=20, bg='brown',
               fg='white').place(x=300, y=280)
