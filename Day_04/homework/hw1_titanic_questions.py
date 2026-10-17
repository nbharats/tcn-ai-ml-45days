"""Homework 1 (Easy, ~10 min): Three more Titanic questions.

Goal: answer three questions about the Titanic dataset using `groupby` ONLY
(no manual loops), then make ONE plot with labelled axes and save it as a PNG.

  Q1. Survival rate by `embark_town`  (where each passenger boarded).
  Q2. Median fare by `class` AND `alone`  (a 2-key groupby).
  Q3. Age histogram of survivors vs non-survivors, using sns.histplot(hue=...).

Run:  py hw1_titanic_questions.py
Needs: pandas, seaborn, matplotlib (all pre-installed on Colab).
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")


def load_titanic():
    """Load the Titanic dataset. Try seaborn's bundled copy first (works offline),
    then fall back to the raw GitHub CSV used in class."""
    try:
        return sns.load_dataset("titanic")
    except Exception:
        url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
        return pd.read_csv(url)


def main():
    df = load_titanic()
    print("loaded:", df.shape, "rows")

    # --- Q1: survival rate by embark_town ------------------------------------
    # survived is 0/1, so .mean() on it = fraction who survived.
    # round(3) keeps 3 decimals (e.g. 0.554 = 55.4%).
    q1 = df.groupby("embark_town")["survived"].mean().round(3)
    print("\nQ1 survival rate by embark_town:")
    print(q1)

    # --- Q2: median fare by class and alone ----------------------------------
    # Two grouping keys -> a multi-index Series. observed=True avoids empty
    # combos for categorical columns (keeps the output tidy).
    q2 = df.groupby(["class", "alone"], observed=True)["fare"].median()
    print("\nQ2 median fare by (class, alone):")
    print(q2)

    # --- Q3: age histogram, survivors vs non-survivors ------------------------
    # sns.histplot draws the two groups side-by-side with hue=...; element="step"
    # makes overlapping bars easier to read.
    fig, ax = plt.subplots(figsize=(8, 4.5))
    sns.histplot(df, x="age", hue="survived", bins=30, element="step", ax=ax)
    ax.set_title("Titanic: age of survivors vs non-survivors")
    ax.set_xlabel("Age (years)")
    ax.set_ylabel("Passenger count")

    fig.savefig("titanic_questions.png", dpi=150, bbox_inches="tight")
    print("\nsaved titanic_questions.png")
    plt.show()


if __name__ == "__main__":
    main()
