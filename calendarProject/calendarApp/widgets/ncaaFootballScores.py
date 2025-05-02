import requests
import datetime
from django.conf import settings
from .base import BaseWidget

class NCAAFootballWidget(BaseWidget):
    name = 'ncaaFootball'
    template_name = "calendarApp/widgets/ncaaFootballScores.html"

    api_url = "https://api.collegefootballdata.com/games"
    api_key = settings.API_KEY_COLLEGEFOOTBALLAPI

    _cached_data = None
    _cache_date = None

    def get_scores(self):
        today = datetime.date.today()

        if self._cache_date == today and self._cached_data:
            return self._cached_data

        try:
            params = {
                "year": today.year,
                "start": today.isoformat(),
                "end": today.isoformat(),
            }
            headers = {
                "Authorization": f"Bearer {self.api_key}"
            }

            response = requests.get(self.api_url, headers=headers, params=params, timeout=5)

            if response.status_code == 200:
                games = response.json()
                results = []

                for game in games:
                    results.append({
                        "home_team": game.get("home_team"),
                        "away_team": game.get("away_team"),
                        "home_score": game.get("home_points"),
                        "away_score": game.get("away_points"),
                        "status": game.get("status")  # e.g., "final", "in_progress", etc.
                    })

                self._cached_data = results
                self._cache_date = today
                return results

        except Exception:
            return [{"error": "Unable to fetch NCAA Football scores."}]

    def get_context_data(self, user=None, config=None):
        return {
            "games": self.get_scores()
        }