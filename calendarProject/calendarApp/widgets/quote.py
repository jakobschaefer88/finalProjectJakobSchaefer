'''
INF601 - Programming in Python
Final Project
I, Jakob Schaefer, affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials.
I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards.
I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies.
By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.

Quote Widget

'''
import requests
import datetime
from .base import BaseWidget

#widget for quote
class QuoteWidget(BaseWidget):
    name = 'quoteWidget'
    template_name = "calendarApp/widgets/quote.html"

    api_url = "https://zenquotes.io/api/random"

    _cached_quote = None
    _cache_date = None

    def get_quote(self):
        today = datetime.date.today()

        if self._cache_date == today and self._cached_quote:
            return self._cached_quote

        try:
            response = requests.get(self.api_url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list) and len(data) > 0:
                    quote = data[0].get("q", "")
                    self._cached_quote = quote
                    self._cache_date = today
                    return quote

            #raise error if API is invalid
            raise ValueError("Invalid response from API")
        except Exception:
            return "No quote available today."
    # returns the context needed to render the template
    def get_context_data(self, user=None, config=None, request=None):  # added 'request=None'
        quote = self.get_quote()
        return {
            "quote": quote
        }