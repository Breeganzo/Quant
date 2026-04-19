# Week 09 Thu: Transaction costs and slippage models

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Finance Core I: market microstructure, execution, slippage, and transaction costs". Your objective is to understand, apply, and communicate transaction costs and slippage models in a way a quant team would trust.

## Continuity Map
- Previous day focus: Order types and execution choices
- Today's focus: Transaction costs and slippage models
- Next day bridge: Turnover, holding period, and capacity intuition

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
Transaction costs and slippage models is part of real quant work inside finance core i: market microstructure, execution, slippage, and transaction costs research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Post-cost strategy return.
2. Technical frame: Build transaction costs and slippage models from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: Net Strategy Return, Turnover, Max Drawdown).
3. Market interpretation: Realistic backtest reporting.. Run one compact, reproducible example for transaction costs and slippage models and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Publishing gross-only performance.

## Practice Problems
- Explain transaction costs and slippage models in one paragraph without jargon.
- Write down one topic-specific formula or workflow for transaction costs and slippage models from memory.
- Connect transaction costs and slippage models to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind transaction costs and slippage models?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Net Strategy Return
$$r_t^{net}=w_{t-1}^Tr_t-c_t$$
Plain-English interpretation: Post-cost strategy return.
Interview pitfall: Publishing gross-only performance.

### Formula 2: Turnover
$$TO_t=\frac{1}{2}\sum_i|w_{i,t}-w_{i,t-1}|$$
Plain-English interpretation: Trade intensity proxy.
Interview pitfall: Ignoring turnover in deployment sizing.

### Formula 3: Max Drawdown
$$MDD=\min_t\left(\frac{W_t}{\max_{s\le t}W_s}-1\right)$$
Plain-English interpretation: Worst peak-to-trough decline.
Interview pitfall: Relying on Sharpe without path risk.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Net Strategy Return | Post-cost strategy return. | Realistic backtest reporting. | Publishing gross-only performance. |
| Turnover | Trade intensity proxy. | Cost and capacity constraints. | Ignoring turnover in deployment sizing. |
| Max Drawdown | Worst peak-to-trough decline. | Risk narrative and kill-switch design. | Relying on Sharpe without path risk. |

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
- Design one topic-specific analysis for transaction costs and slippage models instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Simulate one execution or turnover scenario for transaction costs and slippage models and quantify its cost impact.

## Interview Drill
- Q1: Explain transaction costs and slippage models to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from transaction costs and slippage models is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
