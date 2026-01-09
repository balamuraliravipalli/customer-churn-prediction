<<<<<<< HEAD
# Customer Churn Prediction

## Project Overview
Predicting customer churn is critical for businesses to retain valuable customers and reduce revenue loss. This project leverages machine learning to identify customers at risk of leaving, providing actionable insights to guide retention strategies.

This end-to-end project includes data exploration, preprocessing, feature engineering, model building, and performance evaluation using industry-standard ML techniques.

---

## Key Highlights
- **End-to-End ML Pipeline:** From raw data preprocessing to model evaluation and visualization.
- **Multiple Models:** Implemented Logistic Regression, Random Forest, and XGBoost for comparison.
- **Performance Metrics:** Evaluated models using Accuracy, Precision, Recall, F1-score, and ROC-AUC.
- **Business Insights:** Identifies key factors driving churn, supporting data-driven decision making.
- **Reproducible:** Fully documented Google Colab notebooks for easy experimentation.

---

## Technologies & Tools
- **Languages:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, XGBoost  
- **Environment:** Google Colab, Jupyter Notebook  

---
=======
📌 Customer Churn Prediction API

A production-ready machine learning inference service that predicts whether a customer is likely to churn using structured customer data.

🚀 Features

End-to-end ML pipeline (training → inference)

Scikit-learn Pipeline with preprocessing

FastAPI REST API

Batch prediction support

Swagger UI documentation

Ready for AWS deployment

🧠 Model Overview

Algorithm: RandomForestClassifier

Preprocessing:

Numerical: StandardScaler

Categorical: OneHotEncoder

Target: Exited (0 = stay, 1 = churn)

📂 Project Structure
customer-churn-prediction/
├── backend/
│   ├── train_model.py
│   ├── inference.py
│   ├── server.py
│   └── model.pkl
├── notebooks/
│   └── churn_analysis.ipynb
├── README.md
└── requirements.txt

▶️ Run Locally
pip install -r requirements.txt
python backend/train_model.py
uvicorn backend.server:app --reload


Open:

Swagger UI → http://127.0.0.1:8000/docs

Health check → http://127.0.0.1:8000/health

📡 API Endpoints
Method	Endpoint	Description
GET	/health	Service health check
POST	/predict	Predict churn
📥 Example Request
[
  {
    "CreditScore": 650,
    "Geography": "France",
    "Gender": "Male",
    "Age": 40,
    "Tenure": 5,
    "Balance": 60000,
    "NumOfProducts": 2,
    "HasCrCard": 1,
    "IsActiveMember": 1,
    "EstimatedSalary": 50000
  }
]

📤 Example Response
{
  "predictions": [0],
  "probabilities": [0.12]
}
>>>>>>> eb58951 (Initial commit: Customer Churn Prediction API with FastAPI, scikit-learn, and model pipeline)
