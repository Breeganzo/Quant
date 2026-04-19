# Week 03 Tue: Calculus intuition: slopes, derivatives, and sensitivity

**Estimated time:** 6 hours

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 45 min | Learn slope intuition. |
| Session 2 | 55 min | Understand derivatives as sensitivity. |
| Session 3 | 55 min | Connect derivatives to finance and optimization. |
| Session 4 | 55 min | Code slope examples. |
| Session 5 | 30 min | Interview recap. |

## Why It Matters In Quant
Calculus intuition: slopes, derivatives, and sensitivity is part of real quant work inside math rebuild i: algebra, calculus intuition, probability rules, apis, and monte carlo thinking research, trading, or risk workflows.

## Learning Overview
Calculus starts becoming useful once you stop seeing the derivative as a scary symbol and start seeing it as a sensitivity measure.

In quant finance, sensitivity is everywhere: how price changes when yield changes, how option value changes when volatility changes, or how loss changes when a model parameter changes.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### Slope as rate of change
- Simple explanation: Slope tells you how much one quantity changes when another changes.
- Technical depth: The derivative captures the local rate of change of a function with respect to its input.
- Finance example: A bond price changing when yield changes is a sensitivity problem.

### Derivative as local approximation
- Simple explanation: A derivative approximates what happens for a very small change.
- Technical depth: It is the limit of the difference quotient as the input change goes to zero.
- Finance example: Option Greeks are local sensitivity measures, not full descriptions of all possible moves.

### Optimization intuition
- Simple explanation: Derivatives help locate points where a function stops increasing and may turn around.
- Technical depth: Critical points occur when the first derivative is zero or undefined, and second-derivative intuition helps assess local curvature.
- Finance example: Optimization problems in portfolio or ML settings often rely on sensitivity reasoning.

## Worked Examples
- Find the slope of a line and interpret it economically.
- Use a simple quadratic function to discuss where the derivative becomes zero.

## Practice Questions With Answers
### Question: Why are derivatives important in finance?
Answer: Because finance constantly asks how one value changes with another, which is exactly what sensitivity measures capture.

### Question: What does it mean if a derivative is positive?
Answer: It means the function is locally increasing as the input rises.

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
Implement a small reproducible example for calculus intuition: slopes, derivatives, and sensitivity and explain one assumption that could fail in markets.

## Daily Interview Drill
### Q: How would you explain a derivative without calculus jargon?
A: It measures how sensitive one quantity is to a small change in another quantity.

## Reflection Question
What from calculus intuition: slopes, derivatives, and sensitivity is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
