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
        self.vaccination = tk.Label(self, text = "Have you been vaccinated for COVID-19?")
        self.vaccination.place(x = 30, y = 250)

        self.choice = tk.StringVar()

        self.choice1= tk.Radiobutton(self, text = "Not yet", variable = self.choice, value = "Not yet")
        self.choice1.place(x = 30, y = 275)

        self.choice2= tk.Radiobutton(self, text = "1st Dose", variable = self.choice, value = "1st Dose")
        self.choice2.place(x = 30, y = 300)

        self.choice3= tk.Radiobutton(self, text = "2nd Dose", variable = self.choice, value = "2nd Dose")
        self.choice3.place(x = 30, y = 325)

        self.choice4= tk.Radiobutton(self, text = "1st Booster Shot", variable = self.choice, value = "1st Booster Shot")
        self.choice4.place(x = 30, y = 350)

        self.choice5= tk.Radiobutton(self, text = "2nd Booster Shot", variable = self.choice, value = "2nd Booster Shot")
        self.choice5.place(x = 30, y = 375)

        # Ask if there are symptoms of COVID-19
        # Ask if there are exposure on someone with COVID-19
        # Ask if tested positive on COVID-19 in the last 14 days