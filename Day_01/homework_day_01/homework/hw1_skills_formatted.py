"""Homework 1 (Easy, ~10 min): Your skills, formatted.

Goal: take a dict of 6 skills -> confidence (0..1) and print a clean table,
sorted highest-confidence first, using a comprehension + a lambda + an f-string.
"""

# 6 skills, each with a self-rated confidence between 0 and 1.
skills = {
    "python": 0.65,
    "sql": 0.40,
    "numpy": 0.55,
    "pandas": 0.45,
    "git": 0.75,
    "linux": 0.30,
}

# Sort by confidence descending. `key=lambda kv: kv[1]` reads each (name, conf)
# pair and sorts on the confidence (the value at index 1).
ranked = sorted(skills.items(), key=lambda kv: kv[1], reverse=True)

# Format specs used in the f-string:
#   {name:<12}  -> left-align the name in a 12-char wide column
#   {conf:.0%}  -> show confidence as a percentage with 0 decimals (0.65 -> 65%)
print(f"{'skill':<12} confidence")
print("-" * 22)
for name, conf in ranked:
    print(f"{name:<12} {conf:.0%}")
