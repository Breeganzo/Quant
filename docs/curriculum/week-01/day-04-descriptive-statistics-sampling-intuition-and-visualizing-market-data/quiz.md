# Week 01 Day 04 Quiz: Descriptive statistics, sampling intuition, and visualizing market data

## Instructions
- Attempt closed-book first.
- After answering, compare with the answer key and write one correction note.
- Treat each question as a short trading interview prompt.
- For each item, complete the Python drill using real data and interpret the output.
- Target score: at least 4/5 confidence on every item before moving on.

## Trading Interview Questions, Answers, and Python Drills
### Q1 (basic)
Interview question: Explain descriptive statistics, sampling intuition, and visualizing market data in plain language for a trading or risk audience.

Model answer: A strong answer defines descriptive statistics, sampling intuition, and visualizing market data, gives one concrete workflow or market-facing decision example, and states one practical limitation that must be monitored.
Why this matters: This tests communication quality, not just memorized definitions.

### Q2 (intermediate)
Interview question: Write the Sample Mean formula/workflow from memory and define each symbol.

Model answer: A strong answer includes Sample Mean exactly, explains each symbol, and states one caveat: Assuming mean is robust to outliers.
Why this matters: This checks mathematical fluency and operational reliability.

Python drill: Compute log returns and summarize annualized return/risk with one caveat.
Suggested Python solution:
```python
from pathlib import Path
import pandas as pd

market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
prices = market.pivot(index="date", columns="symbol", values="close").dropna()
ret = prices.pct_change().dropna()
ann_ret = ret.mean() * 252
ann_vol = ret.std() * (252 ** 0.5)
print(pd.DataFrame({"ann_return": ann_ret, "ann_vol": ann_vol}).round(4))

```

### Q3 (intermediate)
Interview question: Give one realistic use case and one failure mode if this concept is misapplied.

Model answer: A strong answer uses one decision workflow such as: Return-level baseline estimate.. Then it states one realistic failure mode: Assuming mean is robust to outliers., and one detection check.
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
