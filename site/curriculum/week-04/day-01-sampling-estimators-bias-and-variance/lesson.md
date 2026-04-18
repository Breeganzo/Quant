# Week 04 Mon: Sampling, estimators, bias, and variance

**Estimated time:** 4 hours

## Study Blocks
- Block 1 (45 min): Learn samples, populations, estimators.
- Block 2 (55 min): Understand bias and variance intuition.
- Block 3 (55 min): Relate estimator quality to finance datasets.
- Block 4 (55 min): Code sampling examples.
- Block 5 (30 min): Interview recap.

## Why It Matters In Quant
Sampling, estimators, bias, and variance is part of real quant work inside math rebuild ii: statistics, inference, regression, optimization, and portfolio theory research, trading, or risk workflows.

## Learning Overview
Statistics becomes far more useful once you understand that sample numbers are not truth. They are estimates produced from noisy limited data.

That mindset is essential in finance because historical samples are often short, unstable, and regime-dependent.

## Core Concepts
### Population versus sample
- Simple explanation: The population is the full underlying process. The sample is the subset you actually observe.
- Technical depth: In finance we almost never observe the full truth, so we rely on sample estimates of quantities like mean return or volatility.
- Finance example: Your backtest uses a historical sample, not the full future distribution of returns.

### Estimators
- Simple explanation: An estimator is a rule for turning data into an estimate.
- Technical depth: Sample mean and sample variance are estimators of underlying population moments.
- Finance example: A historical Sharpe ratio is an estimate, not a permanent property of a strategy.

### Bias and variance
- Simple explanation: Bias means systematic error; variance means how much the estimate moves around across samples.
- Technical depth: Good estimation balances systematic accuracy and stability.
- Finance example: A strategy metric from a tiny sample may have huge variance even if the estimator itself is unbiased.

## Worked Examples
- Compare two small samples from the same distribution and show different means.
- Explain why a noisy estimator can lead to overconfident portfolio choices.

## Practice Questions With Answers
### Question: Why is a sample mean not the same as the true expected return?
Answer: Because it is based on limited noisy observations and may differ materially from the underlying long-run average.

### Question: What is the intuition behind estimator variance?
Answer: If you repeated the sampling process many times, a high-variance estimator would jump around a lot from sample to sample.

## Coding Task
Implement one notebook cell or small script focused on: sampling, estimators, bias, and variance.

## Daily Interview Drill
### Q: Why are small samples dangerous in finance?
A: Because noisy estimates can look strong by chance and drive bad decisions about models, signals, or portfolios.

## Reflection Question
What from sampling, estimators, bias, and variance felt truly clear, and what still needs a slower revisit?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
