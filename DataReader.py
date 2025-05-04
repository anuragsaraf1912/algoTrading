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
        
        # Read data from a file
        try:
            data = pd.read_csv(file_path)
            return data
        except Exception as e:
            raise ValueError(f"Error reading file: {e}") 

    def get_data(self, source):
        """
        Fetch stock price data from a file or a tuple (ticker, start_date, end_date).

        Args:
            source (str or tuple): If str, it is treated as a file path.
                                   If tuple, it should be (ticker, start_date, end_date).

        Returns:
            pd.DataFrame: Stock price data as a DataFrame.
        """
        if isinstance(source, str):
            # Fetch data from a file
            return self._read_data_source(source)
        

        elif isinstance(source, tuple) and len(source) == 3:
            # Fetch data from yfinance
            ticker, start_date, end_date = source
            try:
                data = yf.download(ticker, start=start_date, end=end_date, interval=self._interval)
                return data
            except Exception as e:
                raise ValueError(f"Error fetching data from yfinance: {e}")
        else:
            raise ValueError("Invalid source. Provide a file path or a tuple (ticker, start_date, end_date).")