from .base import BaseWidget
import requests
import random
import datetime

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
            response = requests.get(f"{self.api_url}?key={self.api_key}", timeout=5)
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list) and len(data) > 0:
                    quote = data[0].get("q", "")
                    self._cached_quote = quote
                    self._cache_date = today
                    return quote

            raise ValueError("Invalid response from API")
        except Exception:
            return "No quote available today."

    def get_context_data(self, user=None, config=None):
        quote = self.get_quote()
        return {
            "quote": quote
        }