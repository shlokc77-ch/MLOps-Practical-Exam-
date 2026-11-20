
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "raw" / "breast_cancer.csv"

def validate_dataset():
    df = pd.read_csv(DATA)

    assert len(df) == 569
    assert df["patient_id"].is_unique
    assert df["patient_id"].notna().all()
    assert "target" in df.columns
    assert set(df["target"].unique()) == {0, 1}

    features = [c for c in df.columns
                if c not in ["patient_id", "target"]]

    assert len(features) == 30
    assert df[features].select_dtypes(exclude="number").empty
    assert not df[features].isna().any().any()

    print("DATA VALIDATION PASSED")
    print("Rows:", len(df))
    print("Features:", len(features))
    print("0 = Malignant, 1 = Benign")

if __name__ == "__main__":
    validate_dataset()
