import joblib
import os

# Path to model file
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'issue_classifier.pkl')

# Load the trained model
model = joblib.load(MODEL_PATH)

def predict_category(description: str) -> str:
    if not description:
        return "unknown"
    return model.predict([description])[0]
