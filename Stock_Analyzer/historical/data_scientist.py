# historical/data_scientist.py

import pandas as pd
import numpy as np

class HistoricalDataScientist:
    def __init__(self, historical_data):
        self.historical_data = historical_data

    def feature_engineering(self):
        # Create additional features for analysis
        self.historical_data['Returns'] = self.historical_data['Close'].pct_change()
        self.historical_data['Moving_Average'] = self.historical_data['Close'].rolling(window=20).mean()
        self.historical_data['Volatility'] = self.historical_data['Returns'].rolling(window=20).std()
        self.historical_data.dropna(inplace=True)  # Remove rows with NaN values

    def rate_stocks(self):
        # Create a rating system based on moving average and volatility
        self.historical_data['Rating'] = np.where(
            (self.historical_data['Returns'] > 0) & (self.historical_data['Volatility'] < 0.02), 'Buy',
            np.where(self.historical_data['Returns'] < 0, 'Sell', 'Hold')
        )
        return self.historical_data[['Date', 'Close', 'Moving_Average', 'Volatility', 'Rating']]

if __name__ == "__main__":
    # Example usage
    historical_data = pd.DataFrame()  # Replace with actual historical stock data
    # historical_data = pd.read_csv('historical_stock_data.csv')  # Load your historical data

    scientist = HistoricalDataScientist(historical_data)
    scientist.feature_engineering()
    rated_stocks = scientist.rate_stocks()
    print(rated_stocks)
