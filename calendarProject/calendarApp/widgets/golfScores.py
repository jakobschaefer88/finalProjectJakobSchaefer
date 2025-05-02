import requests
import datetime
from django.conf import settings
from .base import BaseWidget

class GolfWidget(BaseWidget):
    name = 'golf'
    template_name = "calendarApp/widgets/golf.html"

    api_key = settings.API_KEY_SPORTSDATA
    league_id = "4424"  # PGA Tour

    _cached_data = None
    _cache_date = None

    def get_recent_results(self):
        today = datetime.date.today()

        if self._cache_date == today and self._cached_data:
            return self._cached_data

        try:
            url = f"https://www.thesportsdb.com/api/v1/json/{self.api_key}/eventspastleague.php"
            params = {"id": self.league_id}
            response = requests.get(url, params=params, timeout=5)

            if response.status_code == 200:
                data = response.json()
                events = data.get("events", [])[:3]  # Most recent 3 events

                results = []
                for event in events:
                    results.append({
                        "name": event.get("strEvent"),
                        "date": event.get("dateEvent"),
                        "winner": event.get("strResult"),
                    })

                self._cached_data = results
                self._cache_date = today
                return results

        except Exception:
            return [{"error": "Unable to fetch recent golf results."}]

    def get_context_data(self, user=None, config=None):
        return {
            "tournaments": self.get_recent_results()
        }