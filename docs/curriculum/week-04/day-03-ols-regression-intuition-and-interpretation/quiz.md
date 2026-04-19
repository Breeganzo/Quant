# Week 04 Day 03 Quiz: OLS regression intuition and interpretation

## Instructions
- Attempt closed-book first.
- After answering, compare with the answer key and write one correction note.
- Treat each question as a short trading interview prompt.
- For each item, complete the Python drill using real data and interpret the output.
- Target score: at least 4/5 confidence on every item before moving on.

## Trading Interview Questions, Answers, and Python Drills
### Q1 (basic)
Interview question: Explain ols regression intuition and interpretation in plain language for a trading or risk audience.

Model answer: A strong answer defines ols regression intuition and interpretation, gives one concrete workflow or market-facing decision example, and states one practical limitation that must be monitored.
Why this matters: This tests communication quality, not just memorized definitions.

### Q2 (intermediate)
Interview question: Write the OLS Coefficients formula/workflow from memory and define each symbol.

Model answer: A strong answer includes OLS Coefficients exactly, explains each symbol, and states one caveat: Unstable estimates under multicollinearity.
Why this matters: This checks mathematical fluency and operational reliability.

Python drill: Fit a linear regression of QQQ returns on lagged SPY returns and report coefficient and R^2.
Suggested Python solution:
```python
from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression

market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
prices = market.pivot(index="date", columns="symbol", values="close").dropna()
returns = prices.pct_change().dropna()
X = returns[["SPY"]].shift(1).dropna()
y = returns.loc[X.index, "QQQ"]
model = LinearRegression().fit(X, y)
print({"beta_spy": round(float(model.coef_[0]), 6), "intercept": round(float(model.intercept_), 6), "r2": round(float(model.score(X, y)), 4)})

```

### Q3 (intermediate)
Interview question: Give one realistic use case and one failure mode if this concept is misapplied.

Model answer: A strong answer uses one decision workflow such as: Baseline factor/feature sensitivity model.. Then it states one realistic failure mode: Unstable estimates under multicollinearity., and one detection check.
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
