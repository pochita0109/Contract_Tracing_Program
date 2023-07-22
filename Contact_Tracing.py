import tkinter as tk
from tkinter import *

front = tk.Tk()
front.title("Contact Tracing")
front.geometry("1000x550")

add = Button(front, text = "    Add Entry   ") 
add.place(x=465,y=225)

search = Button(front, text = "  Search Entry  ")
search.place(x=465,y=300)

front.mainloop()

