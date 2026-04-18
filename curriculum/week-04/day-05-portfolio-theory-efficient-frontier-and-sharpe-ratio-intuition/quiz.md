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

Model answer: A strong answer defines portfolio theory, efficient frontier, and sharpe ratio intuition, gives one concrete market example, and states why the concept improves decisions under uncertainty.
Why this matters: This tests communication quality, not just memorized definitions.

Python drill: Compute log returns for SPY and QQQ daily closes and explain one volatile day.
Suggested Python solution:
```python
import numpy as np
import pandas as pd
prices = market.pivot(index='date', columns='symbol', values='close')[['SPY','QQQ']].dropna()
log_ret = np.log(prices / prices.shift(1)).dropna()
print(log_ret.tail())
```

### Q2 (intermediate)
Interview question: Write one key formula/workflow and define every symbol with units.

Model answer: A strong answer includes formula meaning, variable units, and one implementation caveat (for example, annualization assumptions or missing data handling).
Why this matters: This checks mathematical fluency and operational reliability.

Python drill: Estimate annualized volatility for SPY, QQQ, TLT, and GLD.
Suggested Python solution:
```python
returns = prices.pct_change().dropna()
ann_vol = returns.std() * (252 ** 0.5)
print(ann_vol.sort_values(ascending=False).round(4))
```

### Q3 (intermediate)
Interview question: Give one realistic use case and one failure mode if this concept is misapplied.

Model answer: A strong answer ties the concept to signal design, portfolio sizing, or risk control, then names one concrete failure mode and detection check.
Why this matters: This evaluates transfer from theory to practical quant workflow.

Python drill: Compute a simple Sharpe ratio proxy and explain one fragility.
Suggested Python solution:
```python
rf = 0.03
ann_ret = returns.mean() * 252
ann_vol = returns.std() * (252 ** 0.5)
sharpe = (ann_ret - rf) / ann_vol
print(sharpe.round(3))
```

### Q4 (advanced)
Interview question: How would you validate real data from yfinance/Robinhood export/local CSV before trusting conclusions?

Model answer: Check schema consistency, missing values, split/dividend handling, date alignment, and sensitivity to stress windows. Then compare at least one metric across two data sources.
Why this matters: This tests real-data robustness discipline and source reconciliation.

Python drill: Run a source-quality checklist before analysis.
Suggested Python solution:
```python
print('rows:', len(market))
print('missing close:', market['close'].isna().sum())
print('duplicates:', market.duplicated(['date','symbol']).sum())
print('symbols:', sorted(market['symbol'].unique()))
```

## Reflection
- Which item was weakest and why?
- What would you improve before saying this answer in a live interview?
- What will you review before tomorrow?
- What evidence shows your answer quality improved versus last week?
