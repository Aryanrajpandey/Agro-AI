"""Project-wide configuration constants."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = str(PROJECT_ROOT / "data" / "agmarknet_data.csv")
