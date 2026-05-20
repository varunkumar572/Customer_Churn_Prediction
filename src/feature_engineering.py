import numpy as np
import pandas as pd


def add_churn_features(df: pd.DataFrame) -> pd.DataFrame:
    features = df.copy()

    previous_usage = features["usage_previous_month_gb"].replace(0, np.nan)
    features["usage_drop_pct"] = (
        (features["usage_previous_month_gb"] - features["usage_current_month_gb"])
        / previous_usage
    ).fillna(0).clip(lower=0)

    features["is_month_to_month"] = (
        features["contract_type"].str.lower() == "month-to-month"
    ).astype(int)

    features["has_fiber_service"] = (
        features["internet_service"].str.lower() == "fiber optic"
    ).astype(int)

    features["uses_electronic_check"] = (
        features["payment_method"].str.lower() == "electronic check"
    ).astype(int)

    features["support_pressure_score"] = (
        features["support_calls_30d"] * 0.6
        + features["complaints_90d"] * 0.4
    )

    features["billing_risk_score"] = (
        features["payment_delay_days"] / 30
        + features["monthly_charges"] / 150
    )

    features["customer_value_score"] = (
        features["tenure_months"] * features["monthly_charges"]
    )

    return features


def get_model_columns() -> list[str]:
    return [
        "tenure_months",
        "monthly_charges",
        "total_charges",
        "support_calls_30d",
        "payment_delay_days",
        "usage_current_month_gb",
        "usage_previous_month_gb",
        "complaints_90d",
        "usage_drop_pct",
        "is_month_to_month",
        "has_fiber_service",
        "uses_electronic_check",
        "support_pressure_score",
        "billing_risk_score",
        "customer_value_score",
    ]
