from pathlib import Path

import pandas as pd


from pathlib import Path

import pandas as pd


def load_data(file_path: Path) -> pd.DataFrame:
    """
    Load the raw earthquake dataset.
    """

    return pd.read_csv(
        file_path,
        sep="\t",
        skiprows=[1],
    )