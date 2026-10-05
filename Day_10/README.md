# Day 06 · Classification: from yes/no to probabilities

Logistic regression: sigmoid, log-loss / cross-entropy, decision boundary, threshold tuning, multiclass (softmax vs one-vs-rest).

## Learning outcomes
By the end of the hour a student can:
1. Explain why linear regression fails for 0/1 targets and how the sigmoid fixes it (log-odds are linear in features).
2. Write log-loss and its gradient, and state that the gradient has the same form as linear regression's.
3. Draw and interpret a linear decision boundary; explain what changing the threshold does to it.
4. Tune a classification threshold to a business cost using confusion counts (precision vs recall trade-off).
5. Use `LogisticRegression` correctly (`C` is inverse regularisation, `predict_proba`, `decision_function`) and handle multiclass with softmax vs `OneVsRestClassifier`.

## 60-minute plan
| Min | Section (HTML id) | What happens |
|---|---|---|
| 00–05 | Hook (`#hook`) | UPI fraud model gives "0.03", bank chooses thresholds; open TensorFlow Playground (0 hidden layers + sigmoid = logistic regression) |
| 05–23 | Concept (`#concept`) | Tap-vs-switch analogy; **live sigmoid lab** (w, b, threshold sliders; "Fit with gradient descent" animation; live TP/FP/FN/TN, precision, recall); **2-D loan-approval boundary** with threshold slider and probability shading; log-loss Chart.js; DRS analogy; **softmax bars** with three score sliders |
| 23–33 | Deeper (`#deeper`) | Sigmoid ⟺ log-odds, log-loss, gradient, softmax + multiclass loss, linear-vs-logistic table, interview phrasing |
| 33–45 | Code (`#code`) | From-scratch NumPy vs sklearn (tabs), predict_proba/decision_function, threshold loop with confusion matrix, Iris softmax vs OvR, DecisionBoundaryDisplay. Switch to notebook |
| 45–50 | Real world & tools (`#realworld`) | MLU-Explain logistic regression, TF Playground, Give Me Some Credit, credit-card fraud dataset, sklearn docs, ISLR ch. 4; tools grid |
| 50–53 | Career (`#career`) | Fintech risk roles, 3 interview Qs, LinkedIn skills + sklearn issue tracker action |
| 53–56 | Quiz (`#quiz`) | σ(0), screening threshold direction, meaning of small C |
| 56–58 | Homework (`#homework`) | Easy / Medium / Stretch |
| 58–60 | Next (`#next`) | Teaser for Day 07 KNN & Naive Bayes |

## Prerequisites
- Day 04–05 (gradient descent, MSE, regularisation, `Pipeline` + `StandardScaler`).
- Basic probability (what "odds" means helps; the page defines it).

## Files in this folder
- `Day_06_Logistic_Regression.html` — lesson page. Interactive: sigmoid/threshold lab with animated gradient descent, 2-D decision boundary with threshold slider, log-loss chart, softmax sliders.
- `Day_06_Logistic_Regression.ipynb` — Colab notebook (CPU): synthetic placement data → why-not-linear plot → from-scratch GD → sklearn + odds ratios → decision boundary → cost-based threshold table → Iris softmax vs OvR → exercise on `C` → Telco churn homework scaffold.
- `README.md` — this plan.

## Links used
- https://playground.tensorflow.org/
- https://mlu-explain.github.io/logistic-regression/
- https://www.kaggle.com/c/GiveMeSomeCredit
- https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
- https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
- https://www.statlearning.com/
- https://github.com/scikit-learn/scikit-learn
- https://www.youtube.com/watch?v=HZGCoVF3YvM (3Blue1Brown, Bayes theorem, pre-watch for Day 07)
- Telco churn CSV: https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv
- Tools: Colab, Kaggle, Streamlit, GitHub Copilot, Claude, Weights & Biases

## Homework summary
- **Easy:** write odds-ratio sentences for the three placement features; find the CGPA where p = 0.5.
- **Medium:** Telco churn, cost-minimising threshold (₹200 call vs ₹3,000 lost customer); scaffold in notebook.
- **Stretch (job hunt):** logistic regression on your own job-application funnel; post the odds-ratio insight on LinkedIn.

## If you're running late, skip
- Idea 4 (softmax sliders) in Concept and notebook Section 6 — mention "softmax = sigmoid for K classes", return to it on Day 18.
- Code snippet 5 (DecisionBoundaryDisplay) — it is in the notebook.
- Do not skip the threshold demo; it is the idea students carry into Day 12.
