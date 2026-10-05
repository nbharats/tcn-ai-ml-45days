# Day 05 · Regression beyond a line

Multiple linear regression, polynomial regression, multicollinearity (VIF), bias-variance trade-off, under/overfitting, and regularization with Ridge and Lasso.

## Learning outcomes
By the end of the hour a student can:
1. Fit and interpret a multiple linear regression (and explain why raw coefficients are not comparable before scaling).
2. Detect multicollinearity with VIF, state the 5/10 rules of thumb, and name three fixes.
3. Explain underfitting vs overfitting and the bias-variance trade-off with a train/test error curve.
4. Explain and apply Ridge (L2) vs Lasso (L1), including why Lasso produces exact zeros and why features must be scaled.
5. Choose `alpha` with `RidgeCV` / `LassoCV` inside a `Pipeline`.

## 60-minute plan
| Min | Section (HTML id) | What happens |
|---|---|---|
| 00–05 | Hook (`#hook`) | Zillow's 2021 iBuying collapse; "what is a 2BHK in Whitefield worth?"; open the Bengaluru Kaggle dataset on the projector |
| 05–23 | Concept (`#concept`) | Thali analogy for weights → multicollinearity; polynomial features; **live polynomial-degree slider** (train vs test MSE, resample-noise button for variance, λ slider); bias-variance Chart.js; **Ridge vs Lasso shrinkage demo** with alpha slider; train-journey packing analogy |
| 23–33 | Deeper (`#deeper`) | Normal equation, VIF formula, bias-variance decomposition, Ridge/Lasso cost functions, comparison table, interview phrasing |
| 33–45 | Code (`#code`) | 5 snippets: California housing OLS, VIF (statsmodels + by hand), degree sweep, Ridge/Lasso pipeline + CV, Lasso coefficient path. Switch to the notebook here |
| 45–50 | Real world & tools (`#realworld`) | MLU-Explain bias-variance, Kaggle House Prices, Bengaluru dataset, sklearn linear models guide, ISLR, Seeing Theory; tools grid |
| 50–53 | Career (`#career`) | Roles, 3 interview Qs, Kaggle submission + resume bullet action |
| 53–56 | Quiz (`#quiz`) | 3 questions (overfit signature, L1 vs L2, reading a VIF) |
| 56–58 | Homework (`#homework`) | Easy / Medium / Stretch |
| 58–60 | Next (`#next`) | Teaser for Day 06 Logistic Regression |

## Prerequisites
- Day 04 (cost function, gradient descent, `LinearRegression`, `train_test_split`).
- Day 03 (pandas basics, matplotlib).
- Colab account; Kaggle account for the homework dataset.

## Files in this folder
- `Day_05_Regression_Deep_Dive.html` — lesson page (projector + self-study). Interactive: polynomial-degree lab, bias-variance chart, Ridge-vs-Lasso coefficient demo.
- `Day_05_Regression_Deep_Dive.ipynb` — Colab notebook (CPU): California housing OLS → VIF → polynomial sweep → bias-variance simulation → Ridge/Lasso paths → CV → exercise → homework scaffold.
- `README.md` — this plan.

## Links used
- https://www.zillow.com/z/zestimate/
- https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data
- https://mlu-explain.github.io/bias-variance/
- https://www.kaggle.com/c/house-prices-advanced-regression-techniques
- https://scikit-learn.org/stable/modules/linear_model.html
- https://www.statlearning.com/
- https://seeing-theory.brown.edu/regression-analysis/index.html
- Tools: Colab, Kaggle, Optuna, Weights & Biases, Claude, Streamlit

## Homework summary
- **Easy:** 12 (hour, commute-minutes) points → fit degrees 1/2/6, pick one with a reason.
- **Medium:** Bengaluru house prices: clean `total_sqft`/`bhk`, compute VIF, compare OLS/Ridge/Lasso RMSE in lakhs (scaffold in notebook).
- **Stretch (job hunt):** Kaggle House Prices submission with `LassoCV` + a 3-line LinkedIn post.

## If you're running late, skip
- Section 5 of the notebook (bias-variance simulation) — the HTML "resample noise" button makes the same point in 30 seconds.
- Code snippet 5 (coefficient path) — mention it, assign as reading.
- Keep the polynomial slider and the Ridge-vs-Lasso demo; they are the lesson.
