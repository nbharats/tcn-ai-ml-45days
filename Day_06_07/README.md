# Day 04 · How a machine learns a line

**Phase 2 · Supervised ML · 60 minutes**

The first learning algorithm: simple linear regression fitted by gradient descent. Hypothesis space, MSE cost,
gradients, the update rule, learning rate, batch/mini-batch/stochastic, feature scaling, closed form and sklearn.
The page's centrepiece is an interactive canvas where a learning-rate slider makes the line converge, crawl or explode.

## Learning outcomes
By the end of the hour students can:
1. Separate the three ideas: model (`ŷ = wx + b`), cost (MSE), optimiser (gradient descent).
2. Write the MSE gradients (`dw = mean(err·x)`, `db = mean(err)`) and the update rule, and implement them in 12 lines of NumPy.
3. Predict what a too-small / too-large learning rate does to the loss curve and diagnose it from the curve.
4. Explain why feature scaling turns a narrow valley into a round bowl and allows a much larger α.
5. Contrast batch, stochastic and mini-batch GD; obtain the same line from the closed form and `sklearn.LinearRegression`/`SGDRegressor`.

## 60-minute plan
| Min | Section (HTML id) | What happens |
|---|---|---|
| 00–05 | Hook (`#hook`) | "What salary should I ask for?" (Riya's counter-offer); TensorFlow Playground learning-rate demo; 3Blue1Brown clip. |
| 05–23 | Concept (`#concept`) | Hypothesis space. Cost via Zomato delivery-time analogy. Gradient descent via fog-on-the-hill analogy. **Interactive line-fit demo** (α slider, batch/mini/SGD, standardise toggle, live loss curve). **Bowl animation** (ball + gradient arrow). Chart.js: three learning rates computed live. |
| 23–33 | Deeper (`#deeper`) | Four formulas decoded symbol by symbol; batch/SGD/mini-batch table; feature scaling and the stability limit 2/λmax; closed form; interview phrasing. |
| 33–45 | Code (`#code`) | cost → gradient_descent → closed form / LinearRegression / SGDRegressor tabs → scaling. Switch to the notebook: animated fit, LR sweep, contour paths, tips dataset. |
| 45–50 | Real world & tools (`#realworld`) | 3Blue1Brown, TF Playground, Distill momentum, Andrew Ng course, SGDRegressor docs, Kaggle salary dataset; tools: scikit-learn, PyTorch, W&B, Optuna, Desmos, Claude. |
| 50–53 | Career corner (`#career`) | "Explain gradient descent" as interview Q1; 3 Qs (LR too high/low, MSE vs MAE, batch vs SGD); action: LinkedIn post with the loss-curve PNG. |
| 53–56 | Quiz (`#quiz`) | 3 questions (diverging loss, ∂J/∂b, what scaling does). |
| 56–58 | Homework (`#homework`) | Easy LR sweep / Medium commute predictor / Stretch two-feature GD. |
| 58–60 | Next (`#next`) | Day 05 teaser + checklist. |

## Prerequisites
- Day 03 (NumPy vectorisation and broadcasting: `(err * x).mean()`, `(X - mean)/std`). School calculus: derivative of a square.

## Files in this folder
- `Day_04_How_Machines_Learn.html` — lesson page with the interactive gradient-descent line-fit demo, the bowl animation and a live-computed Chart.js learning-rate chart.
- `Day_04_How_Machines_Learn.ipynb` — Colab notebook, 29 cells, CPU, ~15 s (includes a matplotlib `FuncAnimation` rendered to an HTML player). Saves `lr_sweep.png`.
- `README.md` — this plan.

## Links used
- https://www.youtube.com/watch?v=IHZwWFHWa-w · https://playground.tensorflow.org/ · https://distill.pub/2017/momentum/
- https://www.coursera.org/specializations/machine-learning-introduction · https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html · https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html
- https://www.kaggle.com/datasets/abhishek14398/salary-dataset-simple-linear-regression
- Tools: https://scikit-learn.org/ · https://pytorch.org/ · https://wandb.ai/site · https://optuna.org/ · https://www.desmos.com/calculator · https://claude.ai/

## Homework summary
- **Easy (10 min):** loss curves for α ∈ {0.001, 0.003, 0.01, 0.03, 0.05} on one log-scale chart, one sentence each; post on LinkedIn.
- **Medium (15 min, daily life):** 15 commute trips (km, minutes) → fit with own GD and sklearn; interpret w (min/km) and b (fixed time).
- **Stretch (15 min):** two-feature GD with `X @ w`; show divergence without scaling and convergence with it.

## If you're running late, skip:
- The batch/mini-batch/stochastic section in the notebook (keep the table in Deeper).
- The `SGDRegressor` tab and the tips dataset cell.
- The closed-form derivation; just state "for a line there is an exact formula; sklearn uses it".
