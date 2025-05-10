import pandas as pd

class DataProcessor():
    def __init__(self, data):
        self.data = data
        self.original_data = data.copy()

    def processMultiColumns(self):
        """
        Corrects the multi-index columns to a single index in case of a single ticker
        """
        self.data.columns = [col.lower() for col in self.data.columns]
        self.data.rename(columns={'date': 'datetime'}, inplace=True)
        return self.data