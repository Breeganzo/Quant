# Week 02 Sat: Revision, error log, and data workflow drill

**Estimated time:** 6 hours

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 25 min | Week 2 recall from memory. |
| Session 2 | 35 min | SQL and data-cleaning drill. |
| Session 3 | 35 min | Error log and concept map. |
| Session 4 | 25 min | Interview practice. |

## Why It Matters In Quant
Revision, error log, and data workflow drill is part of real quant work inside data and linear algebra: numpy, pandas, visualization, diversification, and sql basics research, trading, or risk workflows.

## Learning Overview
This weekend block keeps Week 2 practical. Instead of learning a large new topic, you consolidate the data workflow habits that will support every later quant project.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### Revision through active data tasks
- Simple explanation: The best review is to clean, compute, and explain again without copying old work.
- Technical depth: Retrieval plus application is stronger than passive re-reading for building durable technical fluency.
- Finance example: Recomputing a correlation matrix from scratch is better review than staring at yesterday's output.

## Worked Examples
- Rewrite a simple SQL query from memory.
- Recreate a small price-cleaning pipeline without looking at notes.

## Practice Questions With Answers
### Question: What is one sign you truly understand a data workflow?
Answer: You can rebuild it cleanly from memory and explain why each step exists.

## Daily Quiz (Closed-Book)
1. Explain today's core intuition from memory.
2. Write one formula/workflow and define all symbols/steps.
3. Give one use case and one realistic failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Simple Return
$$r_t = \frac{P_t}{P_{t-1}} - 1$$
Plain-English interpretation: Relative one-period price change used for comparable analytics.
Notation check: Mixing simple and log returns in one pipeline.

### Formula 2: Covariance
$$\mathrm{Cov}(X,Y)=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar x)(y_i-\bar y)$$
Plain-English interpretation: Joint variation of two series around their means.
Notation check: Ignoring missing-value alignment before computing covariance.

### Formula 3: Correlation
$$\rho_{XY}=\frac{\mathrm{Cov}(X,Y)}{\sigma_X\sigma_Y}$$
Plain-English interpretation: Scale-free co-movement measure in [-1, 1].
Notation check: Interpreting correlation as causation.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Simple Return | Relative one-period price change used for comparable analytics. | Build aligned return tables before joins and cleaning. | Mixing simple and log returns in one pipeline. |
| Covariance | Joint variation of two series around their means. | Diversification diagnostics before portfolio construction. | Ignoring missing-value alignment before computing covariance. |
| Correlation | Scale-free co-movement measure in [-1, 1]. | Screen assets for complementary behavior. | Interpreting correlation as causation. |

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
Build a cleaned feature table for revision, error log, and data workflow drill and show one validation check that catches a data issue.

## Daily Interview Drill
### Q: What is one common data-handling mistake in quant research?
A: Misalignment across dates or assets, which can quietly contaminate results.

## Reflection Question
What from revision, error log, and data workflow drill is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
