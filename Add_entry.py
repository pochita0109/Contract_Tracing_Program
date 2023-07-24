import tkinter as tk

class add_entry(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        # Ask the name
        self.name = tk.Label(self, text = "Name")
        self.name.place(x = 50, y = 50)

        self.name_entry = tk.Entry(self)
        self.name_entry.place(x = 100, y = 50)

        # Ask the date of birth
        # Ask the address
        # Ask the phone number
        # Ask the email adress
        # Ask the date of visit
        # Ask the vaccination status
        # Ask if there are symptoms of COVID-19
        # Ask if there are exposure on someone with COVID-19
        # Ask if tested positive on COVID-19 in the last 14 days