import pandas as pd
import matplotlib.pyplot as plt

def plot_category_distribution(
        df:pd.DataFrame,
        column:str
)->None:
    """
    Plot categorical feature distribution.
    """
    counts = df[column].value_counts()

    plt.figure(figsize=(10,5))

    plt.bar(
        counts.index.astype(str),
        counts.values
    )

    plt.xticks(rotation=45)
    plt.title(column)
    plt.ylabel("Count")

    plt.tight_layout()
    plt.show()