# Week 02 Fri: Portfolio weights, rebalancing, cumulative performance, and SQL workflow

**Estimated time:** 4 hours

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 45 min | Learn weight vectors and rebalancing intuition. |
| Session 2 | 55 min | Understand cumulative performance tracking. |
| Session 3 | 55 min | Learn where SQL fits in a quant workflow. |
| Session 4 | 55 min | Run code labs on portfolio tables and SQL queries. |
| Session 5 | 30 min | Interview recap. |

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

## Extended Study (to complete a full 4-hour day)
1. Rewrite each core concept in your own words without looking at notes.
2. Add one extra worked example using different numbers or assumptions.
3. Explain one failure mode where this concept can be misapplied in trading or risk work.
4. Add one short paragraph linking this concept to your weekly project objective.

## Coding Task
Implement one notebook cell or small script focused on: portfolio weights, rebalancing, cumulative performance, and sql workflow.

## Daily Interview Drill
### Q: Where would SQL fit in a quant pipeline?
A: Usually in data retrieval, filtering, joining, and aggregation before features, models, or backtests are built in Python.

## Reflection Question
What from portfolio weights, rebalancing, cumulative performance, and sql workflow felt truly clear, and what still needs a slower revisit?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
