# Week 02 Wed: Plotting and exploratory data analysis for prices and returns

**Estimated time:** 6 hours

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 45 min | Learn why plots are part of research, not decoration. |
| Session 2 | 55 min | Plot price, return, and rolling statistics. |
| Session 3 | 55 min | Interpret visual patterns carefully. |
| Session 4 | 55 min | Code charting drills. |
| Session 5 | 30 min | Interview recap and notes. |

## Why It Matters In Quant
Plotting and exploratory data analysis for prices and returns is part of real quant work inside data and linear algebra: numpy, pandas, visualization, diversification, and sql basics research, trading, or risk workflows.

## Learning Overview
Visualization is part of quantitative reasoning. A good chart can reveal a bug, an outlier, a regime change, or a structure that summary numbers missed.

The main goal today is to stop plotting mechanically and start asking what each visual tells you about the data-generating process.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### Price plots versus return plots
- Simple explanation: Prices show levels over time, while returns show changes over time.
- Technical depth: Price charts can reveal trends and regime shifts, but returns are more suitable for many statistical analyses because they are more comparable across assets.
- Finance example: A steadily rising price series may still hide unstable return volatility.

### Rolling statistics
- Simple explanation: Rolling metrics summarize how averages or volatility behave over a moving window.
- Technical depth: Rolling means and rolling standard deviations help identify local behavior, changing regimes, and volatility clustering.
- Finance example: A strategy may look stable overall while a rolling volatility chart shows hidden turbulence.

### Visual interpretation with caution
- Simple explanation: A chart is evidence, not proof.
- Technical depth: Patterns in charts can be informative but may also be driven by noise, scaling choices, or short samples.
- Finance example: Apparent mean reversion in a tiny sample may disappear out of sample.

## Worked Examples
- Plot prices, returns, and rolling volatility for one toy asset.
- Show how an outlier day is obvious in a return series but not always in a price chart.
- Compare the same data on two chart scales and discuss interpretation risk.

## Practice Questions With Answers
### Question: Why are rolling statistics useful in finance?
Answer: Because market behavior changes over time, so one full-sample average often hides local shifts in trend or risk.

### Question: Why should a quant avoid over-trusting charts?
Answer: Because visual patterns can be sample-specific, scale-dependent, or just noise.

### Question: What can a return histogram reveal?
Answer: It can reveal skew, fat tails, clustering near zero, or outliers that matter for risk and modeling.

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
Build a cleaned feature table for plotting and exploratory data analysis for prices and returns and show one validation check that catches a data issue.

## Daily Interview Drill
### Q: What is the first chart you would make for a new financial series?
A: Usually I would inspect both the price series and the return series, then add a rolling volatility view to understand stability.

## Reflection Question
What from plotting and exploratory data analysis for prices and returns is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
