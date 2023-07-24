import tkinter as tk

class add_entry(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        # Ask the name
        self.name = tk.Label(self, text = "Name")
        self.name.place(x = 65, y = 50)

        self.name_entry = tk.Entry(self)
        self.name_entry.place(x = 105, y = 50)

        # Ask the date of birth
        self.birth = tk.Label(self, text = "Date of Birth")
        self.birth.place(x = 350, y = 50)

        self.birth_entry = tk.Entry(self)
        self.birth_entry.place(x = 425, y = 50)

        # Ask the address
        self.address = tk.Label(self, text = "Address")
        self.address.place(x = 55, y = 100)

        self.address_entry = tk.Entry(self)
        self.address_entry.place(x = 105, y = 100)

        # Ask the phone number
        self.number = tk.Label(self, text = "Cellphone Number")
        self.number.place(x = 315, y = 100)

        self.number_entry = tk.Entry(self)
        self.number_entry.place(x = 425, y = 100)

        # Ask the email adress
        self.email = tk.Label(self, text = "Email Address")
        self.email.place(x = 23, y = 150)

        self.email_entry = tk.Entry(self)
        self.email_entry.place(x = 105, y = 150)

        # Ask the date of visit
        self.visit = tk.Label(self, text = "Date of Visit")
        self.visit.place(x = 355, y = 150)

        self.visit_entry = tk.Entry(self)
        self.visit_entry.place(x = 425, y = 150)
        
        # Ask the vaccination status
        
        # Ask if there are symptoms of COVID-19
        # Ask if there are exposure on someone with COVID-19
        # Ask if tested positive on COVID-19 in the last 14 days