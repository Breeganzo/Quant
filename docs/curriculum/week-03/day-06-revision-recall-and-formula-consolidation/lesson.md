# Week 03 Sat: Revision, recall, and formula consolidation

**Estimated time:** 8 hours

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 25 min | Math recall drill. |
| Session 2 | 35 min | Probability and Bayes recap. |
| Session 3 | 35 min | Error log and formula rewrite. |
| Session 4 | 25 min | Interview practice. |

## Why It Matters In Quant
Revision, recall, and formula consolidation is part of real quant work inside math rebuild i: algebra, calculus intuition, probability rules, apis, and monte carlo thinking research, trading, or risk workflows.

## Learning Overview
Today is about making the new math vocabulary stick. You should be able to explain exponents, logs, derivatives, integrals, probability, and Bayes at a clean beginner level after this revision block.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### Integrated recall
- Simple explanation: The goal is to connect the week's ideas rather than memorize them in isolation.
- Technical depth: Algebra, calculus, and probability support each other in quantitative reasoning, especially when moving between formulas and interpretations.
- Finance example: A pricing or risk formula is easier to understand when you can interpret the algebra, the sensitivity, and the uncertainty together.

## Worked Examples
- Rewrite one formula from each weekday topic without notes.

## Practice Questions With Answers
### Question: What is the real sign that math is improving?
Answer: You can restate the idea in plain English, do a simple calculation, and connect it to a finance use case without freezing.

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

## Extended Study (to complete a full 4-hour day)
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
Implement one notebook cell or small script focused on: revision, recall, and formula consolidation.

## Daily Interview Drill
### Q: What math topic from this week feels most useful for quant work?
A: A good answer is whichever concept you can explain with both intuition and a finance example, such as expected value, derivative as sensitivity, or Bayes-style updating.

## Reflection Question
What from revision, recall, and formula consolidation felt truly clear, and what still needs a slower revisit?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
