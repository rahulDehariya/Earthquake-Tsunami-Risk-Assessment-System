from sklearn.ensemble import RandomForestClassifier

from src.config import RANDOM_STATE

def build_model() -> RandomForestClassifier:
    """
    Build baseline  Random forest model
    """
    return RandomForestClassifier(
        random_state=RANDOM_STATE
    )