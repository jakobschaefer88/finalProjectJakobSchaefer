import requests
import datetime
from django.conf import settings
from .base import BaseWidget

class TennisWidget(BaseWidget):
    name = 'tennis'
    template_name = "calendarApp/widgets/tennis.html"

    api_key = settings.API_KEY_SPORTSDATA
    league_id = "4410"  # Tennis

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
                matches = []

                for event in events:
                    matches.append({
                        "home_team": event.get("strHomeTeam"),
                        "away_team": event.get("strAwayTeam"),
                        "home_score": event.get("intHomeScore"),
                        "away_score": event.get("intAwayScore"),
                        "status": event.get("strStatus")
                    })

                self._cached_data = matches
                self._cache_date = today
                return matches

        except Exception:
            return [{"error": "Unable to fetch Tennis match scores."}]

    def get_context_data(self, user=None, config=None):
        return {
            "matches": self.get_scores()
        }