# ipo/data_engineer.py

import pandas as pd
import yfinance as yf

class IPO_DataEngineer:
    def __init__(self):
        self.ipo_data = []

    def gather_historical_ipo_data(self, symbols):
        for symbol in symbols:
            stock_data = yf.Ticker(symbol).history(period="1y")
            stock_data['Symbol'] = symbol
            self.ipo_data.append(stock_data)

    def get_ipo_data(self):
        return pd.concat(self.ipo_data)

if __name__ == "__main__":
    engineer = IPO_DataEngineer()
    ipos = ['COMPANY_A', 'COMPANY_B']  # Replace with actual IPO symbols
    engineer.gather_historical_ipo_data(ipos)
    ipo_data_df = engineer.get_ipo_data()
    print(ipo_data_df)
