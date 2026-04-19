# Week 02 Tue: pandas DataFrames, indexing, joins, and missing values

**Estimated time:** 6 hours

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 45 min | Learn DataFrame structure and indexing. |
| Session 2 | 55 min | Clean missing values and basic data problems. |
| Session 3 | 55 min | Join and reshape simple market tables. |
| Session 4 | 55 min | Code drills and small cleaning exercises. |
| Session 5 | 30 min | Reflection and interview recap. |

## Why It Matters In Quant
pandas DataFrames, indexing, joins, and missing values is part of real quant work inside data and linear algebra: numpy, pandas, visualization, diversification, and sql basics research, trading, or risk workflows.

## Learning Overview
Most quant work is not glamorous modeling. A large part is understanding tables, cleaning messy inputs, and making sure what you model is actually what you think you are modeling.

Today is about becoming comfortable with pandas as the day-to-day language of practical financial data handling.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### DataFrames as structured market tables
- Simple explanation: A DataFrame is like a spreadsheet with labeled rows and columns.
- Technical depth: pandas DataFrames provide indexing, grouping, joining, missing-value handling, and time-series functionality used heavily in research workflows.
- Finance example: You might store dates, prices, returns, sectors, and volumes in one table and transform it before modeling.

### Missing values and bad data
- Simple explanation: Real market data often has gaps, duplicate records, or inconsistent labels.
- Technical depth: Cleaning decisions matter because dropped rows, forward fills, or wrong joins can change backtest outputs.
- Finance example: A missing price on one date can distort return calculations unless handled explicitly.

### Joins and alignment
- Simple explanation: A join combines tables using a common key such as date or ticker.
- Technical depth: Misaligned joins are a common source of subtle leakage and incorrect analysis in finance data pipelines.
- Finance example: Joining returns with a factor table on the wrong date can accidentally use future information.

## Worked Examples
- Build a price table with a missing value and inspect how `pct_change` behaves.
- Join a price table with a sector table and explain why index alignment matters.
- Compare dropping missing data with a fill strategy and note the trade-off.

## Practice Questions With Answers
### Question: Why is missing data dangerous in return calculations?
Answer: Because missing values can create false jumps, incorrect percentage changes, or unintended row drops if handled casually.

### Question: What is one common join mistake in finance data?
Answer: Joining on the wrong date key and accidentally aligning today's feature with tomorrow's outcome.

### Question: Why do labels matter in pandas?
Answer: Because labeled indices and columns make transformations safer and easier to interpret than raw position-only arrays.

## Daily Quiz (Closed-Book)
1. Explain today's core intuition from memory.
2. Write one formula/workflow and define all symbols/steps.
3. Give one use case and one realistic failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Missingness Rate
$$MR=\frac{\#\text{missing cells}}{\#\text{total cells}}$$
Plain-English interpretation: Fraction of absent observations.
Notation check: Forward-filling without documenting bias.

### Formula 2: Join Cardinality
$$Rows_{out}=Rows_A\bowtie Rows_B$$
Plain-English interpretation: Row-growth behavior after merge.
Notation check: Assuming one-to-one keys without checks.

### Formula 3: Coverage by Symbol
$$Coverage_i=\frac{\#dates_i}{\#dates_{max}}$$
Plain-English interpretation: Relative data history length per asset.
Notation check: Comparing assets with unequal history.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Missingness Rate | Fraction of absent observations. | Data quality monitoring before modeling. | Forward-filling without documenting bias. |
| Join Cardinality | Row-growth behavior after merge. | Prevent duplicate explosion in joins. | Assuming one-to-one keys without checks. |
| Coverage by Symbol | Relative data history length per asset. | Universe eligibility filtering. | Comparing assets with unequal history. |

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
Build a cleaned feature table for pandas dataframes, indexing, joins, and missing values and show one validation check that catches a data issue.

## Daily Interview Drill
### Q: What is the difference between a DataFrame and a NumPy array in practice?
A: A DataFrame has labels and richer data-wrangling features, while a NumPy array is more lightweight and numerically focused.

## Reflection Question
What from pandas dataframes, indexing, joins, and missing values is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
