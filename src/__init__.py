"""
customer-churn-prediction-pipeline
===================================
End-to-end ML pipeline: ingest → validate → feature engineer
→ train → score → retention actions.

Public API
----------
Quick one-liner to kick off the full pipeline from Python:

    from src import run_pipeline
    run_pipeline()

Or import individual stages:

    from src import (
        load_raw_customer_data,
        validate_customer_data,
        clean_customer_data,
        add_churn_features,
        get_model_columns,
        train_churn_model,
        score_customers,
        assign_risk_bucket,
        recommend_retention_action,
    )
"""

from pathlib import Path
import sys

# ── Make sure every sub-module inside src/ is importable regardless of
#    the working directory the caller uses. ─────────────────────────────
_SRC_DIR = Path(__file__).resolve().parent
if str(_SRC_DIR) not in sys.path:
    sys.path.insert(0, str(_SRC_DIR))

# ── Stage 1 – Ingestion ───────────────────────────────────────────────
from data_ingestion import load_raw_customer_data, write_dataframe          # noqa: E402

# ── Stage 2 – Validation & Cleaning ──────────────────────────────────
from data_validation import validate_customer_data, clean_customer_data     # noqa: E402

# ── Stage 3 – Feature Engineering ────────────────────────────────────
from feature_engineering import add_churn_features, get_model_columns       # noqa: E402

# ── Stage 4 – Model Training ──────────────────────────────────────────
from train_model import train_churn_model                                   # noqa: E402

# ── Stage 5 – Scoring ─────────────────────────────────────────────────
from score_customers import score_customers                                 # noqa: E402

# ── Stage 6 – Retention Engine ────────────────────────────────────────
from retention_engine import assign_risk_bucket, recommend_retention_action # noqa: E402


def run_pipeline(config_path: str | None = None) -> None:
    """
    Execute the full churn-prediction pipeline end-to-end.

    Parameters
    ----------
    config_path : str or None
        Optional path to a custom config.yaml.
        Defaults to ``configs/config.yaml`` relative to the project root.

    Example
    -------
    >>> from src import run_pipeline
    >>> run_pipeline()                       # uses default config
    >>> run_pipeline("configs/my_cfg.yaml")  # custom config
    """
    # Delegate to run_pipeline.main() so all config/path logic lives in
    # one place and the CLI entry-point stays identical.
    from run_pipeline import main as _main  # noqa: E402 (local import intentional)

    if config_path is not None:
        # Patch the config loader for callers who need a non-default path
        import run_pipeline as _rp
        import yaml

        _original_load = _rp.load_config

        def _patched_load():
            with open(config_path, "r", encoding="utf-8") as f:
                return yaml.safe_load(f)

        _rp.load_config = _patched_load
        try:
            _main()
        finally:
            _rp.load_config = _original_load  # always restore
    else:
        _main()


__all__ = [
    # Ingestion
    "load_raw_customer_data",
    "write_dataframe",
    # Validation
    "validate_customer_data",
    "clean_customer_data",
    # Features
    "add_churn_features",
    "get_model_columns",
    # Training
    "train_churn_model",
    # Scoring
    "score_customers",
    # Retention
    "assign_risk_bucket",
    "recommend_retention_action",
    # Pipeline runner
    "run_pipeline",
]