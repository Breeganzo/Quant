# Week 17 Sun: Review and limitations

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "ML for Quant I: trees, ensembles, nonlinear interactions, and model interpretation". Your objective is to understand, apply, and communicate review and limitations in a way a quant team would trust.

## Continuity Map
- Previous day focus: Mini lab: nonlinear tabular finance model
- Today's focus: Review and limitations
- Week closure: consolidate this concept into your weekly project narrative.

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 60 min | Closed-book recall and formula rewrite. |
| Session 2 | 60 min | High-value concept reinforcement with worked examples. |
| Session 3 | 60 min | Notebook review and focused extension task. |
| Session 4 | 60 min | Weekly mini-project or capstone build increment. |
| Session 5 | 60 min | Interview rehearsal and technical defense. |
| Session 6 | 60 min | Reflection, error-log cleanup, and next-step planning. |

## Why It Matters In Quant
Review and limitations is part of real quant work inside ml for quant i: trees, ensembles, nonlinear interactions, and model interpretation research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: describe review and limitations in plain language before touching formulas.
2. Technical frame: Build review and limitations from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment.
3. Market interpretation: Run one compact, reproducible example for review and limitations and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: identify one way this concept is commonly misused in research or trading discussion.

## Practice Problems
- Explain review and limitations in one paragraph without jargon.
- Write down one topic-specific formula or workflow for review and limitations from memory.
- Connect review and limitations to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind review and limitations?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Logistic Link
$$p(y=1\mid x)=\frac{1}{1+e^{-z}},\ z=w^Tx+b$$
Plain-English interpretation: Maps linear score to class probability.
Interview pitfall: Treating probability as certainty near threshold.

### Formula 2: Cross-Entropy Loss
$$L=-\frac{1}{n}\sum_{i=1}^n [y_i\log p_i + (1-y_i)\log(1-p_i)]$$
Plain-English interpretation: Penalizes confident wrong classifications strongly.
Interview pitfall: Evaluating only loss without class-balance diagnostics.

### Formula 3: F1 Score
$$F1=2\cdot\frac{\mathrm{Precision}\cdot\mathrm{Recall}}{\mathrm{Precision}+\mathrm{Recall}}$$
Plain-English interpretation: Balances false-positive and false-negative tradeoff.
Interview pitfall: Using accuracy alone on imbalanced labels.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Logistic Link | Maps linear score to class probability. | Probability of positive next-period return event. | Treating probability as certainty near threshold. |
| Cross-Entropy Loss | Penalizes confident wrong classifications strongly. | Train classification baselines for risk events. | Evaluating only loss without class-balance diagnostics. |
| F1 Score | Balances false-positive and false-negative tradeoff. | Model selection under class imbalance. | Using accuracy alone on imbalanced labels. |

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
- Design one topic-specific analysis for review and limitations instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Train a baseline classifier/regressor for review and limitations on market-derived features and report one robust metric beyond accuracy.

## Interview Drill
- Q1: Explain review and limitations to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from review and limitations is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.

## Sunday Mini-Project Blueprint
1. Load real market data from `curriculum/datasets/real_market_prices.csv`.
2. Define a clear project question and one measurable output metric.
3. Build at least one baseline and one variation, then compare outcomes.
4. Write a short conclusion with one limitation and one next-step improvement.
