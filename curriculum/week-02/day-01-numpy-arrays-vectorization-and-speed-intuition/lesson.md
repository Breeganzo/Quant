# Week 02 Mon: NumPy arrays, vectorization, and speed intuition

**Estimated time:** 4 hours

## Study Blocks
- Block 1 (45 min): Understand arrays, shapes, and vectorization.
- Block 2 (55 min): Compare loops with array-based finance calculations.
- Block 3 (55 min): Apply vectorization to return and portfolio work.
- Block 4 (55 min): Complete coding drills and rewrite concepts.
- Block 5 (30 min): Interview recap and error log.

## Why It Matters In Quant
NumPy arrays, vectorization, and speed intuition is part of real quant work inside data and linear algebra: numpy, pandas, visualization, diversification, and sql basics research, trading, or risk workflows.

## Learning Overview
NumPy matters because quant work becomes painful and slow if every calculation is written as a manual loop. Arrays let you express the mathematical structure directly.

The practical habit today is to stop treating market data as isolated numbers and start seeing it as organized numerical objects that can be transformed efficiently.

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

## Coding Task
Implement one notebook cell or small script focused on: numpy arrays, vectorization, and speed intuition.

## Daily Interview Drill
### Q: Why do quants use NumPy instead of plain Python lists for many calculations?
A: Because NumPy arrays support faster, clearer numerical operations and map naturally to vectors and matrices used in finance.

## Reflection Question
What from numpy arrays, vectorization, and speed intuition felt truly clear, and what still needs a slower revisit?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
