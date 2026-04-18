# Week 04 Wed: OLS regression intuition and interpretation

**Estimated time:** 4 hours

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 45 min | Regression intuition. |
| Session 2 | 55 min | Slope, intercept, residuals, fit quality. |
| Session 3 | 55 min | Interpret coefficients economically. |
| Session 4 | 55 min | Code a tiny OLS example. |
| Session 5 | 30 min | Interview recap. |

## Why It Matters In Quant
OLS regression intuition and interpretation is part of real quant work inside math rebuild ii: statistics, inference, regression, optimization, and portfolio theory research, trading, or risk workflows.

## Learning Overview
Regression is a foundational bridge between statistics, ML, and finance. It gives you a language for relationships, sensitivity, and residual noise.

Today is about interpreting regression meaningfully, not memorizing a formula without context.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### Regression as best-fit relationship
- Simple explanation: Regression tries to describe how one variable changes on average with another.
- Technical depth: OLS chooses coefficients that minimize the sum of squared residuals.
- Finance example: You might regress an asset's returns on market returns to estimate beta-like sensitivity.

### Residuals
- Simple explanation: Residuals are what the model did not explain.
- Technical depth: They are the differences between observed values and fitted values.
- Finance example: Large residuals may suggest omitted drivers, noise, or regime changes.

### Interpretation over blind fitting
- Simple explanation: A coefficient means something only if the setup makes economic sense.
- Technical depth: Regression can quantify a relationship, but not every estimated relationship is causal or stable.
- Finance example: A positive regression coefficient on a short sample is not automatically a tradable edge.

## Worked Examples
- Fit a line to market and asset returns.
- Interpret the slope as sensitivity and the residuals as unexplained movement.

## Practice Questions With Answers
### Question: What does the slope coefficient mean in a simple regression?
Answer: It represents the expected change in the target for a one-unit change in the input, on average within the sample.

### Question: Why are residuals useful?
Answer: They show what the model failed to explain and can reveal noise, missing structure, or instability.

## Extended Study (to complete a full 4-hour day)
1. Rewrite each core concept in your own words without looking at notes.
2. Add one extra worked example using different numbers or assumptions.
3. Explain one failure mode where this concept can be misapplied in trading or risk work.
4. Add one short paragraph linking this concept to your weekly project objective.

## Coding Task
Implement one notebook cell or small script focused on: ols regression intuition and interpretation.

## Daily Interview Drill
### Q: How would you explain regression to a non-specialist?
A: It is a way to quantify the average relationship between variables and see how much noise remains around that relationship.

## Reflection Question
What from ols regression intuition and interpretation felt truly clear, and what still needs a slower revisit?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
