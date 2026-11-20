
from src.data.create_dataset import create_dataset
from src.pipeline.build_features import build_features
from src.pipeline.feature_schema import FEATURE_COLUMNS


def test_feature_pipeline():
    create_dataset()
    result = build_features()

    assert len(result) == 569
    assert len(FEATURE_COLUMNS) == 32
    assert result["patient_id"].is_unique
    assert result["target"].isin([0, 1]).all()
    assert result[FEATURE_COLUMNS].notna().all().all()
