# Week 16 Mon: Factor models and common risk decomposition

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Signals II: factor models, statistical arbitrage intuition, cointegration, and regime shifts". Your objective is to understand, apply, and communicate factor models and common risk decomposition in a way a quant team would trust.

## Continuity Map
- Week kickoff: establish baseline intuition and key definitions before moving into formal detail.
- Today's focus: Factor models and common risk decomposition
- Next day bridge: Residual signals and relative-value intuition

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
Factor models and common risk decomposition is part of real quant work inside signals ii: factor models, statistical arbitrage intuition, cointegration, and regime shifts research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Hedged relative-value residual.
2. Technical frame: Build factor models and common risk decomposition from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: Spread, Half-Life, Factor Model).
3. Market interpretation: Pairs and residual strategy setup.. Run one compact, reproducible example for factor models and common risk decomposition and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Using stale hedge ratio.

## Practice Problems
- Explain factor models and common risk decomposition in one paragraph without jargon.
- Write down one topic-specific formula or workflow for factor models and common risk decomposition from memory.
- Connect factor models and common risk decomposition to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind factor models and common risk decomposition?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Spread
$$s_t=y_t-\beta x_t$$
Plain-English interpretation: Hedged relative-value residual.
Interview pitfall: Using stale hedge ratio.

### Formula 2: Half-Life
$$HL=-\frac{\ln 2}{\ln \phi}$$
Plain-English interpretation: Mean-reversion speed estimate.
Interview pitfall: Estimating phi on nonstationary series.

### Formula 3: Factor Model
$$r_t=\alpha+\beta^Tf_t+\epsilon_t$$
Plain-English interpretation: Return decomposition into factor exposures.
Interview pitfall: Assuming static betas across regimes.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Spread | Hedged relative-value residual. | Pairs and residual strategy setup. | Using stale hedge ratio. |
| Half-Life | Mean-reversion speed estimate. | Holding-period sanity checks. | Estimating phi on nonstationary series. |
| Factor Model | Return decomposition into factor exposures. | Risk decomposition and attribution. | Assuming static betas across regimes. |

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
- Design one topic-specific analysis for factor models and common risk decomposition instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Estimate spread/z-score style metrics for factor models and common risk decomposition and define one disciplined entry/exit rule.

## Interview Drill
- Q1: Explain factor models and common risk decomposition to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from factor models and common risk decomposition is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
