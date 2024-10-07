# select_company/frontend_developer.py

import matplotlib.pyplot as plt

class CompanyFrontendDeveloper:
    def __init__(self, predictions, company):
        self.predictions = predictions
        self.company = company

    def create_visualizations(self):
        plt.figure(figsize=(10, 6))
        plt.bar(range(len(self.predictions)), self.predictions)
        plt.title(f'Stock Movement Predictions for {self.company}')
        plt.xlabel('Time Period')
        plt.ylabel('Predicted Probability')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    predictions = [0.75, 0.80, 0.65]  # Example predictions
    developer = CompanyFrontendDeveloper(predictions, 'AAPL')
    developer.create_visualizations()
