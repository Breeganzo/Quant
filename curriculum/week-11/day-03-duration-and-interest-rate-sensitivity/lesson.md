# Week 11 Wed: Duration and interest rate sensitivity

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Finance Core III: fixed income, yield curves, duration, convexity, and credit basics". Your objective is to understand, apply, and communicate duration and interest rate sensitivity in a way a quant team would trust.

## Continuity Map
- Previous day focus: Yield, yield curve, and term structure intuition
- Today's focus: Duration and interest rate sensitivity
- Next day bridge: Convexity and nonlinear bond behavior

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
Duration and interest rate sensitivity is part of real quant work inside finance core iii: fixed income, yield curves, duration, convexity, and credit basics research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: describe duration and interest rate sensitivity in plain language before touching formulas.
2. Technical frame: Build duration and interest rate sensitivity from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment.
3. Market interpretation: Run one compact, reproducible example for duration and interest rate sensitivity and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: identify one way this concept is commonly misused in research or trading discussion.

## Practice Problems
- Explain duration and interest rate sensitivity in one paragraph without jargon.
- Write down one topic-specific formula or workflow for duration and interest rate sensitivity from memory.
- Connect duration and interest rate sensitivity to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind duration and interest rate sensitivity?
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
- Design one topic-specific analysis for duration and interest rate sensitivity instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Price a simple bond setup for duration and interest rate sensitivity and measure sensitivity to a yield shock.

## Interview Drill
- Q1: Explain duration and interest rate sensitivity to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from duration and interest rate sensitivity is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
