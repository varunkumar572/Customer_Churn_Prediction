# Architecture

## Objective

Predict churn risk for telecom customers and trigger retention actions before customers leave.

## Layers

### Bronze Layer
Stores raw customer data from CRM, billing, support, usage, mobile app, and network systems.

### Silver Layer
Cleans and validates data. Removes duplicates, fixes missing values, standardizes categorical fields, and validates churn labels.

### Gold Layer
Creates ML-ready features such as usage drop percentage, support pressure score, billing risk score, customer value score, and contract risk indicators.

### Model Layer
Trains a churn prediction model using historical churn labels. The model outputs churn probability between 0 and 1.

### Scoring Layer
Scores customers daily or in near real time. High-risk customers are written to a business output table.

### Retention Layer
Maps churn probability and customer behavior into recommended actions.

## Production Version

For a real enterprise setup, use:

- Kafka for real-time events
- Databricks Auto Loader for file ingestion
- Delta Lake bronze, silver, and gold tables
- MLflow for model tracking and registry
- Airflow for orchestration
- Feature Store for reusable customer features
- Power BI or Tableau for dashboards
- CRM integration for retention campaigns

## Example Production Flow

```text
CRM/Billing/Usage/Support Systems
    ↓
Kafka + Batch Ingestion
    ↓
Databricks Bronze Delta Tables
    ↓
PySpark Silver Cleaning Jobs
    ↓
Gold Feature Tables
    ↓
MLflow Model Training
    ↓
Batch/Streaming Churn Scoring
    ↓
CRM Retention Campaigns
    ↓
Dashboard + Model Monitoring
```
