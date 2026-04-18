# Week 04 Tue: Confidence intervals and hypothesis testing intuition

**Estimated time:** 8 hours

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 45 min | Confidence interval intuition. |
| Session 2 | 55 min | Hypothesis testing as evidence check. |
| Session 3 | 55 min | Common misuse in finance. |
| Session 4 | 55 min | Code interval examples. |
| Session 5 | 30 min | Interview recap. |

## Why It Matters In Quant
Confidence intervals and hypothesis testing intuition is part of real quant work inside math rebuild ii: statistics, inference, regression, optimization, and portfolio theory research, trading, or risk workflows.

## Learning Overview
Confidence intervals and tests are often memorized badly. Today the goal is not symbolic overload. The goal is to understand what level of uncertainty remains around an estimate.

That matters in finance because weak evidence can easily be mistaken for edge.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### Confidence interval intuition
- Simple explanation: A confidence interval gives a plausible range for an unknown quantity based on the sample.
- Technical depth: It reflects sampling uncertainty around an estimator under model assumptions.
- Finance example: A strategy with a positive sample mean may still have a wide interval that includes weak or negative true edge.

### Hypothesis testing
- Simple explanation: A test asks whether the evidence is strong enough to challenge a baseline claim.
- Technical depth: In many settings the baseline claim is a null hypothesis such as zero mean effect.
- Finance example: You may test whether a signal's average return differs meaningfully from zero.

### Evidence versus certainty
- Simple explanation: A test result is evidence, not proof.
- Technical depth: Statistical significance does not automatically imply economic significance or robustness.
- Finance example: A tiny effect can be statistically noticeable in a large sample yet useless after costs.

## Worked Examples
- Construct a rough interval around a sample mean.
- Explain why a narrow interval is different from a profitable strategy.

## Practice Questions With Answers
### Question: Why is statistical significance not enough in finance?
Answer: Because trading viability also depends on effect size, costs, risk, stability, and implementation realism.

### Question: What does a wide confidence interval suggest?
Answer: It suggests high uncertainty about the true parameter given the sample and assumptions.

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
Implement one notebook cell or small script focused on: confidence intervals and hypothesis testing intuition.

## Daily Interview Drill
### Q: How would you explain a confidence interval simply?
A: It is a range of plausible values for the unknown quantity based on what the sample tells us.

## Reflection Question
What from confidence intervals and hypothesis testing intuition felt truly clear, and what still needs a slower revisit?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
