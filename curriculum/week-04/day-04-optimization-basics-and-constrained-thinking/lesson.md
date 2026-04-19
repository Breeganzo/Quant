# Week 04 Thu: Optimization basics and constrained thinking

**Estimated time:** 6 hours

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 45 min | Optimization intuition. |
| Session 2 | 55 min | Objective functions and constraints. |
| Session 3 | 55 min | Portfolio examples. |
| Session 4 | 55 min | Code simple constrained search. |
| Session 5 | 30 min | Interview recap. |

## Why It Matters In Quant
Optimization basics and constrained thinking is part of real quant work inside math rebuild ii: statistics, inference, regression, optimization, and portfolio theory research, trading, or risk workflows.

## Learning Overview
Optimization is simply the art of choosing the best feasible option under a clear objective and constraints.

In finance, constraints matter as much as objectives because real portfolios are not free to do anything.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### Objective function
- Simple explanation: An objective function measures what you are trying to maximize or minimize.
- Technical depth: Examples include maximizing expected return, minimizing variance, or minimizing prediction error.
- Finance example: A portfolio optimizer might minimize volatility for a given return target.

### Constraints
- Simple explanation: Constraints limit what choices are allowed.
- Technical depth: Constraints can include weights summing to one, no shorting, leverage limits, or turnover caps.
- Finance example: A portfolio with no-shorting cannot assign negative weights.

### Trade-offs
- Simple explanation: Optimization is usually about balancing competing goals.
- Technical depth: Higher return may come with higher risk, and cleaner predictions may require more model complexity.
- Finance example: A high-return portfolio may be unacceptable if it violates risk or concentration limits.

## Worked Examples
- Pick portfolio weights from a small grid to minimize simple variance under constraints.
- Explain how the answer changes if short selling is allowed versus forbidden.

## Practice Questions With Answers
### Question: Why are constraints essential in finance optimization?
Answer: Because the mathematically best answer is often unrealistic or risky if not limited by practical rules.

### Question: What is an objective function in plain language?
Answer: It is the score you are trying to make as good as possible.

## Daily Quiz (Closed-Book)
1. Explain today's core intuition from memory.
2. Write one formula/workflow and define all symbols/steps.
3. Give one use case and one realistic failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Constrained Objective
$$\min_w f(w)\ 	ext{s.t.}\ Aw=b,\ w\ge0$$
Plain-English interpretation: Target with feasibility constraints.
Notation check: Ignoring feasibility checks before solving.

### Formula 2: Lagrangian
$$\mathcal{L}(w,\lambda)=f(w)+\lambda^T(Aw-b)$$
Plain-English interpretation: Constraint-aware objective transform.
Notation check: Not verifying KKT conditions post-solve.

### Formula 3: KKT Stationarity
$$\nabla_w\mathcal{L}=0$$
Plain-English interpretation: Necessary optimality condition.
Notation check: Stopping at numerical output without diagnostics.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Constrained Objective | Target with feasibility constraints. | Portfolio optimization setup. | Ignoring feasibility checks before solving. |
| Lagrangian | Constraint-aware objective transform. | Solve equality-constrained problems. | Not verifying KKT conditions post-solve. |
| KKT Stationarity | Necessary optimality condition. | Audit optimization solution quality. | Stopping at numerical output without diagnostics. |

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
Implement a small reproducible example for optimization basics and constrained thinking and explain one assumption that could fail in markets.

## Daily Interview Drill
### Q: How would you explain optimization simply?
A: It is choosing the best available option after defining what 'best' means and what rules cannot be broken.

## Reflection Question
What from optimization basics and constrained thinking is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
