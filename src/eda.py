import pandas as pd

def dataset_overview(df:pd.DataFrame):
    """
    Display Basic information about dataset
    """
    print("=" * 60)
    print("DATASET OVERVIEW")
    print("=" * 60)

    print(f"\nShape:{df.shape}")
    print("\nColumns:")
    print(f"\nColoumns;{df.columns}")

    print("\nData Type:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

def target_analysis(df:pd.DataFrame):
    """
    Display Target distribution
    """
    print("\nTarget Distribution")
    print(df['Tsunami'].value_counts())

    print("\nPercentage")
    print(
        round(
            df["Tsunami"].value_counts(normalize=True) * 100
        )
    )
