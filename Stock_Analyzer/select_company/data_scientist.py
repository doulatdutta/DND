# select_company/data_scientist.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

class CompanyDataScientist:
    def __init__(self, historical_data):
        self.historical_data = historical_data
        self.model = RandomForestClassifier()

    def prepare_data(self):
        self.historical_data['Returns'] = self.historical_data['Close'].pct_change()
        self.historical_data.dropna(inplace=True)
        X = self.historical_data[['Open', 'High', 'Low', 'Volume']]
        y = (self.historical_data['Returns'] > 0).astype(int)  # Binary target
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        probabilities = self.model.predict_proba(X_test)[:, 1]
        return probabilities

if __name__ == "__main__":
    # Example historical data
    historical_data = pd.DataFrame()  # Replace with actual data
    scientist = CompanyDataScientist(historical_data)
    X_train, X_test, y_train, y_test = scientist.prepare_data()
    scientist.train_model(X_train, y_train)
    predictions = scientist.predict(X_test)
    print(predictions)
