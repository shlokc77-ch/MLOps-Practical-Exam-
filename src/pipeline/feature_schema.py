
# Member 3: Feature Schema

# Unique patient identification column
ID_COLUMN = "patient_id"

# Timestamp column required by Feast
TIME_COLUMN = "event_timestamp"

# Target/output column
TARGET_COLUMN = "target"


# 30 original dataset features
BASE_FEATURES = [
    "mean radius",
    "mean texture",
    "mean perimeter",
    "mean area",
    "mean smoothness",
    "mean compactness",
    "mean concavity",
    "mean concave points",
    "mean symmetry",
    "mean fractal dimension",

    "radius error",
    "texture error",
    "perimeter error",
    "area error",
    "smoothness error",
    "compactness error",
    "concavity error",
    "concave points error",
    "symmetry error",
    "fractal dimension error",

    "worst radius",
    "worst texture",
    "worst perimeter",
    "worst area",
    "worst smoothness",
    "worst compactness",
    "worst concavity",
    "worst concave points",
    "worst symmetry",
    "worst fractal dimension"
]


# Two newly engineered features
FEATURE_COLUMNS = BASE_FEATURES + [
    "radius_to_texture_ratio",
    "area_to_perimeter_ratio"
]
