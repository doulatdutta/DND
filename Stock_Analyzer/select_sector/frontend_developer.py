# select_sector/frontend_developer.py

import matplotlib.pyplot as plt

class SectorFrontendDeveloper:
    def __init__(self, predictions):
        self.predictions = predictions

    def create_visualizations(self):
        plt.figure(figsize=(10, 6))
        plt.bar(self.predictions.index, self.predictions.values)
        plt.title('Predicted Stock Returns')
        plt.xlabel('Companies')
        plt.ylabel('Predicted Probability')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Example predictions
    predictions = {'AAPL': 0.85, 'GOOGL': 0.78}
    developer = SectorFrontendDeveloper(predictions)
    developer.create_visualizations()
