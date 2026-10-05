# SugarSense: Early Diabetes Risk Screening — Summary

## Best model
**Logistic Regression** (tuned via `RandomizedSearchCV`, `C≈1.40`, L2 penalty). Despite tuning Random Forest and XGBoost, neither matched Logistic Regression's validation ROC-AUC or generalization gap — the simplest model in the comparison generalized best on this 768-row, mostly-linear dataset. Random Forest and XGBoost both reached perfect training ROC-AUC (1.000) with default settings, a textbook overfitting case; tuning (shallower `max_depth`, stronger regularization) shrank but did not close their gap relative to Logistic Regression's near-zero gap (0.011).

## Key metrics (test set, n=154)

| Metric | Default threshold (0.5) | Tuned threshold (0.347) |
|---|---|---|
| ROC-AUC | 0.816 | 0.816 (unchanged — threshold doesn't affect ranking) |
| Recall (diabetic) | 74% (14 missed) | **87% (7 missed)** |
| Precision (diabetic) | 61% | 55% |
| False positives | 26 | 38 |

CV validation ROC-AUC: 0.845 (5-fold stratified).

## Threshold choice
The default 0.5 threshold missed 14 of 54 diabetic patients in testing — too high a miss rate for a screening tool. Using out-of-fold predictions on the training set, a threshold of **0.347** was selected as the lowest value achieving ≥85% recall with the best available precision. Applied once to the test set, it cut missed diabetics in half (14→7) at the cost of 12 additional false alarms (26→38). For this use case the trade is justified: a missed diabetic has no further diagnostic opportunity until symptoms worsen, while a false alarm only costs one extra, low-stakes lab visit.

## Limitations
- Dataset covers only **female patients aged 21+** from one population (Pima heritage) — not validated for men, children, or other groups
- **Insulin (48.7%)** and **SkinThickness (29.6%)** had a large share of values imputed rather than measured, after identifying disguised missingness (zeros recorded where a measurement should never be zero)
- A regression bonus task confirmed Glucose **cannot** be reliably estimated from cheaper measurements alone (low R²) — the real glucose tolerance test remains necessary, it cannot be "guessed away"
- This is a **screening aid, not a diagnosis**. Every flagged (or cleared) result still requires a qualified clinician's follow-up judgment.
