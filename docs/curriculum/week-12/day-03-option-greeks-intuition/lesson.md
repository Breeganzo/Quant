# Week 12 Wed: Option Greeks intuition

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Finance Core IV: derivatives, options, Greeks, hedging, and risk management". Your objective is to understand, apply, and communicate option greeks intuition in a way a quant team would trust.

## Continuity Map
- Previous day focus: Calls, puts, and payoff diagrams
- Today's focus: Option Greeks intuition
- Next day bridge: Volatility smile and pricing inputs

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
Option Greeks intuition is part of real quant work inside finance core iv: derivatives, options, greeks, hedging, and risk management research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Price sensitivity to underlying.
2. Technical frame: Build option greeks intuition from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: Delta, Gamma, Vega).
3. Market interpretation: Hedge-ratio baseline.. Run one compact, reproducible example for option greeks intuition and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Treating delta as constant.

## Practice Problems
- Explain option greeks intuition in one paragraph without jargon.
- Write down one topic-specific formula or workflow for option greeks intuition from memory.
- Connect option greeks intuition to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind option greeks intuition?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Delta
$$\Delta=\frac{\partial V}{\partial S}$$
Plain-English interpretation: Price sensitivity to underlying.
Interview pitfall: Treating delta as constant.

### Formula 2: Gamma
$$\Gamma=\frac{\partial^2 V}{\partial S^2}$$
Plain-English interpretation: Delta curvature sensitivity.
Interview pitfall: Ignoring gamma in large spot moves.

### Formula 3: Vega
$$Vega=\frac{\partial V}{\partial \sigma}$$
Plain-English interpretation: Sensitivity to implied volatility.
Interview pitfall: Ignoring vol-regime shifts.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Delta | Price sensitivity to underlying. | Hedge-ratio baseline. | Treating delta as constant. |
| Gamma | Delta curvature sensitivity. | Re-hedging frequency intuition. | Ignoring gamma in large spot moves. |
| Vega | Sensitivity to implied volatility. | Volatility-risk exposure sizing. | Ignoring vol-regime shifts. |

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
- Design one topic-specific analysis for option greeks intuition instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Implement payoff and sensitivity calculations for option greeks intuition and interpret one hedging implication.

## Interview Drill
- Q1: Explain option greeks intuition to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from option greeks intuition is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
