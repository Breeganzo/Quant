# Week 11 Day 04 Quiz: Convexity and nonlinear bond behavior

## Instructions
- Attempt closed-book first.
- After answering, compare with the answer key and write one correction note.
- Treat each question as a short trading interview prompt.
- For each item, complete the Python drill using real data and interpret the output.
- Target score: at least 4/5 confidence on every item before moving on.

## Trading Interview Questions, Answers, and Python Drills
### Q1 (basic)
Interview question: Explain convexity and nonlinear bond behavior in plain language for a trading or risk audience.

Model answer: A strong answer defines convexity and nonlinear bond behavior, gives one concrete workflow or market-facing decision example, and states one practical limitation that must be monitored.
Why this matters: This tests communication quality, not just memorized definitions.

### Q2 (intermediate)
Interview question: Write the Convexity formula/workflow from memory and define each symbol.

Model answer: A strong answer includes Convexity exactly, explains each symbol, and states one caveat: Ignoring convexity in volatile rate regimes.
Why this matters: This checks mathematical fluency and operational reliability.

Python drill: Price a simple bond and compute modified duration under a yield assumption.
Suggested Python solution:
```python
import numpy as np

face = 100
coupon = 0.05
y = 0.04
n = 5
cf = np.array([face * coupon] * (n - 1) + [face * (1 + coupon)])
t = np.arange(1, n + 1)
disc = (1 + y) ** t
price = float((cf / disc).sum())
d_mac = float((t * cf / disc).sum() / price)
d_mod = d_mac / (1 + y)
print({"price": round(price, 4), "mod_duration": round(d_mod, 4)})

```

### Q3 (intermediate)
Interview question: Give one realistic use case and one failure mode if this concept is misapplied.

Model answer: A strong answer uses one decision workflow such as: Improve bond shock approximations.. Then it states one realistic failure mode: Ignoring convexity in volatile rate regimes., and one detection check.
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
