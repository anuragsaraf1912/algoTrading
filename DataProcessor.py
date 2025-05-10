import pandas as pd

class DataProcessor():
    def __init__(self, data, ticker=None):
        self.__data = data
        self.original_data = data.copy()
        self.ticker = ticker

    def multiToSingleIndexCol(self):
        """
        Corrects the multi-index columns to a single index in case of a single ticker
        """
        if isinstance(self.__data.columns, pd.MultiIndex):
            tick = self.__data.columns.get_level_values(1)[0]
            self.__data = self.__data.xs(tick, axis=1, level="Ticker")
            self.ticker = tick
        return self
    
    def resetData(self):
        """
        Resets the data to its original state
        """
        self.__data = self.original_data.copy()
        return self
    
    @property
    def data(self):
        return self.__data.copy()