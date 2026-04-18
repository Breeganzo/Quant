# Week 04 Mon: Sampling, estimators, bias, and variance

**Estimated time:** 8 hours

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 45 min | Learn samples, populations, estimators. |
| Session 2 | 55 min | Understand bias and variance intuition. |
| Session 3 | 55 min | Relate estimator quality to finance datasets. |
| Session 4 | 55 min | Code sampling examples. |
| Session 5 | 30 min | Interview recap. |

## Why It Matters In Quant
Sampling, estimators, bias, and variance is part of real quant work inside math rebuild ii: statistics, inference, regression, optimization, and portfolio theory research, trading, or risk workflows.

## Learning Overview
Statistics becomes far more useful once you understand that sample numbers are not truth. They are estimates produced from noisy limited data.

That mindset is essential in finance because historical samples are often short, unstable, and regime-dependent.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### Population versus sample
- Simple explanation: The population is the full underlying process. The sample is the subset you actually observe.
- Technical depth: In finance we almost never observe the full truth, so we rely on sample estimates of quantities like mean return or volatility.
- Finance example: Your backtest uses a historical sample, not the full future distribution of returns.

### Estimators
- Simple explanation: An estimator is a rule for turning data into an estimate.
- Technical depth: Sample mean and sample variance are estimators of underlying population moments.
- Finance example: A historical Sharpe ratio is an estimate, not a permanent property of a strategy.

### Bias and variance
- Simple explanation: Bias means systematic error; variance means how much the estimate moves around across samples.
- Technical depth: Good estimation balances systematic accuracy and stability.
- Finance example: A strategy metric from a tiny sample may have huge variance even if the estimator itself is unbiased.

## Worked Examples
- Compare two small samples from the same distribution and show different means.
- Explain why a noisy estimator can lead to overconfident portfolio choices.

## Practice Questions With Answers
### Question: Why is a sample mean not the same as the true expected return?
Answer: Because it is based on limited noisy observations and may differ materially from the underlying long-run average.

### Question: What is the intuition behind estimator variance?
Answer: If you repeated the sampling process many times, a high-variance estimator would jump around a lot from sample to sample.

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
Implement one notebook cell or small script focused on: sampling, estimators, bias, and variance.

## Daily Interview Drill
### Q: Why are small samples dangerous in finance?
A: Because noisy estimates can look strong by chance and drive bad decisions about models, signals, or portfolios.

## Reflection Question
What from sampling, estimators, bias, and variance felt truly clear, and what still needs a slower revisit?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
