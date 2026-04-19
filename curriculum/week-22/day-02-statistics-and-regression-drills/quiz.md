# Week 22 Day 02 Quiz: Statistics and regression drills

## Instructions
- Attempt closed-book first.
- After answering, compare with the answer key and write one correction note.
- Treat each question as a short trading interview prompt.
- For each item, complete the Python drill using real data and interpret the output.
- Target score: at least 4/5 confidence on every item before moving on.

## Trading Interview Questions, Answers, and Python Drills
### Q1 (basic)
Interview question: Explain statistics and regression drills in plain language for a trading or risk audience.

Model answer: A strong answer defines statistics and regression drills, gives one concrete workflow or market-facing decision example, and states one practical limitation that must be monitored.
Why this matters: This tests communication quality, not just memorized definitions.

### Q2 (intermediate)
Interview question: Write the Expected Value formula/workflow from memory and define each symbol.

Model answer: A strong answer includes Expected Value exactly, explains each symbol, and states one caveat: Ignoring payoff asymmetry.
Why this matters: This checks mathematical fluency and operational reliability.

Python drill: Run a short timed drill set and compute accuracy by topic category.
Suggested Python solution:
```python
import pandas as pd

drills = pd.DataFrame(
    {
        "topic": ["probability", "stats", "python", "sql", "markets"],
        "correct": [1, 0, 1, 1, 0],
        "minutes": [6, 8, 7, 5, 9],
    }
)
print(drills)
print("Accuracy:", round(float(drills["correct"].mean()), 3))
print("Mean minutes:", round(float(drills["minutes"].mean()), 2))

```

### Q3 (intermediate)
Interview question: Give one realistic use case and one failure mode if this concept is misapplied.

Model answer: A strong answer uses one decision workflow such as: Fast interview math checks.. Then it states one realistic failure mode: Ignoring payoff asymmetry., and one detection check.
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
