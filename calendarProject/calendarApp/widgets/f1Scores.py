import requests
import datetime
from .base import BaseWidget

class F1Widget(BaseWidget):
    name = 'f1'
    template_name = "calendarApp/widgets/f1.html"

    _cached_data = None
    _cache_date = None

    def get_latest_results(self):
        today = datetime.date.today()

        if self._cache_date == today and self._cached_data:
            return self._cached_data

        try:
            url = "https://ergast.com/api/f1/current/last/results.json"
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                data = response.json()
                race_data = data["MRData"]["RaceTable"]["Races"][0]

                race_info = {
                    "race_name": race_data["raceName"],
                    "circuit": race_data["Circuit"]["circuitName"],
                    "date": race_data["date"],
                    "results": []
                }

                for result in race_data["Results"][:3]:  # Top 3
                    race_info["results"].append({
                        "position": result["position"],
                        "driver": f"{result['Driver']['givenName']} {result['Driver']['familyName']}",
                        "constructor": result["Constructor"]["name"],
                        "time": result.get("Time", {}).get("time", result.get("status"))
                    })

                self._cached_data = race_info
                self._cache_date = today
                return race_info

        except Exception:
            return {"error": "Unable to fetch Formula 1 results."}

    def get_context_data(self, user=None, config=None):
        return {
            "race": self.get_latest_results()
        }