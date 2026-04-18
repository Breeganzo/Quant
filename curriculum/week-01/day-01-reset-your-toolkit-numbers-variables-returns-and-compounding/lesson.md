# Week 01 Mon: Reset your toolkit: numbers, variables, returns, and compounding

**Estimated time:** 4 hours

## Study Blocks
- Block 1 (45 min): Reset notation: prices, returns, percentages, and variables.
- Block 2 (60 min): Learn simple return, gross return, and compounding intuition.
- Block 3 (45 min): Work through hand-calculated examples and common traps.
- Block 4 (60 min): Implement returns and wealth paths in Python and pandas.
- Block 5 (30 min): Practice, reflect, and do a short interview drill.

## Why It Matters In Quant
Quants constantly translate market moves into numbers. If returns and compounding are shaky, every later topic like portfolio optimization, forecasting, and risk measurement becomes confusing.

## Learning Overview
This day rebuilds the language of quantitative finance from the ground up. Before models, factors, or machine learning, you need a precise way to describe how money changes over time.

The main habit to build is to stop thinking only in absolute price differences and start thinking in relative changes, wealth paths, and compounding. That shift is foundational for backtesting, portfolio tracking, and risk reporting.

## Core Concepts
### Price change versus return
- Simple explanation: If a stock moves from 100 to 105, the price change is 5, but the return is 5 divided by 100, which is 5 percent. Returns let us compare moves across assets with different price levels.
- Technical depth: For a one-period simple return, use r_t = P_t / P_(t-1) - 1. The gross return is 1 + r_t = P_t / P_(t-1).
- Finance example: A 5-point move means something very different for a stock priced at 20 than for a stock priced at 500. Returns normalize that difference.

### Compounding and the wealth path
- Simple explanation: Once your capital changes, the next day's gain or loss applies to the new amount, not the old amount. That is why growth is multiplicative.
- Technical depth: If wealth starts at W_0, then after returns r_1, r_2, ..., r_t, wealth is W_t = W_0 * product(1 + r_i).
- Finance example: A loss of 50 percent requires a later gain of 100 percent just to get back to the starting point.

### Why arithmetic intuition can mislead
- Simple explanation: A gain of 10 percent and a loss of 10 percent do not cancel out because the second move happens on a different base.
- Technical depth: The path 100 -> 110 -> 99 gives returns of +10 percent and -10 percent, but total wealth falls by 1 percent.
- Finance example: This is why traders care about drawdowns and recovery periods, not just average daily returns.

## Worked Examples
- Asset A: 50 -> 55. Simple return = 10 percent.
- Portfolio capital: 1000 -> after +10 percent becomes 1100 -> after -5 percent becomes 1045. Net return is not 5 percent; it is 4.5 percent.
- Path dependency: +20 percent then -20 percent produces 96 from 100, not 100.

## Practice Questions With Answers
### Question: A stock moves from 80 to 92. What is the simple return?
Answer: Return = 92 / 80 - 1 = 0.15, so 15 percent.

### Question: You start with 2000 and earn returns of 5 percent, 3 percent, and -2 percent. What is final wealth?
Answer: 2000 * 1.05 * 1.03 * 0.98 = 2119.32.

### Question: Why is a 30 percent loss harder to recover from than it first sounds?
Answer: Because the required recovery is measured from the reduced base. After falling from 100 to 70, you need 30 / 70 = 42.86 percent to get back to 100.

## Daily Quiz (Closed-Book)
1. State the main intuition in your own words without notes.
2. Write one key formula/workflow from memory and define all symbols.
3. Give one practical quant use case and one failure mode.

## Formula Organization
- Core formula: rewrite and annotate each symbol.
- Related formula: connect it to variance/risk/return interpretation.
- Implementation note: list one coding pitfall to avoid.

## Real-World Data Application
- Open `curriculum/datasets/real_market_prices.csv` and filter SPY, QQQ, TLT, and GLD.
- Compute daily returns and annualized volatility for each symbol.
- Compare cumulative growth from a common starting value.
- Write one risk-control takeaway you would use in a real portfolio conversation.

## Coding Task
In Python, create a list of 5 prices, convert them into returns, and calculate final wealth from an initial capital of 1000.

## Daily Interview Drill
### Q: Why do quants work with returns instead of raw prices?
A: Returns make moves comparable across assets and line up naturally with portfolio aggregation, statistics, and risk analysis.

### Q: What does compounding change in performance analysis?
A: It makes the order of gains and losses matter because capital evolves multiplicatively over time.

## Reflection Question
Did I understand returns as changes in relative terms, or was I still thinking only in absolute rupees or dollars?

## Completion Checklist
- I completed each study block or consciously rescheduled it.
- I rewrote the key formulas or concepts from memory.
- I finished the coding lab and checked the output.
- I added at least one item to the error log if something was unclear.
- I practiced at least one interview answer aloud.
