
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "raw" / "breast_cancer.csv"


def validate_dataset(path: Path = DATA) -> pd.DataFrame:
    df = pd.read_csv(path)

    assert len(df) == 569, f"Expected 569 rows, got {len(df)}"
    assert df["patient_id"].is_unique, "patient_id must be unique"
    assert df["patient_id"].notna().all(), "patient_id contains nulls"
    assert "target" in df.columns, "target column is missing"
    assert set(df["target"].unique()) == {0, 1}, "target must contain 0 and 1"

    feature_cols = [
        c for c in df.columns
        if c not in {"patient_id", "target"}
    ]

    assert len(feature_cols) == 30, f"Expected 30 features, got {len(feature_cols)}"
    assert df[feature_cols].select_dtypes(exclude="number").empty, "Features must be numeric"
    assert not df[feature_cols].isna().any().any(), "Feature values contain missing data"

    print("DATA VALIDATION PASSED")
    print(f"Rows = {len(df)}, Features = {len(feature_cols)}")
    print("Target mapping: 0 = malignant, 1 = benign")

    return df


if __name__ == "__main__":
    validate_dataset()
