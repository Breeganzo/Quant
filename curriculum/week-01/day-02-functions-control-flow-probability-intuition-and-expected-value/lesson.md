# Week 01 Tue: Functions, control flow, probability intuition, and expected value

**Estimated time:** 6 hours

## Study Blocks
- Block 1 (45 min): Review Python functions and reusable finance logic.
- Block 2 (60 min): Learn control flow and payoff rules.
- Block 3 (60 min): Build probability intuition and expected value.
- Block 4 (45 min): Connect payoff asymmetry to trading setups.
- Block 5 (30 min): Code, reflect, and interview drill.

## Why It Matters In Quant
Quant code is built from reusable functions, and quant decisions often reduce to expected value under uncertainty.

## Learning Overview
Today is about two habits: writing clean reusable code and thinking in probabilities instead of stories. Both are central in quant research.

A quant is constantly turning a financial question into a function, a decision rule, or an expected payoff under uncertainty. That is why functions and expected value belong together on the same day.

## Core Concepts
### Functions as reusable research building blocks
- Simple explanation: A function is a named block of logic that you can call again with different inputs. This helps keep research clean, testable, and less error-prone.
- Technical depth: A function maps inputs to outputs. In quant work, small functions for returns, drawdowns, expected value, or signal transforms keep the pipeline modular.
- Finance example: Instead of recomputing a return formula manually in many cells, a function lets you standardize the calculation across assets.

### Control flow as rule logic
- Simple explanation: Control flow decides what the program should do under different conditions.
- Technical depth: Conditionals like if/else mirror rule-based finance logic: if a signal crosses a threshold, enter; otherwise stay flat.
- Finance example: A stop-loss or risk cap is basically a decision rule embedded in code.

### Expected value and asymmetric payoffs
- Simple explanation: Expected value is the average outcome if the same uncertain setup is repeated many times.
- Technical depth: For discrete outcomes x_i with probabilities p_i, E[X] = sum p_i x_i. A positive hit rate alone is not enough; payoff size matters.
- Finance example: A strategy can win 70 percent of the time and still lose money if the average loss is much larger than the average gain.

## Worked Examples
- A trade with 60 percent chance of +2 and 40 percent chance of -1 has expected value 0.8.
- A trade with 80 percent chance of +1 and 20 percent chance of -5 has expected value -0.2 despite a high win rate.
- A function `simple_return(buy, sell)` is a reusable way to turn prices into decisions or labels.

## Practice Questions With Answers
### Question: Why might a strategy with many winning trades still have negative expected value?
Answer: Because the losses may be much larger than the wins. Expected value depends on both probability and payoff magnitude.

### Question: What does an if/else statement represent in a trading rule?
Answer: It represents a conditional action, such as buy if a signal exceeds a threshold and otherwise do nothing or reduce exposure.

### Question: A setup has outcomes +4 with probability 0.25 and -1 with probability 0.75. What is expected value?
Answer: 0.25 * 4 + 0.75 * (-1) = 0.25.

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
Write a Python function for expected value of a discrete strategy and test it on 3 toy trading setups.

## Daily Interview Drill
### Q: How is expected value different from the most likely outcome?
A: Expected value is the average weighted outcome over many repetitions, while the most likely outcome is just the single highest-probability event.

### Q: Why do quants care about payoff asymmetry?
A: Because good trading ideas are about the full payoff distribution, not just the percentage of winning trades.

## Reflection Question
Do I naturally ask what the average payoff is, or do I get distracted by single wins and losses?

## Completion Checklist
- I completed each study block or consciously rescheduled it.
- I rewrote the key formulas or concepts from memory.
- I finished the coding lab and checked the output.
- I added at least one item to the error log if something was unclear.
- I practiced at least one interview answer aloud.
