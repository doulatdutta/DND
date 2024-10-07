# overall_next_day/frontend_developer.py

import matplotlib.pyplot as plt

class OverallFrontendDeveloper:
    def __init__(self, predictions, companies):
        self.predictions = predictions
        self.companies = companies

    def create_visualizations(self):
        plt.figure(figsize=(10, 6))
        plt.bar(self.companies, self.predictions)
        plt.title('Next Day Stock Predictions')
        plt.xlabel('Companies')
        plt.ylabel('Predicted Probability of Price Increase')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    predictions = [0.75, 0.80, 0.65, 0.90, 0.85]  # Example predictions
    companies = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']  # Example companies
    developer = OverallFrontendDeveloper(predictions, companies)
    developer.create_visualizations()
