from pathlib import Path
import pandas as pd


def load_raw_customer_data(raw_path: str) -> pd.DataFrame:
    file_path = Path(raw_path)
    if not file_path.exists():
        raise FileNotFoundError(f"Raw input file not found: {raw_path}")
    return pd.read_csv(file_path)


def write_dataframe(df: pd.DataFrame, output_path: str) -> None:
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
