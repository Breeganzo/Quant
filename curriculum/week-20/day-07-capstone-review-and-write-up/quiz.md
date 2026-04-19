# Week 20 Day 07 Quiz: Capstone review and write-up

## Instructions
- Attempt closed-book first.
- After answering, compare with the answer key and write one correction note.
- Treat each question as a short trading interview prompt.
- For each item, complete the Python drill using real data and interpret the output.
- Target score: at least 4/5 confidence on every item before moving on.

## Trading Interview Questions, Answers, and Python Drills
### Q1 (basic)
Interview question: Explain capstone review and write-up in plain language for a trading or risk audience.

Model answer: A strong answer defines capstone review and write-up, gives one concrete workflow or market-facing decision example, and states one practical limitation that must be monitored.
Why this matters: This tests communication quality, not just memorized definitions.

### Q2 (intermediate)
Interview question: Write the Precision formula/workflow from memory and define each symbol.

Model answer: A strong answer includes Precision exactly, explains each symbol, and states one caveat: High precision with very low coverage.
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

Model answer: A strong answer ties the concept to one production decision, defines a measurable success metric, and names one concrete failure mode plus detection check.
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
