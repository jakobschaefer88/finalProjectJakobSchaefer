import requests
import datetime
from .base import BaseWidget

class WordOfDayWidget(BaseWidget):
    name = 'word_of_the_day'
    template_name = "calendarApp/widgets/wordOfDay.html"

    api_url = "https://random-word-api.herokuapp.com/word"

    _cached_word = None
    _cache_date = None

    def get_word(self):
        today = datetime.date.today()

        # Check if the word is already cached for today
        if self._cache_date == today and self._cached_word:
            return self._cached_word

        try:
            response = requests.get(self.api_url, timeout=5)
            if response.status_code == 200:
                word_data = response.json()
                if word_data:
                    word = word_data[0]  # Get the random word from the response
                    self._cached_word = {
                        'word': word
                    }
                    self._cache_date = today
                    return self._cached_word
            else:
                return {}

        except Exception:
            return {}

    def get_context_data(self, user=None, config=None, request=None):  # added 'request=None'
        word_data = self.get_word()
        return {
            "word_of_the_day": word_data
        }