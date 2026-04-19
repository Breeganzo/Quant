# Week 11 Sat: Mini lab: simple bond price sensitivity

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Finance Core III: fixed income, yield curves, duration, convexity, and credit basics". Your objective is to understand, apply, and communicate mini lab: simple bond price sensitivity in a way a quant team would trust.

## Continuity Map
- Previous day focus: Credit spreads and default risk basics
- Today's focus: Mini lab: simple bond price sensitivity
- Next day bridge: Review and recap

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
Mini lab: simple bond price sensitivity is part of real quant work inside finance core iii: fixed income, yield curves, duration, convexity, and credit basics research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Present value of discounted cash flows.
2. Technical frame: Build mini lab: simple bond price sensitivity from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: Bond Price, Modified Duration, Convexity).
3. Market interpretation: Mark-to-model pricing for plain-vanilla bonds.. Run one compact, reproducible example for mini lab: simple bond price sensitivity and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Mixing compounding conventions.

## Practice Problems
- Explain mini lab: simple bond price sensitivity in one paragraph without jargon.
- Write down one topic-specific formula or workflow for mini lab: simple bond price sensitivity from memory.
- Connect mini lab: simple bond price sensitivity to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind mini lab: simple bond price sensitivity?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Bond Price
$$P=\sum_{t=1}^{T}\frac{CF_t}{(1+y)^t}$$
Plain-English interpretation: Present value of discounted cash flows.
Interview pitfall: Mixing compounding conventions.

### Formula 2: Modified Duration
$$D_{mod}=\frac{D_{mac}}{1+y}$$
Plain-English interpretation: Approximate percentage price sensitivity to yield.
Interview pitfall: Using duration alone for large yield moves.

### Formula 3: Convexity
$$C=\frac{1}{P}\sum_{t=1}^{T}\frac{CF_t\,t(t+1)}{(1+y)^{t+2}}$$
Plain-English interpretation: Second-order sensitivity adjustment to yield moves.
Interview pitfall: Ignoring convexity in stressed scenarios.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Bond Price | Present value of discounted cash flows. | Mark-to-model pricing for plain-vanilla bonds. | Mixing compounding conventions. |
| Modified Duration | Approximate percentage price sensitivity to yield. | Rate-shock risk estimation. | Using duration alone for large yield moves. |
| Convexity | Second-order sensitivity adjustment to yield moves. | Improve rate-shock approximation accuracy. | Ignoring convexity in stressed scenarios. |

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
- Design one topic-specific analysis for mini lab: simple bond price sensitivity instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Price a simple bond setup for mini lab: simple bond price sensitivity and measure sensitivity to a yield shock.

## Interview Drill
- Q1: Explain mini lab: simple bond price sensitivity to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from mini lab: simple bond price sensitivity is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.

## Saturday Revision Protocol
1. Rebuild your week summary from memory before opening notes.
2. Rework two weak problems from your error log with corrected reasoning.
3. Refresh formula sheet entries and mark confidence 0-5 per formula.
4. Prepare one interview-style explanation for the week's hardest concept.
