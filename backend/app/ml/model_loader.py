import joblib

from app.core.config import MODEL_PATH, SCALER_PATH


class ModelLoader:

    def __init__(self):
        self.model = joblib.load(MODEL_PATH)
        self.scaler = joblib.load(SCALER_PATH)

    def predict(self, X):
        return self.model.predict(X)

    def predict_proba(self, X):
        return self.model.predict_proba(X)

    def transform(self, X):
        return self.scaler.transform(X)


model_loader = ModelLoader()
