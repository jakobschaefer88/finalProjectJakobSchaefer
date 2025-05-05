'''
INF601 - Programming in Python
Final Project
I, Jakob Schaefer, affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials.
I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards.
I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies.
By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.

Joke Widget

'''

import requests
import datetime
from .base import BaseWidget

#Widget that displays a joke
class JokeWidget(BaseWidget):
    name = 'jokeWidget'
    template_name = "calendarApp/widgets/joke.html"

    api_url = "https://official-joke-api.appspot.com/random_joke"

    _cached_joke = None
    _cache_date = None

    def get_joke(self):
        today = datetime.date.today()

        # Use cached joke if available and up to date
        if self._cache_date == today and self._cached_joke:
            return self._cached_joke

        try:
            response = requests.get(self.api_url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                joke = {
                    "setup": data.get("setup", ""),
                    "punchline": data.get("punchline", "")
                }
                if joke["setup"] and joke["punchline"]:
                    self._cached_joke = joke
                    self._cache_date = today
                    return joke
            raise ValueError("Invalid joke response.")
        #fallback if API fails
        except Exception:
            return {
                "setup": "Why don't scientists trust atoms?",
                "punchline": "Because they make up everything!"
            }

    # returns the context needed to render the template
    def get_context_data(self, user=None, config=None, request=None):  # added 'request=None'
        return {
            "joke": self.get_joke()
        }