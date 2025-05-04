import requests
import datetime
from django.conf import settings
from .base import BaseWidget

class NewsWidget(BaseWidget):
    name = 'newsWidget'
    template_name = "calendarApp/widgets/news.html"

    api_url = "https://newsapi.org/v2/top-headlines"
    api_key = settings.API_KEY_NEWSAPI

    _cached_news = None
    _cache_date = None

    def get_news(self):
        today = datetime.date.today()

        # Use cached headlines if available
        if self._cache_date == today and self._cached_news:
            return self._cached_news

        try:
            params = {
                "country": "us",         # Can be customized later
                "pageSize": 3,           # Limit to 2–3 headlines
                "apiKey": self.api_key
            }
            response = requests.get(self.api_url, params=params, timeout=5)
            if response.status_code == 200:
                data = response.json()
                articles = data.get("articles", [])
                headlines = [{
                    "title": article.get("title", "No Title"),
                    "url": article.get("url", "#")
                } for article in articles[:3]]

                self._cached_news = headlines
                self._cache_date = today
                return headlines

            raise ValueError("Invalid API response.")
        except Exception:
            return [{
                "title": "News unavailable at the moment.",
                "url": "#"
            }]

    def get_context_data(self, user=None, config=None, request=None):  # added 'request=None'
        return {
            "headlines": self.get_news()
        }