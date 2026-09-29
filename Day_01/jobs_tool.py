"""Tiny job-market analyzer.  Usage:  python jobs_tool.py jobs.csv [--city Pune]"""
import sys, csv, json
from collections import Counter

def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            try:
                r["salary_lpa"] = float(r["salary_lpa"])
            except ValueError:
                continue
            r["skills"] = {s.strip().lower() for s in r["skills"].split(";") if s.strip()}
            rows.append(r)
    return rows

def report(rows, top_n=5):
    counts = Counter(s for r in rows for s in r["skills"])
    avg = sum(r["salary_lpa"] for r in rows) / len(rows) if rows else 0.0
    return {"n_jobs": len(rows), "avg_salary_lpa": round(avg, 2), "top_skills": counts.most_common(top_n)}

if __name__ == "__main__":                       # only runs when executed directly, not on import
    rows = load(sys.argv[1])
    if "--city" in sys.argv:
        city = sys.argv[sys.argv.index("--city") + 1]
        rows = [r for r in rows if r["city"].lower() == city.lower()]
    print(json.dumps(report(rows), indent=2))
