# Week 04 Sat: Capstone build day

**Estimated time:** 8 hours

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 20 min | Capstone plan. |
| Session 2 | 55 min | Implement exploratory asset-allocation notebook. |
| Session 3 | 20 min | Interpret results. |
| Session 4 | 25 min | Interview practice. |

## Why It Matters In Quant
Capstone build day is part of real quant work inside math rebuild ii: statistics, inference, regression, optimization, and portfolio theory research, trading, or risk workflows.

## Learning Overview
This is the first proper Month 1 capstone build session. The job is not to create a perfect optimizer, but to combine returns, volatility, correlation, and portfolio logic into one coherent piece of work.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### Capstone integration
- Simple explanation: A capstone should combine the week's ideas rather than repeating one isolated topic.
- Technical depth: This one brings together descriptive statistics, covariance, and simple portfolio comparison.
- Finance example: A small asset-allocation study mirrors the early structure of real portfolio research.

## Worked Examples
- Test a few candidate weights and compare return-risk trade-offs.

## Practice Questions With Answers
### Question: What makes a capstone useful for applications?
Answer: It shows you can frame a question, implement analysis, interpret results, and communicate limitations.

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
Implement one notebook cell or small script focused on: capstone build day.

## Daily Interview Drill
### Q: How would you describe this capstone briefly?
A: I built an exploratory asset-allocation study comparing a few simple portfolios using return, volatility, and correlation logic.

## Reflection Question
What from capstone build day felt truly clear, and what still needs a slower revisit?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
