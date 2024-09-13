from app.stock_api import StockAPI
from app.utils import exponential_smoothing
import pandas as pd

class StockService:
    def __init__(self):
        self.api = StockAPI()

    def get_stock_data(self, symbol: str, start_date: str, end_date: str):
        """
        Fetch stock data and filter by the date range.
        """
        # Fetch stock data using StockAPI (use get_daily_stock_data)
        stock_data = self.api.get_daily_stock_data(symbol)

        # Ensure the dates are properly formatted
        try:
            start_date = pd.to_datetime(start_date)
            end_date = pd.to_datetime(end_date)
        except Exception as e:
            raise ValueError(f"Error parsing dates: {e}")

        # Filter stock data by date range
        stock_data = stock_data[(stock_data.index >= start_date) & (stock_data.index <= end_date)]

        if stock_data.empty:
            raise ValueError(f"No data available for {symbol} between {start_date.date()} and {end_date.date()}")

        return stock_data

    def apply_exponential_smoothing(self, data):
        """
        Apply exponential smoothing to the stock data.
        """
        return exponential_smoothing(data, alpha=0.2)