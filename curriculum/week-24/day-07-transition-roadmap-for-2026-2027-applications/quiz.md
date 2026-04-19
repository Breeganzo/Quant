# Week 24 Day 07 Quiz: Transition roadmap for 2026-2027 applications

## Instructions
- Attempt closed-book first.
- After answering, compare with the answer key and write one correction note.
- Treat each question as a short trading interview prompt.
- For each item, complete the Python drill using real data and interpret the output.
- Target score: at least 4/5 confidence on every item before moving on.

## Trading Interview Questions, Answers, and Python Drills
### Q1 (basic)
Interview question: Explain transition roadmap for 2026-2027 applications in plain language for a trading or risk audience.

Model answer: A strong answer defines transition roadmap for 2026-2027 applications, gives one concrete workflow or market-facing decision example, and states one practical limitation that must be monitored.
Why this matters: This tests communication quality, not just memorized definitions.

### Q2 (intermediate)
Interview question: Write the Net Return formula/workflow from memory and define each symbol.

Model answer: A strong answer includes Net Return exactly, explains each symbol, and states one caveat: Presenting gross-only metrics.
Why this matters: This checks mathematical fluency and operational reliability.

Python drill: Train a simple out-of-sample baseline and report RMSE with one risk caveat.
Suggested Python solution:
```python
from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
prices = market.pivot(index="date", columns="symbol", values="close").dropna()
ret = prices.pct_change().dropna()
X = ret.shift(1).dropna()
y = ret["SPY"].loc[X.index]
split = int(len(X) * 0.7)
model = LinearRegression()
model.fit(X.iloc[:split], y.iloc[:split])
pred = model.predict(X.iloc[split:])
rmse = mean_squared_error(y.iloc[split:], pred) ** 0.5
print("Out-of-sample RMSE:", round(float(rmse), 6))

```

### Q3 (intermediate)
Interview question: Give one realistic use case and one failure mode if this concept is misapplied.

Model answer: A strong answer uses one decision workflow such as: Final report realism.. Then it states one realistic failure mode: Presenting gross-only metrics., and one detection check.
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
