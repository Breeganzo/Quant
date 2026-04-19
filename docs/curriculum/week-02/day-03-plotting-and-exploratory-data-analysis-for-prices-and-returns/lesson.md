# Week 02 Wed: Plotting and exploratory data analysis for prices and returns

**Estimated time:** 10 hours

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 60 min | Concept briefing and assumptions map. |
| Session 2 | 60 min | Formula derivation and notation drills. |
| Session 3 | 60 min | Solved real-world case walkthrough. |
| Session 4 | 60 min | Data-quality checks and diagnostics. |
| Session 5 | 60 min | Baseline notebook implementation with comments. |
| Session 6 | 60 min | Extension coding and parameter variation. |
| Session 7 | 60 min | Risk caveat and robustness analysis. |
| Session 8 | 60 min | Interview-style quiz defense rehearsal. |
| Session 9 | 60 min | Revision and error-log correction cycle. |
| Session 10 | 60 min | Desk memo and next-day experiment plan. |

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
### Formula 1: Simple Return
$$r_t=\frac{P_t}{P_{t-1}}-1$$
Plain-English interpretation: One-period relative price change.
Notation check: Comparing assets without handling frequency or missing days.

### Formula 2: Log Return
$$\ell_t=\ln\left(\frac{P_t}{P_{t-1}}\right)$$
Plain-English interpretation: Additive return representation across time.
Notation check: Mixing log and simple returns in one report.

### Formula 3: Compounded Wealth
$$W_T=W_0\prod_{t=1}^{T}(1+r_t)$$
Plain-English interpretation: Capital path under sequential returns.
Notation check: Averaging returns instead of compounding them.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Simple Return | One-period relative price change. | Baseline daily performance attribution. | Comparing assets without handling frequency or missing days. |
| Log Return | Additive return representation across time. | Multi-period return decomposition. | Mixing log and simple returns in one report. |
| Compounded Wealth | Capital path under sequential returns. | Backtest equity-curve reconstruction. | Averaging returns instead of compounding them. |

## Extended Study (to complete a full 10-hour day)
1. Rewrite each core concept in your own words without looking at notes.
2. Add one extra solved case using different assumptions and compare outputs.
3. Explain one failure mode where this concept can be misapplied in trading or risk work.
4. Add one short paragraph linking this concept to your weekly project objective.
5. Propose one follow-up experiment for tomorrow and define success/failure criteria.

## Real-World Data Application
1. Use `curriculum/datasets/real_market_prices.csv` as reproducible fallback market panel.
2. Run one baseline analysis and one stressed-assumption variant.
3. Document one risk caveat and one robustness check before finalizing conclusions.

- Use yfinance first for SPY, QQQ, TLT, and GLD when internet is available.
- If available, validate against a Robinhood-style export CSV for consistency checks.
- Fall back to curriculum/datasets/real_market_prices.csv for reproducible runs.
- Design one topic-specific analysis for plotting and exploratory data analysis for prices and returns instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

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
