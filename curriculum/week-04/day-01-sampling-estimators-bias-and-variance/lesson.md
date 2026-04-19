# Week 04 Mon: Sampling, estimators, bias, and variance

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
Sampling, estimators, bias, and variance is part of real quant work inside math rebuild ii: statistics, inference, regression, optimization, and portfolio theory research, trading, or risk workflows.

## Learning Overview
Statistics becomes far more useful once you understand that sample numbers are not truth. They are estimates produced from noisy limited data.

That mindset is essential in finance because historical samples are often short, unstable, and regime-dependent.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

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

## Daily Quiz (Closed-Book)
1. Explain today's core intuition from memory.
2. Write one formula/workflow and define all symbols/steps.
3. Give one use case and one realistic failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Sample Mean
$$\bar x=\frac{1}{n}\sum_{i=1}^n x_i$$
Plain-English interpretation: Average observed value.
Notation check: Assuming mean is robust to outliers.

### Formula 2: Sample Standard Deviation
$$s=\sqrt{\frac{1}{n-1}\sum_{i=1}^n(x_i-\bar x)^2}$$
Plain-English interpretation: Observed variability estimate.
Notation check: Comparing volatility across mismatched windows.

### Formula 3: z-Score
$$z=\frac{x-\mu}{\sigma}$$
Plain-English interpretation: Distance from mean in sigma units.
Notation check: Using unstable rolling moments.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Sample Mean | Average observed value. | Return-level baseline estimate. | Assuming mean is robust to outliers. |
| Sample Standard Deviation | Observed variability estimate. | Volatility proxy from sample returns. | Comparing volatility across mismatched windows. |
| z-Score | Distance from mean in sigma units. | Outlier and regime diagnostics. | Using unstable rolling moments. |

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
- Design one topic-specific analysis for sampling, estimators, bias, and variance instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Implement a small reproducible example for sampling, estimators, bias, and variance and explain one assumption that could fail in markets.

## Daily Interview Drill
### Q: Why are small samples dangerous in finance?
A: Because noisy estimates can look strong by chance and drive bad decisions about models, signals, or portfolios.

## Reflection Question
What from sampling, estimators, bias, and variance is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
