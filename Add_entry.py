import tkinter as tk
import csv
from tkinter import messagebox

class add_entry(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.configure(bg = "light blue")

        # Ask the name
        self.name = tk.Label(self, text = "Name", bg = "light blue")
        self.name.place(x = 65, y = 50)

        self.name_entry = tk.Entry(self, bg = "light blue")
        self.name_entry.place(x = 105, y = 50)

        # Ask the date of birth
        self.birth = tk.Label(self, text = "Date of Birth", bg = "light blue")
        self.birth.place(x = 350, y = 50)

        self.birth_entry = tk.Entry(self, bg = "light blue")
        self.birth_entry.place(x = 425, y = 50)

        # Ask the address
        self.address = tk.Label(self, text = "Address", bg = "light blue")
        self.address.place(x = 55, y = 100)

        self.address_entry = tk.Entry(self, bg = "light blue")
        self.address_entry.place(x = 105, y = 100)

        # Ask the phone number
        self.number = tk.Label(self, text = "Cellphone Number", bg = "light blue")
        self.number.place(x = 315, y = 100)

        self.number_entry = tk.Entry(self, bg = "light blue")
        self.number_entry.place(x = 425, y = 100)

        # Ask the email adress
        self.email = tk.Label(self, text = "Email Address", bg = "light blue")
        self.email.place(x = 23, y = 150)

        self.email_entry = tk.Entry(self, bg = "light blue")
        self.email_entry.place(x = 105, y = 150)

        # Ask the date of visit
        self.visit = tk.Label(self, text = "Date of Visit", bg = "light blue")
        self.visit.place(x = 355, y = 150)

        self.visit_entry = tk.Entry(self, bg = "light blue")
        self.visit_entry.place(x = 425, y = 150)
        
        # Ask the vaccination status
        self.vaccination = tk.Label(self, text = "Have you been vaccinated for COVID-19?", bg = "light blue")
        self.vaccination.place(x = 30, y = 200)

        self.choice = tk.StringVar()

        self.choice1= tk.Radiobutton(self, text = "Not yet", variable = self.choice, value = "Not yet", bg = "light blue")
        self.choice1.place(x = 30, y = 225)

        self.choice2= tk.Radiobutton(self, text = "1st Dose", variable = self.choice, value = "1st Dose", bg = "light blue")
        self.choice2.place(x = 30, y = 250)

        self.choice3= tk.Radiobutton(self, text = "2nd Dose", variable = self.choice, value = "2nd Dose", bg = "light blue")
        self.choice3.place(x = 30, y = 275)

        self.choice4= tk.Radiobutton(self, text = "1st Booster Shot", variable = self.choice, value = "1st Booster Shot", bg = "light blue")
        self.choice4.place(x = 30, y = 300)

        self.choice5= tk.Radiobutton(self, text = "2nd Booster Shot", variable = self.choice, value = "2nd Booster Shot", bg = "light blue")
        self.choice5.place(x = 30, y = 325)

        # Ask if there are symptoms of COVID-19
        self.symptom = tk.Label(self, text = "Do you have a symptoms of COVID-19?", bg = "light blue")
        self.symptom.place(x = 30, y = 375)

        self.symptom_choice = tk.StringVar()

        self.symptom_choice1 = tk.Radiobutton(self, text = "Yes", variable = self.symptom_choice, value = "Yes", bg = "light blue")
        self.symptom_choice1.place(x = 30, y = 400)
        
        self.symptom_choice2 = tk.Radiobutton(self, text = "No", variable = self.symptom_choice, value = "No", bg = "light blue")
        self.symptom_choice2.place(x = 30, y = 425)
        
        self.symptom_choice3 = tk.Radiobutton(self, text = "Uncertain", variable = self.symptom_choice, value = "Uncertain", bg = "light blue")
        self.symptom_choice3.place(x = 30, y = 450)

        # Ask if there are exposure on someone with COVID-19
        self.exposure = tk.Label(self, text = "Do you have an exposure on someone with COVID 19?", bg = "light blue")
        self.exposure.place(x = 300, y = 375)

        self.exposure_choice = tk.StringVar()

        self.exposure_choice1 = tk.Radiobutton(self, text = "Yes", variable = self.exposure_choice, value = "Yes", bg = "light blue")
        self.exposure_choice1.place(x = 300, y = 400)
        
        self.exposure_choice2 = tk.Radiobutton(self, text = "No", variable = self.exposure_choice, value = "No", bg = "light blue")
        self.exposure_choice2.place(x = 300, y = 425)
        
        self.exposure_choice3 = tk.Radiobutton(self, text = "Uncertain", variable = self.exposure_choice, value = "Uncertain", bg = "light blue")
        self.exposure_choice3.place(x = 300, y = 450)
        
        # Ask if tested positive on COVID-19 in the last 14 days
        self.test = tk.Label(self, text = "Have you been tested for COVID-19 in the last 14 days?", bg = "light blue")
        self.test.place(x = 300, y = 200)

        self.test_choice = tk.StringVar()

        self.test_choice1 = tk.Radiobutton(self, text = "No", variable = self.test_choice, value = "No", bg = "light blue")
        self.test_choice1.place(x = 300, y = 225)

        
        self.test_choice2 = tk.Radiobutton(self, text = "Yes - Positive", variable = self.test_choice, value = "Yes - Positive", bg = "light blue")
        self.test_choice2.place(x = 300, y = 250)
        
        self.test_choice3 = tk.Radiobutton(self, text = "Yes - Negative", variable = self.test_choice, value = "Yes - Negative", bg = "light blue")
        self.test_choice3.place(x = 300, y = 275)

        self.test_choice4 = tk.Radiobutton(self, text = "Yes - Pending", variable = self.test_choice, value = "Yes - Pending", bg = "light blue")
        self.test_choice4.place(x = 300, y = 300)

        # Added label for personal information and for COVID-19 information
        self.personal = tk.Label(self, text = "PERSONAL INFORMATION", font=("Times", 20), bg = "light blue")
        self.personal.place(x = 130, y = 5)

        # Added a submit button 
        self.submit = tk.Button(self, text = "  Submit  ", command = self.get_data, bg = "yellow")
        self.submit.place(x = 200, y = 525)

        # Add an exit Button
        self.exit = tk.Button(self, text = "  Exit  ", command = self.close, bg = "red")
        self.exit.place(x = 350, y = 525)

    def close(self):
        self.master.destroy()

    # Get the information gathered from user
    def get_data(self):
        name = self.name_entry.get()
        birthday = self.birth_entry.get()
        address = self.address_entry.get()
        phone = self.number_entry.get()
        email = self.email_entry.get()
        visit_date = self.visit_entry.get()
        vaccination_status = self.choice.get()
        symptom_status = self.symptom_choice.get()
        exposure_status = self.exposure_choice.get()
        test_status = self.test_choice.get()

        # Save the information gathered into excel file using csv
        with open("data_storage.csv", "a", newline = "") as file:
            store = csv.writer(file)
            store.writerow([name, birthday, address, phone, email, visit_date, vaccination_status, symptom_status, exposure_status, test_status])

        # Create a messagebox that will let the user know that their data has ben submitted
        messagebox.showinfo("Admin", "The information has been submitted.")
        self.clear_entry()

    def clear_entry(self):
        self.name_entry.delete(0, tk.END)
        self.birth_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.number_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.visit_entry.delete(0, tk.END)
        self.choice.set(None)
        self.symptom_choice.set(None)
        self.exposure_choice.set(None)
        self.test_choice.set(None)