# select_sector/data_engineer.py

import pandas as pd
import yfinance as yf

class SectorDataEngineer:
    def __init__(self, companies):
        self.companies = companies
        self.historical_data = {}

    def collect_historical_data(self):
        for company in self.companies:
            self.historical_data[company] = yf.download(company, period='5y')
    
    def filter_companies(self):
        # Placeholder for filtering logic
        filtered_companies = {k: v for k, v in self.historical_data.items() if v['Close'].mean() > 100}
        return filtered_companies

if __name__ == "__main__":
    companies = ['AAPL', 'GOOGL', 'MSFT']  # Example company symbols
    engineer = SectorDataEngineer(companies)
    engineer.collect_historical_data()
    filtered_data = engineer.filter_companies()
    print(filtered_data)
