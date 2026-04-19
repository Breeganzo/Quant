# Week 01 Day 03 Quiz: Vectors, matrices, and linear algebra intuition for portfolios and ML

## Instructions
- Attempt closed-book first.
- After answering, compare with the answer key and write one correction note.
- Treat each question as a short trading interview prompt.
- For each item, complete the Python drill using real data and interpret the output.
- Target score: at least 4/5 confidence on every item before moving on.

## Trading Interview Questions, Answers, and Python Drills
### Q1 (basic)
Interview question: Explain vectors, matrices, and linear algebra intuition for portfolios and ml in plain language for a trading or risk audience.

Model answer: A strong answer defines vectors, matrices, and linear algebra intuition for portfolios and ml, gives one concrete workflow or market-facing decision example, and states one practical limitation that must be monitored.
Why this matters: This tests communication quality, not just memorized definitions.

### Q2 (intermediate)
Interview question: Write the Portfolio Return formula/workflow from memory and define each symbol.

Model answer: A strong answer includes Portfolio Return exactly, explains each symbol, and states one caveat: Misaligned weight and return ordering.
Why this matters: This checks mathematical fluency and operational reliability.

Python drill: Compute portfolio return and variance from a return matrix and covariance estimate.
Suggested Python solution:
```python
from pathlib import Path
import numpy as np
import pandas as pd

market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
prices = market.pivot(index="date", columns="symbol", values="close").dropna()
returns = prices.pct_change().dropna()
w = np.array([0.4, 0.3, 0.2, 0.1])
mu = returns.mean().values
cov = returns.cov().values
exp_ret = float(w @ mu)
var = float(w @ cov @ w)
print({"expected_daily_return": round(exp_ret, 6), "daily_variance": round(var, 8)})

```

### Q3 (intermediate)
Interview question: Give one realistic use case and one failure mode if this concept is misapplied.

Model answer: A strong answer uses one decision workflow such as: Fast multi-asset return aggregation.. Then it states one realistic failure mode: Misaligned weight and return ordering., and one detection check.
Why this matters: This evaluates transfer from theory to practical quant workflow.

### Q4 (advanced)
Interview question: How would you validate data quality and implementation assumptions before trusting conclusions?

Model answer: Check schema consistency, missing values, temporal alignment, leakage risks, and sensitivity to stress windows. Then compare one metric across alternate assumptions or data sources.
Why this matters: This tests robustness discipline and implementation realism.

## Reflection
- Which item was weakest and why?
- What would you improve before saying this answer in a live interview?
- What will you review before tomorrow?
- What evidence shows your answer quality improved versus last week?
