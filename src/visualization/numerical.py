import matplotlib.pyplot as plt
import pandas as pd


def plot_numerical_distribution(
    df: pd.DataFrame,
    column: str,
) -> None:
    """
    Plot histogram for a numerical feature.
    """

    plt.figure(figsize=(8, 5))

    plt.hist(
        df[column].dropna(),
        bins=30,
    )

    plt.title(f"{column} Distribution")
    plt.xlabel(column)
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()


def plot_boxplot(
    df: pd.DataFrame,
    column: str,
) -> None:
    """
    Plot boxplot for a numerical feature.
    """

    plt.figure(figsize=(8, 2))

    plt.boxplot(
        df[column].dropna(),
        vert=False,
    )

    plt.title(column)

    plt.tight_layout()
    plt.show()