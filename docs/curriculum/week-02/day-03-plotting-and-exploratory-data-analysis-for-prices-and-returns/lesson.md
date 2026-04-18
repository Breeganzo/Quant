# Week 02 Wed: Plotting and exploratory data analysis for prices and returns

**Estimated time:** 8 hours

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

## Formula Organization
- Core formula and meaning
- Variable definitions and units
- Practical implementation caveat

## Extended Study (to complete a full 4-hour day)
1. Rewrite each core concept in your own words without looking at notes.
2. Add one extra worked example using different numbers or assumptions.
3. Explain one failure mode where this concept can be misapplied in trading or risk work.
4. Add one short paragraph linking this concept to your weekly project objective.

## Real-World Data Application
1. Load `curriculum/datasets/real_market_prices.csv` for SPY, QQQ, TLT, and GLD.
2. Compute daily returns and compare annualized volatility across symbols.
3. Build one cumulative growth chart and one correlation table.
4. Write one practical portfolio/risk insight from the data.

## Coding Task
Implement one notebook cell or small script focused on: plotting and exploratory data analysis for prices and returns.

## Daily Interview Drill
### Q: What is the first chart you would make for a new financial series?
A: Usually I would inspect both the price series and the return series, then add a rolling volatility view to understand stability.

## Reflection Question
What from plotting and exploratory data analysis for prices and returns felt truly clear, and what still needs a slower revisit?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
