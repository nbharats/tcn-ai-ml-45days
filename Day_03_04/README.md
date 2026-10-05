# Day 03 · The data stack: NumPy, Pandas, Matplotlib (+ Git)

**Phase 1 · Python for AI (pre-requisite) · 60 minutes**

Delete the loops from Day 01: vectorised NumPy, Pandas load → inspect → clean → groupby → merge, Seaborn/Matplotlib
plots for a README, and the first `git push`. Dataset: Titanic (891 rows) end to end.

## Learning outcomes
By the end of the hour students can:
1. Create and manipulate ndarrays (`shape`, `dtype`, `axis`), explain vectorisation and state the broadcasting rule (align right; equal or 1) and apply it to standardise a feature matrix.
2. Distinguish views from copies in NumPy indexing (slices vs masks) and `loc` vs `iloc` in Pandas.
3. Load a CSV, take the four first looks, and handle missing values per column (drop / fill per-group median / flag).
4. Answer questions with `groupby`/`agg`, `pivot_table` and `merge` (and check row counts after a join).
5. Produce labelled Seaborn/Matplotlib figures, save them as PNG, and push notebook + image to GitHub (add → commit → push, or Colab "Save a copy in GitHub").

## 60-minute plan
| Min | Section (HTML id) | What happens |
|---|---|---|
| 00–05 | Hook (`#hook`) | Kaggle Titanic page; "every dataset is a table of numbers" (images, batches, sentences); three tabs. |
| 05–22 | Concept (`#concept`) | Three mental models (array / frame / figure). NumPy laddoo-box analogy + interactive broadcasting visualizer. Pandas IPL points-table analogy + animated split-apply-combine. Chart.js survival-by-class-and-sex (real numbers). Matplotlib two-line pattern. |
| 22–32 | Deeper (`#deeper`) | Broadcasting formally; indexing table; missing values policy; merge/join; Git three-areas interactive diagram; interview phrasing. |
| 32–45 | Code (`#code`) | NumPy in 12 lines; load/inspect/clean; same question three ways (groupby / pivot / pure Python); plot + save + git commands. Switch to notebook. |
| 45–50 | Real world & tools (`#realworld`) | Kaggle Titanic, Kaggle Learn Pandas, Seaborn gallery, NumPy broadcasting docs, Indian startup funding dataset, GitHub Skills; tools: Colab, Polars, DuckDB, Plotly, GitHub Desktop, Claude/ChatGPT. |
| 50–53 | Career corner (`#career`) | Analyst → ML engineer path; 3 interview Qs (missing values, loc vs iloc, broadcasting); action: push + README + LinkedIn skills. |
| 53–56 | Quiz (`#quiz`) | 3 questions (broadcast error, groupby return type, staging area). |
| 56–58 | Homework (`#homework`) | Easy Titanic groupby / Medium own spending CSV / Stretch Indian startup funding cleanup. |
| 58–60 | Next (`#next`) | Day 04 teaser + 3Blue1Brown gradient-descent video. |

## Prerequisites
- Days 01–02 (containers, comprehensions, `with open`, classes). GitHub account from Day 00. Internet for the Titanic CSV (the notebook falls back to seaborn's cached copy if the URL fails).

## Files in this folder
- `Day_03_NumPy_Pandas_Viz.html` — lesson page with the broadcasting visualizer, split-apply-combine animation, Git flow diagram and a Chart.js chart.
- `Day_03_NumPy_Pandas_Viz.ipynb` — Colab notebook, 36 cells, CPU, ~20 s. Downloads Titanic, writes `titanic_eda.png` and `titanic_clean.csv`, runs a local git demo in `/tmp`.
- `README.md` — this plan.

## Links used
- https://www.kaggle.com/competitions/titanic · https://www.kaggle.com/competitions/titanic/data · https://www.kaggle.com/learn/pandas
- https://numpy.org/doc/stable/user/absolute_beginners.html · https://numpy.org/doc/stable/user/basics.broadcasting.html · https://pandas.pydata.org/docs/user_guide/10min.html
- https://seaborn.pydata.org/examples/index.html · https://www.kaggle.com/datasets/sudalairajkumar/indian-startup-funding · https://github.com/skills/introduction-to-github · https://github.com/trending/jupyter-notebook
- Data: https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv
- Tools: https://colab.research.google.com/ · https://pola.rs/ · https://duckdb.org/ · https://plotly.com/python/ · https://github.com/apps/desktop · https://claude.ai/
- Video for tomorrow: https://www.youtube.com/watch?v=IHZwWFHWa-w

## Homework summary
- **Easy (10 min):** three more Titanic groupby questions + one labelled, saved plot.
- **Medium (15 min, daily life):** your own orders/UPI/screen-time CSV → spend per weekday, top merchants, monthly line plot; commit (no personal identifiers).
- **Stretch (15 min):** clean the Indian startup funding dataset (string amounts, inconsistent cities) and plot funding by year and top-10 cities.

## If you're running late, skip:
- The views-vs-copies cell (one sentence: "slices share memory, masks copy; use `.copy()` when unsure").
- The `apply` vs `pd.cut` comparison and the correlation heatmap.
- The terminal git demo; use Colab's "File → Save a copy in GitHub" only.
