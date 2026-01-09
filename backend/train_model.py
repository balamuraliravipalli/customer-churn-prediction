import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

# -------------------------
# Load dataset
# -------------------------
DATA_PATH = "data/Churn_Modelling.csv"
MODEL_PATH = "backend/model.pkl"

df = pd.read_csv(DATA_PATH)

# -------------------------
# Define features & target
# -------------------------
X = df.drop(columns=["Exited", "CustomerId", "Surname", "RowNumber"])
y = df["Exited"]

categorical_features = ["Geography", "Gender"]
numerical_features = [col for col in X.columns if col not in categorical_features]

# -------------------------
# Preprocessing
# -------------------------
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numerical_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
    ]
)

# -------------------------
# Pipeline
# -------------------------
pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(
            n_estimators=200,
            random_state=42,
            n_jobs=-1
        )),
    ]
)

# -------------------------
# Train-test split
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# -------------------------
# Train model
# -------------------------
pipeline.fit(X_train, y_train)

# -------------------------
# Save model
# -------------------------
joblib.dump(pipeline, MODEL_PATH)
print(f"✅ Model trained and saved to {MODEL_PATH}")
