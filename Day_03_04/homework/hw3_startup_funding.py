"""Homework 3 (Stretch, ~15 min): Indian startup funding cleanup.

Goal: take the messy Kaggle "Indian Startup Funding" dataset and clean the two
things that are always broken in real data:
  - amounts are strings like "1,50,00,000" (Indian numbering with commas) that
    must become numbers we can sum.
  - city names are spelled five different ways (Bangalore / Bengaluru /
    bangalore / Banglore ...) that must be merged into one label.

Then plot (1) total funding by year and (2) the top 10 cities by funding.

A small sample `startup_funding.csv` is included so the script runs without
downloading from Kaggle. Replace it with the full Kaggle CSV for real practice
(columns: startup, city, amount, date, industry).

Run:  py hw3_startup_funding.py
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-whitegrid")


def clean_amount(series):
    """Turn Indian-format amount strings into floats.

    Indian amounts use commas as thousand separators: "1,50,00,000" = 1,50,00,000
    = 15,000,000 in Western notation. We just remove every comma, then ask
    pandas to convert to a number. errors="coerce" makes unparseable values NaN
    (which we drop) instead of raising.
    """
    s = series.astype(str)
    s = s.str.replace(",", "", regex=False)
    s = s.str.replace("₹", "", regex=False)     # some rows may carry the symbol
    return pd.to_numeric(s, errors="coerce")


def clean_city(series):
    """Merge the many spellings of one city into a single canonical name.

    First strip spaces and lower-case everything (so "Bengaluru " and
    "bengaluru" match). Then a mapping dict fixes the known misspellings/aliases
    to one official spelling. `.map()` returns NaN for anything not in the
    dict, so we keep the cleaned-but-unmapped name as a fallback.
    """
    s = series.astype(str).str.strip().str.lower()

    city_map = {
        "bangalore": "Bengaluru",
        "bengaluru": "Bengaluru",
        "banglore": "Bengaluru",     # common typo
        "banglore ": "Bengaluru",
        "delhi": "Delhi",
        "new delhi": "Delhi",
        "mumbai": "Mumbai",
        "bombay": "Mumbai",
        "gurugram": "Gurugram",
        "gurgaon": "Gurugram",
        "noida": "Noida",
    }
    # map the cleaned name; if not found, just capitalize the cleaned name.
    return s.map(city_map).fillna(s.str.title())


def main():
    df = pd.read_csv("startup_funding.csv")
    print("loaded", len(df), "rows")

    # --- clean amount --------------------------------------------------------
    df["amount"] = clean_amount(df["amount"])
    df = df.dropna(subset=["amount"])         # drop rows whose amount failed

    # --- clean city ----------------------------------------------------------
    df["city"] = clean_city(df["city"])

    # --- parse the date so we can group by year ------------------------------
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["year"] = df["date"].dt.year

    print("\ncleaned cities:", sorted(df["city"].unique()))
    print("amount dtype is numeric:", df["amount"].dtype)

    # --- plot 1: total funding by year ---------------------------------------
    by_year = df.groupby("year")["amount"].sum()
    print("\nTotal funding by year (Rs):")
    print(by_year)

    # --- plot 2: top 10 cities by funding ------------------------------------
    top_cities = df.groupby("city")["amount"].sum().sort_values(ascending=False).head(10)
    print("\nTop 10 cities by funding (Rs):")
    print(top_cities)

    fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))

    axes[0].bar(by_year.index.astype(int).astype(str), by_year.values)
    axes[0].set_title("Total funding by year")
    axes[0].set_xlabel("year")
    axes[0].set_ylabel("funding (₹)")

    axes[1].barh(top_cities.index[::-1], top_cities.values[::-1])
    axes[1].set_title("Top 10 cities by funding")
    axes[1].set_xlabel("funding (₹)")

    plt.tight_layout()
    plt.savefig("startup_funding_clean.png", dpi=150)
    print("\nsaved startup_funding_clean.png")
    plt.show()


if __name__ == "__main__":
    main()
