from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import logging

from backend.inference import ChurnModel

# -------------------------
# Logging
# -------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -------------------------
# App init
# -------------------------
app = FastAPI(
    title="Customer Churn Prediction API",
    version="1.0.0"
)

model = ChurnModel()

# -------------------------
# Request schema
# -------------------------
class Customer(BaseModel):
    CreditScore: int
    Geography: str
    Gender: str
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float


# -------------------------
# Routes
# -------------------------
@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(customers: List[Customer]):
    try:
        results = model.predict([c.dict() for c in customers])
        return results
    except Exception as e:
        logger.exception("Prediction failed")
        return {"error": str(e)}
