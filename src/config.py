from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODEL_DIR = BASE_DIR / "models"
OUTPUT_DIR = BASE_DIR / "outputs"

RAW_DATA_PATH = RAW_DATA_DIR / "earthquake_data.tsv"

MODEL_PATH = MODEL_DIR / "earthquake_model.pkl"

RANDOM_STATE = 42
TEST_SIZE = 0.2

UNUSED_COLUMNS = [
    "Tsu",
    "Vol",
]

TARGET_COLUMN = "Tsunami"