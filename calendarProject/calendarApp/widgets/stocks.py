'''
INF601 - Programming in Python
Final Project
I, Jakob Schaefer, affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials.
I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards.
I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies.
By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.

Stocks Widget

'''

import yfinance as yf
import datetime
from .base import BaseWidget

#Stock widget
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
                        "price": round(latest_data["Close"], 2), # rounds the closing price
                        "timestamp": latest_data.name.strftime("%Y-%m-%d %H:%M:%S")
                    })
                else:
                    stock_data.append({
                        "name": display_name,
                        "price": "Error: No data",
                        "timestamp": None
                    })

            #returns an error if API fails
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