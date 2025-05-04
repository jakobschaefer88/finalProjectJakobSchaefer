import requests
import datetime
from .base import BaseWidget

class FortuneCookieWidget(BaseWidget):
    name = 'fortuneCookie'
    template_name = "calendarApp/widgets/fortuneCookie.html"

    api_url = "https://api.adviceslip.com/advice"

    _cached_fortune = None
    _cache_date = None

    def get_fortune(self):
        today = datetime.date.today()

        # If today's fortune is already cached, return it
        if self._cache_date == today and self._cached_fortune:
            return self._cached_fortune

        try:
            response = requests.get(self.api_url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                fortune = data.get("slip", {}).get("advice", "")
                if fortune:
                    self._cached_fortune = fortune
                    self._cache_date = today
                    return fortune
            raise ValueError("Invalid response from API.")
        except Exception:
            return "No fortune available today."

    def get_context_data(self, user=None, config=None, request=None):  # added 'request=None'
        return {
            "fortune": self.get_fortune()
        }