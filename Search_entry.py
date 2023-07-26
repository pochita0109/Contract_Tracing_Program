import tkinter as tk
import csv

class search_entry(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.search_title = tk.Label(self, text = "SEARCH YOUR ENTRY HERE", font = ("Helvetica", 20))
        self.search_title.place(x = 110, y = 25)

        self.search_label = tk.Label(self, text = "Enter Name to Search:")
        self.search_label.place(x = 125, y = 100)

        self.search_entry = tk.Entry(self)
        self.search_entry.place(x = 250, y = 100)

        self.search_button = tk.Button(self, text= "  Search  ")
        self.search_button.place(x = 385, y = 100)