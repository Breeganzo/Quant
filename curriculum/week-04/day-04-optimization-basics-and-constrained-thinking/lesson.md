# Week 04 Thu: Optimization basics and constrained thinking

**Estimated time:** 8 hours

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

## Formula Organization
- Core formula and meaning
- Variable definitions and units
- Practical implementation caveat

## Extended Study (to complete a full 4-hour day)
1. Rewrite each core concept in your own words without looking at notes.
2. Add one extra worked example using different numbers or assumptions.
3. Explain one failure mode where this concept can be misapplied in trading or risk work.
4. Add one short paragraph linking this concept to your weekly project objective.

## Real-World Data Application
1. Load `curriculum/datasets/real_market_prices.csv` for SPY, QQQ, TLT, and GLD.
2. Compute daily returns and compare annualized volatility across symbols.
3. Build one cumulative growth chart and one correlation table.
4. Write one practical portfolio/risk insight from the data.

## Coding Task
Implement one notebook cell or small script focused on: optimization basics and constrained thinking.

## Daily Interview Drill
### Q: How would you explain optimization simply?
A: It is choosing the best available option after defining what 'best' means and what rules cannot be broken.

## Reflection Question
What from optimization basics and constrained thinking felt truly clear, and what still needs a slower revisit?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
