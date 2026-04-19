# Week 01 Sat: Revision, spaced repetition, and first market diary notebook

**Estimated time:** 6 hours

## Study Blocks
- Block 1 (45 min): Active recall and formula rewrite from memory.
- Block 2 (55 min): Error log deep clean and spaced repetition schedule update.
- Block 3 (50 min): Market diary with one chart and one quantitative observation.
- Block 4 (50 min): Code labs plus one extension variation on your own.
- Block 5 (60 min): Interview recap, weak-point drill, and short written memo.

## Why It Matters In Quant
Weekend revision is where short-term exposure becomes long-term memory.

## Learning Overview
Weekend work should not feel like a weak leftover. It is where consolidation happens.

Today is about building a repeatable revision system so weak points do not quietly accumulate until later quantitative topics become overwhelming.

## Core Concepts
### Spaced repetition
- Simple explanation: Review material just before you would naturally forget it.
- Technical depth: A practical sequence for weak concepts is 1 day, 3 days, 7 days, and 14 days after first exposure.
- Finance example: If compounding felt shaky on Monday, it should appear again in the review schedule instead of being assumed solved.

### Error logs
- Simple explanation: An error log records what you got wrong, why it happened, and what the corrected idea is.
- Technical depth: The goal is not to collect mistakes passively, but to convert them into future review prompts and cleaner mental models.
- Finance example: Mixing up price change and return is a conceptual error worth logging immediately because it contaminates many later topics.

### Market diary
- Simple explanation: A market diary turns passive reading into structured observation.
- Technical depth: Each entry should include instrument, driver, risk, and one numerical observation or chart comment.
- Finance example: You might note that bond yields rose, equity futures fell, and the likely link was rate expectations.

## Worked Examples
- Weak concept: standard deviation vs variance. Mistake: confusing the squared unit issue. Correction: variance is squared deviation, standard deviation is the square root and easier to interpret.
- Market diary entry: asset = S&P 500 ETF, driver = rate-sensitive growth sentiment, risk = macro surprise, numeric note = daily move and volume spike.

## Practice Questions With Answers
### Question: What should an error log entry contain besides the wrong answer?
Answer: It should contain the exact misconception, the corrected idea, and the next review date.

### Question: Why is active recall stronger than re-reading?
Answer: Because pulling an idea from memory reveals whether it is actually learned rather than merely familiar.

## Daily Quiz (Closed-Book)
1. State the main intuition in your own words without notes.
2. Write one key formula/workflow from memory and define all symbols.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Log Return
$$\ell_t=\ln\left(\frac{P_t}{P_{t-1}}\right)$$
Plain-English interpretation: Additive return representation across time.
Notation check: Mixing with simple returns without context.

### Formula 2: Annualized Volatility
$$\sigma_{ann}=\sqrt{252}\cdot\mathrm{Std}(r_t)$$
Plain-English interpretation: Daily uncertainty scaled to annual horizon.
Notation check: Mismatched frequency assumptions.

### Formula 3: Sharpe Ratio
$$S=\frac{R_{ann}-R_f}{\sigma_{ann}}$$
Plain-English interpretation: Excess return per risk unit.
Notation check: Ignoring regime instability.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Log Return | Additive return representation across time. | Multi-period analytics. | Mixing with simple returns without context. |
| Annualized Volatility | Daily uncertainty scaled to annual horizon. | Risk budgeting. | Mismatched frequency assumptions. |
| Sharpe Ratio | Excess return per risk unit. | Strategy comparison. | Ignoring regime instability. |

## Real-World Data Application
- Use curriculum/datasets/real_market_prices.csv as reproducible fallback data.
- Build one table and one chart supporting a decision.
- Document one limitation and one robustness check.

## Coding Task
Create a notebook section called 'market diary' and record one asset, one news item, one risk, and one numerical observation.

## Daily Interview Drill
### Q: How do you keep yourself from repeating the same mistakes?
A: I use an error log with scheduled reviews and I force myself to restate weak concepts from memory before re-reading notes.

## Reflection Question
What did I understand best this week, and what did I only feel like I understood?

## Completion Checklist
- I completed each study block or consciously rescheduled it.
- I rewrote the key formulas or concepts from memory.
- I finished the coding lab and checked the output.
- I added at least one item to the error log if something was unclear.
- I practiced at least one interview answer aloud.
