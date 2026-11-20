
from src.data.create_dataset import create_dataset
from src.data.validate_dataset import validate_dataset


def test_dataset_creation_and_validation():
    create_dataset()
    df = validate_dataset()

    assert df.shape == (569, 32)
