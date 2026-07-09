def target_analysis(df: pd.DataFrame) -> None:
    """
    Display target variable distribution.
    """

    print("=" * 60)
    print("TARGET ANALYSIS")
    print("=" * 60)

    print(df["Tsunami"].value_counts())

    print("\nPercentage")

    print(
        round(
            df["Tsunami"].value_counts(normalize=True) * 100,
            2,
        )
    )