import requests
import datetime
from .base import BaseWidget

class JokeWidget(BaseWidget):
    name = 'jokeWidget'
    template_name = "calendarApp/widgets/joke_widget.html"

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
        except Exception:
            return {
                "setup": "Why don't scientists trust atoms?",
                "punchline": "Because they make up everything!"
            }

    def get_context_data(self, user=None, config=None):
        return {
            "joke": self.get_joke()
        }