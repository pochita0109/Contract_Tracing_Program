import tkinter as tk
from Add_entry import add_entry

class main_page(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contact Tracing")
        self.geometry("600x550")
        
        self.add = tk.Button(self, text = "   Add Entry   ", command = main_page.go_to_add_entry)
        self.add.place(x = 465, y = 225)

        self.search = tk.Button(self, text = "   Search Entry   ")
        self.search.place(x = 465, y = 300)
        
    def go_to_add_entry():
        entry = add_entry()
        entry.place(relwidth = 1, relheight = 1)

if __name__=="__main__":
    app = main_page()
    app.mainloop()