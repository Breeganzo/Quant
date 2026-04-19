# Week 14 Wed: Position sizing and exposure control

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Quant Workflow II: backtesting architecture, position sizing, and performance attribution". Your objective is to understand, apply, and communicate position sizing and exposure control in a way a quant team would trust.

## Continuity Map
- Previous day focus: Look-ahead, survivorship, and data snooping pitfalls
- Today's focus: Position sizing and exposure control
- Next day bridge: Turnover, slippage, and implementation realism

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
Position sizing and exposure control is part of real quant work inside quant workflow ii: backtesting architecture, position sizing, and performance attribution research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: describe position sizing and exposure control in plain language before touching formulas.
2. Technical frame: Build position sizing and exposure control from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment.
3. Market interpretation: Run one compact, reproducible example for position sizing and exposure control and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: identify one way this concept is commonly misused in research or trading discussion.

## Practice Problems
- Explain position sizing and exposure control in one paragraph without jargon.
- Write down one topic-specific formula or workflow for position sizing and exposure control from memory.
- Connect position sizing and exposure control to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind position sizing and exposure control?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Strategy Return with Costs
$$r_t^{strat}=w_{t-1}^Tr_t-c_t$$
Plain-English interpretation: Net return after implementation frictions.
Interview pitfall: Ignoring costs in reported performance.

### Formula 2: Max Drawdown
$$MDD=\min_t\left(\frac{W_t}{\max_{s\le t}W_s}-1\right)$$
Plain-English interpretation: Worst peak-to-trough capital decline.
Interview pitfall: Reporting Sharpe without drawdown context.

### Formula 3: Turnover
$$\mathrm{TO}_t=\frac{1}{2}\sum_i|w_{i,t}-w_{i,t-1}|$$
Plain-English interpretation: Trading intensity proxy for cost pressure.
Interview pitfall: High-turnover alpha that vanishes net of costs.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Strategy Return with Costs | Net return after implementation frictions. | Realistic backtest evaluation. | Ignoring costs in reported performance. |
| Max Drawdown | Worst peak-to-trough capital decline. | Risk limit calibration. | Reporting Sharpe without drawdown context. |
| Turnover | Trading intensity proxy for cost pressure. | Capacity and slippage monitoring. | High-turnover alpha that vanishes net of costs. |

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
- Design one topic-specific analysis for position sizing and exposure control instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Backtest a toy rule for position sizing and exposure control with transaction costs and report net metrics.

## Interview Drill
- Q1: Explain position sizing and exposure control to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from position sizing and exposure control is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
