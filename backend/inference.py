import pandas as pd
import joblib
import logging
from typing import List, Dict, Any

MODEL_PATH = "backend/model.pkl"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ChurnModel:
    def __init__(self):
        self.model = self._load_model()

    def _load_model(self):
        try:
            model = joblib.load(MODEL_PATH)
            logger.info("✅ Model loaded successfully")
            return model
        except FileNotFoundError:
            logger.error(f"❌ Model not found at {MODEL_PATH}")
            raise

    def predict(self, records: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        records: List of customer records (JSON)
        """

        df = pd.DataFrame(records)

        # Drop unused columns if present
        drop_cols = ["RowNumber", "CustomerId", "Surname"]
        df = df.drop(columns=drop_cols, errors="ignore")

        predictions = self.model.predict(df)

        probabilities = None
        if hasattr(self.model, "predict_proba"):
            probabilities = self.model.predict_proba(df)[:, 1]

        return {
            "predictions": predictions.tolist(),
            "probabilities": probabilities.tolist() if probabilities is not None else None
        }
