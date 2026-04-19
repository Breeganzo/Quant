# Week 15 Sun: Review and critique

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Signals I: momentum, mean reversion, cross-sectional signals, and attribution". Your objective is to understand, apply, and communicate review and critique in a way a quant team would trust.

## Continuity Map
- Previous day focus: Mini lab: compare momentum versus mean reversion rule
- Today's focus: Review and critique
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
Review and critique is part of real quant work inside signals i: momentum, mean reversion, cross-sectional signals, and attribution research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Past trend strength over lookback k.
2. Technical frame: Build review and critique from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: Momentum Signal, Mean-Reversion z-Score, Alpha Attribution).
3. Market interpretation: Cross-sectional ranking strategies.. Run one compact, reproducible example for review and critique and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Ignoring crash risk in reversals.

## Practice Problems
- Explain review and critique in one paragraph without jargon.
- Write down one topic-specific formula or workflow for review and critique from memory.
- Connect review and critique to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind review and critique?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Momentum Signal
$$m_t=\frac{P_t}{P_{t-k}}-1$$
Plain-English interpretation: Past trend strength over lookback k.
Interview pitfall: Ignoring crash risk in reversals.

### Formula 2: Mean-Reversion z-Score
$$z_t=\frac{x_t-\mu_t}{\sigma_t}$$
Plain-English interpretation: Deviation from local mean in standard units.
Interview pitfall: Using unstable rolling windows.

### Formula 3: Alpha Attribution
$$\alpha_t=r_t^{strat}-\beta_t r_t^{mkt}$$
Plain-English interpretation: Residual performance after market exposure.
Interview pitfall: Assuming constant beta through regimes.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Momentum Signal | Past trend strength over lookback k. | Cross-sectional ranking strategies. | Ignoring crash risk in reversals. |
| Mean-Reversion z-Score | Deviation from local mean in standard units. | Entry/exit bands for reversal trades. | Using unstable rolling windows. |
| Alpha Attribution | Residual performance after market exposure. | Diagnose true signal contribution. | Assuming constant beta through regimes. |

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
- Design one topic-specific analysis for review and critique instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Build and compare at least two signal variants for review and critique and explain why one is more robust.

## Interview Drill
- Q1: Explain review and critique to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from review and critique is now evidence-backed in your notes, and what still needs a focused retry?

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
