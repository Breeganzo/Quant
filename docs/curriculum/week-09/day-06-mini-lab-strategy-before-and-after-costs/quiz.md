# Week 09 Day 06 Quiz: Mini lab: strategy before and after costs

## Instructions
- Attempt closed-book first.
- After answering, compare with the answer key and write one correction note.
- Treat each question as a short trading interview prompt.
- For each item, complete the Python drill using real data and interpret the output.
- Target score: at least 4/5 confidence on every item before moving on.

## Trading Interview Questions, Answers, and Python Drills
### Q1 (basic)
Interview question: Explain mini lab: strategy before and after costs in plain language for a trading or risk audience.

Model answer: A strong answer defines mini lab: strategy before and after costs, gives one concrete workflow or market-facing decision example, and states one practical limitation that must be monitored.
Why this matters: This tests communication quality, not just memorized definitions.

### Q2 (intermediate)
Interview question: Write the Mid Price formula/workflow from memory and define each symbol.

Model answer: A strong answer includes Mid Price exactly, explains each symbol, and states one caveat: Comparing fills to stale mid prices.
Why this matters: This checks mathematical fluency and operational reliability.

Python drill: Estimate turnover and a simple cost proxy from a toy rebalance schedule.
Suggested Python solution:
```python
import pandas as pd

weights = pd.DataFrame(
    {
        "SPY": [0.40, 0.35, 0.30],
        "QQQ": [0.30, 0.35, 0.35],
        "TLT": [0.20, 0.20, 0.25],
        "GLD": [0.10, 0.10, 0.10],
    },
    index=["t0", "t1", "t2"],
)
turnover = 0.5 * weights.diff().abs().sum(axis=1).fillna(0.0)
cost_bps = 8
est_cost = turnover * (cost_bps / 10000)
print(pd.DataFrame({"turnover": turnover, "estimated_cost": est_cost}))

```

### Q3 (intermediate)
Interview question: Give one realistic use case and one failure mode if this concept is misapplied.

Model answer: A strong answer ties the concept to one production decision, defines a measurable success metric, and names one concrete failure mode plus detection check.
Why this matters: This evaluates transfer from theory to practical quant workflow.

### Q4 (advanced)
Interview question: How would you validate data quality and implementation assumptions before trusting conclusions?

Model answer: Check schema consistency, missing values, temporal alignment, leakage risks, and sensitivity to stress windows. Then compare one metric across alternate assumptions or data sources.
Why this matters: This tests robustness discipline and implementation realism.

### Q5 (advanced)
Interview question: From your error log, pick one repeated mistake and describe the correction protocol for next week.

Model answer: State the exact misconception, corrected rule, retrieval prompt, and next review schedule (1d/3d/7d/14d).
Why this matters: Saturday should convert weak spots into an explicit revision mechanism.

## Reflection
- Which item was weakest and why?
- What would you improve before saying this answer in a live interview?
- What will you review before tomorrow?
- What evidence shows your answer quality improved versus last week?
