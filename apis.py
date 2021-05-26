import time
import datetime

import requests
import json

#
# api_key = "a10bf15f7151ec1f279019d4dffc5a20"
# lat = "34.052235"
# lon = "-118.243683"
#
# url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
#
# response = requests.get(url)
# data = json.loads(response.text)
# print(data)


def convert_temp(kelvin):
    # find someway to properly do this later
    kelvin = float(kelvin)

    celsius = kelvin - 273.15

    faren = celsius * 1.8 + 32

    return faren


def convert_dt(raw_dt):
    dt_format = "%m/%d/%y %I:%M %p"
    new = datetime.datetime.fromtimestamp(raw_dt)
    new = new.strftime(dt_format)

    return new


class Weather:

    def __init__(self, latitude="", longitude=""):

        self.coordinates = {
            'lon': longitude,
            'lat': latitude
        }

        self.url = self.build_url()
        self.raw_data = self.get_data()

        self.location = {
            'id': "",
            'cod': "",
            'last_dt': "",
            'country': "",
            'timezone': "",
            'name': "",
            'sunrise': "",
            'sunset': ""
        }

        self.weather = {
            'main': "",
            'description': "",
            'temperatures': {
                'temp': "",
                'feels_like': "",
                'min': "",
                'max': ""
            },
            'pressure': "",
            'humidity': "",
            'visibility': "",
        }
        self.wind = {
            'speed': "",
            'deg': "",
            'gust': ""
        }

    def __str__(self):
        text = f"""
City Info:
    Name: {self.location['name'].title()} [{self.location['cod']}]
    City ID: {self.location['id']}
    Country: {self.location['country']}
    
    Coordinates: <{self.coordinates['lat']}, {self.coordinates['lon']}>
    TimeZone: {self.location['timezone']}
    
    Sunrise: \t{convert_dt(self.location['sunrise'])}
    Sunset: \t{convert_dt(self.location['sunset'])}
        
    Weather:
        Temperatures:
            Base: \t{convert_temp(self.weather['temperatures']['temp']):.2f} F    [{self.weather['temperatures']['min']}K - {self.weather['temperatures']['max']}K]
            Feels: \t{convert_temp(self.weather['temperatures']['feels_like']):.2f} F
            Min Temp: \t{convert_temp(self.weather['temperatures']['min']):.2f} F
            Max Temp: \t{convert_temp(self.weather['temperatures']['max']):.2f} F
    
        Humidity: {self.weather['humidity']} %
        Pressure: {self.weather['pressure']} hPa
    
        Wind:
            Speed: {self.wind['speed']} m/s
            Deg: {self.wind['deg']} degrees
            
"""
        return text

    def build_url(self):
        api_key = "a10bf15f7151ec1f279019d4dffc5a20"
        lat = self.coordinates['lat']
        lon = self.coordinates['lon']

        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

        return url

    def get_data(self):
        try:
            response = requests.get(self.url)
        except requests.exceptions.HTTPError as http_error:
            print(f"HTTP Error: {http_error}")
            return False
        except requests.exceptions.ConnectionError as conn_error:
            print(f"Connection Error: {conn_error}")
            return False
        except requests.exceptions.Timeout as time_error:
            print(f"Timeout Error: {time_error}")
            return False
        except requests.exceptions.RequestException as error:
            print(f"OOPS! Other Error: {error}")
            return False

        return json.loads(response.text)

    def extract_data(self):
        # Make sure its up to date
        # self.raw_data = self.get_data()

        self.location = {
            'id': self.raw_data['id'],
            'cod': self.raw_data['cod'],
            'last_dt': self.raw_data['dt'],
            'country': self.raw_data['sys']['country'],
            'timezone': self.raw_data['timezone'],
            'name': self.raw_data['name'],
            'sunrise': self.raw_data['sys']['sunrise'],
            'sunset': self.raw_data['sys']['sunset']
        }

        self.weather = {
            'main': self.raw_data['weather'][0]['main'],
            'description': self.raw_data['weather'][0]['description'],
            'temperatures': {
                'temp': self.raw_data['main']['temp'],
                'feels_like': self.raw_data['main']['feels_like'],
                'min': self.raw_data['main']['temp_min'],
                'max': self.raw_data['main']['temp_max']
            },
            'pressure': self.raw_data['main']['pressure'],
            'humidity': self.raw_data['main']['humidity'],
            'visibility': self.raw_data['visibility'],
        }
        self.wind = {
            'speed': self.raw_data['wind']['speed'],
            'deg': self.raw_data['wind']['deg'],
            # 'gust': self.raw_data['wind']['gust']
        }

        return True


if __name__ == "__main__":
    la_weather = Weather("34.052235", "-118.243683")

    la_weather.extract_data()

    print(la_weather)

