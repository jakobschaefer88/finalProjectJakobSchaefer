'''
INF601 - Programming in Python
Final Project
I, Jakob Schaefer, affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials.
I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards.
I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies.
By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.

Word of the Day Widget

'''

import requests
import datetime
from .base import BaseWidget

#Word of the Day Widget
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