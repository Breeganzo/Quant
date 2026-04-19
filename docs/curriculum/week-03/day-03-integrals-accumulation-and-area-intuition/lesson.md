# Week 03 Wed: Integrals, accumulation, and area intuition

**Estimated time:** 6 hours

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 45 min | Understand accumulation and area intuition. |
| Session 2 | 55 min | Relate integrals to totals and averages. |
| Session 3 | 55 min | Connect accumulation to finance. |
| Session 4 | 55 min | Code approximation examples. |
| Session 5 | 30 min | Interview recap. |

## Why It Matters In Quant
Integrals, accumulation, and area intuition is part of real quant work inside math rebuild i: algebra, calculus intuition, probability rules, apis, and monte carlo thinking research, trading, or risk workflows.

## Learning Overview
Integrals are easier to digest when seen as accumulation rather than as abstract notation.

In finance, accumulation ideas appear in continuous-time reasoning, total exposure, and moving from local change to total effect.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### Integral as accumulation
- Simple explanation: An integral adds up many tiny pieces to get a total.
- Technical depth: Definite integrals can be viewed as limits of sums over small intervals.
- Finance example: Accumulating a continuously changing growth rate over time leads naturally to integral thinking.

### Area intuition
- Simple explanation: The area under a curve is one geometric way to understand a definite integral.
- Technical depth: This geometric picture is useful even when the interpretation is not literally area.
- Finance example: If instantaneous returns or rates vary through time, the total effect is an accumulated quantity.

### Local change to total effect
- Simple explanation: If the derivative tells you local change, the integral helps recover the total accumulated change.
- Technical depth: Differentiation and integration are linked by the fundamental theorem of calculus.
- Finance example: Sensitivity and accumulation are two sides of the same modeling story.

## Worked Examples
- Approximate the area under a simple curve with rectangles.
- Interpret a constant rate over time as repeated accumulation.

## Practice Questions With Answers
### Question: What is the simplest intuition for an integral?
Answer: It adds up many tiny contributions to get a total accumulated quantity.

### Question: How is integration related to finance?
Answer: Finance often studies quantities that evolve continuously, so accumulation over time naturally leads to integral thinking.

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
Implement a small reproducible example for integrals, accumulation, and area intuition and explain one assumption that could fail in markets.

## Daily Interview Drill
### Q: How would you explain the link between derivatives and integrals?
A: Derivatives describe local change, while integrals accumulate those local changes into a total effect.

## Reflection Question
What from integrals, accumulation, and area intuition is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
