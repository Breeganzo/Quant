# Week 19 Day 06 Quiz: Mini lab: AI-assisted research memo

## Instructions
- Attempt closed-book first.
- After answering, compare with the answer key and write one correction note.
- Treat each question as a short trading interview prompt.
- For each item, complete the Python drill using real data and interpret the output.
- Use a structured answer style: direct answer, evidence, caveat, and follow-up check.
- Target score: at least 4/5 confidence on every item before moving on.

## Trading Interview Questions, Answers, and Python Drills
### Q1 (basic)
Interview question: Explain mini lab: ai-assisted research memo in plain language for a trading or risk audience.

Model answer: A strong answer defines mini lab: ai-assisted research memo, gives one concrete workflow or market-facing decision example, and states one practical limitation that must be monitored.
How to answer in a live interview: Definition -> practical use case -> limitation/risk check.
Why this matters: This tests communication quality, not just memorized definitions.

### Q2 (intermediate)
Interview question: Write the Precision formula/workflow from memory and define each symbol.

Model answer: A strong answer includes Precision exactly, explains each symbol, and states one caveat: High precision with very low coverage.
How to answer in a live interview: State formula -> define symbols -> add caveat and context.
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
Interview question: Give one realistic use case, one implementation choice, and one failure mode if this concept is misapplied.

Model answer: A strong answer uses one decision workflow such as: Quality control of extracted insights.. Then it states one realistic failure mode: High precision with very low coverage., one detection check, and one mitigation action.
How to answer in a live interview: Use case -> implementation choice -> failure mode -> mitigation.
Why this matters: This evaluates transfer from theory to practical quant workflow.

### Q4 (advanced)
Interview question: How would you validate data quality and implementation assumptions before trusting conclusions in production?

Model answer: Check schema consistency, missing values, temporal alignment, leakage risks, and sensitivity to stress windows. Then compare one metric across alternate assumptions or data sources, and set a threshold that triggers a review.
How to answer in a live interview: Validation checklist -> stress check -> escalation threshold.
Why this matters: This tests robustness discipline and implementation realism.

### Q5 (advanced)
Interview question: A PM asks for a decision in 30 seconds. What metric would you lead with and what caveat would you immediately include?

Model answer: Lead with one actionable metric tied to objective (for example risk-adjusted return, hit rate under costs, or drawdown stability), then immediately state one caveat on sample dependence, costs, regime shift, or data quality.
How to answer in a live interview: Primary metric -> direct recommendation -> caveat.
Why this matters: This tests concise decision communication under time pressure.

### Q6 (advanced)
Interview question: What is one follow-up experiment you would run tomorrow to reduce uncertainty in today's conclusion?

Model answer: Propose one focused experiment (alternate window, benchmark, transaction-cost assumption, or feature variation), state expected impact, and define what result would change your recommendation.
How to answer in a live interview: Experiment design -> expected effect -> decision boundary.
Why this matters: This tests scientific thinking and iterative research discipline.

### Q7 (advanced)
Interview question: From your error log, pick one repeated mistake and describe the correction protocol for next week.

Model answer: State the exact misconception, corrected rule, retrieval prompt, and next review schedule (1d/3d/7d/14d).
How to answer in a live interview: Mistake -> correction rule -> retrieval plan -> review cadence.
Why this matters: Saturday should convert weak spots into an explicit revision mechanism.

## Reflection
- Which item was weakest and why?
- What would you improve before saying this answer in a live interview?
- What will you review before tomorrow?
- What evidence shows your answer quality improved versus last week?
- If a PM challenged your conclusion, what single additional test would you run first?
