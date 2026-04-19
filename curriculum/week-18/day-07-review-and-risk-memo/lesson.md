# Week 18 Sun: Review and risk memo

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "ML for Quant II: volatility, EWMA, GARCH intuition, risk forecasting, and stress testing". Your objective is to understand, apply, and communicate review and risk memo in a way a quant team would trust.

## Continuity Map
- Previous day focus: Mini lab: volatility forecast comparison
- Today's focus: Review and risk memo
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
Review and risk memo is part of real quant work inside ml for quant ii: volatility, ewma, garch intuition, risk forecasting, and stress testing research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: describe review and risk memo in plain language before touching formulas.
2. Technical frame: Build review and risk memo from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment.
3. Market interpretation: Run one compact, reproducible example for review and risk memo and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: identify one way this concept is commonly misused in research or trading discussion.

## Practice Problems
- Explain review and risk memo in one paragraph without jargon.
- Write down one topic-specific formula or workflow for review and risk memo from memory.
- Connect review and risk memo to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind review and risk memo?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Realized Volatility
$$\sigma_{ann}=\sqrt{252}\cdot\mathrm{Std}(r_t)$$
Plain-English interpretation: Sample-based annualized risk estimate.
Interview pitfall: Ignoring clustering and regime changes.

### Formula 2: EWMA Volatility
$$\sigma_t^2=\lambda\sigma_{t-1}^2+(1-\lambda)r_{t-1}^2$$
Plain-English interpretation: Recency-weighted volatility forecasting.
Interview pitfall: Decay hyperparameter not validated out-of-sample.

### Formula 3: GARCH(1,1)
$$\sigma_t^2=\omega+\alpha r_{t-1}^2+\beta\sigma_{t-1}^2$$
Plain-English interpretation: Conditional variance with persistence and shocks.
Interview pitfall: Assuming model stability across crises.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Realized Volatility | Sample-based annualized risk estimate. | Position sizing and stress planning. | Ignoring clustering and regime changes. |
| EWMA Volatility | Recency-weighted volatility forecasting. | Adaptive VaR pipelines. | Decay hyperparameter not validated out-of-sample. |
| GARCH(1,1) | Conditional variance with persistence and shocks. | Risk forecast under volatility clustering. | Assuming model stability across crises. |

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
- Design one topic-specific analysis for review and risk memo instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Compare at least two volatility/risk forecasts for review and risk memo and discuss one stress weakness.

## Interview Drill
- Q1: Explain review and risk memo to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from review and risk memo is now evidence-backed in your notes, and what still needs a focused retry?

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
