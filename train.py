from src.config import RAW_DATA_PATH, PROCESSED_DATA_DIR
from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.feature_engineering import build_features
from src.eda import dataset_overview, target_analysis
from src.visualization import plot_missing_values


def main():

    df = load_data(RAW_DATA_PATH)

    df = clean_data(df)
    
    # Feature engimeering
    df = build_features(df)
    dataset_overview(df)
    target_analysis(df)
    # plot_target_distribution(df)
    plot_missing_values(df)




if __name__ == "__main__":
    main()