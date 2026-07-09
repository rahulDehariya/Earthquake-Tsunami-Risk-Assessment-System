import pandas as pd


def dataset_overview(df: pd.DataFrame) -> None:
    """
    Display dataset overview.
    """

    print("=" * 60)
    print("DATASET OVERVIEW")
    print("=" * 60)

    print(f"\nShape: {df.shape}")

    print("\nData Types")
    print(df.dtypes)

    # Columns with the most missing values appear first.
    print("\nMissing Values")
    print(df.isnull().sum().sort_values(ascending=False))

    print("\nDuplicate Rows")
    print(df.duplicated().sum())