# Week 16 Fri: Cross-sectional portfolio construction

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Signals II: factor models, statistical arbitrage intuition, cointegration, and regime shifts". Your objective is to understand, apply, and communicate cross-sectional portfolio construction in a way a quant team would trust.

## Continuity Map
- Previous day focus: Regime shifts and model instability
- Today's focus: Cross-sectional portfolio construction
- Next day bridge: Capstone build day

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
Cross-sectional portfolio construction is part of real quant work inside signals ii: factor models, statistical arbitrage intuition, cointegration, and regime shifts research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: describe cross-sectional portfolio construction in plain language before touching formulas.
2. Technical frame: Build cross-sectional portfolio construction from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment.
3. Market interpretation: Run one compact, reproducible example for cross-sectional portfolio construction and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: identify one way this concept is commonly misused in research or trading discussion.

## Practice Problems
- Explain cross-sectional portfolio construction in one paragraph without jargon.
- Write down one topic-specific formula or workflow for cross-sectional portfolio construction from memory.
- Connect cross-sectional portfolio construction to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind cross-sectional portfolio construction?
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
- Design one topic-specific analysis for cross-sectional portfolio construction instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Estimate spread/z-score style metrics for cross-sectional portfolio construction and define one disciplined entry/exit rule.

## Interview Drill
- Q1: Explain cross-sectional portfolio construction to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from cross-sectional portfolio construction is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
