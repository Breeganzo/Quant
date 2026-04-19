# Week 04 Wed: OLS regression intuition and interpretation

**Estimated time:** 10 hours

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 60 min | Concept briefing and assumptions map. |
| Session 2 | 60 min | Formula derivation and notation drills. |
| Session 3 | 60 min | Solved real-world case walkthrough. |
| Session 4 | 60 min | Data-quality checks and diagnostics. |
| Session 5 | 60 min | Baseline notebook implementation with comments. |
| Session 6 | 60 min | Extension coding and parameter variation. |
| Session 7 | 60 min | Risk caveat and robustness analysis. |
| Session 8 | 60 min | Interview-style quiz defense rehearsal. |
| Session 9 | 60 min | Revision and error-log correction cycle. |
| Session 10 | 60 min | Desk memo and next-day experiment plan. |

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

## Daily Quiz (Closed-Book)
1. Explain today's core intuition from memory.
2. Write one formula/workflow and define all symbols/steps.
3. Give one use case and one realistic failure mode.

## Interview-Ready Formula Sheet
### Formula 1: OLS Coefficients
$$\hat\beta=(X^TX)^{-1}X^Ty$$
Plain-English interpretation: Least-squares linear parameter estimate.
Notation check: Unstable estimates under multicollinearity.

### Formula 2: Residual
$$e_i=y_i-\hat y_i$$
Plain-English interpretation: Unexplained model component.
Notation check: Ignoring residual autocorrelation.

### Formula 3: R-Squared
$$R^2=1-\frac{\sum e_i^2}{\sum (y_i-\bar y)^2}$$
Plain-English interpretation: Variance explained fraction.
Notation check: Using R^2 alone for forecast model quality.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| OLS Coefficients | Least-squares linear parameter estimate. | Baseline factor/feature sensitivity model. | Unstable estimates under multicollinearity. |
| Residual | Unexplained model component. | Model misspecification diagnostics. | Ignoring residual autocorrelation. |
| R-Squared | Variance explained fraction. | Quick baseline fit summary. | Using R^2 alone for forecast model quality. |

## Extended Study (to complete a full 10-hour day)
1. Rewrite each core concept in your own words without looking at notes.
2. Add one extra solved case using different assumptions and compare outputs.
3. Explain one failure mode where this concept can be misapplied in trading or risk work.
4. Add one short paragraph linking this concept to your weekly project objective.
5. Propose one follow-up experiment for tomorrow and define success/failure criteria.

## Real-World Data Application
1. Use `curriculum/datasets/real_market_prices.csv` as reproducible fallback market panel.
2. Run one baseline analysis and one stressed-assumption variant.
3. Document one risk caveat and one robustness check before finalizing conclusions.

- Use yfinance first for SPY, QQQ, TLT, and GLD when internet is available.
- If available, validate against a Robinhood-style export CSV for consistency checks.
- Fall back to curriculum/datasets/real_market_prices.csv for reproducible runs.
- Design one topic-specific analysis for ols regression intuition and interpretation instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Implement a small reproducible example for ols regression intuition and interpretation and explain one assumption that could fail in markets.

## Daily Interview Drill
### Q: How would you explain regression to a non-specialist?
A: It is a way to quantify the average relationship between variables and see how much noise remains around that relationship.

## Reflection Question
What from ols regression intuition and interpretation is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
