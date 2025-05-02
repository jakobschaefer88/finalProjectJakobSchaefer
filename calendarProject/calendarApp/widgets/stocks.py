import requests
import datetime
from django.conf import settings
from .base import BaseWidget

class StocksWidget(BaseWidget):
    name = 'stocks'
    template_name = "calendarApp/widgets/stocks.html"

    api_key = settings.API_KEY_STOCKSAPI
    stock_symbols = ['AAPL', 'GOOGL', 'AMZN']  # Default stocks

    _cached_data = None
    _cache_date = None

    def get_stock_data(self):
        today = datetime.date.today()

        # Check if the data is already cached for today
        if self._cache_date == today and self._cached_data:
            return self._cached_data

        stock_data = []
        for symbol in self.stock_symbols:
            try:
                url = f"https://www.alphavantage.co/query"
                params = {
                    "function": "TIME_SERIES_INTRADAY",
                    "symbol": symbol,
                    "interval": "5min",  # 5-minute interval data (can be adjusted)
                    "apikey": self.api_key
                }

                # Send request to Alpha Vantage API
                response = requests.get(url, params=params, timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    time_series = data.get("Time Series (5min)", {})
                    latest_time = next(iter(time_series))  # Get the most recent timestamp
                    latest_data = time_series[latest_time]
                    stock_data.append({
                        "symbol": symbol,
                        "price": latest_data.get("4. close", "N/A"),
                        "timestamp": latest_time
                    })
                else:
                    stock_data.append({
                        "symbol": symbol,
                        "price": "Error fetching data",
                        "timestamp": None
                    })

            except Exception:
                stock_data.append({
                    "symbol": symbol,
                    "price": "Error fetching data",
                    "timestamp": None
                })

        # Cache the stock data for today
        self._cached_data = stock_data
        self._cache_date = today
        return stock_data

    def get_context_data(self, user=None, config=None):
        return {
            "stocks": self.get_stock_data()
        }