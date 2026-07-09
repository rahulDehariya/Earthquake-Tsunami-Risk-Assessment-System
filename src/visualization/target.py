import matplotlib.pyplot as plt
import pandas as pd

from src.config import TARGET_COLUMN

def plot_target_distribution(df:pd.DataFrame):
    """
    Plot the distribution of the target variable.
    """
    counts = df[TARGET_COLUMN].value_counts()

    plt.figure(figsize=(6,4))

    counts.plot(
        kind="bar"
    )
    plt.title("Tsunami distributin")
    plt.xlabel("Tsunami")
    plt.ylabel(counts)
    plt.tight_layout()

    plt.show()