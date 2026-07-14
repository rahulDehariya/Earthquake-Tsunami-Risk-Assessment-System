# 🌊 Earthquake & Tsunami Risk Assessment System

An end-to-end Machine Learning project that predicts whether a significant earthquake is likely to generate a tsunami using historical earthquake records from NOAA.

---

## 📌 Project Overview

Tsunamis are among the most destructive natural disasters. Early identification of earthquakes that are likely to generate a tsunami can support disaster preparedness and early warning systems.

This project builds a complete Machine Learning pipeline, from raw data ingestion to model evaluation, following production-style software engineering practices.

---

## 🎯 Business Problem

Given historical earthquake information, predict whether an earthquake is associated with a tsunami.

**Target Variable**

- `Tsunami`
    - `1` → Tsunami occurred
    - `0` → No tsunami

---

## 📂 Dataset

**Source**

NOAA / NCEI Global Significant Earthquake Database

The dataset contains historical earthquake events with information such as:

- Magnitude
- Location
- Latitude
- Longitude
- Focal Depth
- Date & Time
- Human Impact
- Economic Damage
- Tsunami Indicator

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Pytest

---

# 📁 Project Structure

```
Earthquake & Tsunami Risk Assessment System/

├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│
├── output/
│
├── src/
│   ├── config.py
│   ├── data_loader.py
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── preprocessing.py
│   ├── evaluate.py
│   │
│   ├── eda/
│   │   ├── overview.py
│   │   └── target.py
│   │
│   └── visualization/
│       ├── target.py
│       ├── missing_values.py
│       ├── numerical.py
│       ├── categorical.py
│       └── correlation.py
│
├── tests/
│
├── train.py
├── predict.py
└── README.md
```

---

# 🔄 Machine Learning Workflow

```
Raw Dataset
      │
      ▼
Data Loading
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Visualization
      │
      ▼
Preprocessing Pipeline
      │
      ▼
Train/Test Split
      │
      ▼
Random Forest Classifier
      │
      ▼
Model Evaluation
```

---

# 🧹 Data Cleaning

The project includes a dedicated data cleaning module to:

- Remove unnecessary metadata
- Remove empty columns
- Standardize the dataset
- Prepare raw data for analysis

---

# ⚙️ Feature Engineering

Features created during preprocessing include:

- Binary Tsunami Target
- Removal of unnecessary features
- Selection of prediction-time features only

Special care was taken to avoid **data leakage** by excluding variables that are only known after an earthquake event (e.g. deaths, injuries, damage).

---

# 📊 Exploratory Data Analysis

The project includes reusable EDA modules for:

- Dataset overview
- Missing value analysis
- Target distribution
- Numerical feature analysis
- Correlation analysis

---

# 📈 Visualization

Implemented reusable visualization functions:

- Target Distribution
- Missing Values
- Histogram
- Box Plot
- Correlation Matrix
- Category Distribution

---

# 🤖 Machine Learning Model

Baseline Model:

- Random Forest Classifier

---

# 📏 Evaluation Metrics

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix

---

# 📊 Baseline Model Performance

| Metric | Score |
|---------|-------|
| Accuracy | **81.38%** |
| Precision | **82.94%** |
| Recall | **50.36%** |
| F1 Score | **62.67%** |
| ROC-AUC | **72.85%** |

Confusion Matrix

```
                 Predicted

               No      Yes

Actual No      879      43

Actual Yes     206     209
```

---

# 💡 Key Learnings

This project demonstrates:

- End-to-end ML pipeline development
- Production-style project architecture
- Data cleaning for real-world datasets
- Feature engineering
- Data leakage prevention
- Pipeline-based preprocessing
- Machine Learning model evaluation
- Business interpretation of ML metrics

---

# 🚀 Future Improvements

Possible future enhancements include:

- Hyperparameter tuning
- Gradient Boosting Models
- XGBoost / LightGBM
- Feature Importance Analysis
- Model Explainability (SHAP)
- Interactive Dashboard
- Real-time Prediction API

---

# ▶️ How to Run

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Train the model

```bash
python train.py
```

Generate predictions

```bash
python predict.py
```

---

# 👨‍💻 Author

**Rahul Dehariya**

GitHub:
https://github.com/rahulDehariya

LinkedIn:
https://www.linkedin.com/in/rahul-dehariya-660363188/

---

## ⭐ If you found this project interesting, consider giving it a star!