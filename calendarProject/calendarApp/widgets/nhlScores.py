import requests
import datetime
from django.conf import settings
from .base import BaseWidget

class NHLWidget(BaseWidget):
    name = 'nhl'
    template_name = "calendarApp/widgets/nhlScores.html"

    api_key = settings.API_KEY_SPORTSDATA
    league_id = "4387"  # NHL

    _cached_data = None
    _cache_date = None

    def get_scores(self):
        today = datetime.date.today()

        if self._cache_date == today and self._cached_data:
            return self._cached_data

        try:
            url = f"https://www.thesportsdb.com/api/v1/json/{self.api_key}/eventsday.php"
            params = {
                "d": today.isoformat(),
                "l": self.league_id,
            }

            response = requests.get(url, params=params, timeout=5)

            if response.status_code == 200:
                data = response.json()
                events = data.get("events", [])
                games = []

                for event in events:
                    games.append({
                        "home_team": event.get("strHomeTeam"),
                        "away_team": event.get("strAwayTeam"),
                        "home_score": event.get("intHomeScore"),
                        "away_score": event.get("intAwayScore"),
                        "status": event.get("strStatus")
                    })

                self._cached_data = games
                self._cache_date = today
                return games

        except Exception:
            return [{"error": "Unable to fetch NHL scores."}]

    def get_context_data(self, user=None, config=None):
        return {
            "games": self.get_scores()
        }