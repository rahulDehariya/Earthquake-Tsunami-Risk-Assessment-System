from src.config import RAW_DATA_PATH, PROCESSED_DATA_DIR
from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.feature_engineering import build_features
from src.eda import (
    dataset_overview,
    target_analysis,
)


def main():

    df = load_data(RAW_DATA_PATH)

    df = clean_data(df)
    
    # Feature engimeering
    df = build_features(df)
    PROCESSED_DATA_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(
        PROCESSED_DATA_DIR / "earthquake_clean.csv",
        index=False,
    )




if __name__ == "__main__":
    main()