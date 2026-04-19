# Week 15 Fri: Attribution: what is actually driving PnL?

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Signals I: momentum, mean reversion, cross-sectional signals, and attribution". Your objective is to understand, apply, and communicate attribution: what is actually driving pnl? in a way a quant team would trust.

## Continuity Map
- Previous day focus: Signal combination and normalization
- Today's focus: Attribution: what is actually driving PnL?
- Next day bridge: Mini lab: compare momentum versus mean reversion rule

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
Attribution: what is actually driving PnL? is part of real quant work inside signals i: momentum, mean reversion, cross-sectional signals, and attribution research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: describe attribution: what is actually driving pnl? in plain language before touching formulas.
2. Technical frame: Build attribution: what is actually driving pnl? from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment.
3. Market interpretation: Run one compact, reproducible example for attribution: what is actually driving pnl? and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: identify one way this concept is commonly misused in research or trading discussion.

## Practice Problems
- Explain attribution: what is actually driving pnl? in one paragraph without jargon.
- Write down one topic-specific formula or workflow for attribution: what is actually driving pnl? from memory.
- Connect attribution: what is actually driving pnl? to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind attribution: what is actually driving pnl??
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
- Design one topic-specific analysis for attribution: what is actually driving pnl? instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Build and compare at least two signal variants for attribution: what is actually driving pnl? and explain why one is more robust.

## Interview Drill
- Q1: Explain attribution: what is actually driving pnl? to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from attribution: what is actually driving pnl? is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
