from tkinter import *
from tkinter.ttk import OptionMenu, Button, Checkbutton
from tkinter import messagebox
import tkinter as tk
from datetime import date
from calendar import monthrange
from PIL import ImageTk, Image
import requests
import json
import urllib.request


#PoGSdWWaN1mXfdkOpHRGcGHC2edgBO00HWeEobxU       API NASA

api_key = 'PoGSdWWaN1mXfdkOpHRGcGHC2edgBO00HWeEobxU'
nasa_apod = 'https://api.nasa.gov/planetary/apod?api_key='


today = date.today()

root = Tk()
root.title('Dzienne astronomiczne zdjęcie')

upframe = tk.Frame(root, highlightbackground='black', highlightthickness=1, padx=10, pady=10)
upframe.pack(expand=False, fill='both')

year_label = Label(upframe, text='Year', justify="center")
year_label.grid(row=0, column=0)

year_entry = Entry(upframe, width=10, justify='center')
year_entry.grid(row=1, column=0)

month_label = Label(upframe, text='Month', justify="center")
month_label.grid(row=0, column=1)

month_entry = Entry(upframe, width=10, justify='center')
month_entry.grid(row=1, column=1)

day_label = Label(upframe, text='Day', justify="center")
day_label.grid(row=0, column=2)

day_entry = Entry(upframe, width=10, justify='center')
day_entry.grid(row=1, column=2)

midframe = tk.Frame(root)
midframe.pack(expand=False)

photoframe = tk.Frame(root, highlightbackground='black', highlightthickness=1, padx=10, pady=10)
photoframe.pack(expand=True, fill='both')

photo = ImageTk.PhotoImage(Image.open('F:\\APOD\\bad.jpeg'))
photo_label = Label(photoframe, image=photo)
photo_label.pack()

def reload_image():
    global photo
    photo = ImageTk.PhotoImage(Image.open('F:\\APOD\\bad.jpeg'))
    photo_label.config(image=photo)

def error():
    if year_entry.get() == '' or month_entry.get() == '' or day_entry.get() == '':
        reload_image()
        return True

    if year_entry.get().isdecimal() == False or month_entry.get().isdecimal() == False or day_entry.get().isdecimal() == False:
        messagebox.showerror("Error!", "Values must contain positive numbers")
        return True

    if year_entry.get() == '0' or month_entry.get() == '0' or day_entry.get() == '0':
        messagebox.showerror("Error!", "There can't be 0 in any entry")
        return True

    if int(month_entry.get())>12:
        messagebox.showerror("Error!", "There are 12 months")
        return True

    max_day = monthrange(int(year_entry.get()), int(month_entry.get()))
    if int(day_entry.get())>max_day[1]:
        messagebox.showerror("Error!", "Month "+month_entry.get()+" has less days")
        return True
    
    if int(month_entry.get())<10 or int(day_entry.get())<10:
        if int(month_entry.get())<10 and int(day_entry.get())<10:
            small_month='0'+month_entry.get()
            small_day='0'+day_entry.get()
            if int(year_entry.get()+small_month+small_day)>int(today.strftime("%Y%m%d")):
                messagebox.showerror("Error!", "Date can't be higher than today")
                return True
        elif int(month_entry.get())<10:
            small_month='0'+month_entry.get()
            if int(year_entry.get()+small_month+day_entry.get())>int(today.strftime("%Y%m%d")):
                messagebox.showerror("Error!", "Date can't be higher than today")
                return True
        elif int(day_entry.get())<10:
            small_day='0'+day_entry.get()
            if int(year_entry.get()+month_entry.get()+small_day)>int(today.strftime("%Y%m%d")):
                messagebox.showerror("Error!", "Date can't be higher than today")
                return True

    if int(year_entry.get()+month_entry.get()+day_entry.get())>int(today.strftime("%Y%m%d")):
        messagebox.showerror("Error!", "Date can't be higher than today")
        return True

    if int(month_entry.get())<10 or int(day_entry.get())<10:
        if int(month_entry.get())<10 and int(day_entry.get())<10:
            small_month='0'+month_entry.get()
            small_day='0'+day_entry.get()
            if int(year_entry.get()+small_month+small_day)<20150101:
                messagebox.showerror("Error!", "Nasa oldest APOD is from January 1st 2015")
                return True
        elif int(month_entry.get())<10:
            small_month='0'+month_entry.get()
            if int(year_entry.get()+small_month+day_entry.get())<20150101:
                messagebox.showerror("Error!", "Nasa oldest APOD is from January 1st 2015")
                return True
        elif int(day_entry.get())<10:
            small_day='0'+day_entry.get()
            if int(year_entry.get()+month_entry.get()+small_day)<20150101:
                messagebox.showerror("Error!", "Nasa oldest APOD is from January 1st 2015")
                return True
    elif int(year_entry.get()+month_entry.get()+day_entry.get())<20150101:
            messagebox.showerror("Error!", "Nasa oldest APOD is from January 1st 2015")
            return True
    


def search_api():
    search_button.config(state='disabled')
    if error() == True:
        search_button.config(state='enabled')
        return
    date = {'date':year_entry.get()+'-'+month_entry.get()+'-'+day_entry.get()}
    response = requests.get(nasa_apod+api_key, params=date)

    #print(response.status_code)
    #print(response.json()['url'])
    urllib.request.urlretrieve(response.json()['url'], 'bad.jpeg')
    reload_image()
    search_button.config(state='enabled')

search_button = Button(upframe, text="search", command=search_api)
search_button.grid(row=0, column=3)

root.mainloop()