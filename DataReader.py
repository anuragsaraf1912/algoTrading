import pandas as pd
import yfinance as yf

class DataReader:
    def __init__(self):
        self._interval = '1d'

    def setInterval(self, interval):
        """
        Set the interval for fetching stock data.
        Args:
            interval (str): The interval for fetching data (1m,2m,5m,15m, 60m,90m,1h,1d,5d,1wk,1mo,3mo).
        """
        if interval not in ['1m','2m','5m','15m', '60m','90m','1h','1d','5d','1wk','1mo','3mo']:
            raise ValueError("Invalid interval. Choose from '1m','2m','5m','15m', '60m','90m','1h','1d','5d','1wk','1mo','3mo'")
        self._interval = interval


    def _read_data_file(self, file_path):
        try:
            data = pd.read_csv(file_path)
            return data
        except Exception as e:
            raise ValueError(f"Error reading file: {e}") 
    
    def _read_data_yahoo(self, args):
        """
        Fetch stock price data from Yahoo Finance.

        Args:
            ticker (str): The stock ticker symbol.
            start_date (str): The start date for fetching data (YYYY-MM-DD).
            end_date (str): The end date for fetching data (YYYY-MM-DD).

        Returns:
            pd.DataFrame: Stock price data as a DataFrame.
        """
        try:
            ticker, start_date, end_date = args
            data = yf.download(ticker, start=start_date, end=end_date, interval=self._interval)
            return data
        except Exception as e:
            raise ValueError(f"Error fetching data from yfinance: {e}")

    def get_data(self, *args):
        """
        Fetch stock price data from a file or a tuple (ticker, start_date, end_date).

        Args:
            source (str or tuple): If single entry, the file path to read data from.
                If three entries, the entries should be in order ticker, start_date, end_date.

        Returns:
            pd.DataFrame: Stock price data as a DataFrame.
        """
        if len(args) == 1: return self._read_data_source(args[0])
        
        elif len(args) == 3:
            return self._read_data_yahoo(args)
        else:
            raise ValueError("Invalid source. Provide a file path or ticker, start_date, end_date.")