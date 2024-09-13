import yfinance as yf
import pandas as pd

class StockAPI:
    def get_daily_stock_data(self, symbol: str):
        """
        Fetches daily stock data for the given symbol using Yahoo Finance (yfinance).
        """
        try:
            # Fetch historical stock data using yfinance
            stock_data = yf.download(symbol, period='max', interval='1d')

            # Check if data is returned
            if stock_data.empty:
                raise ValueError(f"No data available for {symbol}")

            # Select only the required columns (adjust if needed)
            df = stock_data[['Open', 'High', 'Low', 'Close', 'Volume']]

            return df

        except Exception as e:
            print(f"Error fetching stock data for {symbol}: {e}")
            raise