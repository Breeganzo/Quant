# Week 01 Sun: Week 1 quiz and mini project: build a simple return and risk dashboard

**Estimated time:** 4 hours

## Study Blocks
- Block 1 (45 min): Closed-book quiz and formula retrieval from memory.
- Block 2 (70 min): Mini-project build and extension with one extra metric.
- Block 3 (55 min): Interpretation write-up with failure-mode analysis.
- Block 4 (50 min): Interview practice and weekly review.

## Why It Matters In Quant
A quant portfolio grows through small finished artifacts, not only reading.

## Learning Overview
The first weekend project is deliberately simple. The point is to prove that you can move from concept to code to interpretation in one clean artifact.

You are not being judged on complexity yet. You are building the habit of finishing, documenting, and explaining quantitative work.

## Core Concepts
### Project framing
- Simple explanation: A good small project has a clear input, a few correct calculations, and a clean interpretation.
- Technical depth: The first project should include a price series, return conversion, summary statistics, cumulative wealth, and an economic comment.
- Finance example: Even a toy risk-return dashboard can demonstrate clarity, reproducibility, and communication discipline.

### Evaluation and interpretation
- Simple explanation: A chart or number becomes useful only when you explain what it means.
- Technical depth: Interpret average return, volatility, drawdown-like behavior, and data limitations rather than presenting raw outputs only.
- Finance example: If the wealth curve looks smooth but the sample is tiny, that limitation must be stated.

### Portfolio communication
- Simple explanation: Recruiters and admissions reviewers care about whether you can explain your work clearly.
- Technical depth: A short conclusion should include the objective, method, result, and one limitation or next step.
- Finance example: This is the seed of a later master's project summary or interview walkthrough.

## Worked Examples
- Compute returns from a toy 30-day price series.
- Summarize mean return, volatility, min, max, and final wealth from 100.
- Write a short note on whether the series appears smooth, noisy, or regime-changing.

## Practice Questions With Answers
### Question: What makes a beginner quant project strong even if it is simple?
Answer: Correctness, reproducibility, and clear interpretation. Simplicity is fine if the logic is sound.

### Question: What should you include in a short project conclusion?
Answer: The goal, what you computed, what the results suggest, and one limitation or next step.

## Daily Quiz (Closed-Book)
1. State the main intuition in your own words without notes.
2. Write one key formula/workflow from memory and define all symbols.
3. Give one practical quant use case and one failure mode.

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

## Real-World Data Application
- Start with yfinance (SPY, QQQ, TLT, GLD) when internet is available.
- If available, load a Robinhood-style export CSV and compare to your yfinance pull.
- Use `curriculum/datasets/real_market_prices.csv` as reproducible fallback.
- Compute log returns, annualized volatility, and Sharpe ratio for each symbol.
- Write one risk-control takeaway you would use in a real portfolio conversation.

## Coding Task
Finish the mini project notebook and write a 150-word conclusion aimed at a master's admissions reviewer.

## Daily Interview Drill
### Q: How would you present this Week 1 project in an interview?
A: I would say I built a small return-and-risk dashboard from a toy price series to demonstrate correct handling of returns, compounding, descriptive statistics, and communication. Then I would mention one limitation and what I would extend next.

## Reflection Question
If I had to show one thing from this week to a recruiter, would I be comfortable defending it?

## Completion Checklist
- I completed each study block or consciously rescheduled it.
- I rewrote the key formulas or concepts from memory.
- I finished the coding lab and checked the output.
- I added at least one item to the error log if something was unclear.
- I practiced at least one interview answer aloud.
