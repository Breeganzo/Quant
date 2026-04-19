# Week 08 Day 06 Quiz: Capstone build day

## Instructions
- Attempt closed-book first.
- After answering, compare with the answer key and write one correction note.
- Treat each question as a short trading interview prompt.
- For each item, complete the Python drill using real data and interpret the output.
- Target score: at least 4/5 confidence on every item before moving on.

## Trading Interview Questions, Answers, and Python Drills
### Q1 (basic)
Interview question: Explain capstone build day in plain language for a trading or risk audience.

Model answer: A strong answer defines capstone build day, gives one concrete workflow or market-facing decision example, and states one practical limitation that must be monitored.
Why this matters: This tests communication quality, not just memorized definitions.

### Q2 (intermediate)
Interview question: Write the AR(1) formula/workflow from memory and define each symbol.

Model answer: A strong answer includes AR(1) exactly, explains each symbol, and states one caveat: Ignoring non-stationarity before fitting AR models.
Why this matters: This checks mathematical fluency and operational reliability.

Python drill: Compute lag autocorrelation and rolling mean/volatility diagnostics.
Suggested Python solution:
```python
from pathlib import Path
import pandas as pd

market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
spy = market[market["symbol"] == "SPY"].sort_values("date").set_index("date")["close"]
ret = spy.pct_change().dropna()
diag = pd.DataFrame(
    {
        "ret": ret,
        "lag1": ret.shift(1),
        "roll_mean_20": ret.rolling(20).mean(),
        "roll_vol_20": ret.rolling(20).std(),
    }
).dropna()
print("Lag-1 autocorr:", round(diag["ret"].corr(diag["lag1"]), 4))
print(diag.tail())

```

### Q3 (intermediate)
Interview question: Give one realistic use case and one failure mode if this concept is misapplied.

Model answer: A strong answer ties the concept to one production decision, defines a measurable success metric, and names one concrete failure mode plus detection check.
Why this matters: This evaluates transfer from theory to practical quant workflow.

### Q4 (advanced)
Interview question: How would you validate data quality and implementation assumptions before trusting conclusions?

Model answer: Check schema consistency, missing values, temporal alignment, leakage risks, and sensitivity to stress windows. Then compare one metric across alternate assumptions or data sources.
Why this matters: This tests robustness discipline and implementation realism.

### Q5 (advanced)
Interview question: From your error log, pick one repeated mistake and describe the correction protocol for next week.

Model answer: State the exact misconception, corrected rule, retrieval prompt, and next review schedule (1d/3d/7d/14d).
Why this matters: Saturday should convert weak spots into an explicit revision mechanism.

## Reflection
- Which item was weakest and why?
- What would you improve before saying this answer in a live interview?
- What will you review before tomorrow?
- What evidence shows your answer quality improved versus last week?
