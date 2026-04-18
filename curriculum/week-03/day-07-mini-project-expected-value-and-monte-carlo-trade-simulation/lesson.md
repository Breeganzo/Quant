# Week 03 Sun: Mini project: expected value and Monte Carlo trade simulation

**Estimated time:** 8 hours

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 20 min | Project framing. |
| Session 2 | 55 min | Monte Carlo simulation build. |
| Session 3 | 20 min | Interpretation and reflection. |
| Session 4 | 25 min | Weekly review. |

## Why It Matters In Quant
Mini project: expected value and Monte Carlo trade simulation is part of real quant work inside math rebuild i: algebra, calculus intuition, probability rules, apis, and monte carlo thinking research, trading, or risk workflows.

## Learning Overview
The Week 3 project ties math to uncertainty. A Monte Carlo notebook is one of the cleanest beginner ways to see how probability, expected value, and sampling variation interact.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### Monte Carlo intuition
- Simple explanation: Monte Carlo means simulating many possible outcomes to understand a distribution.
- Technical depth: Even when analytic answers exist, simulation helps build intuition for variability, tail risk, and the gap between expected and realized outcomes.
- Finance example: Repeatedly simulating a trading payoff shows why a positive edge still produces streaks of losses.

## Worked Examples
- Simulate 1000 paths of a simple discrete trading payoff.
- Compare the simulated sample mean with the theoretical expected value.

## Practice Questions With Answers
### Question: Why is Monte Carlo useful for beginners in quant finance?
Answer: Because it makes uncertainty concrete and shows the distribution of possible outcomes instead of only one formula.

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
Implement one notebook cell or small script focused on: mini project: expected value and monte carlo trade simulation.

## Daily Interview Drill
### Q: What does a Monte Carlo simulation help you see that a single expected value does not?
A: It shows dispersion, tail outcomes, streaks, and the range of realistic sample paths.

## Reflection Question
What from mini project: expected value and monte carlo trade simulation felt truly clear, and what still needs a slower revisit?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
