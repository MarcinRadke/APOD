import datetime
from calendar import monthrange
import requests
import urllib.request

class ApodController:

    earliest_NASA_APOD_API_date = datetime.date(2015,1,1)
    api_key = 'PoGSdWWaN1mXfdkOpHRGcGHC2edgBO00HWeEobxU'
    nasa_apod = 'https://api.nasa.gov/planetary/apod?api_key='

    def set_view(self, view):
        self.view = view

    def search_api(self, year: str, month: str, day: str):
        self.view.search_button.config(state='disabled')
        if self.error_handler(year, month, day) == True:
            self.view.search_button.config(state='normal')
            return
        date = {'date':year+'-'+month+'-'+day}
        response = requests.get(self.nasa_apod+self.api_key, params=date)

        #print(response.status_code)
        #print(response.json()['url'])
        urllib.request.urlretrieve(response.json()['url'], 'photos.jpeg')
        self.view.reload_image()
        self.view.search_button.config(state='normal')

    def error_handler(self, year: str, month: str, day: str):
        today = datetime.date.today()

        if year.isdecimal() == False or month.isdecimal() == False or day.isdecimal() == False:
            print("Error!", "Values must contain positive numbers")
            return True

        if year == '0' or month == '0' or day == '0':
            print("Error!", "There can't be 0 in any entry")
            return True
        
        if year.startswith('0') or month.startswith('0') or day.startswith('0'):
            print("Error!", "Any entry can't start with 0")
            return True

        year_int = int(year)
        month_int = int(month)
        day_int = int(day)
        
        if month_int > 12:
            print("Error!", "There are 12 months")
            return True

        max_day = monthrange(year_int, month_int)
        if day_int > max_day[1]:
            print("Error!", "Month "+month+" has less days")
            return True
        
        user_date = datetime.date(year_int, month_int, day_int)

        if today < user_date:
            print("Error!", "Date can't be higher than today")
            return True

        if self.earliest_NASA_APOD_API_date > user_date:
            print("Error!", "Nasa oldest APOD is from January 1st 2015")
            return True
