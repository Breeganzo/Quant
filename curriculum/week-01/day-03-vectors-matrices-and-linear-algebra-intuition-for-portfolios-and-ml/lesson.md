# Week 01 Wed: Vectors, matrices, and linear algebra intuition for portfolios and ML

**Estimated time:** 10 hours

## Study Blocks
- Block 1 (60 min): Concept briefing and key-assumption mapping.
- Block 2 (60 min): Formula/workflow derivation and notation rewrite.
- Block 3 (60 min): Solved real-world case walkthrough.
- Block 4 (60 min): Data checks and exploratory diagnostics.
- Block 5 (60 min): Core notebook implementation with comments.
- Block 6 (60 min): Extension coding task and sensitivity variation.
- Block 7 (60 min): Risk caveat and robustness scenario testing.
- Block 8 (60 min): Interview-style quiz answers and defense drill.
- Block 9 (60 min): Revision sprint and error-log updates.
- Block 10 (60 min): Desk memo summary and tomorrow transition plan.

## Why It Matters In Quant
Portfolio weights, factor exposures, and ML features are easiest to understand as vectors and matrices.

## Learning Overview
Linear algebra becomes easier when you stop treating it as abstract symbols and start seeing it as organized financial information.

Portfolio weights, factor exposures, feature tables, and historical return panels all become clearer once you think in vectors and matrices.

## Core Concepts
### Scalars, vectors, and matrices
- Simple explanation: A scalar is one number, a vector is an ordered list of numbers, and a matrix is a table of numbers.
- Technical depth: In quant work, vectors often store weights, returns, or factor exposures, while matrices store many observations across time or assets.
- Finance example: A portfolio of three assets with weights [0.5, 0.3, 0.2] is naturally represented as a vector.

### Dot product as weighted sum
- Simple explanation: The dot product multiplies matching entries and adds them. In finance that gives a weighted return or exposure.
- Technical depth: If w is a weight vector and r is a return vector, portfolio return is w^T r.
- Finance example: A portfolio return is just the sum of each asset's return times its portfolio weight.

### Matrices as data structures
- Simple explanation: A matrix helps store many assets over many dates or many features for many observations.
- Technical depth: An n by p matrix may represent n observations and p features for machine learning, or p assets over n dates for portfolio analytics.
- Finance example: A return matrix with rows as days and columns as assets is the standard input to covariance and optimization work.

## Worked Examples
- Weights [0.5, 0.3, 0.2] with returns [0.02, -0.01, 0.03] produce a portfolio return of 0.013 or 1.3 percent.
- A 3 by 2 feature matrix can represent 3 assets and 2 features such as momentum and volatility.
- Covariance is a matrix summary of how asset returns move together over time.

## Solved Real-World Flow
- Define one concrete desk decision that this topic informs.
- Use reproducible market data and state one data-quality check.
- Apply one core formula/workflow and report one numerical output.
- Add one risk caveat and one robustness check before trusting the conclusion.

## Practice Questions With Answers
### Question: What does a weight vector mean economically?
Answer: It tells you what fraction of the portfolio is allocated to each asset or strategy component.

### Question: Why is the dot product useful in quant work?
Answer: Because many quantities are weighted sums: portfolio return, factor exposure, and expected payoff all fit that pattern.

### Question: Why does covariance show up naturally after matrices?
Answer: Because once returns are organized in a matrix, covariance measures the pairwise co-movement across columns or assets.

## Daily Quiz (Closed-Book)
1. State the main intuition in your own words without notes.
2. Write one key formula/workflow from memory and define all symbols.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Portfolio Return
$$r_p=w^Tr$$
Plain-English interpretation: Weight-return dot product.
Notation check: Misaligned weight and return ordering.

### Formula 2: Portfolio Variance
$$\sigma_p^2=w^T\Sigma w$$
Plain-English interpretation: Total covariance-weighted risk.
Notation check: Using unstable covariance without checks.

### Formula 3: Covariance Matrix
$$\Sigma=\mathbb{E}[(r-\mu)(r-\mu)^T]$$
Plain-English interpretation: Cross-asset co-movement structure.
Notation check: Treating covariance as static across regimes.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Portfolio Return | Weight-return dot product. | Fast multi-asset return aggregation. | Misaligned weight and return ordering. |
| Portfolio Variance | Total covariance-weighted risk. | Diversification and sizing decisions. | Using unstable covariance without checks. |
| Covariance Matrix | Cross-asset co-movement structure. | Risk model construction. | Treating covariance as static across regimes. |

## Real-World Data Application
- Use curriculum/datasets/real_market_prices.csv as reproducible fallback data.
- Build one table and one chart supporting a decision.
- Document one limitation and one robustness check.

## Coding Task
Use NumPy arrays to compute 3 portfolio returns from a matrix of asset returns and a vector of weights.

## Daily Interview Drill
### Q: How would you explain a vector to a trader?
A: It is just an organized list of related numbers, like a set of portfolio weights or factor exposures.

### Q: What is the finance interpretation of a dot product?
A: It is usually a weighted sum, most commonly a portfolio return from weights and asset returns.

## Reflection Question
Can I explain a portfolio as a weighted combination of assets without getting lost in notation?

## Completion Checklist
- I completed each study block or consciously rescheduled it.
- I rewrote the key formulas or concepts from memory.
- I finished the coding lab and checked the output.
- I added at least one item to the error log if something was unclear.
- I practiced at least one interview answer aloud.
- I documented one actionable desk-style takeaway and one follow-up experiment.
