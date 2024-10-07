# overall_next_day/data_engineer.py

import yfinance as yf
import pandas as pd

class OverallDataEngineer:
    def __init__(self):
        self.top_companies = []

    def select_top_companies(self):
        # Example of predefined company symbols
        companies = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
        metrics = {}

        for company in companies:
            data = yf.Ticker(company)
            info = data.info
            metrics[company] = {
                'marketCap': info.get('marketCap', 0),
                'peRatio': info.get('trailingPE', 0),
                'dividendYield': info.get('dividendYield', 0)
            }

        # Sort companies based on market cap and select top 5
        self.top_companies = sorted(metrics.items(), key=lambda x: x[1]['marketCap'], reverse=True)[:5]

    def get_top_companies(self):
        return self.top_companies

if __name__ == "__main__":
    engineer = OverallDataEngineer()
    engineer.select_top_companies()
    top_companies = engineer.get_top_companies()
    print(top_companies)
