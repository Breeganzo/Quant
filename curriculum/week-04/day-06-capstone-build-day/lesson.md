# Week 04 Sat: Capstone build day

**Estimated time:** 6 hours

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 20 min | Capstone plan. |
| Session 2 | 55 min | Implement exploratory asset-allocation notebook. |
| Session 3 | 20 min | Interpret results. |
| Session 4 | 25 min | Interview practice. |

## Why It Matters In Quant
Capstone build day is part of real quant work inside math rebuild ii: statistics, inference, regression, optimization, and portfolio theory research, trading, or risk workflows.

## Learning Overview
This is the first proper Month 1 capstone build session. The job is not to create a perfect optimizer, but to combine returns, volatility, correlation, and portfolio logic into one coherent piece of work.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### Capstone integration
- Simple explanation: A capstone should combine the week's ideas rather than repeating one isolated topic.
- Technical depth: This one brings together descriptive statistics, covariance, and simple portfolio comparison.
- Finance example: A small asset-allocation study mirrors the early structure of real portfolio research.

## Worked Examples
- Test a few candidate weights and compare return-risk trade-offs.

## Practice Questions With Answers
### Question: What makes a capstone useful for applications?
Answer: It shows you can frame a question, implement analysis, interpret results, and communicate limitations.

## Daily Quiz (Closed-Book)
1. Explain today's core intuition from memory.
2. Write one formula/workflow and define all symbols/steps.
3. Give one use case and one realistic failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Net Return
$$r_t^{net}=r_t^{gross}-cost_t$$
Plain-English interpretation: Performance after implementation frictions.
Notation check: Presenting gross-only metrics.

### Formula 2: Out-of-Sample RMSE
$$RMSE_{OOS}=\sqrt{\frac{1}{n}\sum_i(\hat y_i-y_i)^2}$$
Plain-English interpretation: Forecast quality on unseen data.
Notation check: Leaking test data into tuning.

### Formula 3: Max Drawdown
$$MDD=\min_t\left(\frac{W_t}{\max_{s\le t}W_s}-1\right)$$
Plain-English interpretation: Worst path-dependent loss.
Notation check: Reporting return with no drawdown context.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Net Return | Performance after implementation frictions. | Final report realism. | Presenting gross-only metrics. |
| Out-of-Sample RMSE | Forecast quality on unseen data. | Capstone model comparison. | Leaking test data into tuning. |
| Max Drawdown | Worst path-dependent loss. | Risk defense in presentations. | Reporting return with no drawdown context. |

## Extended Study (to complete a full 6-hour day)
1. Rewrite each core concept in your own words without looking at notes.
2. Add one extra worked example using different numbers or assumptions.
3. Explain one failure mode where this concept can be misapplied in trading or risk work.
4. Add one short paragraph linking this concept to your weekly project objective.

## Real-World Data Application
1. Pull SPY, QQQ, TLT, and GLD with yfinance when internet is available.
2. If available, compare with a Robinhood-style export CSV for source consistency.
3. Use `curriculum/datasets/real_market_prices.csv` as reproducible fallback.
4. Compute log returns, annualized volatility, and Sharpe ratio across symbols.
5. Build one cumulative growth chart and one correlation table.
6. Write one practical portfolio/risk insight from the data.

## Coding Task
Implement a small reproducible example for capstone build day and explain one assumption that could fail in markets.

## Daily Interview Drill
### Q: How would you describe this capstone briefly?
A: I built an exploratory asset-allocation study comparing a few simple portfolios using return, volatility, and correlation logic.

## Reflection Question
What from capstone build day is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
