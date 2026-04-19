# Week 04 Day 05 Quiz: Portfolio theory, efficient frontier, and Sharpe ratio intuition

## Instructions
- Attempt closed-book first.
- After answering, compare with the answer key and write one correction note.
- Treat each question as a short trading interview prompt.
- For each item, complete the Python drill using real data and interpret the output.
- Target score: at least 4/5 confidence on every item before moving on.

## Trading Interview Questions, Answers, and Python Drills
### Q1 (basic)
Interview question: Explain portfolio theory, efficient frontier, and sharpe ratio intuition in plain language for a trading or risk audience.

Model answer: A strong answer defines portfolio theory, efficient frontier, and sharpe ratio intuition, gives one concrete workflow or market-facing decision example, and states one practical limitation that must be monitored.
Why this matters: This tests communication quality, not just memorized definitions.

### Q2 (intermediate)
Interview question: Write the Expected Value formula/workflow from memory and define each symbol.

Model answer: A strong answer includes Expected Value exactly, explains each symbol, and states one caveat: Ignoring tail risk while focusing only on mean payoff.
Why this matters: This checks mathematical fluency and operational reliability.

Python drill: Load market data and compute a correlation/covariance diagnostic tied to today's topic.
Suggested Python solution:
```python
from pathlib import Path
import pandas as pd

market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
prices = market.pivot(index="date", columns="symbol", values="close").dropna()
returns = prices.pct_change().dropna()
print(returns.corr().round(3))
print("\nCovariance:")
print(returns.cov().round(6))

```

### Q3 (intermediate)
Interview question: Give one realistic use case and one failure mode if this concept is misapplied.

Model answer: A strong answer ties the concept to one production decision, defines a measurable success metric, and names one concrete failure mode plus detection check.
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
