"""Homework 2 (Medium, ~15 min): JD keyword counter.

Read 3 job-description text files (jd1.txt, jd2.txt, jd3.txt), count how often
each skill we care about appears (case-insensitive), and print the union of
skills that show up in ANY of the 3 files -> that is your study list.
"""

from collections import Counter


def count_skills(path, skills):
    """Return a Counter: how many times each skill string appears in `path`.

    Uses `with open` (auto-closes the file), a dict comprehension to build the
    counts, and `try/except FileNotFoundError` so a missing file does not crash
    the whole run.
    """
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read().lower()
    except FileNotFoundError:
        print(f"[warn] {path} not found, skipping")
        return Counter()

    # Lower the text once, then count each (lowercased) skill in it.
    # .count() does simple substring matching, which is fine for a homework.
    return Counter({s: text.count(s.lower()) for s in skills})


# The skills we are tracking across job descriptions.
my_skills = ["python", "sql", "pytorch", "pandas", "aws", "docker", "nlp", "spark"]

# Count skills in each JD file (a list comprehension builds the 3 Counters).
counts = [count_skills(f"jd{i}.txt", my_skills) for i in (1, 2, 3)]

for i, c in enumerate(counts, start=1):
    print(f"jd{i}.txt -> {dict(c)}")

# Union of skills that appear in ANY JD = your study list.
# set().union(*iterable) merges the keys of all 3 Counters into one set.
study_list = set().union(*[c.keys() for c in counts])

print("\nStudy list (skills asked across the 3 JDs):")
print(sorted(study_list))
