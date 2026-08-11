from pathlib import Path

# Backend root directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Data paths
DATA_DIR = BASE_DIR / "data" / "raw"
MODEL_DIR = BASE_DIR / "trained_models"

# Files
DATASET_PATH = DATA_DIR / "hyderabad_food_outlets_with_features.csv"
MODEL_PATH = MODEL_DIR / "food_success_model.pkl"
SCALER_PATH = MODEL_DIR / "scaler.pkl"
