# Week 04 Tue: Confidence intervals and hypothesis testing intuition

**Estimated time:** 6 hours

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 45 min | Confidence interval intuition. |
| Session 2 | 55 min | Hypothesis testing as evidence check. |
| Session 3 | 55 min | Common misuse in finance. |
| Session 4 | 55 min | Code interval examples. |
| Session 5 | 30 min | Interview recap. |

## Why It Matters In Quant
Confidence intervals and hypothesis testing intuition is part of real quant work inside math rebuild ii: statistics, inference, regression, optimization, and portfolio theory research, trading, or risk workflows.

## Learning Overview
Confidence intervals and tests are often memorized badly. Today the goal is not symbolic overload. The goal is to understand what level of uncertainty remains around an estimate.

That matters in finance because weak evidence can easily be mistaken for edge.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### Confidence interval intuition
- Simple explanation: A confidence interval gives a plausible range for an unknown quantity based on the sample.
- Technical depth: It reflects sampling uncertainty around an estimator under model assumptions.
- Finance example: A strategy with a positive sample mean may still have a wide interval that includes weak or negative true edge.

### Hypothesis testing
- Simple explanation: A test asks whether the evidence is strong enough to challenge a baseline claim.
- Technical depth: In many settings the baseline claim is a null hypothesis such as zero mean effect.
- Finance example: You may test whether a signal's average return differs meaningfully from zero.

### Evidence versus certainty
- Simple explanation: A test result is evidence, not proof.
- Technical depth: Statistical significance does not automatically imply economic significance or robustness.
- Finance example: A tiny effect can be statistically noticeable in a large sample yet useless after costs.

## Worked Examples
- Construct a rough interval around a sample mean.
- Explain why a narrow interval is different from a profitable strategy.

## Practice Questions With Answers
### Question: Why is statistical significance not enough in finance?
Answer: Because trading viability also depends on effect size, costs, risk, stability, and implementation realism.

### Question: What does a wide confidence interval suggest?
Answer: It suggests high uncertainty about the true parameter given the sample and assumptions.

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
Implement a small reproducible example for confidence intervals and hypothesis testing intuition and explain one assumption that could fail in markets.

## Daily Interview Drill
### Q: How would you explain a confidence interval simply?
A: It is a range of plausible values for the unknown quantity based on what the sample tells us.

## Reflection Question
What from confidence intervals and hypothesis testing intuition is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
