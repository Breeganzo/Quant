# Week 18 Day 05 Quiz: Stress testing and scenario design

## Instructions
- Attempt closed-book first.
- After answering, compare with the answer key and write one correction note.
- Treat each question as a short trading interview prompt.
- For each item, complete the Python drill using real data and interpret the output.
- Target score: at least 4/5 confidence on every item before moving on.

## Trading Interview Questions, Answers, and Python Drills
### Q1 (basic)
Interview question: Explain stress testing and scenario design in plain language for a trading or risk audience.

Model answer: A strong answer defines stress testing and scenario design, gives one concrete workflow or market-facing decision example, and states one practical limitation that must be monitored.
Why this matters: This tests communication quality, not just memorized definitions.

### Q2 (intermediate)
Interview question: Write the Parametric VaR formula/workflow from memory and define each symbol.

Model answer: A strong answer includes Parametric VaR exactly, explains each symbol, and states one caveat: Assuming normal tails in crisis regimes.
Why this matters: This checks mathematical fluency and operational reliability.

Python drill: Compare rolling volatility and EWMA volatility estimates.
Suggested Python solution:
```python
from pathlib import Path
import pandas as pd

market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
spy = market[market["symbol"] == "SPY"].sort_values("date").set_index("date")["close"]
ret = spy.pct_change().dropna()
roll = ret.rolling(20).std()
ewma = ret.pow(2).ewm(alpha=0.06, adjust=False).mean().pow(0.5)
out = pd.DataFrame({"roll20": roll, "ewma": ewma}).dropna()
print(out.tail())

```

### Q3 (intermediate)
Interview question: Give one realistic use case and one failure mode if this concept is misapplied.

Model answer: A strong answer uses one decision workflow such as: Daily risk-limit reporting.. Then it states one realistic failure mode: Assuming normal tails in crisis regimes., and one detection check.
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
