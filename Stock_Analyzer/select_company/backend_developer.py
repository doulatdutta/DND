# select_company/backend_developer.py

class CompanyBackendDeveloper:
    def __init__(self, predictions):
        self.predictions = predictions

    def set_alerts(self):
        for i, prob in enumerate(self.predictions):
            if prob > 0.8:
                print(f"Alert: High probability for movement at index {i} - Probability: {prob:.2f}")

if __name__ == "__main__":
    predictions = [0.75, 0.85, 0.90]  # Example predictions
    backend = CompanyBackendDeveloper(predictions)
    backend.set_alerts()
