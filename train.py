from src.config import RAW_DATA_PATH, PROCESSED_DATA_DIR
from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.feature_engineering import build_features
from src.eda import dataset_overview, target_analysis


def main():

    df = load_data(RAW_DATA_PATH)

    df = clean_data(df)
    
    # Feature engimeering
    df = build_features(df)
    dataset_overview(df)
    target_analysis(df)




if __name__ == "__main__":
    main()