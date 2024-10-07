# historical/backend_developer.py

import pandas as pd

class HistoricalBackendDeveloper:
    def __init__(self, historical_data):
        self.historical_data = historical_data

    def set_alerts(self):
        for index, row in self.historical_data.iterrows():
            if row['Rating'] == 'Buy':
                print(f"Alert: {row['Date']} - Consider buying stock at price: {row['Close']:.2f}")
            elif row['Rating'] == 'Sell':
                print(f"Alert: {row['Date']} - Consider selling stock at price: {row['Close']:.2f}")

if __name__ == "__main__":
    historical_data = pd.DataFrame()  # Replace with actual historical stock data
    # historical_data = pd.read_csv('historical_stock_data.csv')  # Load your historical data

    backend = HistoricalBackendDeveloper(historical_data)
    backend.set_alerts()
