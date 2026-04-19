# Week 02 Fri: Portfolio weights, rebalancing, cumulative performance, and SQL workflow

**Estimated time:** 10 hours

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 60 min | Concept briefing and assumptions map. |
| Session 2 | 60 min | Formula derivation and notation drills. |
| Session 3 | 60 min | Solved real-world case walkthrough. |
| Session 4 | 60 min | Data-quality checks and diagnostics. |
| Session 5 | 60 min | Baseline notebook implementation with comments. |
| Session 6 | 60 min | Extension coding and parameter variation. |
| Session 7 | 60 min | Risk caveat and robustness analysis. |
| Session 8 | 60 min | Interview-style quiz defense rehearsal. |
| Session 9 | 60 min | Revision and error-log correction cycle. |
| Session 10 | 60 min | Desk memo and next-day experiment plan. |

## Why It Matters In Quant
Portfolio weights, rebalancing, cumulative performance, and SQL workflow is part of real quant work inside data and linear algebra: numpy, pandas, visualization, diversification, and sql basics research, trading, or risk workflows.

## Learning Overview
A quant researcher needs both portfolio mechanics and data retrieval discipline. Today combines those two practical skills.

The goal is to understand how weights translate into performance and why SQL remains useful even when much of the analysis happens in Python.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### Portfolio weights and rebalancing
- Simple explanation: Weights tell you how much of the portfolio is assigned to each asset. Rebalancing resets those weights after markets move.
- Technical depth: Without rebalancing, weights drift as relative asset performance changes. That changes exposures and risk over time.
- Finance example: A 60/40 portfolio does not stay 60/40 if equities rally strongly and no rebalance is performed.

### Cumulative performance
- Simple explanation: Cumulative performance tracks how wealth evolves when returns compound over time.
- Technical depth: A cumulative wealth index is typically formed by chaining gross returns period by period.
- Finance example: Two strategies with the same average return can produce very different wealth paths if their volatility differs.

### SQL in quant research
- Simple explanation: SQL is a way to query structured data stored in tables.
- Technical depth: Even if modeling is done in Python, SQL is often used to filter, group, aggregate, and join historical market or transaction datasets efficiently.
- Finance example: You might query daily prices for a ticker universe before moving the result into pandas for analysis.

## Worked Examples
- Track a two-asset portfolio with and without rebalancing.
- Build a simple wealth index from daily portfolio returns.
- Use SQL-style queries on a toy price table with DuckDB.

## Practice Questions With Answers
### Question: Why does a portfolio drift if you do not rebalance?
Answer: Because winners and losers change their portfolio weights mechanically as their values change.

### Question: Why is SQL still useful for a quant?
Answer: Because many research workflows start by pulling or filtering large structured datasets before numerical analysis begins.

### Question: What is a simple cumulative wealth index?
Answer: It is the compounded value of starting capital after applying each period's gross return in sequence.

## Daily Quiz (Closed-Book)
1. Explain today's core intuition from memory.
2. Write one formula/workflow and define all symbols/steps.
3. Give one use case and one realistic failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Portfolio Return
$$r_{p,t}=\sum_i w_{i,t-1}r_{i,t}$$
Plain-English interpretation: Weighted one-step return.
Notation check: Using contemporaneous (leaky) weights.

### Formula 2: Turnover
$$\mathrm{TO}_t=\frac{1}{2}\sum_i|w_{i,t}-w_{i,t-1}|$$
Plain-English interpretation: Rebalance trading requirement.
Notation check: Ignoring transaction costs in alpha claims.

### Formula 3: Cumulative Wealth
$$W_t=W_0\prod_{j=1}^{t}(1+r_{p,j})$$
Plain-English interpretation: Compounded capital path.
Notation check: Averaging returns instead of compounding.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Portfolio Return | Weighted one-step return. | Portfolio backtest baseline. | Using contemporaneous (leaky) weights. |
| Turnover | Rebalance trading requirement. | Estimate execution cost pressure. | Ignoring transaction costs in alpha claims. |
| Cumulative Wealth | Compounded capital path. | Compare portfolio design trajectories. | Averaging returns instead of compounding. |

## Extended Study (to complete a full 10-hour day)
1. Rewrite each core concept in your own words without looking at notes.
2. Add one extra solved case using different assumptions and compare outputs.
3. Explain one failure mode where this concept can be misapplied in trading or risk work.
4. Add one short paragraph linking this concept to your weekly project objective.
5. Propose one follow-up experiment for tomorrow and define success/failure criteria.

## Real-World Data Application
1. Use `curriculum/datasets/real_market_prices.csv` as reproducible fallback market panel.
2. Run one baseline analysis and one stressed-assumption variant.
3. Document one risk caveat and one robustness check before finalizing conclusions.

- Use yfinance first for SPY, QQQ, TLT, and GLD when internet is available.
- If available, validate against a Robinhood-style export CSV for consistency checks.
- Fall back to curriculum/datasets/real_market_prices.csv for reproducible runs.
- Design one topic-specific analysis for portfolio weights, rebalancing, cumulative performance, and sql workflow instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Build a cleaned feature table for portfolio weights, rebalancing, cumulative performance, and sql workflow and show one validation check that catches a data issue.

## Daily Interview Drill
### Q: Where would SQL fit in a quant pipeline?
A: Usually in data retrieval, filtering, joining, and aggregation before features, models, or backtests are built in Python.

## Reflection Question
What from portfolio weights, rebalancing, cumulative performance, and sql workflow is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
