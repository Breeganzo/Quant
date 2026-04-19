# Week 08 Day 02 Quiz: Stationarity, trends, seasonality, and differencing

## Instructions
- Attempt closed-book first.
- After answering, compare with the answer key and write one correction note.
- Treat each question as a short trading interview prompt.
- For each item, complete the Python drill using real data and interpret the output.
- Target score: at least 4/5 confidence on every item before moving on.

## Trading Interview Questions, Answers, and Python Drills
### Q1 (basic)
Interview question: Explain stationarity, trends, seasonality, and differencing in plain language for a trading or risk audience.

Model answer: A strong answer defines stationarity, trends, seasonality, and differencing, gives one concrete workflow or market-facing decision example, and states one practical limitation that must be monitored.
Why this matters: This tests communication quality, not just memorized definitions.

### Q2 (intermediate)
Interview question: Write the First Difference formula/workflow from memory and define each symbol.

Model answer: A strong answer includes First Difference exactly, explains each symbol, and states one caveat: Over-differencing useful signal away.
Why this matters: This checks mathematical fluency and operational reliability.

Python drill: Build a lag-based forecast baseline and compute RMSE on the last 30 observations.
Suggested Python solution:
```python
from pathlib import Path
import numpy as np
import pandas as pd

market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
spy = market[market["symbol"] == "SPY"].sort_values("date").set_index("date")["close"]
r = spy.pct_change().dropna()
lag1 = r.shift(1).dropna()
y = r.loc[lag1.index]
split = max(30, int(len(y) * 0.8))
pred = lag1.iloc[split:]
truth = y.iloc[split:]
rmse = float(np.sqrt(((pred - truth) ** 2).mean()))
print({"rmse": round(rmse, 6), "test_points": len(truth)})

```

### Q3 (intermediate)
Interview question: Give one realistic use case and one failure mode if this concept is misapplied.

Model answer: A strong answer uses one decision workflow such as: Stabilize mean for modeling.. Then it states one realistic failure mode: Over-differencing useful signal away., and one detection check.
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
