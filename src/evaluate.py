
from sklearn.metrics import (
    accuracy_score, f1_score, precision_score,
    recall_score, roc_auc_score, confusion_matrix
)

def evaluate_model(y_true, y_pred, y_prob):
    matrix = confusion_matrix(
        y_true,
        y_pred
    )
    matrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "Precision": precision_score(y_true, y_pred),
        "recall": recall_score(y_true, y_pred),
        "f1_score": f1_score(y_true, y_pred),
        "roc_auc": roc_auc_score(y_true, y_pred),
        "confusion_matrix" : matrix
    }
    return matrics

