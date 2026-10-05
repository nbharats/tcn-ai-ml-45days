"""Homework 2 (Medium, ~15 min, daily life): Your own data.

Goal: take some real spending data of yours (Swiggy/Zomato orders, a UPI
statement, screen time...) and answer three questions with Pandas:
  - spend per weekday  (which day do you spend the most?)
  - top 5 merchants    (where does most of your money go?)
  - a line plot of monthly total spend

A small sample file `orders.csv` is included here so the script runs out of the
box. To use your REAL data, export your order history as a CSV with the same
three columns (date, merchant, amount) and point `load_orders` at it. Remember
to strip personal identifiers before committing to a public repo.

Run:  py hw2_your_own_data.py
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-whitegrid")


def load_orders(path="orders.csv"):
    """Read the CSV and clean the amount column.

    Real-world amount columns are messy strings like "₹1,250". We strip the
    currency symbol and the thousands commas, then ask pandas to convert to
    numbers. `pd.to_numeric(errors="coerce")` turns anything unparseable into
    NaN instead of crashing, which we then drop.
    """
    df = pd.read_csv(path)
    # Remove the rupee sign and any commas, then convert to float.
    df["amount"] = df["amount"].str.replace("₹", "", regex=False)
    df["amount"] = df["amount"].str.replace(",", "", regex=False)
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["amount"])          # drop any row that failed to parse

    # Parse the date so we can pull weekday and month out of it later.
    df["date"] = pd.to_datetime(df["date"])
    df["weekday"] = df["date"].dt.day_name()    # e.g. "Monday"
    df["month"] = df["date"].dt.to_period("M")  # e.g. 2026-01
    return df


def main():
    df = load_orders()
    print("loaded", len(df), "orders, total spend Rs",
          f"{df['amount'].sum():,.0f}")

    # --- 1. spend per weekday -------------------------------------------------
    # groupby weekday -> sum amounts. Sorted high to low to see your heaviest day.
    by_weekday = df.groupby("weekday")["amount"].sum().sort_values(ascending=False)
    print("\nSpend per weekday:")
    print(by_weekday.round(0))

    # --- 2. top 5 merchants ----------------------------------------------------
    # Two stats at once with .agg: how many orders ("size") and the total ("sum").
    top = (df.groupby("merchant")["amount"]
             .agg(["size", "sum"])
             .sort_values("sum", ascending=False)
             .head(5))
    print("\nTop 5 merchants:")
    print(top.round(0))

    # --- 3. line plot of monthly total ----------------------------------------
    monthly = df.groupby("month")["amount"].sum()
    ax = monthly.plot(kind="line", marker="o", title="Monthly spend (₹)",
                      figsize=(8, 3.5))
    ax.set_xlabel("month")
    ax.set_ylabel("₹")
    plt.tight_layout()
    plt.savefig("monthly_spend.png", dpi=150)
    print("\nsaved monthly_spend.png")
    plt.show()


if __name__ == "__main__":
    main()
