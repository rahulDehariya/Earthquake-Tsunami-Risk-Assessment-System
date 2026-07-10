import pandas as pd
import matplotlib.pyplot as plt

def plot_correlation_matrix(df:pd.DataFrame) -> None:
    """
    Plot correlation matrix.
    """
    correlation = df.corr(numeric_only=True)

    plt.figure(figsize=(10,8))

    plt.imshow(
        correlation,
        aspect="auto"
    )

    plt.colorbar()

    plt.xticks(
        range(len(correlation.columns)),
        correlation.columns,
        rotation=90
    )

    plt.yticks(
        range(len(correlation.columns)),
        correlation.columns,
        rotation = 90
    )
    plt.tight_layout()
    plt.show()