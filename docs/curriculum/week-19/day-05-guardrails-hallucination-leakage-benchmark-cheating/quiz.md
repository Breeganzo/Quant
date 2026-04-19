# Week 19 Day 05 Quiz: Guardrails: hallucination, leakage, benchmark cheating

## Instructions
- Attempt closed-book first.
- After answering, compare with the answer key and write one correction note.
- Treat each question as a short trading interview prompt.
- For each item, complete the Python drill using real data and interpret the output.
- Target score: at least 4/5 confidence on every item before moving on.

## Trading Interview Questions, Answers, and Python Drills
### Q1 (basic)
Interview question: Explain guardrails: hallucination, leakage, benchmark cheating in plain language for a trading or risk audience.

Model answer: A strong answer defines guardrails: hallucination, leakage, benchmark cheating, gives one concrete workflow or market-facing decision example, and states one practical limitation that must be monitored.
Why this matters: This tests communication quality, not just memorized definitions.

### Q2 (intermediate)
Interview question: Write the Precision formula/workflow from memory and define each symbol.

Model answer: A strong answer includes Precision exactly, explains each symbol, and states one caveat: High precision with tiny coverage.
Why this matters: This checks mathematical fluency and operational reliability.

Python drill: Score a small AI-generated memo for citation support and hallucination risk.
Suggested Python solution:
```python
import pandas as pd

memo = pd.DataFrame(
    [
        {"claim": "Signal improved Sharpe by 20%", "supported": 1},
        {"claim": "Model generalizes across all regimes", "supported": 0},
        {"claim": "Turnover fell after constraints", "supported": 1},
    ]
)
hallucination_rate = 1 - memo["supported"].mean()
print(memo)
print("Hallucination rate:", round(float(hallucination_rate), 3))

```

### Q3 (intermediate)
Interview question: Give one realistic use case and one failure mode if this concept is misapplied.

Model answer: A strong answer uses one decision workflow such as: Quality control for AI outputs.. Then it states one realistic failure mode: High precision with tiny coverage., and one detection check.
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
