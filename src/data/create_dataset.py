
from pathlib import Path
from sklearn.datasets import load_breast_cancer

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "raw" / "breast_cancer.csv"

def create_dataset():
    dataset = load_breast_cancer(as_frame=True)
    df = dataset.data.copy()

    df["target"] = dataset.target.astype("int64")
    df.insert(0, "patient_id",
              [f"patient_{i:04d}" for i in range(len(df))])

    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False)

    print("Dataset saved successfully!")
    print("Dataset shape:", df.shape)
    print(df["target"].value_counts().sort_index())

if __name__ == "__main__":
    create_dataset()
