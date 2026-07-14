Section 1 — Project Overview (Must Know)
Q1. Tell me about your project.

Answer Skeleton

I built an end-to-end Machine Learning project called Earthquake & Tsunami Risk Assessment System using the NOAA Global Significant Earthquake Database.

The business objective was to predict whether a significant earthquake would generate a tsunami.

I designed the project using a modular architecture consisting of data loading, cleaning, feature engineering, EDA, preprocessing, model training, evaluation, and visualization.

I trained a Random Forest classifier and evaluated it using Accuracy, Precision, Recall, F1-score, ROC-AUC, and Confusion Matrix. I also ensured the project avoided data leakage by excluding post-event variables such as deaths and damage.

Q2. Why did you choose this project?

They want to know whether you copied it.

Good answer:

I wanted to work on a real-world disaster prediction problem instead of another common dataset like Titanic or Iris. The NOAA dataset contained messy data, missing values, and domain-specific challenges, which helped me practice data cleaning, feature engineering, and building an end-to-end ML pipeline.

Q3. What was the business problem?

Answer:

Given historical earthquake information available immediately after an earthquake occurs, predict whether the earthquake is likely to generate a tsunami.

Section 2 — Dataset
Q4. Where did you get the dataset?

Answer:

NOAA / NCEI Global Significant Earthquake Database.

Q5. Why this dataset?

Answer:

Public
Reliable
Real-world
Large historical dataset
Contains geographical and geological information
Q6. How many rows?

Know this.

Example:

Approximately 6,682 earthquake records.

Q7. How many features?

Know this too.

Q8. What is your target variable?

Answer:

Tsunami

0 → No Tsunami

1 → Tsunami
Section 3 — Data Cleaning
Q9. What cleaning did you perform?

Expected answer:

Removed empty columns
Removed metadata
Cleaned raw dataset
Organized pipeline
Q10. Why separate data loading and cleaning?

Excellent interview question.

Answer:

Because loading and cleaning have different responsibilities.

Data loading only reads the file.

Data cleaning modifies the dataset.

This follows the Single Responsibility Principle.

Section 4 — Feature Engineering
Q11. What feature engineering did you perform?

Answer:

Created

Tsunami

target variable.

Dropped

Tsu

Vol

Removed unnecessary features.

Q12. Why create Tsunami?

Answer:

Because machine learning models require a target variable.

Q13. Why drop Vol?

Answer:

Vol is a volcano identifier.

Identifiers generally don't contribute predictive information.

Section 5 — Data Leakage ⭐⭐⭐⭐⭐

This is one of the biggest interview topics.

Q14. Why didn't you use Deaths?

Excellent question.

Answer:

Because deaths occur after the earthquake.

If we use deaths to predict tsunami,

the model would have information unavailable at prediction time.

This causes data leakage.

Q15. What is Data Leakage?

Answer:

Data leakage occurs when information unavailable at prediction time is used during model training.

It results in unrealistically high performance that won't generalize.

Section 6 — EDA
Q16. What did you analyze?

Answer:

Missing values
Target distribution
Numerical distributions
Correlation
Categorical features
Q17. Why perform EDA?

Answer:

To understand data quality, detect missing values, outliers, distributions, and identify useful features before modeling.

Section 7 — Preprocessing
Q18. Why Pipeline?

Answer:

To ensure the exact same preprocessing is applied during both training and inference.

Q19. Why ColumnTransformer?

Answer:

Because numerical and categorical features require different preprocessing steps.

Q20. Why One-Hot Encoding?

Answer:

Location Name is categorical.

One-Hot Encoding converts categories into numerical vectors.

Q21. Why StandardScaler?

Answer:

Although Random Forest doesn't require scaling, I built a reusable preprocessing pipeline that can also support algorithms like Logistic Regression, SVM, and KNN.

That's a strong engineering decision.

Section 8 — Model
Q22. Why Random Forest?

Expected answer:

Robust
Handles nonlinear relationships
Handles missing patterns well after preprocessing
Less prone to overfitting than a single Decision Tree
Strong baseline model
Q23. Why not Logistic Regression?

Answer:

Because earthquake-tsunami relationships are unlikely to be purely linear.

Random Forest can model nonlinear interactions.

Section 9 — Evaluation
Q24. What metrics did you use?

Answer:

Accuracy
Precision
Recall
F1
ROC-AUC
Confusion Matrix
Q25. Why not only Accuracy?

Answer:

The dataset is imbalanced.

Accuracy alone can be misleading.

Q26. Explain Precision.
Q27. Explain Recall.
Q28. Explain F1.
Q29. Explain ROC-AUC.
Q30. Explain Confusion Matrix.
Section 10 — Your Results ⭐⭐⭐⭐⭐

Know these.

Accuracy

81.38%

Precision

82.94%

Recall

50.36%

F1

62.67%

ROC

72.85%
Q31.

Which metric would you improve?

Answer:

Recall.

Because missing tsunami events is more dangerous.

Q32.

What are False Negatives?

Answer:

Actual tsunami

↓

Model predicted No Tsunami.

Q33.

Which is worse?

False Positive?

False Negative?

Answer:

False Negative.

Lives could be at risk.

Section 11 — Software Engineering
Q34.

Why modular architecture?

Q35.

Why separate files?

Q36.

Why Config?

Q37.

Why feature_engineering.py?

Q38.

Why preprocessing.py?

Q39.

Why evaluate.py?

Q40.

Why visualization module?

Section 12 — Improvements
Q41.

If you had more time?

Answer:

XGBoost
Hyperparameter tuning
SHAP
API deployment
Dashboard
Q42.

Biggest challenge?

You can mention:

NOAA dataset formatting
Cleaning metadata
Preventing data leakage
Feature selection
Q43.

What would you do differently?

Mention:

More feature engineering
More model comparison
Better temporal validation if event timestamps were critical
Better handling of class imbalance
Section 13 — Coding Questions

Expect questions like:

Why Pipeline?
Why fit()?
Why predict_proba()?
Difference between fit and transform?
Why train_test_split?
Random State?
OneHotEncoder(handle_unknown="ignore")?
Why median imputation?
Why most_frequent imputation?
⭐ My Favorite Interview Questions

These are the questions I'd ask if I were interviewing you:

Walk me through your entire pipeline from raw data to prediction.
Why did you choose Random Forest?
Explain your preprocessing pipeline.
What is data leakage, and how did you avoid it?
If recall is only 50%, what would you do next?
Why is recall more important than accuracy for tsunami prediction?
Why did you organize your project into multiple modules?
What did you learn from this project that you didn't learn from the Titanic project?
If a new earthquake arrives today, how would your pipeline process it?
If the dataset doubles in size tomorrow, what parts of your architecture would still work without changes?