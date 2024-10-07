# select_sector/backend_developer.py

class SectorBackendDeveloper:
    def __init__(self, predictions):
        self.predictions = predictions

    def set_alerts(self):
        for company, prob in self.predictions.items():
            if prob > 0.8:
                print(f"Alert: Consider buying {company} stock! Probability: {prob:.2f}")

if __name__ == "__main__":
    predictions = {'AAPL': 0.85, 'GOOGL': 0.78}
    backend = SectorBackendDeveloper(predictions)
    backend.set_alerts()
