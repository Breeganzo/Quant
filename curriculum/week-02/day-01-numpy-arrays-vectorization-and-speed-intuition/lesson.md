# Week 02 Mon: NumPy arrays, vectorization, and speed intuition

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
NumPy arrays, vectorization, and speed intuition is part of real quant work inside data and linear algebra: numpy, pandas, visualization, diversification, and sql basics research, trading, or risk workflows.

## Learning Overview
NumPy matters because quant work becomes painful and slow if every calculation is written as a manual loop. Arrays let you express the mathematical structure directly.

The practical habit today is to stop treating market data as isolated numbers and start seeing it as organized numerical objects that can be transformed efficiently.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### Arrays as financial objects
- Simple explanation: An array is a structured collection of numbers. In quant work those numbers might be prices, returns, weights, signals, or volumes.
- Technical depth: NumPy arrays support vectorized operations, broadcasting, and matrix-style computations that are much faster and clearer than many explicit Python loops.
- Finance example: A daily return vector across 100 assets is naturally stored as one array.

### Vectorization
- Simple explanation: Vectorization means applying the same operation to many values at once.
- Technical depth: Instead of looping through each asset return manually, array operations act on the whole structure in one expression.
- Finance example: Computing portfolio returns over many days becomes one matrix multiplication rather than repeated manual sums.

### Shape and dimension discipline
- Simple explanation: You need to know whether data are one-dimensional or two-dimensional before using them correctly.
- Technical depth: Shape mismatches are a common source of quant coding bugs, especially in ML pipelines and portfolio analytics.
- Finance example: A weight vector and a return matrix must align properly for portfolio calculations to be correct.

## Worked Examples
- Transform a vector of prices into returns with one array expression.
- Compute portfolio returns from a 3-day by 3-asset return matrix and one weight vector.
- Compare a loop-based sum with a dot product to show they mean the same thing conceptually.

## Practice Questions With Answers
### Question: Why is vectorization useful in quant finance?
Answer: It keeps code closer to the math, reduces manual error, and scales better when data become large.

### Question: What does shape mean for an array?
Answer: Shape tells you how many rows and columns or dimensions the array has, which determines what operations are valid.

### Question: Why can shape mistakes be dangerous in finance code?
Answer: Because a mismatched operation may silently produce the wrong result, which can distort signals, risk, or portfolio calculations.

## Daily Quiz (Closed-Book)
1. Explain today's core intuition from memory.
2. Write one formula/workflow and define all symbols/steps.
3. Give one use case and one realistic failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Vectorized Return
$$r=\frac{P_{1:}}{P_{:-1}}-1$$
Plain-English interpretation: Batch return transform over arrays.
Notation check: Off-by-one index mismatches.

### Formula 2: Dot Product
$$w\cdot r=\sum_i w_i r_i$$
Plain-English interpretation: Linear weighted aggregation.
Notation check: Shape mismatch between vectors.

### Formula 3: Broadcasting Rule
$$(m\times n)\odot(n,)\rightarrow(m\times n)$$
Plain-English interpretation: Dimension-safe elementwise scaling.
Notation check: Silent broadcast along wrong axis.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Vectorized Return | Batch return transform over arrays. | Replace loop-heavy feature extraction. | Off-by-one index mismatches. |
| Dot Product | Linear weighted aggregation. | Portfolio and factor combination. | Shape mismatch between vectors. |
| Broadcasting Rule | Dimension-safe elementwise scaling. | Scale features by column constants. | Silent broadcast along wrong axis. |

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
- Design one topic-specific analysis for numpy arrays, vectorization, and speed intuition instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Build a cleaned feature table for numpy arrays, vectorization, and speed intuition and show one validation check that catches a data issue.

## Daily Interview Drill
### Q: Why do quants use NumPy instead of plain Python lists for many calculations?
A: Because NumPy arrays support faster, clearer numerical operations and map naturally to vectors and matrices used in finance.

## Reflection Question
What from numpy arrays, vectorization, and speed intuition is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
