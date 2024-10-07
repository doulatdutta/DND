# ipo/backend_developer.py

class IPO_BackendDeveloper:
    def __init__(self, predictions, companies):
        self.predictions = predictions
        self.companies = companies

    def set_alerts(self):
        for company, prob in zip(self.companies, self.predictions):
            if prob > 0.75:  # Threshold for alert
                print(f"Alert: {company} has a high predicted probability of {prob:.2f} for price increase.")

if __name__ == "__main__":
    predictions = [0.72, 0.88, 0.65]  # Example predictions
    companies = ['COMPANY_A', 'COMPANY_B', 'COMPANY_C']  # Example companies
    backend = IPO_BackendDeveloper(predictions, companies)
    backend.set_alerts()
