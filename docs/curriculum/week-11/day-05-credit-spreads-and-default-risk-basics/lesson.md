# Week 11 Fri: Credit spreads and default risk basics

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Finance Core III: fixed income, yield curves, duration, convexity, and credit basics". Your objective is to understand, apply, and communicate credit spreads and default risk basics in a way a quant team would trust.

## Continuity Map
- Previous day focus: Convexity and nonlinear bond behavior
- Today's focus: Credit spreads and default risk basics
- Next day bridge: Mini lab: simple bond price sensitivity

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
Credit spreads and default risk basics is part of real quant work inside finance core iii: fixed income, yield curves, duration, convexity, and credit basics research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Compensation over risk-free yield.
2. Technical frame: Build credit spreads and default risk basics from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: Credit Spread, Expected Loss, Hazard Approximation).
3. Market interpretation: Credit-risk pricing comparison.. Run one compact, reproducible example for credit spreads and default risk basics and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Ignoring liquidity premium component.

## Practice Problems
- Explain credit spreads and default risk basics in one paragraph without jargon.
- Write down one topic-specific formula or workflow for credit spreads and default risk basics from memory.
- Connect credit spreads and default risk basics to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind credit spreads and default risk basics?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Credit Spread
$$s_{credit}=y_{corp}-y_{gov}$$
Plain-English interpretation: Compensation over risk-free yield.
Interview pitfall: Ignoring liquidity premium component.

### Formula 2: Expected Loss
$$EL=PD\times LGD\times EAD$$
Plain-English interpretation: Average credit loss estimate.
Interview pitfall: Static PD/LGD assumptions across regimes.

### Formula 3: Hazard Approximation
$$h\approx\frac{s_{credit}}{1-R}$$
Plain-English interpretation: Spread-to-default intensity proxy.
Interview pitfall: Using approximation outside assumptions.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Credit Spread | Compensation over risk-free yield. | Credit-risk pricing comparison. | Ignoring liquidity premium component. |
| Expected Loss | Average credit loss estimate. | Risk budgeting and scenario design. | Static PD/LGD assumptions across regimes. |
| Hazard Approximation | Spread-to-default intensity proxy. | Quick sanity checks on spread levels. | Using approximation outside assumptions. |

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
- Design one topic-specific analysis for credit spreads and default risk basics instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Price a simple bond setup for credit spreads and default risk basics and measure sensitivity to a yield shock.

## Interview Drill
- Q1: Explain credit spreads and default risk basics to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from credit spreads and default risk basics is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
