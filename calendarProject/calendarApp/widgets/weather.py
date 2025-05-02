import requests
import datetime
from django.conf import settings
from .base import BaseWidget

class WeatherWidget(BaseWidget):
    name = 'weather'
    template_name = "calendarApp/widgets/weather.html"

    api_key = settings.API_KEY_OPENWEATHER
    url = "http://api.openweathermap.org/data/2.5/weather"

    _cached_weather = None
    _cache_date = None

    def get_weather(self, city):
        today = datetime.date.today()

        # Check if the data is already cached for today
        if self._cache_date == today and self._cached_weather and self._cached_weather.get("city") == city:
            return self._cached_weather

        try:
            params = {
                "q": city,  # City (dynamic input)
                "appid": self.api_key,
                "units": "metric",
                "lang": "en",
            }
            response = requests.get(self.url, params=params, timeout=5)
            if response.status_code == 200:
                data = response.json()
                weather = {
                    "city": city,
                    "temperature": data['main']['temp'],
                    "description": data['weather'][0]['description'],
                    "humidity": data['main']['humidity'],
                    "wind_speed": data['wind']['speed'],
                    "icon": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"  # Weather icon
                }
                self._cached_weather = weather
                self._cache_date = today
                return weather
            else:
                return {}

        except Exception:
            return {}

    def get_context_data(self, user=None, config=None):
        city = config.get('city', 'London')  # Default city if not provided
        weather_data = self.get_weather(city)
        return {
            "weather": weather_data,
            "city": city
        }