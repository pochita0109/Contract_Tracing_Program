import tkinter as tk
import csv

class search_entry(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.configure(bg = "light green")

        self.search_title = tk.Label(self, text = "SEARCH YOUR ENTRY HERE", font = ("Times", 20), bg = "light green")
        self.search_title.place(x = 115, y = 25)

        self.search_label = tk.Label(self, text = "Enter Name to Search:", bg = "light green")
        self.search_label.place(x = 125, y = 100)

        self.search_entry = tk.Entry(self, bg = "light green")
        self.search_entry.place(x = 250, y = 100)

        self.search_button = tk.Button(self, text= "  Search  ", command = self.search_name, bg = "yellow")
        self.search_button.place(x = 385, y = 100)

    def search_name(self):
        name_entry = self.search_entry.get()

        with open("data_storage.csv", "r", newline = "") as file:
            reader = csv.reader(file)
            found_entries = []
            for row in reader:
                if name_entry in row[0]:
                    found_entries.append(row)

        if found_entries:
            for i, entry in enumerate(found_entries):
                result = f"Name: {entry[0]}\n"
                result += f"Date of Birth: {entry[1]}\n"
                result += f"Address: {entry[2]}\n"
                result += f"Cellphone Number: {entry[3]}\n"
                result += f"Email Address: {entry[4]}\n"
                result += f"Date of Visit: {entry[5]}\n"
                result += f"Vaccination Status: {entry[6]}\n"
                result += f"Symptoms of COVID-19: {entry[7]}\n"
                result += f"Exposure to COVID-19: {entry[8]}\n"
                result += f"COVID-19 Test Status: {entry[9]}"

                result = tk.Label(text = result, font = ("Arial", 15) , justify=("left"), bg = "light green")
                result.place(x = 100, y = 200)

        else:
            no_result = tk.Label(text="No matching entries found.")
            no_result.place(x = 25, y = 50)