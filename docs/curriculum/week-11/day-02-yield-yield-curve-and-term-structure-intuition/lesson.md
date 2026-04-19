# Week 11 Tue: Yield, yield curve, and term structure intuition

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Finance Core III: fixed income, yield curves, duration, convexity, and credit basics". Your objective is to understand, apply, and communicate yield, yield curve, and term structure intuition in a way a quant team would trust.

## Continuity Map
- Previous day focus: Bond cash flows and discounting
- Today's focus: Yield, yield curve, and term structure intuition
- Next day bridge: Duration and interest rate sensitivity

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
Yield, yield curve, and term structure intuition is part of real quant work inside finance core iii: fixed income, yield curves, duration, convexity, and credit basics research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Present-value weight at maturity T.
2. Technical frame: Build yield, yield curve, and term structure intuition from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: Discount Factor, Forward Rate, Term Spread).
3. Market interpretation: Curve construction and pricing.. Run one compact, reproducible example for yield, yield curve, and term structure intuition and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Mixing compounding conventions.

## Practice Problems
- Explain yield, yield curve, and term structure intuition in one paragraph without jargon.
- Write down one topic-specific formula or workflow for yield, yield curve, and term structure intuition from memory.
- Connect yield, yield curve, and term structure intuition to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind yield, yield curve, and term structure intuition?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Discount Factor
$$DF(T)=\frac{1}{(1+s_T)^T}$$
Plain-English interpretation: Present-value weight at maturity T.
Interview pitfall: Mixing compounding conventions.

### Formula 2: Forward Rate
$$f_{t,t+1}=\frac{(1+s_{t+1})^{t+1}}{(1+s_t)^t}-1$$
Plain-English interpretation: Implied future short rate.
Interview pitfall: Interpreting forwards as unbiased forecasts.

### Formula 3: Term Spread
$$TS=s_{10Y}-s_{2Y}$$
Plain-English interpretation: Slope between long and short yields.
Interview pitfall: Using one spread as complete macro model.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Discount Factor | Present-value weight at maturity T. | Curve construction and pricing. | Mixing compounding conventions. |
| Forward Rate | Implied future short rate. | Term-structure expectations analysis. | Interpreting forwards as unbiased forecasts. |
| Term Spread | Slope between long and short yields. | Macro regime signal monitoring. | Using one spread as complete macro model. |

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
- Design one topic-specific analysis for yield, yield curve, and term structure intuition instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Price a simple bond setup for yield, yield curve, and term structure intuition and measure sensitivity to a yield shock.

## Interview Drill
- Q1: Explain yield, yield curve, and term structure intuition to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from yield, yield curve, and term structure intuition is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
