# select_company/data_engineer.py

import yfinance as yf
import pandas as pd

class CompanyDataEngineer:
    def __init__(self, company):
        self.company = company
        self.historical_data = None

    def collect_historical_data(self):
        self.historical_data = yf.download(self.company, period='5y')

    def get_historical_data(self):
        return self.historical_data

if __name__ == "__main__":
    company = 'AAPL'  # Example company symbol
    engineer = CompanyDataEngineer(company)
    engineer.collect_historical_data()
    data = engineer.get_historical_data()
    print(data)
