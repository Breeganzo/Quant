# Week 15 Day 07 Quiz: Review and critique

## Instructions
- Attempt closed-book first.
- After answering, compare with the answer key and write one correction note.
- Treat each question as a short trading interview prompt.
- For each item, complete the Python drill using real data and interpret the output.
- Target score: at least 4/5 confidence on every item before moving on.

## Trading Interview Questions, Answers, and Python Drills
### Q1 (basic)
Interview question: Explain review and critique in plain language for a trading or risk audience.

Model answer: A strong answer defines review and critique, gives one concrete workflow or market-facing decision example, and states one practical limitation that must be monitored.
Why this matters: This tests communication quality, not just memorized definitions.

### Q2 (intermediate)
Interview question: Write the Momentum Signal formula/workflow from memory and define each symbol.

Model answer: A strong answer includes Momentum Signal exactly, explains each symbol, and states one caveat: Ignoring crash risk in reversals.
Why this matters: This checks mathematical fluency and operational reliability.

Python drill: Construct a simple signal and evaluate one risk-aware performance diagnostic.
Suggested Python solution:
```python
from pathlib import Path
import pandas as pd

market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
prices = market.pivot(index="date", columns="symbol", values="close").dropna()
ret = prices.pct_change().dropna()
signal = ret["SPY"].rolling(20).mean().shift(1).dropna()
aligned = ret.loc[signal.index, "SPY"]
strat = aligned * signal.apply(lambda x: 1 if x > 0 else -1)
ann_ret = strat.mean() * 252
ann_vol = strat.std() * (252 ** 0.5)
print({"ann_return": round(float(ann_ret), 4), "ann_vol": round(float(ann_vol), 4)})

```

### Q3 (intermediate)
Interview question: Give one realistic use case and one failure mode if this concept is misapplied.

Model answer: A strong answer uses one decision workflow such as: Cross-sectional ranking strategies.. Then it states one realistic failure mode: Ignoring crash risk in reversals., and one detection check.
Why this matters: This evaluates transfer from theory to practical quant workflow.

### Q4 (advanced)
Interview question: How would you validate data quality and implementation assumptions before trusting conclusions?

Model answer: Check schema consistency, missing values, temporal alignment, leakage risks, and sensitivity to stress windows. Then compare one metric across alternate assumptions or data sources.
Why this matters: This tests robustness discipline and implementation realism.

### Q5 (advanced)
Interview question: What mini-project decision would you defend from this week and what evidence supports it?

Model answer: Name the decision, show one metric/table/plot supporting it, and mention one limitation plus next-step test.
Why this matters: Sunday focuses on project communication quality, not only calculations.

## Reflection
- Which item was weakest and why?
- What would you improve before saying this answer in a live interview?
- What will you review before tomorrow?
- What evidence shows your answer quality improved versus last week?
