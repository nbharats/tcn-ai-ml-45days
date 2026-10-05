# Day 07 · Lazy learners and probabilistic learners: KNN & Naive Bayes

K-Nearest Neighbours (distance metrics, choosing k, scaling, curse of dimensionality) and Naive Bayes (Bayes' theorem, Gaussian / Multinomial, Laplace smoothing), ending with a real SMS spam filter.

## Learning outcomes
By the end of the hour a student can:
1. Explain KNN as an instance-based, lazy learner; write it from scratch; state its O(n·d) prediction cost.
2. Choose k by cross-validation and explain it as a bias-variance knob; explain why feature scaling is mandatory for KNN.
3. Describe the curse of dimensionality and its practical consequence for distance-based models.
4. State Bayes' theorem, the naive independence assumption, and the Multinomial NB likelihood with Laplace smoothing (and why alpha = 0 breaks it).
5. Build and honestly evaluate a `CountVectorizer` + `MultinomialNB` spam filter on imbalanced data.

## 60-minute plan
| Min | Section (HTML id) | What happens |
|---|---|---|
| 00–05 | Hook (`#hook`) | 1998 Bayesian spam filters + the Swiggy delivery-partner "ask the nearest three" story; open the CS231n KNN demo and Paul Graham's essay |
| 05–23 | Concept (`#concept`) | New-neighbourhood analogy; **KNN playground** (click to place a query, k slider, Euclidean/Manhattan, scale toggle showing rupees drowning km, decision-region painting, live leave-one-out accuracy); **curse-of-dimensionality Chart.js** computed live; CID-inspector analogy for Bayes; **live Naive Bayes** (type a message, per-word log-odds bars, prior slider) |
| 23–33 | Deeper (`#deeper`) | Euclidean/Manhattan/Minkowski/cosine, prediction cost and k choice, curse formula, Bayes + naive factorisation, Multinomial (Laplace) and Gaussian likelihoods, KNN vs NB vs LogReg table, interview phrasing |
| 33–45 | Code (`#code`) | KNN pipeline + k sweep (sklearn vs scratch tabs), GaussianNB attributes, spam pipeline, spammiest words from `feature_log_prob_`, classification report on imbalanced data. Switch to notebook |
| 45–50 | Real world & tools (`#realworld`) | UCI SMS dataset, CS231n demo, A Plan for Spam, FAISS, sklearn guides, 3Blue1Brown Bayes; tools grid |
| 50–53 | Career (`#career`) | Trust & Safety / NLP / search roles, 3 interview Qs, deploy-on-HF-Spaces action |
| 53–56 | Quiz (`#quiz`) | k and bias-variance, zero-probability bug, which model stores the data |
| 56–58 | Homework (`#homework`) | Easy / Medium / Stretch |
| 58–60 | Next (`#next`) | Teaser for Day 08 Decision Trees |

## Prerequisites
- Day 05–06 (bias-variance vocabulary, `Pipeline` + `StandardScaler`, confusion matrix basics).
- Basic probability: conditional probability; the 3Blue1Brown Bayes video was assigned on Day 06.

## Files in this folder
- `Day_07_KNN_NaiveBayes.html` — lesson page. Interactive: KNN click-to-query playground, curse-of-dimensionality chart, live Naive Bayes message classifier.
- `Day_07_KNN_NaiveBayes.ipynb` — Colab notebook (CPU): KNN from scratch → scaling demo → k by CV + decision regions → curse simulation → digits mistakes gallery → Bayes worked example + GaussianNB rebuilt by hand → SMS spam filter (download with offline fallback) → smoothing exercise → homework/Gradio scaffold.
- `README.md` — this plan.

## Links used
- http://vision.stanford.edu/teaching/cs231n-demos/knn/
- http://www.paulgraham.com/spam.html
- https://archive.ics.uci.edu/dataset/228/sms+spam+collection
- https://github.com/facebookresearch/faiss
- https://scikit-learn.org/stable/modules/neighbors.html and https://scikit-learn.org/stable/modules/naive_bayes.html
- https://www.youtube.com/watch?v=HZGCoVF3YvM
- SMS data mirror used by the notebook: https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv
- Tools: Colab, Kaggle, Hugging Face, Chroma, Gradio, ChatGPT

## Homework summary
- **Easy:** run 20 of your own (anonymised) SMS through the filter; find the word that fooled it.
- **Medium:** k-sweep on `load_digits` with CV; gallery of mistakes next to their nearest neighbour.
- **Stretch (job hunt):** deploy the spam filter as a Gradio app on Hugging Face Spaces; add the link to resume/LinkedIn.

## If you're running late, skip
- Notebook Section 3 (curse simulation) — the HTML chart already shows it.
- Notebook Section 4 (digits gallery) — assign as the Medium homework, which it already is.
- Keep the KNN playground (scale toggle!) and the live NB demo; they carry the two key insights.
