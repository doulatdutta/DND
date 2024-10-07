# overall_next_day/backend_developer.py

class OverallBackendDeveloper:
    def __init__(self, predictions, companies):
        self.predictions = predictions
        self.companies = companies

    def set_alerts(self):
        for company, prob in zip(self.companies, self.predictions):
            if prob > 0.8:
                print(f"Alert: {company} has a high predicted probability of {prob:.2f} for price increase.")

if __name__ == "__main__":
    predictions = [0.75, 0.85, 0.90, 0.80, 0.65]  # Example predictions
    companies = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']  # Example companies
    backend = OverallBackendDeveloper(predictions, companies)
    backend.set_alerts()
