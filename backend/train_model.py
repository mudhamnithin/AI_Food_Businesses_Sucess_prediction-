import os
import joblib
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

from imblearn.over_sampling import SMOTE

import seaborn as sns
import matplotlib.pyplot as plt

# ==========================================================
# Configuration
# ==========================================================

DATASET_PATH = "data/raw/hyderabad_food_outlets_with_features.csv"
MODEL_DIR = "trained_models"

FEATURE_COLUMNS = [
    "footfall_index",
    "nearby_shops_count",
    "nearby_offices_count",
    "nearby_colleges_count",
    "nearby_hospitals_count",
    "nearby_restaurants_count",
    "nearby_parks_count",
    "distance_to_nearest_brand_chai",
    "rent_estimate",
    "avg_income_area",
]


# ==========================================================
# Load Dataset
# ==========================================================

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_csv(DATASET_PATH)

print(f"Dataset Shape : {df.shape}")

df[FEATURE_COLUMNS] = df[FEATURE_COLUMNS].fillna(
    df[FEATURE_COLUMNS].median(numeric_only=True)
)


# ==========================================================
# Generate Success Labels
# ==========================================================

base_score = (
    df["footfall_index"] * 0.40
    + df["avg_income_area"] * 0.30
    + df["rent_estimate"] * 0.15
    + df["nearby_offices_count"] * 0.10
    + df["nearby_colleges_count"] * 0.05
    - df["nearby_shops_count"] * 0.25
)

df["success_score_norm"] = (base_score - base_score.min()) / (
    base_score.max() - base_score.min()
)

rng = np.random.default_rng(42)

df["success_score_norm"] += rng.normal(
    0,
    0.05,
    len(df),
)

df["success_score_norm"] = df["success_score_norm"].clip(0, 1)

df["success_label"] = np.where(
    df["success_score_norm"] > 0.20,
    1,
    0,
)


# ==========================================================
# Label Distribution
# ==========================================================

print("\n")
print("=" * 60)
print("Label Distribution")
print("=" * 60)

counts = df["success_label"].value_counts()

print(counts)

ratio = counts[1] / len(df) * 100

print(f"\nSuccess Ratio : {ratio:.2f}%")


# ==========================================================
# Train Test Split
# ==========================================================

X = df[FEATURE_COLUMNS]

y = df["success_label"]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)


# ==========================================================
# SMOTE
# ==========================================================

print("\n")
print("=" * 60)
print("Applying SMOTE...")
print("=" * 60)

smote = SMOTE(random_state=42)

X_train, y_train = smote.fit_resample(
    X_train,
    y_train,
)

print("Balanced Classes")

print(np.bincount(y_train))


# ==========================================================
# Model
# ==========================================================

print("\n")
print("=" * 60)
print("Training Random Forest...")
print("=" * 60)

model = RandomForestClassifier(
    n_estimators=350,
    max_depth=12,
    min_samples_leaf=3,
    min_samples_split=4,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1,
)

model.fit(
    X_train,
    y_train,
)


# ==========================================================
# Evaluation
# ==========================================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    y_pred,
)

print("\n")
print("=" * 60)
print(f"Accuracy : {accuracy*100:.2f}%")
print("=" * 60)

print(
    classification_report(
        y_test,
        y_pred,
    )
)


# ==========================================================
# Cross Validation
# ==========================================================

scores = cross_val_score(
    model,
    X_scaled,
    y,
    cv=5,
)

print(f"\nCross Validation : {scores.mean()*100:.2f}% ± {scores.std()*100:.2f}%")


# ==========================================================
# Feature Importance
# ==========================================================

importance = pd.DataFrame(
    {"Feature": FEATURE_COLUMNS, "Importance": model.feature_importances_}
)

importance = importance.sort_values(
    by="Importance",
    ascending=False,
)

print("\n")
print("=" * 60)
print("Feature Importance")
print("=" * 60)

print(importance)

plt.figure(figsize=(8, 5))

sns.barplot(
    data=importance,
    x="Importance",
    y="Feature",
)

plt.title("Feature Importance")

plt.tight_layout()

plt.savefig("feature_importance.png")
plt.close()


# ==========================================================
# Confusion Matrix
# ==========================================================

plt.figure(figsize=(5, 4))

sns.heatmap(
    confusion_matrix(
        y_test,
        y_pred,
    ),
    annot=True,
    fmt="d",
)

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.title("Confusion Matrix")

plt.tight_layout()

plt.savefig("feature_importance.png")
plt.close()


# ==========================================================
# Save Model
# ==========================================================

print("\n")
print("=" * 60)
print("Saving Model...")
print("=" * 60)

os.makedirs(MODEL_DIR, exist_ok=True)

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "food_success_model.pkl",
)

SCALER_PATH = os.path.join(
    MODEL_DIR,
    "scaler.pkl",
)

joblib.dump(
    model,
    MODEL_PATH,
)

joblib.dump(
    scaler,
    SCALER_PATH,
)

print("\n")
print("=" * 60)
print("Training Completed Successfully")
print("=" * 60)

print(f"Model  : {MODEL_PATH}")
print(f"Scaler : {SCALER_PATH}")
print("=" * 60)
