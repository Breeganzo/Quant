# Week 21 Day 06 Quiz: Mini lab: draft your application story

## Instructions
- Attempt closed-book first.
- After answering, compare with the answer key and write one correction note.
- Treat each question as a short trading interview prompt.
- For each item, complete the Python drill using real data and interpret the output.
- Target score: at least 4/5 confidence on every item before moving on.

## Trading Interview Questions, Answers, and Python Drills
### Q1 (basic)
Interview question: Explain mini lab: draft your application story in plain language for a trading or risk audience.

Model answer: A strong answer defines mini lab: draft your application story, gives one concrete workflow or market-facing decision example, and states one practical limitation that must be monitored.
Why this matters: This tests communication quality, not just memorized definitions.

### Q2 (intermediate)
Interview question: Write the Program Fit Score formula/workflow from memory and define each symbol.

Model answer: A strong answer includes Program Fit Score exactly, explains each symbol, and states one caveat: Ignoring downside constraints like debt burden.
Why this matters: This checks mathematical fluency and operational reliability.

Python drill: Build a program-fit and cost matrix and rank options by weighted score.
Suggested Python solution:
```python
import pandas as pd

options = pd.DataFrame(
    {
        "program": ["A", "B", "C"],
        "curriculum_fit": [0.9, 0.8, 0.7],
        "career_fit": [0.8, 0.9, 0.7],
        "cost_score": [0.6, 0.4, 0.9],
    }
)
w = {"curriculum_fit": 0.45, "career_fit": 0.35, "cost_score": 0.20}
options["fit_score"] = (
    options["curriculum_fit"] * w["curriculum_fit"]
    + options["career_fit"] * w["career_fit"]
    + options["cost_score"] * w["cost_score"]
)
print(options.sort_values("fit_score", ascending=False))

```

### Q3 (intermediate)
Interview question: Give one realistic use case and one failure mode if this concept is misapplied.

Model answer: A strong answer uses one decision workflow such as: Prioritize application targets.. Then it states one realistic failure mode: Ignoring downside constraints like debt burden., and one detection check.
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
