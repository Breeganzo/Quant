# Week 12 Day 04 Quiz: Volatility smile and pricing inputs

## Instructions
- Attempt closed-book first.
- After answering, compare with the answer key and write one correction note.
- Treat each question as a short trading interview prompt.
- For each item, complete the Python drill using real data and interpret the output.
- Target score: at least 4/5 confidence on every item before moving on.

## Trading Interview Questions, Answers, and Python Drills
### Q1 (basic)
Interview question: Explain volatility smile and pricing inputs in plain language for a trading or risk audience.

Model answer: A strong answer defines volatility smile and pricing inputs, gives one concrete workflow or market-facing decision example, and states one practical limitation that must be monitored.
Why this matters: This tests communication quality, not just memorized definitions.

### Q2 (intermediate)
Interview question: Write the Call Payoff formula/workflow from memory and define each symbol.

Model answer: A strong answer includes Call Payoff exactly, explains each symbol, and states one caveat: Confusing payoff with profit (ignoring premium).
Why this matters: This checks mathematical fluency and operational reliability.

Python drill: Build option payoff vectors and estimate delta numerically at one point.
Suggested Python solution:
```python
import numpy as np

k = 100
s_grid = np.linspace(70, 130, 13)
call = np.maximum(s_grid - k, 0)
put = np.maximum(k - s_grid, 0)
s0 = 101
eps = 0.5
call_price = lambda s: max(s - k, 0)
delta = (call_price(s0 + eps) - call_price(s0 - eps)) / (2 * eps)
print("Call payoff:", call)
print("Put payoff:", put)
print("Delta estimate near S=101:", round(float(delta), 4))

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
