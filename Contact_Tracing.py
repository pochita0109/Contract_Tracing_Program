import tkinter as tk

class main_page(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contact Tracing")
        self.geometry("1000x550")
        
        self.add = tk.Button(self, text = "   Add Entry   ")
        self.add.place(x = 465, y = 225)

        self.search = tk.Button(self, text = "   Search Entry   ")
        self.search.place(x = 465, y = 300)
        
if __name__=="__main__":
    app = main_page()
    app.mainloop()
