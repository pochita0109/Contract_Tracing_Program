import tkinter as tk
from Add_entry import add_entry
from Search_entry import search_entry

class main_page(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contact Tracing")
        self.geometry("600x600")
        self.configure(bg = "violet")
        
        self.main_title = tk.Label(self, text = "COVID-19 CONTACT TRACING FORM", font = ("Times", 20), bg = "violet")
        self.main_title.place(x = 70, y = 25)

        self.add = tk.Button(self, text = " Add Entry ", command = main_page.go_to_add_entry, bg = "light blue")
        self.add.place(x = 265, y = 225)

        self.search = tk.Button(self, text = "Search Entry", command = main_page.go_to_search_entry, bg = "light green")
        self.search.place(x = 260, y = 300)

        self.exit = tk.Button(self, text = "       Exit       ", command = self.exit, bg = "yellow")
        self.exit.place(x = 260, y = 375)
        
    def go_to_add_entry():
        entry = add_entry()
        entry.place(relwidth = 1, relheight = 1)

    def go_to_search_entry():
        search = search_entry()
        search.place(relwidth = 1, relheight = 1)

    def exit(self):
        self.destroy()

if __name__=="__main__":
    app = main_page()
    app.mainloop()