import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the raw NOAA earthquake dataset.
    """

    df = df.copy()

    # Remove completely empty columns
    df = df.dropna(axis=1, how="all")

    return df