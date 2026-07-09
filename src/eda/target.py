import pandas as pd

def target_analysis(df: pd.DataFrame) -> None:
    """
    Display target variable distribution.
    """

    print("=" * 60)
    print("TARGET ANALYSIS")
    print("=" * 60)

    print(df["Tsunami"].value_counts())

    print("\nPercentage")

    percentage = (
        df["Tsunami"]
        .value_counts(normalize=True)
        .mul(100)
        .round(2)
    )
    print(percentage)