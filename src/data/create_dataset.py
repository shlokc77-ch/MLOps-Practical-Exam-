
from pathlib import Path
from sklearn.datasets import load_breast_cancer

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "raw" / "breast_cancer.csv"


def create_dataset() -> Path:
    dataset = load_breast_cancer(as_frame=True)

    frame = dataset.data.copy()

    # Target convention: 0 = malignant, 1 = benign
    frame["target"] = dataset.target.astype("int64")

    # Create unique patient IDs
    frame.insert(
        0,
        "patient_id",
        [f"patient_{i:04d}" for i in range(len(frame))]
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(OUT, index=False)

    print(f"Saved: {OUT}")
    print(f"Shape: {frame.shape}")
    print(frame["target"].value_counts().sort_index().to_dict())

    return OUT


if __name__ == "__main__":
    create_dataset()
