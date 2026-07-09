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

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())