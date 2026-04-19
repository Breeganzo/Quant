# Week 16 Sun: Capstone review and write-up

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Signals II: factor models, statistical arbitrage intuition, cointegration, and regime shifts". Your objective is to understand, apply, and communicate capstone review and write-up in a way a quant team would trust.

## Continuity Map
- Previous day focus: Capstone build day
- Today's focus: Capstone review and write-up
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
Capstone review and write-up is part of real quant work inside signals ii: factor models, statistical arbitrage intuition, cointegration, and regime shifts research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: describe capstone review and write-up in plain language before touching formulas.
2. Technical frame: Build capstone review and write-up from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment.
3. Market interpretation: Run one compact, reproducible example for capstone review and write-up and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: identify one way this concept is commonly misused in research or trading discussion.

## Practice Problems
- Explain capstone review and write-up in one paragraph without jargon.
- Write down one topic-specific formula or workflow for capstone review and write-up from memory.
- Connect capstone review and write-up to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind capstone review and write-up?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Spread
$$s_t=y_t-\beta x_t$$
Plain-English interpretation: Relative value residual after hedge ratio adjustment.
Interview pitfall: Skipping hedge-ratio estimation stability checks.

### Formula 2: Spread z-Score
$$z_t=\frac{s_t-\mu_s}{\sigma_s}$$
Plain-English interpretation: Normalized spread deviation signal.
Interview pitfall: Using static moments in regime shifts.

### Formula 3: Half-Life
$$\mathrm{HL}= -\frac{\ln 2}{\ln \phi}$$
Plain-English interpretation: Expected mean-reversion speed from AR(1) phi.
Interview pitfall: Estimating phi on non-stationary spread.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Spread | Relative value residual after hedge ratio adjustment. | Pairs trading mean-reversion setup. | Skipping hedge-ratio estimation stability checks. |
| Spread z-Score | Normalized spread deviation signal. | Rule-based entry and exit bands. | Using static moments in regime shifts. |
| Half-Life | Expected mean-reversion speed from AR(1) phi. | Set holding horizon expectations. | Estimating phi on non-stationary spread. |

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
- Design one topic-specific analysis for capstone review and write-up instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Estimate spread/z-score style metrics for capstone review and write-up and define one disciplined entry/exit rule.

## Interview Drill
- Q1: Explain capstone review and write-up to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from capstone review and write-up is now evidence-backed in your notes, and what still needs a focused retry?

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
