import requests
import datetime
from django.conf import settings
from .base import BaseWidget

class TVShowsWidget(BaseWidget):
    name = 'tv_shows'
    template_name = "calendarApp/widgets/tvShow.html"

    api_key = settings.API_KEY_TVSHOWAPI
    url = "https://api.themoviedb.org/3/tv/popular"

    _cached_shows = None
    _cache_date = None

    def get_tv_shows(self):
        """Fetch the top-rated TV shows."""
        if self._cache_date == datetime.date.today() and self._cached_shows:
            return self._cached_shows

        try:
            params = {
                "api_key": self.api_key,
                "language": "en-US",
                "page": 1  # Fetch the first page of TV shows
            }
            response = requests.get(self.url, params=params, timeout=5)
            if response.status_code == 200:
                data = response.json()
                tv_shows = data['results'][:5]  # Get the top 5 shows
                shows = [{
                    'name': show['name'],
                    'rating': show.get('vote_average', 'N/A'),
                    'image': f"https://image.tmdb.org/t/p/w500{show['poster_path']}" if show.get('poster_path') else None
                } for show in tv_shows]

                self._cached_shows = shows
                self._cache_date = datetime.date.today()
                return shows
            else:
                return []

        except Exception:
            return []

    def get_context_data(self, user=None, config=None, request=None):  # added 'request=None'
        return {
            "tv_shows": self.get_tv_shows()
        }