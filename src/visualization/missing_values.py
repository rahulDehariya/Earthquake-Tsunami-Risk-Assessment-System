import matplotlib.pyplot as plt
import pandas as pd


def plot_missing_values(df: pd.DataFrame) -> None:
    """
    Plot missing values for each feature.
    """

    missing = (
        df.isnull()
          .sum()
          .sort_values(ascending=False)
    )

    missing = missing[missing > 0]

    plt.figure(figsize=(10, 6))

    missing.plot(kind="bar")

    plt.title("Missing Values")
    plt.xlabel("Features")
    plt.ylabel("Count")

    plt.xticks(rotation=90)

    plt.tight_layout()

    plt.show()