# Week 04 Tue: Confidence intervals and hypothesis testing intuition

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

## Daily Quiz (Closed-Book)
1. Explain today's core intuition from memory.
2. Write one formula/workflow and define all symbols/steps.
3. Give one use case and one realistic failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Confidence Interval (Mean)
$$\bar x \pm t_{n-1,\alpha/2}\cdot\frac{s}{\sqrt{n}}$$
Plain-English interpretation: Range of plausible mean values.
Notation check: Treating interval as probability for fixed parameter.

### Formula 2: t-Statistic
$$t=\frac{\bar x-\mu_0}{s/\sqrt{n}}$$
Plain-English interpretation: Signal-to-noise vs null mean.
Notation check: Ignoring dependence/autocorrelation.

### Formula 3: p-Value
$$p=P(T\ge |t_{obs}|\mid H_0)$$
Plain-English interpretation: Extremeness under null model.
Notation check: Confusing p with effect size.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Confidence Interval (Mean) | Range of plausible mean values. | Uncertainty-aware return estimates. | Treating interval as probability for fixed parameter. |
| t-Statistic | Signal-to-noise vs null mean. | Edge significance checks. | Ignoring dependence/autocorrelation. |
| p-Value | Extremeness under null model. | Reject/retain null decision support. | Confusing p with effect size. |

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
- Design one topic-specific analysis for confidence intervals and hypothesis testing intuition instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Implement a small reproducible example for confidence intervals and hypothesis testing intuition and explain one assumption that could fail in markets.

## Daily Interview Drill
### Q: How would you explain a confidence interval simply?
A: It is a range of plausible values for the unknown quantity based on what the sample tells us.

## Reflection Question
What from confidence intervals and hypothesis testing intuition is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
