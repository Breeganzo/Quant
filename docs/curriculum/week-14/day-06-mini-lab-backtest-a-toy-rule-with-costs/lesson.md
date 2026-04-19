# Week 14 Sat: Mini lab: backtest a toy rule with costs

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Quant Workflow II: backtesting architecture, position sizing, and performance attribution". Your objective is to understand, apply, and communicate mini lab: backtest a toy rule with costs in a way a quant team would trust.

## Continuity Map
- Previous day focus: Performance attribution and diagnostics
- Today's focus: Mini lab: backtest a toy rule with costs
- Next day bridge: Review and write-up

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
Mini lab: backtest a toy rule with costs is part of real quant work inside quant workflow ii: backtesting architecture, position sizing, and performance attribution research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: describe mini lab: backtest a toy rule with costs in plain language before touching formulas.
2. Technical frame: Build mini lab: backtest a toy rule with costs from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment.
3. Market interpretation: Run one compact, reproducible example for mini lab: backtest a toy rule with costs and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: identify one way this concept is commonly misused in research or trading discussion.

## Practice Problems
- Explain mini lab: backtest a toy rule with costs in one paragraph without jargon.
- Write down one topic-specific formula or workflow for mini lab: backtest a toy rule with costs from memory.
- Connect mini lab: backtest a toy rule with costs to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind mini lab: backtest a toy rule with costs?
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
- Design one topic-specific analysis for mini lab: backtest a toy rule with costs instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Backtest a toy rule for mini lab: backtest a toy rule with costs with transaction costs and report net metrics.

## Interview Drill
- Q1: Explain mini lab: backtest a toy rule with costs to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from mini lab: backtest a toy rule with costs is now evidence-backed in your notes, and what still needs a focused retry?

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
