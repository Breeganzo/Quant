# Week 04 Day 02 Quiz: Confidence intervals and hypothesis testing intuition

## Instructions
- Attempt closed-book first.
- After answering, compare with the answer key and write one correction note.
- Treat each question as a short trading interview prompt.
- For each item, complete the Python drill using real data and interpret the output.
- Target score: at least 4/5 confidence on every item before moving on.

## Trading Interview Questions, Answers, and Python Drills
### Q1 (basic)
Interview question: Explain confidence intervals and hypothesis testing intuition in plain language for a trading or risk audience.

Model answer: A strong answer defines confidence intervals and hypothesis testing intuition, gives one concrete workflow or market-facing decision example, and states one practical limitation that must be monitored.
Why this matters: This tests communication quality, not just memorized definitions.

### Q2 (intermediate)
Interview question: Write the Confidence Interval (Mean) formula/workflow from memory and define each symbol.

Model answer: A strong answer includes Confidence Interval (Mean) exactly, explains each symbol, and states one caveat: Treating interval as probability for fixed parameter.
Why this matters: This checks mathematical fluency and operational reliability.

Python drill: Compute a 95% confidence interval for SPY daily returns and report the t-statistic vs zero.
Suggested Python solution:
```python
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats

market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
spy = market[market["symbol"] == "SPY"].sort_values("date")["close"].pct_change().dropna()
n = len(spy)
mean = float(spy.mean())
std = float(spy.std(ddof=1))
se = std / np.sqrt(n)
t_crit = stats.t.ppf(0.975, n - 1)
ci = (mean - t_crit * se, mean + t_crit * se)
t_stat = mean / se
print({"mean": round(mean, 6), "ci_95": tuple(round(x, 6) for x in ci), "t_stat": round(float(t_stat), 4)})

```

### Q3 (intermediate)
Interview question: Give one realistic use case and one failure mode if this concept is misapplied.

Model answer: A strong answer uses one decision workflow such as: Uncertainty-aware return estimates.. Then it states one realistic failure mode: Treating interval as probability for fixed parameter., and one detection check.
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
