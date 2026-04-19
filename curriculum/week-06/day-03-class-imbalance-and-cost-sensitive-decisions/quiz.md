# Week 06 Day 03 Quiz: Class imbalance and cost-sensitive decisions

## Instructions
- Attempt closed-book first.
- After answering, compare with the answer key and write one correction note.
- Treat each question as a short trading interview prompt.
- For each item, complete the Python drill using real data and interpret the output.
- Target score: at least 4/5 confidence on every item before moving on.

## Trading Interview Questions, Answers, and Python Drills
### Q1 (basic)
Interview question: Explain class imbalance and cost-sensitive decisions in plain language for a trading or risk audience.

Model answer: A strong answer defines class imbalance and cost-sensitive decisions, gives one concrete workflow or market-facing decision example, and states one practical limitation that must be monitored.
Why this matters: This tests communication quality, not just memorized definitions.

### Q2 (intermediate)
Interview question: Write the Logistic Link formula/workflow from memory and define each symbol.

Model answer: A strong answer includes Logistic Link exactly, explains each symbol, and states one caveat: Treating probability as certainty near threshold.
Why this matters: This checks mathematical fluency and operational reliability.

Python drill: Train a simple classification baseline and report precision/recall/F1.
Suggested Python solution:
```python
from pathlib import Path
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
prices = market.pivot(index="date", columns="symbol", values="close").dropna()
returns = prices.pct_change().dropna()
X = returns.shift(1).dropna()
y = (returns["SPY"].loc[X.index] > 0).astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=False)
model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)
pred = model.predict(X_test)
print(classification_report(y_test, pred, digits=3))

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
