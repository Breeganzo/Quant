# Week 02 Sun: Mini project: compare three assets and explain diversification

**Estimated time:** 6 hours

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 20 min | Mini-project planning. |
| Session 2 | 55 min | Build comparison notebook. |
| Session 3 | 20 min | Write interpretation. |
| Session 4 | 25 min | Weekly review and interview summary. |

## Why It Matters In Quant
Mini project: compare three assets and explain diversification is part of real quant work inside data and linear algebra: numpy, pandas, visualization, diversification, and sql basics research, trading, or risk workflows.

## Learning Overview
The Week 2 mini-project turns your data skills into a simple research artifact: compare three assets and explain diversification with evidence.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### Mini-project framing
- Simple explanation: The project should connect data cleaning, return computation, correlation, and interpretation in one clean notebook.
- Technical depth: A strong beginner project shows a full analytical chain from raw table to insight, not just isolated code cells.
- Finance example: A three-asset comparison can already demonstrate why co-movement matters for portfolio thinking.

## Worked Examples
- Compare three toy assets with different volatility and correlation profiles.
- Write one paragraph on which pair looks most diversifying and why.

## Practice Questions With Answers
### Question: What makes the Week 2 project stronger than just a chart dump?
Answer: A clear question, clean data handling, an interpretable correlation result, and an honest written conclusion.

## Daily Quiz (Closed-Book)
1. Explain today's core intuition from memory.
2. Write one formula/workflow and define all symbols/steps.
3. Give one use case and one realistic failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Covariance
$$\mathrm{Cov}(X,Y)=\frac{1}{n-1}\sum_i(x_i-\bar x)(y_i-\bar y)$$
Plain-English interpretation: Joint variation around means.
Notation check: Miscaligned timestamps inflate noise.

### Formula 2: Correlation
$$\rho_{XY}=\frac{\mathrm{Cov}(X,Y)}{\sigma_X\sigma_Y}$$
Plain-English interpretation: Scale-free co-movement in [-1,1].
Notation check: Confusing correlation with causation.

### Formula 3: 2-Asset Variance
$$\sigma_p^2=w_1^2\sigma_1^2+w_2^2\sigma_2^2+2w_1w_2\rho_{12}\sigma_1\sigma_2$$
Plain-English interpretation: Risk decomposition for two-asset mix.
Notation check: Ignoring correlation regime shifts.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Covariance | Joint variation around means. | Diversification diagnostics. | Miscaligned timestamps inflate noise. |
| Correlation | Scale-free co-movement in [-1,1]. | Asset clustering and hedging checks. | Confusing correlation with causation. |
| 2-Asset Variance | Risk decomposition for two-asset mix. | Show diversification impact directly. | Ignoring correlation regime shifts. |

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
Build a cleaned feature table for mini project: compare three assets and explain diversification and show one validation check that catches a data issue.

## Daily Interview Drill
### Q: How would you describe this project in one line?
A: I built a small data-to-insight notebook showing how return co-movement affects diversification across three assets.

## Reflection Question
What from mini project: compare three assets and explain diversification is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
