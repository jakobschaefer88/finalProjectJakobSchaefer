'''
INF601 - Programming in Python
Final Project
I, Jakob Schaefer, affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials.
I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards.
I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies.
By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.

Weather Widget

'''

import requests
from django.conf import settings
from .base import BaseWidget

#Weather Widget
class WeatherWidget(BaseWidget):
    name = 'weather'
    template_name = "calendarApp/widgets/weather.html"

    api_key = settings.API_KEY_OPENWEATHER
    url = "http://api.openweathermap.org/data/2.5/weather"

    _cached_weather = None
    _cache_date = None

    # gets the location of the user's device
    def get_weather_by_coords(self, lat, lon):
        try:
            params = {
                "lat": lat,
                "lon": lon,
                "appid": self.api_key,
                "units": "imperial",
                "lang": "en",
            }
            response = requests.get(self.url, params=params, timeout=5)
            if response.status_code == 200:
                data = response.json()
                return {
                    "city": data['name'],
                    "temperature": data['main']['temp'],
                    "description": data['weather'][0]['description'],
                    "humidity": data['main']['humidity'],
                    "wind_speed": data['wind']['speed'],
                    "icon": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
                }
        except Exception:
            pass
        return {}

    def get_context_data(self, user=None, config=None, request=None):
        lat = request.GET.get("lat")
        lon = request.GET.get("lon")
        if lat and lon:
            weather_data = self.get_weather_by_coords(lat, lon)
            city = weather_data.get("city", "Unknown")
        else:
            weather_data = {}
            city = "Detecting..."
        return {
            "weather": weather_data,
            "city": city
        }