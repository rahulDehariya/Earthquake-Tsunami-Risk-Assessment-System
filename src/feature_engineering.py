import pandas as pd

from src.config import UNUSED_COLUMNS

def _create_target(df:pd.DataFrame) -> pd.DataFrame:
    """
    Create binary tsunami target.
    """

    df = df.copy()

    df['Tsunami'] =  df['Tsu'].notna().astype(int)

    return df

def _drop_unused_columns(
        df:pd.DataFrame,
        columns:list[str]
) -> pd.DataFrame:
    """
    Drop unused columns.
    """
    return df.drop(columns=columns)

    
def build_features(df:pd.DataFrame) -> pd.DataFrame:
        """
        Execute feature engineering pipeline.
        """
        df = _create_target(df)

        df = _drop_unused_columns(
            df,
            UNUSED_COLUMNS
        )
        return df