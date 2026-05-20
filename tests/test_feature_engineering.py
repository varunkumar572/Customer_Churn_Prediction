from pathlib import Path
import sys

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.feature_engineering import add_churn_features


def test_usage_drop_feature_is_created():
    df = pd.DataFrame(
        {
            "contract_type": ["Month-to-month"],
            "internet_service": ["Fiber optic"],
            "payment_method": ["Electronic check"],
            "usage_previous_month_gb": [100],
            "usage_current_month_gb": [70],
            "support_calls_30d": [2],
            "complaints_90d": [1],
            "payment_delay_days": [5],
            "monthly_charges": [90],
            "tenure_months": [24],
        }
    )

    result = add_churn_features(df)

    assert "usage_drop_pct" in result.columns
    assert round(result.loc[0, "usage_drop_pct"], 2) == 0.30
    assert result.loc[0, "is_month_to_month"] == 1
