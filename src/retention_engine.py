def assign_risk_bucket(churn_probability: float, high_threshold: float, medium_threshold: float) -> str:
    if churn_probability >= high_threshold:
        return "High Risk"
    if churn_probability >= medium_threshold:
        return "Medium Risk"
    return "Low Risk"


def recommend_retention_action(row) -> str:
    risk_bucket = row["risk_bucket"]

    if risk_bucket == "High Risk" and row["tenure_months"] >= 36:
        return "Loyalty manager call + 20% discount"

    if risk_bucket == "High Risk" and row["support_calls_30d"] >= 3:
        return "Priority support callback + service credit"

    if risk_bucket == "High Risk":
        return "Immediate retention offer"

    if risk_bucket == "Medium Risk" and row["payment_delay_days"] > 0:
        return "Flexible payment reminder + plan review"

    if risk_bucket == "Medium Risk":
        return "Personalized plan recommendation"

    return "Normal monitoring"
