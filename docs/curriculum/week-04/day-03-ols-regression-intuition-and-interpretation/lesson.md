# Week 04 Wed: OLS regression intuition and interpretation

**Estimated time:** 6 hours

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 45 min | Regression intuition. |
| Session 2 | 55 min | Slope, intercept, residuals, fit quality. |
| Session 3 | 55 min | Interpret coefficients economically. |
| Session 4 | 55 min | Code a tiny OLS example. |
| Session 5 | 30 min | Interview recap. |

## Why It Matters In Quant
OLS regression intuition and interpretation is part of real quant work inside math rebuild ii: statistics, inference, regression, optimization, and portfolio theory research, trading, or risk workflows.

## Learning Overview
Regression is a foundational bridge between statistics, ML, and finance. It gives you a language for relationships, sensitivity, and residual noise.

Today is about interpreting regression meaningfully, not memorizing a formula without context.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### Regression as best-fit relationship
- Simple explanation: Regression tries to describe how one variable changes on average with another.
- Technical depth: OLS chooses coefficients that minimize the sum of squared residuals.
- Finance example: You might regress an asset's returns on market returns to estimate beta-like sensitivity.

### Residuals
- Simple explanation: Residuals are what the model did not explain.
- Technical depth: They are the differences between observed values and fitted values.
- Finance example: Large residuals may suggest omitted drivers, noise, or regime changes.

### Interpretation over blind fitting
- Simple explanation: A coefficient means something only if the setup makes economic sense.
- Technical depth: Regression can quantify a relationship, but not every estimated relationship is causal or stable.
- Finance example: A positive regression coefficient on a short sample is not automatically a tradable edge.

## Worked Examples
- Fit a line to market and asset returns.
- Interpret the slope as sensitivity and the residuals as unexplained movement.

## Practice Questions With Answers
### Question: What does the slope coefficient mean in a simple regression?
Answer: It represents the expected change in the target for a one-unit change in the input, on average within the sample.

### Question: Why are residuals useful?
Answer: They show what the model failed to explain and can reveal noise, missing structure, or instability.

## Daily Quiz (Closed-Book)
1. Explain today's core intuition from memory.
2. Write one formula/workflow and define all symbols/steps.
3. Give one use case and one realistic failure mode.

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
Implement a small reproducible example for ols regression intuition and interpretation and explain one assumption that could fail in markets.

## Daily Interview Drill
### Q: How would you explain regression to a non-specialist?
A: It is a way to quantify the average relationship between variables and see how much noise remains around that relationship.

## Reflection Question
What from ols regression intuition and interpretation is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
