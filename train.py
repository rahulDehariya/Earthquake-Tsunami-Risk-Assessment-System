from src.config import RAW_DATA_PATH
from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.feature_engineering import build_features


def main():

    df = load_data(RAW_DATA_PATH)

    df = clean_data(df)
    
    # Feature engimeering
    df = build_features(df)
    print(df.head())



if __name__ == "__main__":
    main()