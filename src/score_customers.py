from pathlib import Path
import joblib
import pandas as pd

from feature_engineering import get_model_columns
from retention_engine import assign_risk_bucket, recommend_retention_action


def score_customers(
    feature_df: pd.DataFrame,
    model_path: str,
    output_path: str,
    high_threshold: float,
    medium_threshold: float,
) -> pd.DataFrame:
    model = joblib.load(model_path)
    model_columns = get_model_columns()

    scored = feature_df.copy()
    scored["churn_probability"] = model.predict_proba(scored[model_columns])[:, 1]
    scored["risk_bucket"] = scored["churn_probability"].apply(
        lambda score: assign_risk_bucket(score, high_threshold, medium_threshold)
    )
    scored["retention_action"] = scored.apply(recommend_retention_action, axis=1)

    final_cols = [
        "customer_id",
        "tenure_months",
        "monthly_charges",
        "support_calls_30d",
        "payment_delay_days",
        "usage_drop_pct",
        "churn_probability",
        "risk_bucket",
        "retention_action",
    ]

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    scored[final_cols].to_csv(output_path, index=False)
    return scored[final_cols]
