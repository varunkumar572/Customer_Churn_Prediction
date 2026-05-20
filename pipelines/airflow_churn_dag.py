"""
Airflow DAG sample for production orchestration.
Place this file inside your Airflow dags folder after updating project path.
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

PROJECT_PATH = "/opt/customer-churn-prediction-pipeline"

with DAG(
    dag_id="customer_churn_prediction_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args={
        "owner": "data-engineering",
        "retries": 2,
        "retry_delay": timedelta(minutes=5),
    },
) as dag:
    run_churn_pipeline = BashOperator(
        task_id="run_churn_pipeline",
        bash_command=f"cd {PROJECT_PATH} && python src/run_pipeline.py",
    )

    run_churn_pipeline
