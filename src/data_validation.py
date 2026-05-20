import pandas as pd

REQUIRED_COLUMNS = {
    "customer_id",
    "tenure_months",
    "monthly_charges",
    "total_charges",
    "contract_type",
    "payment_method",
    "internet_service",
    "support_calls_30d",
    "payment_delay_days",
    "usage_current_month_gb",
    "usage_previous_month_gb",
    "complaints_90d",
    "churn",
}


def validate_customer_data(df: pd.DataFrame) -> None:
    missing_cols = REQUIRED_COLUMNS.difference(df.columns)
    if missing_cols:
        raise ValueError(f"Missing required columns: {sorted(missing_cols)}")

    if df["customer_id"].isna().any():
        raise ValueError("customer_id cannot be null")

    if df["customer_id"].duplicated().any():
        raise ValueError("Duplicate customer_id records found")

    if not set(df["churn"].dropna().unique()).issubset({0, 1}):
        raise ValueError("churn column must contain only 0 or 1")


def clean_customer_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()
    cleaned = cleaned.drop_duplicates(subset=["customer_id"])

    numeric_cols = [
        "tenure_months",
        "monthly_charges",
        "total_charges",
        "support_calls_30d",
        "payment_delay_days",
        "usage_current_month_gb",
        "usage_previous_month_gb",
        "complaints_90d",
    ]

    for col_name in numeric_cols:
        cleaned[col_name] = pd.to_numeric(cleaned[col_name], errors="coerce").fillna(0)

    text_cols = ["contract_type", "payment_method", "internet_service"]
    for col_name in text_cols:
        cleaned[col_name] = cleaned[col_name].fillna("Unknown").astype(str).str.strip()

    cleaned["churn"] = cleaned["churn"].fillna(0).astype(int)
    return cleaned
