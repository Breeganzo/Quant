# Week 12 Thu: Volatility smile and pricing inputs

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Finance Core IV: derivatives, options, Greeks, hedging, and risk management". Your objective is to understand, apply, and communicate volatility smile and pricing inputs in a way a quant team would trust.

## Continuity Map
- Previous day focus: Option Greeks intuition
- Today's focus: Volatility smile and pricing inputs
- Next day bridge: Risk management: VaR, stress, and scenarios

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
Volatility smile and pricing inputs is part of real quant work inside finance core iv: derivatives, options, greeks, hedging, and risk management research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Upside-only terminal payoff.
2. Technical frame: Build volatility smile and pricing inputs from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: Call Payoff, Put Payoff, Put-Call Parity).
3. Market interpretation: Directional convex exposures.. Run one compact, reproducible example for volatility smile and pricing inputs and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Confusing payoff with net profit.

## Practice Problems
- Explain volatility smile and pricing inputs in one paragraph without jargon.
- Write down one topic-specific formula or workflow for volatility smile and pricing inputs from memory.
- Connect volatility smile and pricing inputs to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind volatility smile and pricing inputs?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Call Payoff
$$\max(S_T-K,0)$$
Plain-English interpretation: Upside-only terminal payoff.
Interview pitfall: Confusing payoff with net profit.

### Formula 2: Put Payoff
$$\max(K-S_T,0)$$
Plain-English interpretation: Downside-protection terminal payoff.
Interview pitfall: Ignoring premium/time decay.

### Formula 3: Put-Call Parity
$$C-P=S_0-Ke^{-rT}$$
Plain-English interpretation: No-arbitrage relation across vanilla options.
Interview pitfall: Applying parity with mismatched maturities.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Call Payoff | Upside-only terminal payoff. | Directional convex exposures. | Confusing payoff with net profit. |
| Put Payoff | Downside-protection terminal payoff. | Tail-risk hedge intuition. | Ignoring premium/time decay. |
| Put-Call Parity | No-arbitrage relation across vanilla options. | Consistency checks in pricing surfaces. | Applying parity with mismatched maturities. |

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
- Design one topic-specific analysis for volatility smile and pricing inputs instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Implement payoff and sensitivity calculations for volatility smile and pricing inputs and interpret one hedging implication.

## Interview Drill
- Q1: Explain volatility smile and pricing inputs to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from volatility smile and pricing inputs is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
