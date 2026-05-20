# Customer Churn Prediction Pipeline

End-to-end customer churn prediction system for a telecom-style company. The pipeline ingests customer data, cleans it, creates churn features, trains a machine learning model, scores customers, and recommends retention actions.

## Business Problem

Telecom customers may leave because of high bills, poor experience, low usage, support issues, or better competitor offers. This project predicts churn risk before the customer leaves and assigns a retention action.

Example:

A customer with 5 years of tenure suddenly reduces usage, raises support complaints, and has payment delays. The model gives this customer a high churn score, and the system recommends a retention call or discount.

## Architecture

```text
Raw Customer Data
    ↓
Bronze Layer: Ingest raw CSV/API data
    ↓
Silver Layer: Clean, validate, standardize data
    ↓
Gold Layer: Feature engineering
    ↓
Model Training: Train churn prediction model
    ↓
Batch Scoring: Predict churn probability
    ↓
Retention Engine: Recommend next best action
    ↓
Dashboard Output: Business-ready customer risk table
```

## Tech Stack

- Python
- Pandas
- Scikit-learn
- XGBoost optional fallback through GradientBoostingClassifier
- MLflow-style model version folder
- Airflow DAG sample
- PySpark/Databricks production design included in docs
- GitHub Actions CI sample

## Project Structure

```text
customer-churn-prediction-pipeline/
├── configs/
│   └── config.yaml
├── data/
│   ├── raw/
│   │   └── telecom_churn_sample.csv
│   └── processed/
├── docs/
│   ├── architecture.md
│   └── interview_explanation.md
├── models/
├── pipelines/
│   └── airflow_churn_dag.py
├── src/
│   ├── data_ingestion.py
│   ├── data_validation.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── score_customers.py
│   ├── retention_engine.py
│   └── run_pipeline.py
├── tests/
│   └── test_feature_engineering.py
├── requirements.txt
└── README.md
```

## How to Run Locally

### 1. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run full pipeline

```bash
python src/run_pipeline.py
```

### 4. Check output

Final scored customer output will be created here:

```text
data/processed/customer_churn_scores.csv
```

Model will be saved here:

```text
models/churn_model.pkl
```

## Final Output Example

| customer_id | churn_probability | risk_bucket | retention_action |
|---|---:|---|---|
| C1001 | 0.89 | High Risk | Loyalty manager call + 20% discount |
| C1002 | 0.31 | Low Risk | Normal monitoring |

## GitHub Push Commands

After downloading this project, run:

```bash
cd customer-churn-prediction-pipeline
git init
git add .
git commit -m "Initial customer churn prediction pipeline"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/customer-churn-prediction-pipeline.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

## Resume / Interview Line

Built an end-to-end customer churn prediction pipeline that ingests telecom customer data, performs data validation and feature engineering, trains a churn model, scores customer churn probability, and generates retention actions for high-risk customers.
