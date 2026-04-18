# Week 01 Wed: Vectors, matrices, and linear algebra intuition for portfolios and ML

**Estimated time:** 4 hours

## Study Blocks
- Block 1 (45 min): Learn scalars, vectors, and matrices through finance objects.
- Block 2 (60 min): Understand the dot product as portfolio return.
- Block 3 (60 min): Use matrices for scenarios, features, and multiple assets.
- Block 4 (45 min): Preview covariance and diversification.
- Block 5 (30 min): Code and interview drill.

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
### Formula 1: Log Return
$$\ell_t = \ln\left(\frac{P_t}{P_{t-1}}\right)$$
Plain-English interpretation: Additive return representation over time.
Notation check: Define each symbol and unit before coding.

### Formula 2: Annualized Volatility
$$\sigma_{ann} = \sqrt{252} \cdot \mathrm{Std}(r_t)$$
Plain-English interpretation: Scales daily return uncertainty to annual horizon.
Notation check: Confirm return frequency matches annualization factor.

### Formula 3: Sharpe Ratio
$$S = \frac{R_{ann} - R_f}{\sigma_{ann}}$$
Plain-English interpretation: Excess return earned per unit of risk.
Notation check: Use consistent annualized units for return, risk-free rate, and volatility.

### Symbol Definitions
| Symbol | Meaning | Units | Example |
| --- | --- | --- | --- |
| $P_t$ | Price at time $t$ | USD/share | 110.50 |
| $r_t$ | Simple return | decimal | 0.012 |
| $R_{ann}$ | Annualized return | annualized decimal | 0.14 |
| $\sigma_{ann}$ | Annualized volatility | annualized decimal | 0.18 |
| $R_f$ | Risk-free rate | annualized decimal | 0.03 |
| $TO_t$ | Portfolio turnover | fraction of portfolio | 0.12 |

## Real-World Data Application
- Start with yfinance (SPY, QQQ, TLT, GLD) when internet is available.
- If available, load a Robinhood-style export CSV and compare to your yfinance pull.
- Use `curriculum/datasets/real_market_prices.csv` as reproducible fallback.
- Compute log returns, annualized volatility, and Sharpe ratio for each symbol.
- Write one risk-control takeaway you would use in a real portfolio conversation.

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
