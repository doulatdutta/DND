# historical/frontend_developer.py

import matplotlib.pyplot as plt
import pandas as pd

class HistoricalFrontendDeveloper:
    def __init__(self, historical_data):
        self.historical_data = historical_data

    def visualize_stock_performance(self):
        plt.figure(figsize=(14, 7))
        plt.plot(self.historical_data['Date'], self.historical_data['Close'], label='Closing Price', color='blue')
        plt.plot(self.historical_data['Date'], self.historical_data['Moving_Average'], label='20-Day Moving Average', color='orange')
        plt.title('Historical Stock Performance')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    historical_data = pd.DataFrame()  # Replace with actual historical stock data
    # historical_data = pd.read_csv('historical_stock_data.csv')  # Load your historical data

    frontend = HistoricalFrontendDeveloper(historical_data)
    frontend.visualize_stock_performance()
