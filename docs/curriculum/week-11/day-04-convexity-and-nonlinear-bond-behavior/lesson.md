# Week 11 Thu: Convexity and nonlinear bond behavior

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Finance Core III: fixed income, yield curves, duration, convexity, and credit basics". Your objective is to understand, apply, and communicate convexity and nonlinear bond behavior in a way a quant team would trust.

## Continuity Map
- Previous day focus: Duration and interest rate sensitivity
- Today's focus: Convexity and nonlinear bond behavior
- Next day bridge: Credit spreads and default risk basics

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
Convexity and nonlinear bond behavior is part of real quant work inside finance core iii: fixed income, yield curves, duration, convexity, and credit basics research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Second-order yield sensitivity.
2. Technical frame: Build convexity and nonlinear bond behavior from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: Convexity, Price Change Approx, Curve Shock PnL).
3. Market interpretation: Improve bond shock approximations.. Run one compact, reproducible example for convexity and nonlinear bond behavior and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Ignoring convexity in volatile rate regimes.

## Practice Problems
- Explain convexity and nonlinear bond behavior in one paragraph without jargon.
- Write down one topic-specific formula or workflow for convexity and nonlinear bond behavior from memory.
- Connect convexity and nonlinear bond behavior to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind convexity and nonlinear bond behavior?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Convexity
$$C=\frac{1}{P}\sum_t\frac{CF_t\,t(t+1)}{(1+y)^{t+2}}$$
Plain-English interpretation: Second-order yield sensitivity.
Interview pitfall: Ignoring convexity in volatile rate regimes.

### Formula 2: Price Change Approx
$$\frac{\Delta P}{P}\approx -D_{mod}\Delta y + \frac{1}{2}C(\Delta y)^2$$
Plain-English interpretation: Duration-convexity Taylor approximation.
Interview pitfall: Applying for very large non-local shifts.

### Formula 3: Curve Shock PnL
$$PnL\approx -DV01\cdot\Delta bp + \frac{1}{2}C\cdot(\Delta y)^2P$$
Plain-English interpretation: PnL estimate under rate shocks.
Interview pitfall: Not separating parallel vs non-parallel moves.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Convexity | Second-order yield sensitivity. | Improve bond shock approximations. | Ignoring convexity in volatile rate regimes. |
| Price Change Approx | Duration-convexity Taylor approximation. | Scenario stress calculations. | Applying for very large non-local shifts. |
| Curve Shock PnL | PnL estimate under rate shocks. | Risk reporting and hedge checks. | Not separating parallel vs non-parallel moves. |

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
- Design one topic-specific analysis for convexity and nonlinear bond behavior instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Price a simple bond setup for convexity and nonlinear bond behavior and measure sensitivity to a yield shock.

## Interview Drill
- Q1: Explain convexity and nonlinear bond behavior to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from convexity and nonlinear bond behavior is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
