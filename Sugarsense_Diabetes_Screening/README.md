# SugarSense — Early Diabetes Risk Screening

A supervised machine-learning mini-project predicting diabetes risk from 8 cheap, quick clinical measurements, built for a public-health NGO screening use case.

## Problem

Lab-grade diabetes diagnosis is expensive and slow, so many cases go undetected until complications appear. This project builds a model that flags high-risk patients from cheap measurements (age, BMI, blood pressure, etc.) so health workers know who to send for a full lab test — a screening aid, not a diagnosis.

Binary classification: predict `Outcome` (1 = diabetic) from 8 features in the Pima Indians Diabetes Database (768 patients, all female, age 21+). Primary metrics: **ROC-AUC** and **recall for the diabetic class** — missing a diabetic patient is treated as costlier than a false alarm.

## Approach

1. **Data audit** — `isna().sum()` showed no missing values, but `describe()` revealed biologically impossible zeros in Glucose, BloodPressure, SkinThickness, BMI, and especially Insulin (48.7% zero) and SkinThickness (29.6% zero) — these were relabeled as missing.
2. **EDA** — Glucose showed by far the clearest separation by Outcome; BloodPressure and SkinThickness showed little standalone signal.
3. **Feature engineering** — 4 same-row, leak-free features: `Insulin_Missing` flag, `Is_Obese` flag, `Age_Glucose_Risk` interaction, `BodyFat_Proxy`.
4. **Pipelines** — stratified 80/20 split (`random_state=42`), per-model `Pipeline` (median imputation → scaling where needed → model), class imbalance handled via `class_weight='balanced'` / `scale_pos_weight`. Imputer/scaler fit only on training folds to avoid leakage.
5. **Model comparison** — 6 models (Logistic Regression, KNN, Decision Tree, Random Forest, XGBoost, SVM) under 5-fold stratified CV, compared on accuracy/precision/recall/F1/ROC-AUC plus an overfit gap (train − val).
6. **Tuning** — `RandomizedSearchCV` (scoring=`roc_auc`) on Logistic Regression, Random Forest, and XGBoost.
7. **Test evaluation** — final model evaluated once on the held-out test set.
8. **Threshold tuning** — out-of-fold training predictions used to find a threshold hitting ≥85% recall.
9. **Interpretation** — permutation importance checked against EDA; conclusion and limitations documented.

## Results

**Final model: Logistic Regression** — despite tuning, Random Forest and XGBoost could not match its validation ROC-AUC or generalization gap; a regularized linear model outperformed tuned ensembles on this modest, mostly-linear dataset.

| | Default threshold (0.5) | Tuned threshold (0.347) |
|---|---|---|
| Recall (diabetic) | 74% (40/54 caught, 14 missed) | 87% (47/54 caught, 7 missed) |
| Precision (diabetic) | 61% | 55% |
| False positives | 26 | 38 |

- Test ROC-AUC: **0.816** (CV estimate: 0.845)
- Glucose dominates feature importance (~6x the next strongest feature), consistent with EDA
- Imputer comparison: median and KNN-imputation perform identically; dropping missing rows looked better on paper but trains on half the data and risks excluding a specific sub-population

See `summary.md` for the full write-up including limitations and ethics notes.

## Repo structure

```
Sugarsense_Diabetes_Screening/
├── README.md
├── summary.md
├── data/
│   └── diabetes_screening_data.csv
├── notebooks/
│   └── sugarsense.ipynb
└── models/
    └── sugarsense_model.joblib
```

## How to run

1. Clone the repo and `cd Sugarsense_Diabetes_Screening`
2. Install dependencies: `pip install numpy pandas matplotlib seaborn scikit-learn xgboost joblib`
3. Open `notebooks/sugarsense.ipynb` and **Restart & Run All** — the notebook runs top to bottom without errors
4. To screen a new patient without rerunning the notebook:
   ```python
   import joblib
   model = joblib.load("models/sugarsense_model.joblib")
   # see screen_patient() in the notebook for the full preprocessing wrapper
   ```

## Limitations & responsible use

This dataset covers only female patients aged 21+ from one population; the model has not been validated on men, children, or other groups. Large portions of Insulin (48.7%) and SkinThickness (29.6%) were imputed rather than measured. This tool is a low-cost **screening aid** to flag patients for a full lab work-up — it is not a diagnosis, and every result still requires a qualified clinician's judgment.
