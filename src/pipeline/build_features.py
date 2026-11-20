
from pathlib import Path

import pandas as pd

from src.pipeline.feature_schema import (
    ID_COLUMN,
    TIME_COLUMN,
    TARGET_COLUMN,
    BASE_FEATURES,
    FEATURE_COLUMNS,
)

ROOT = Path(__file__).resolve().parents[2]
RAW_DATA = ROOT / "data" / "raw" / "breast_cancer.csv"
OUTPUT = ROOT / "data" / "processed" / "features.parquet"


def build_features() -> pd.DataFrame:
    df = pd.read_csv(RAW_DATA)

    required_columns = [ID_COLUMN] + BASE_FEATURES + [TARGET_COLUMN]

    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    features = df[required_columns].copy()

    # Feature engineering
    features["radius_to_texture_ratio"] = (
        features["mean radius"] / features["mean texture"].replace(0, 1e-9)
    )

    features["area_to_perimeter_ratio"] = (
        features["mean area"] / features["mean perimeter"].replace(0, 1e-9)
    )

    # Stable synthetic timestamps for Feast
    features[TIME_COLUMN] = pd.date_range(
        start="2024-01-01",
        periods=len(features),
        freq="s",
        tz="UTC",
    )

    output_columns = (
        [ID_COLUMN, TIME_COLUMN] + FEATURE_COLUMNS + [TARGET_COLUMN]
    )

    result = features[output_columns].copy()

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    result.to_parquet(OUTPUT, index=False)

    print(f"Saved: {OUTPUT}")
    print(f"Shape: {result.shape}")

    return result


if __name__ == "__main__":
    build_features()
