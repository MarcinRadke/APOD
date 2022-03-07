from tkinter import *
from tkinter.ttk import OptionMenu, Button, Checkbutton
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image

class ApodView:

    def init_window(self, controller):
        self.controller = controller
        self.root = Tk()
        self.root.title('Astronomy picture of the day')

        upframe = tk.Frame(self.root, highlightbackground='black', highlightthickness=1, padx=10, pady=10)
        upframe.pack(expand=False, fill='both')

        year_label = Label(upframe, text='Year', justify="center")
        year_label.grid(row=0, column=0)

        self.year_entry = Entry(upframe, width=10, justify='center')
        self.year_entry.grid(row=1, column=0)

        month_label = Label(upframe, text='Month', justify="center")
        month_label.grid(row=0, column=1)

        self.month_entry = Entry(upframe, width=10, justify='center')
        self.month_entry.grid(row=1, column=1)

        day_label = Label(upframe, text='Day', justify="center")
        day_label.grid(row=0, column=2)

        self.day_entry = Entry(upframe, width=10, justify='center')
        self.day_entry.grid(row=1, column=2)

        midframe = tk.Frame(self.root)
        midframe.pack(expand=False)

        photoframe = tk.Frame(self.root, highlightbackground='black', highlightthickness=1, padx=10, pady=10)
        photoframe.pack(expand=True, fill='both')

        photo = ImageTk.PhotoImage(Image.open('photos.jpeg'))
        self.photo_label = Label(photoframe, image=photo)
        self.photo_label.pack()

        self.search_button = Button(upframe, text="search", command=self.search_button_handler)
        self.search_button.grid(row=0, column=3)

        self.root.mainloop()

    def search_button_handler(self):
        self.controller.search_api(self.year_entry.get(), self.month_entry.get(), self.day_entry.get())

    def reload_image(self):
        global photo
        photo = ImageTk.PhotoImage(Image.open('photos.jpeg'))
        self.photo_label.config(image=photo)
