# Day 02 · Python that senior engineers write

**Phase 1 · Python for AI (pre-requisite) · 60 minutes**

The six constructs that separate a script from a library, each tied to where it appears in AI code:
classes with dunder methods (= a PyTorch `Dataset`), generators (= streaming data bigger than RAM),
decorators (`@timer`, `@retry`, `@lru_cache`), context managers, dataclasses and type hints.

## Learning outcomes
By the end of the hour students can:
1. Write a class with `__init__`, `__len__`, `__getitem__`, `__repr__`, `__call__` and explain that PyTorch's `DataLoader` only ever calls `len()` and `[i]`.
2. Explain inheritance vs composition and why `super().__init__()` must come first.
3. Write a generator and a three-stage generator pipeline that processes a file in constant memory; explain single-use exhaustion.
4. Write `@timer`, a parameterised `@retry(times, delay)` and use `@functools.lru_cache`; explain `*args/**kwargs` and `functools.wraps`.
5. Write a context manager both as a class and with `@contextmanager`; use `@dataclass` (with `field(default_factory=...)`) and modern type hints for a config object.

## 60-minute plan
| Min | Section (HTML id) | What happens |
|---|---|---|
| 00–05 | Hook (`#hook`) | Open the PyTorch custom-Dataset tutorial; "the 50 GB file" story (readlines vs `for row in f`); three real source files. |
| 05–23 | Concept (`#concept`) | Classes + dunder grid (IRCTC coach analogy) with the interactive Dataset/DataLoader visual (index, batch_size, shuffle). Generators (thali vs dosa counter) with the `next(g)` step-through and list-vs-generator memory bars. Decorators (Swiggy packaging) with the animated onion + call log. lru_cache speed chart. |
| 23–33 | Deeper (`#deeper`) | Inheritance/super; decorator without sugar (`*args/**kwargs`, `wraps`); context-manager protocol; dataclass/type-hint/functools/collections table; interview phrasing. |
| 33–46 | Code (`#code`) | Snippets: ReviewDataset, streaming pipeline, three decorators (tabs), `timed()` + `TrainConfig`. Switch to the notebook for live runs. |
| 46–51 | Real world & tools (`#realworld`) | PyTorch data tutorial, HF streaming datasets, tenacity, Pydantic, mypy cheat sheet, Real Python decorators; tools: Pyright, Ruff, W&B, Claude/ChatGPT, Copilot, Python Tutor. |
| 51–54 | Career corner (`#career`) | Role titles; 3 interview Qs (generators, decorators + wraps, str vs repr); action: commit `ml_utils.py`. |
| 54–57 | Quiz (`#quiz`) | 3 questions (generator exhaustion, Dataset methods, decorator sugar). |
| 57–59 | Homework (`#homework`) | Easy `@log_calls` / Medium `JobDataset` / Stretch constant-memory streaming. |
| 59–60 | Next (`#next`) | Day 03 teaser + checklist. |

## Prerequisites
- Day 01 (containers, functions, comprehensions, `with open`, `try/except`). The Medium homework reuses Day 01's `jobs.csv` (the notebook generates a stand-in if missing).

## Files in this folder
- `Day_02_Python_Advanced.html` — lesson page with three interactive visuals (Dataset/DataLoader, generator step-through, decorator onion) and one Chart.js chart.
- `Day_02_Python_Advanced.ipynb` — Colab notebook, 38 cells, CPU, runs top-to-bottom in about 10 seconds. Writes `upi.csv` (2.8 MB) and streams it back.
- `README.md` — this plan.

## Links used
- https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html · https://github.com/pytorch/pytorch/blob/main/torch/utils/data/dataset.py
- https://github.com/huggingface/transformers/blob/main/src/transformers/training_args.py · https://github.com/scikit-learn/scikit-learn/blob/main/sklearn/base.py
- https://huggingface.co/docs/datasets/stream · https://github.com/jd/tenacity · https://docs.pydantic.dev/latest/ · https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html · https://realpython.com/primer-on-python-decorators/
- Tools: https://github.com/microsoft/pyright · https://docs.astral.sh/ruff/ · https://wandb.ai/site · https://claude.ai/ · https://github.com/features/copilot · https://pythontutor.com/python-compiler.html

## Homework summary
- **Easy (10 min):** `@log_calls` decorator that prints name, args, kwargs and return value; generic via `*args/**kwargs` + `functools.wraps`.
- **Medium (15 min, job hunt):** `@dataclass Job` + `JobDataset` (`__len__`, `__getitem__`, `filter(city=...)` returning a new dataset, generator method `skills()` fed to `Counter`).
- **Stretch (15 min):** generate a 200 MB CSV with a generator and compute mean/max with a generator pipeline; verify constant memory with `tracemalloc`; wrap in `with timed(...)`.

## If you're running late, skip:
- The `__call__` Tokenizer example (mention "model(x) is `__call__`" in one sentence).
- The `functools.partial` / `collections` cell (point to the table in the Deeper section).
- The retry-with-failure animation; show the cache HIT path only.
