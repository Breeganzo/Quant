# Week 09 Sun: Review and trading diary

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Finance Core I: market microstructure, execution, slippage, and transaction costs". Your objective is to understand, apply, and communicate review and trading diary in a way a quant team would trust.

## Continuity Map
- Previous day focus: Mini lab: strategy before and after costs
- Today's focus: Review and trading diary
- Week closure: consolidate this concept into your weekly project narrative.

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
Review and trading diary is part of real quant work inside finance core i: market microstructure, execution, slippage, and transaction costs research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: describe review and trading diary in plain language before touching formulas.
2. Technical frame: Build review and trading diary from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment.
3. Market interpretation: Run one compact, reproducible example for review and trading diary and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: identify one way this concept is commonly misused in research or trading discussion.

## Practice Problems
- Explain review and trading diary in one paragraph without jargon.
- Write down one topic-specific formula or workflow for review and trading diary from memory.
- Connect review and trading diary to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind review and trading diary?
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
- Design one topic-specific analysis for review and trading diary instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Simulate one execution or turnover scenario for review and trading diary and quantify its cost impact.

## Interview Drill
- Q1: Explain review and trading diary to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from review and trading diary is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.

## Sunday Mini-Project Blueprint
1. Load real market data from `curriculum/datasets/real_market_prices.csv`.
2. Define a clear project question and one measurable output metric.
3. Build at least one baseline and one variation, then compare outcomes.
4. Write a short conclusion with one limitation and one next-step improvement.
