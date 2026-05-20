from pathlib import Path
import sys
import yaml

CURRENT_DIR = Path(__file__).resolve().parent
sys.path.append(str(CURRENT_DIR))

from data_ingestion import load_raw_customer_data, write_dataframe
from data_validation import clean_customer_data, validate_customer_data
from feature_engineering import add_churn_features
from train_model import train_churn_model
from score_customers import score_customers


def load_config() -> dict:
    config_path = Path(__file__).resolve().parents[1] / "configs" / "config.yaml"
    with open(config_path, "r", encoding="utf-8") as config_file:
        return yaml.safe_load(config_file)


def main() -> None:
    config = load_config()
    paths = config["paths"]
    model_cfg = config["model"]

    raw_df = load_raw_customer_data(paths["raw_data"])
    validate_customer_data(raw_df)

    cleaned_df = clean_customer_data(raw_df)
    write_dataframe(cleaned_df, paths["cleaned_data"])

    feature_df = add_churn_features(cleaned_df)
    write_dataframe(feature_df, paths["feature_data"])

    metrics = train_churn_model(
        feature_df=feature_df,
        model_path=paths["model_path"],
        test_size=model_cfg["test_size"],
        random_state=model_cfg["random_state"],
    )

    scored_df = score_customers(
        feature_df=feature_df,
        model_path=paths["model_path"],
        output_path=paths["scored_data"],
        high_threshold=model_cfg["high_risk_threshold"],
        medium_threshold=model_cfg["medium_risk_threshold"],
    )

    print("Pipeline completed successfully")
    print(f"Model metrics: {metrics}")
    print(scored_df.head(10).to_string(index=False))


if __name__ == "__main__":
    main()
