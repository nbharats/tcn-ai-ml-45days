# Day 03 Homework — NumPy, Pandas & Visualization

Three short tasks. Each one in this folder is a runnable Python file
(`hw1_...`, `hw2_...`, `hw3_...`). Run them with `py hw1_titanic_questions.py`,
etc. Sample data files (`orders.csv`, `startup_funding.csv`) are included so
every script runs out of the box. Each script saves a labelled PNG plot.

> Tip: on a normal laptop run these directly (a plot window pops up). On a
> headless machine set `MPLBACKEND=Agg` first so the plot saves without a window.

---

## Q1 (Easy, 10 min) — Three more Titanic questions

**What the question is asking**
Using only `groupby` (no manual loops), answer three questions about the
Titanic passengers:
  1. What was the survival rate for each boarding town (`embark_town`)?
  2. What was the median ticket fare, split by class AND by whether the passenger
     was alone (`alone`)?
  3. Make one age histogram that shows survivors and non-survivors on the same
     chart, using `sns.histplot(hue=...)`. Label the axes and save it as a PNG.

**How to approach it**
Load the Titanic dataset (seaborn has it built-in). For Q1, group the rows by
`embark_town` and take the mean of the `survived` column — since `survived` is
0 or 1, the mean is exactly the survival fraction. For Q2, group by two keys
at once (`class` and `alone`) and take the median of `fare`; using
`observed=True` keeps the output tidy. For Q3, make one figure with
`fig, ax = plt.subplots()`, call `sns.histplot` with `x="age"` and
`hue="survived"` (that colour-splits the bars by who lived), give the axes
labels and a title, and `fig.savefig` the result.

**How the solution does it (in words)**
`load_titanic` first tries seaborn's bundled copy of the data and falls back to
the raw CSV URL if offline. Q1 prints the survival rate per town (Cherbourg
highest at ~55%, Southampton lowest at ~34%). Q2 prints the median fare for
each class/alone combination on one tidy table. Q3 draws the age histogram with
the two groups as stepped bars so overlaps stay readable, labels both axes,
saves `titanic_questions.png`, then shows the plot.

---

## Q2 (Medium, 15 min, daily life) — Your own data

**What the question is asking**
Get some real spending data of yours — Swiggy/Zomato orders, a UPI statement,
or phone screen time — as a CSV (or type ~30 rows by hand). Load it, clean the
amount column (which comes as messy text), and answer three questions:
  - how much you spend on each weekday,
  - your top 5 merchants,
  - a line plot of your total spend per month.
Then commit it to your repo after removing any personal identifiers.

**How to approach it**
Read the CSV with pandas. The amount column is the hard part: real-world amounts
look like "₹1,250" — a currency symbol plus comma thousands separators — which
pandas cannot read as a number. So strip the "₹" and the commas with
`str.replace`, then `pd.to_numeric(errors="coerce")` to turn the cleaned text
into numbers (anything still unparseable becomes NaN and is dropped). Parse
the date column with `to_datetime` so you can pull the weekday name and the
month out of it. For the three answers: `groupby("weekday")["amount"].sum()`
sorted descending; `groupby("merchant")["amount"].agg(["size", "sum"])` to get
both order count and total per merchant, taking the top 5; and
`groupby("month")["amount"].sum()` plotted as a line.

**How the solution does it (in words)**
`load_orders` reads the included `orders.csv`, cleans the "₹" and commas off the
amounts, converts to numbers, drops any bad rows, and adds `weekday` and `month`
columns from the date. The script then prints total spend, the per-weekday
breakdown (Saturday heaviest), the top 5 merchants with both order count and
total, and saves a labelled monthly line plot as `monthly_spend.png`. To use
your real data, export a CSV with the same `date, merchant, amount` columns and
swap the file path in `load_orders`.

---

## Q3 (Stretch, 15 min) — Indian startup funding cleanup

**What the question is asking**
Take the messy Kaggle "Indian Startup Funding" dataset. Two columns are always
broken: the amounts are Indian-format strings like `"1,50,00,000"` (commas as
thousand separators) and the city names are spelled five different ways
(Bangalore / Bengaluru / bangalore / Banglore ...). Clean both, then make two
plots: total funding by year, and the top 10 cities by funding. This is the
exact messiness of real working data.

**How to approach it**
For the amount: convert to a string, remove every comma (and the rupee symbol
just in case), then `pd.to_numeric(errors="coerce")` to get numbers, and drop
the rows that still failed. For the city: strip outer spaces and lowercase
everything so "Bengaluru " and "bangalore" look the same, then use a mapping
dictionary to fold every known spelling/alias into one official name (e.g. all
of Bangalore/Bengaluru/Banglore -> "Bengaluru"); anything not in the dictionary
just gets capitalized as a fallback. Parse the date so you can group by year.
Finally, `groupby("year")["amount"].sum()` for the first plot and
`groupby("city")["amount"].sum().sort_values().head(10)` for the second, drawn
side by side in one figure.

**How the solution does it (in words)**
`clean_amount` strips commas and the rupee symbol and converts to numbers,
dropping unparseable rows. `clean_city` strips and lowercases the city text,
maps every known spelling to one canonical name via a dictionary, and falls
back to a simple title-case for anything unmapped. After cleaning, the script
prints the unique cities (all merged cleanly: Bengaluru, Delhi, Gurugram,
Mumbai, Noida), the total funding per year, and the top 10 cities, then saves a
two-panel figure (`startup_funding_clean.png`) with a bar chart of funding by
year and a horizontal bar chart of the top cities. The included
`startup_funding.csv` is a 20-row sample; swap in the full Kaggle CSV (same
columns) for real practice.
