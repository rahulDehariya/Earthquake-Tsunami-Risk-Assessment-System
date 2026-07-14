from src.config import (RAW_DATA_PATH,
PROCESSED_DATA_DIR,
FEATURE_COLUMNS,
TARGET_COLUMN,
TEST_SIZE,
RANDOM_STATE
)
from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.feature_engineering import build_features
from src.eda import dataset_overview, target_analysis
from src.visualization import (
    plot_missing_value,
    plot_numerical_distribution,
    plot_boxplot,
    plot_category_distribution,
    plot_correlation_matrix
)
from sklearn.pipeline import Pipeline
from src.preprocessing import builder_preprocessing

from sklearn.model_selection import train_test_split
from models.model import build_model
from src.evaluate import evaluate_model



def main():
    # Buld
    df = load_data(RAW_DATA_PATH)

    # clean
    df = clean_data(df)
    
    # Feature engimeering
    df = build_features(df)

    #EDA
    #dataset_overview(df)
    #target_analysis(df)
    # plot_target_distribution(df)
    #plot_missing_value(df)
    #plot_numerical_distribution(df,"Mag")
    #plot_boxplot(df, "Mag")
    #plot_category_distribution(df, "Mag")
    #plot_correlation_matrix(df)

    # Split
    X = df[FEATURE_COLUMNS]
    Y = df[TARGET_COLUMN]

    X_train, X_test, y_train, Y_test = train_test_split(
        X,
        Y,
        test_size= TEST_SIZE,
        random_state= RANDOM_STATE
    ) 

    # PreProcessing
    preprocessing = builder_preprocessing()
    model = build_model()

    pipeline = Pipeline(
        steps=[
            (
                "preprocessing",
                preprocessing
            ),
            (
                "model",
                model
            )
        ]
    )

    # Train
    pipeline.fit(
        X_train,
        y_train
    )

    # Prediction
    y_pred = pipeline.predict(X_test)

    y_prob = pipeline.predict_proba(X_test)[:,1]


    matrics = evaluate_model(
        y_true=Y_test,
        y_pred=y_pred,
        y_prob=y_prob
    )
    print(matrics)

    """
    {'accuracy': 0.8137621540762902, 'Precision': 0.8293650793650794, 'recall': 0.5036144578313253, 'f1_score': 0.6266866566716641, 'roc_auc': 0.7284883568983092}
    Accuracy  : 81.38%
    Precision : 82.94%
    Recall    : 50.36%
    F1 Score  : 62.67%
    ROC AUC   : 72.85%
    """



if __name__ == "__main__":
    main()