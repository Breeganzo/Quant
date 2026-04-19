# Week 06 Tue: Confusion matrix, precision, recall, F1, and ROC-AUC

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "ML Foundations II: classification, metrics, imbalance, validation, and risk use cases". Your objective is to understand, apply, and communicate confusion matrix, precision, recall, f1, and roc-auc in a way a quant team would trust.

## Continuity Map
- Previous day focus: Classification intuition and decision boundaries
- Today's focus: Confusion matrix, precision, recall, F1, and ROC-AUC
- Next day bridge: Class imbalance and cost-sensitive decisions

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 60 min | Theory deep dive: definitions, intuition, and assumptions. |
| Session 2 | 60 min | Formula and workflow lab with topic-specific derivations. |
| Session 3 | 60 min | Worked examples with interpretation and failure-mode checks. |
| Session 4 | 60 min | Notebook implementation and output interpretation. |
| Session 5 | 60 min | Interview-style quiz and closed-book retrieval. |
| Session 6 | 60 min | Revision sprint, error-log update, and summary memo. |

## Why It Matters In Quant
Confusion matrix, precision, recall, F1, and ROC-AUC is part of real quant work inside ml foundations ii: classification, metrics, imbalance, validation, and risk use cases research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Probability mapping from linear score.
2. Technical frame: Build confusion matrix, precision, recall, f1, and roc-auc from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: Logistic Link, Precision, Recall).
3. Market interpretation: Binary event prediction.. Run one compact, reproducible example for confusion matrix, precision, recall, f1, and roc-auc and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Thresholding without business-cost calibration.

## Practice Problems
- Explain confusion matrix, precision, recall, f1, and roc-auc in one paragraph without jargon.
- Write down one topic-specific formula or workflow for confusion matrix, precision, recall, f1, and roc-auc from memory.
- Connect confusion matrix, precision, recall, f1, and roc-auc to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind confusion matrix, precision, recall, f1, and roc-auc?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Logistic Link
$$p(y=1|x)=\frac{1}{1+e^{-z}}$$
Plain-English interpretation: Probability mapping from linear score.
Interview pitfall: Thresholding without business-cost calibration.

### Formula 2: Precision
$$Precision=\frac{TP}{TP+FP}$$
Plain-English interpretation: Correctness among predicted positives.
Interview pitfall: Optimizing precision alone under imbalance.

### Formula 3: Recall
$$Recall=\frac{TP}{TP+FN}$$
Plain-English interpretation: Coverage of true positives.
Interview pitfall: Ignoring precision-recall tradeoff.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Logistic Link | Probability mapping from linear score. | Binary event prediction. | Thresholding without business-cost calibration. |
| Precision | Correctness among predicted positives. | False-alarm control. | Optimizing precision alone under imbalance. |
| Recall | Coverage of true positives. | Miss-risk control. | Ignoring precision-recall tradeoff. |

## Common Mistakes and Fixes
- Mistake: copying formulas without defining each symbol. Fix: annotate each term in plain language.
- Mistake: reporting one number without context. Fix: compare to benchmark or alternate scenario.
- Mistake: reading model output as certainty. Fix: include one failure mode and one robustness check.
- Mistake: skipping assumptions. Fix: list assumptions before interpretation.

## Revision Sprint
- Re-solve one earlier problem from memory before checking notes.
- Review yesterday's weak point and state whether it is fixed.
- Schedule the next spaced repetition date before ending the session.

## Real-World Data Lab
- Use yfinance first for SPY, QQQ, TLT, and GLD when internet is available.
- If available, validate against a Robinhood-style export CSV for consistency checks.
- Fall back to curriculum/datasets/real_market_prices.csv for reproducible runs.
- Design one topic-specific analysis for confusion matrix, precision, recall, f1, and roc-auc instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Train a baseline classifier/regressor for confusion matrix, precision, recall, f1, and roc-auc on market-derived features and report one robust metric beyond accuracy.

## Interview Drill
- Q1: Explain confusion matrix, precision, recall, f1, and roc-auc to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from confusion matrix, precision, recall, f1, and roc-auc is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
