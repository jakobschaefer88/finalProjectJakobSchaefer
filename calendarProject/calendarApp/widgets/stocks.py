import yfinance as yf
import datetime
from django.conf import settings
from .base import BaseWidget

class StocksWidget(BaseWidget):
    name = 'stocks'
    template_name = "calendarApp/widgets/stocks.html"

    # Map ticker symbols to friendly names
    stock_info = {
        '^GSPC': 'S&P 500',
        '^DJI': 'Dow Jones',
        '^IXIC': 'NASDAQ'
    }

    _cached_data = None
    _cache_date = None

    def get_stock_data(self):
        today = datetime.date.today()

        if self._cache_date == today and self._cached_data:
            return self._cached_data

        stock_data = []
        for symbol, display_name in self.stock_info.items():
            try:
                stock = yf.Ticker(symbol)
                historical_data = stock.history(period="1d")

                if not historical_data.empty:
                    latest_data = historical_data.iloc[-1]
                    stock_data.append({
                        "name": display_name,
                        "price": round(latest_data["Close"], 2),
                        "timestamp": latest_data.name.strftime("%Y-%m-%d %H:%M:%S")
                    })
                else:
                    stock_data.append({
                        "name": display_name,
                        "price": "Error: No data",
                        "timestamp": None
                    })

            except Exception as e:
                stock_data.append({
                    "name": display_name,
                    "price": f"Error: {str(e)}",
                    "timestamp": None
                })

        self._cached_data = stock_data
        self._cache_date = today
        return stock_data

    def get_context_data(self, user=None, config=None, request=None):
        return {
            "stocks": self.get_stock_data()
        }