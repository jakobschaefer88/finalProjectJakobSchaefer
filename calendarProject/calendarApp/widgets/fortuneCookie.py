'''
INF601 - Programming in Python
Final Project
I, Jakob Schaefer, affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials.
I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards.
I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies.
By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.

Fortune Cookie Widget

'''

import requests
import datetime
from .base import BaseWidget

#Widget that displays a fortune message
class FortuneCookieWidget(BaseWidget):
    name = 'fortuneCookie'
    template_name = "calendarApp/widgets/fortuneCookie.html"

    api_url = "https://api.adviceslip.com/advice"

    #caching to avoid fetching the same fortune multiple times
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
            #fallback message if API fails
            raise ValueError("Invalid response from API.")
        except Exception:
            return "No fortune available today."

    #returns the context needed to render the template
    def get_context_data(self, user=None, config=None, request=None):  # added 'request=None'
        return {
            "fortune": self.get_fortune()
        }