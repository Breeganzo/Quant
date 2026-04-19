# Week 09 Fri: Turnover, holding period, and capacity intuition

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Finance Core I: market microstructure, execution, slippage, and transaction costs". Your objective is to understand, apply, and communicate turnover, holding period, and capacity intuition in a way a quant team would trust.

## Continuity Map
- Previous day focus: Transaction costs and slippage models
- Today's focus: Turnover, holding period, and capacity intuition
- Next day bridge: Mini lab: strategy before and after costs

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
Turnover, holding period, and capacity intuition is part of real quant work inside finance core i: market microstructure, execution, slippage, and transaction costs research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Reference price between best bid and ask.
2. Technical frame: Build turnover, holding period, and capacity intuition from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: Mid Price, Effective Spread, Turnover).
3. Market interpretation: Execution quality benchmarking.. Run one compact, reproducible example for turnover, holding period, and capacity intuition and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Comparing fills to stale mid prices.

## Practice Problems
- Explain turnover, holding period, and capacity intuition in one paragraph without jargon.
- Write down one topic-specific formula or workflow for turnover, holding period, and capacity intuition from memory.
- Connect turnover, holding period, and capacity intuition to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind turnover, holding period, and capacity intuition?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Mid Price
$$m_t=\frac{\mathrm{bid}_t+\mathrm{ask}_t}{2}$$
Plain-English interpretation: Reference price between best bid and ask.
Interview pitfall: Comparing fills to stale mid prices.

### Formula 2: Effective Spread
$$\mathrm{EffSpread}_t=2\cdot\left|\frac{p_t^{exec}-m_t}{m_t}\right|$$
Plain-English interpretation: Realized transaction cost proxy.
Interview pitfall: Ignoring direction and sign conventions.

### Formula 3: Turnover
$$\mathrm{TO}_t=\frac{1}{2}\sum_i|w_{i,t}-w_{i,t-1}|$$
Plain-English interpretation: Fraction of portfolio traded on rebalance.
Interview pitfall: Reporting gross turnover without cost translation.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Mid Price | Reference price between best bid and ask. | Execution quality benchmarking. | Comparing fills to stale mid prices. |
| Effective Spread | Realized transaction cost proxy. | Estimate execution drag in backtests. | Ignoring direction and sign conventions. |
| Turnover | Fraction of portfolio traded on rebalance. | Capacity and cost control. | Reporting gross turnover without cost translation. |

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
- Design one topic-specific analysis for turnover, holding period, and capacity intuition instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Simulate one execution or turnover scenario for turnover, holding period, and capacity intuition and quantify its cost impact.

## Interview Drill
- Q1: Explain turnover, holding period, and capacity intuition to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from turnover, holding period, and capacity intuition is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
