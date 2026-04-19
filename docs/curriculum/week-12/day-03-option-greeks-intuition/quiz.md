# Week 12 Day 03 Quiz: Option Greeks intuition

## Instructions
- Attempt closed-book first.
- After answering, compare with the answer key and write one correction note.
- Treat each question as a short trading interview prompt.
- For each item, complete the Python drill using real data and interpret the output.
- Target score: at least 4/5 confidence on every item before moving on.

## Trading Interview Questions, Answers, and Python Drills
### Q1 (basic)
Interview question: Explain option greeks intuition in plain language for a trading or risk audience.

Model answer: A strong answer defines option greeks intuition, gives one concrete workflow or market-facing decision example, and states one practical limitation that must be monitored.
Why this matters: This tests communication quality, not just memorized definitions.

### Q2 (intermediate)
Interview question: Write the Delta formula/workflow from memory and define each symbol.

Model answer: A strong answer includes Delta exactly, explains each symbol, and states one caveat: Treating delta as constant.
Why this matters: This checks mathematical fluency and operational reliability.

Python drill: Build option payoff vectors and approximate delta around the strike.
Suggested Python solution:
```python
import numpy as np

k = 100
s = np.linspace(70, 130, 13)
call = np.maximum(s - k, 0)
put = np.maximum(k - s, 0)
eps = 1.0
s0 = 100
delta = (max(s0 + eps - k, 0) - max(s0 - eps - k, 0)) / (2 * eps)
print("call:", call)
print("put:", put)
print("delta near strike:", round(float(delta), 4))

```

### Q3 (intermediate)
Interview question: Give one realistic use case and one failure mode if this concept is misapplied.

Model answer: A strong answer uses one decision workflow such as: Hedge-ratio baseline.. Then it states one realistic failure mode: Treating delta as constant., and one detection check.
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
