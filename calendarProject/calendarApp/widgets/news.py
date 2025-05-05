'''
INF601 - Programming in Python
Final Project
I, Jakob Schaefer, affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials.
I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards.
I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies.
By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.

News Widget

'''

import requests
import datetime
from django.conf import settings
from .base import BaseWidget

#Widget that displays 2 or 3 news articles
class NewsWidget(BaseWidget):
    name = 'newsWidget'
    template_name = "calendarApp/widgets/news.html"

    api_url = "https://newsapi.org/v2/top-headlines"
    api_key = settings.API_KEY_NEWSAPI

    _cached_news = None
    _cache_date = None

    #Gets top US news headlines
    def get_news(self):
        today = datetime.date.today()

        # Use cached headlines if available
        if self._cache_date == today and self._cached_news:
            return self._cached_news

        try:
            #pulls 3 US news headlines
            params = {
                "country": "us",         # Can be customized later
                "pageSize": 3,           # Limit to 2–3 headlines
                "apiKey": self.api_key
            }
            response = requests.get(self.api_url, params=params, timeout=5)
            if response.status_code == 200:
                data = response.json()
                articles = data.get("articles", [])
                #gets the title and url for each article
                headlines = [{
                    "title": article.get("title", "No Title"),
                    "url": article.get("url", "#")
                } for article in articles[:3]]

                self._cached_news = headlines
                self._cache_date = today
                return headlines

            #error if API fails
            raise ValueError("Invalid API response.")
        except Exception:
            return [{
                "title": "News unavailable at the moment.",
                "url": "#"
            }]

    # returns the context needed to render the template
    def get_context_data(self, user=None, config=None, request=None):  # added 'request=None'
        return {
            "headlines": self.get_news()
        }