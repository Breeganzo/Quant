# Week 17 Day 02 Quiz: Random forests and bagging intuition

## Instructions
- Attempt closed-book first.
- After answering, compare with the answer key and write one correction note.
- Treat each question as a short trading interview prompt.
- For each item, complete the Python drill using real data and interpret the output.
- Target score: at least 4/5 confidence on every item before moving on.

## Trading Interview Questions, Answers, and Python Drills
### Q1 (basic)
Interview question: Explain random forests and bagging intuition in plain language for a trading or risk audience.

Model answer: A strong answer defines random forests and bagging intuition, gives one concrete workflow or market-facing decision example, and states one practical limitation that must be monitored.
Why this matters: This tests communication quality, not just memorized definitions.

### Q2 (intermediate)
Interview question: Write the Bagging Predictor formula/workflow from memory and define each symbol.

Model answer: A strong answer includes Bagging Predictor exactly, explains each symbol, and states one caveat: Assuming bias also vanishes automatically.
Why this matters: This checks mathematical fluency and operational reliability.

Python drill: Train a random forest classifier and report feature importances.
Suggested Python solution:
```python
from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
prices = market.pivot(index="date", columns="symbol", values="close").dropna()
returns = prices.pct_change().dropna()
X = returns.shift(1).dropna()
y = (returns.loc[X.index, "SPY"] > 0).astype(int)
model = RandomForestClassifier(n_estimators=200, random_state=7)
model.fit(X, y)
print(pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False))

```

### Q3 (intermediate)
Interview question: Give one realistic use case and one failure mode if this concept is misapplied.

Model answer: A strong answer uses one decision workflow such as: Variance reduction.. Then it states one realistic failure mode: Assuming bias also vanishes automatically., and one detection check.
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
