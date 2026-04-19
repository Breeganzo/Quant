# Week 17 Mon: Decision trees and rule-based splits

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "ML for Quant I: trees, ensembles, nonlinear interactions, and model interpretation". Your objective is to understand, apply, and communicate decision trees and rule-based splits in a way a quant team would trust.

## Continuity Map
- Week kickoff: establish baseline intuition and key definitions before moving into formal detail.
- Today's focus: Decision trees and rule-based splits
- Next day bridge: Random forests and bagging intuition

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
Decision trees and rule-based splits is part of real quant work inside ml for quant i: trees, ensembles, nonlinear interactions, and model interpretation research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Class-mix impurity at node.
2. Technical frame: Build decision trees and rule-based splits from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: Gini Impurity, Information Gain, Tree Depth).
3. Market interpretation: Split quality scoring.. Run one compact, reproducible example for decision trees and rule-based splits and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Overfitting deep trees without pruning.

## Practice Problems
- Explain decision trees and rule-based splits in one paragraph without jargon.
- Write down one topic-specific formula or workflow for decision trees and rule-based splits from memory.
- Connect decision trees and rule-based splits to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind decision trees and rule-based splits?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Gini Impurity
$$G=1-\sum_k p_k^2$$
Plain-English interpretation: Class-mix impurity at node.
Interview pitfall: Overfitting deep trees without pruning.

### Formula 2: Information Gain
$$IG=H(parent)-\sum_j\frac{n_j}{n}H(child_j)$$
Plain-English interpretation: Entropy reduction from split.
Interview pitfall: Bias toward high-cardinality features.

### Formula 3: Tree Depth
$$Depth=\max(path\ length)$$
Plain-English interpretation: Model complexity measure.
Interview pitfall: Letting depth grow without validation.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Gini Impurity | Class-mix impurity at node. | Split quality scoring. | Overfitting deep trees without pruning. |
| Information Gain | Entropy reduction from split. | Feature split selection. | Bias toward high-cardinality features. |
| Tree Depth | Model complexity measure. | Control variance and interpretability. | Letting depth grow without validation. |

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
- Design one topic-specific analysis for decision trees and rule-based splits instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Train a baseline classifier/regressor for decision trees and rule-based splits on market-derived features and report one robust metric beyond accuracy.

## Interview Drill
- Q1: Explain decision trees and rule-based splits to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from decision trees and rule-based splits is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
