# ipo/frontend_developer.py

import matplotlib.pyplot as plt

class IPO_FrontendDeveloper:
    def __init__(self, predictions, companies):
        self.predictions = predictions
        self.companies = companies

    def create_visualizations(self):
        plt.figure(figsize=(10, 6))
        plt.bar(self.companies, self.predictions)
        plt.title('IPO Stock Predictions')
        plt.xlabel('Companies')
        plt.ylabel('Predicted Probability of Price Increase')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    predictions = [0.7, 0.8, 0.6]  # Example predictions
    companies = ['COMPANY_A', 'COMPANY_B', 'COMPANY_C']  # Example companies
    developer = IPO_FrontendDeveloper(predictions, companies)
    developer.create_visualizations()
