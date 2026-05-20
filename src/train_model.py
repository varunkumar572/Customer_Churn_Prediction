from pathlib import Path
import joblib
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split

from feature_engineering import get_model_columns


def train_churn_model(
    feature_df: pd.DataFrame,
    model_path: str,
    test_size: float,
    random_state: int,
) -> dict:
    model_columns = get_model_columns()
    X = feature_df[model_columns]
    y = feature_df["churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )

    model = GradientBoostingClassifier(random_state=random_state)
    model.fit(X_train, y_train)

    predicted_labels = model.predict(X_test)
    predicted_probs = model.predict_proba(X_test)[:, 1]

    metrics = {
        "accuracy": round(accuracy_score(y_test, predicted_labels), 4),
        "precision": round(precision_score(y_test, predicted_labels, zero_division=0), 4),
        "recall": round(recall_score(y_test, predicted_labels, zero_division=0), 4),
        "roc_auc": round(roc_auc_score(y_test, predicted_probs), 4),
    }

    Path(model_path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)
    return metrics
