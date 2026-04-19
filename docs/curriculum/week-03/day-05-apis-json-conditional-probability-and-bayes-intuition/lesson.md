# Week 03 Fri: APIs, JSON, conditional probability, and Bayes intuition

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
APIs, JSON, conditional probability, and Bayes intuition is part of real quant work inside math rebuild i: algebra, calculus intuition, probability rules, apis, and monte carlo thinking research, trading, or risk workflows.

## Learning Overview
A modern quant often pulls or inspects data from APIs, but the deeper idea today is evidence updating. Bayes intuition teaches you not to overreact to one observation without considering base rates.

That habit is useful in markets, model evaluation, and research interpretation.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### APIs and JSON
- Simple explanation: An API is a way for one program to request data from another. JSON is a common text format used to return structured data.
- Technical depth: Understanding nested structures, keys, and parsing is enough to begin inspecting API outputs in finance workflows.
- Finance example: A market-data endpoint may return timestamps, prices, and metadata in JSON format before you convert them into a table.

### Conditional probability
- Simple explanation: Conditional probability asks how likely an event is given that another event has happened.
- Technical depth: P(A|B) measures the probability of A under the condition that B is known.
- Finance example: The probability of loss given a volatility spike is a conditional question.

### Bayes intuition
- Simple explanation: Bayes updates beliefs when new evidence arrives, but it does not ignore the prior baseline.
- Technical depth: Posterior belief combines prior belief with the likelihood of the new evidence.
- Finance example: One strong signal should update your confidence, but not erase the base rate of noisy market behavior.

## Worked Examples
- Parse a toy JSON response representing daily prices.
- Use a simple Bayes-style disease-test style analogy and then connect it to noisy trading signals.

## Practice Questions With Answers
### Question: Why is Bayes intuition useful in trading research?
Answer: Because it teaches you to combine new evidence with prior uncertainty instead of overreacting to one signal or one backtest result.

### Question: What is conditional probability in simple terms?
Answer: It is the probability of one event after you already know another event has happened.

## Daily Quiz (Closed-Book)
1. Explain today's core intuition from memory.
2. Write one formula/workflow and define all symbols/steps.
3. Give one use case and one realistic failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Expected Value
$$\mathbb{E}[X]=\sum_i p_i x_i$$
Plain-English interpretation: Probability-weighted average payoff.
Notation check: Ignoring payoff asymmetry and tails.

### Formula 2: Variance
$$\mathrm{Var}(X)=\mathbb{E}[(X-\mu)^2]$$
Plain-English interpretation: Spread around expected payoff.
Notation check: Using only mean without uncertainty.

### Formula 3: Kelly Fraction (Binary)
$$f^*=\frac{bp-q}{b}$$
Plain-English interpretation: Theoretical growth-optimal bet size.
Notation check: Applying full Kelly under estimation error.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Expected Value | Probability-weighted average payoff. | Filter positive-edge trading setups. | Ignoring payoff asymmetry and tails. |
| Variance | Spread around expected payoff. | Risk-adjusted strategy comparison. | Using only mean without uncertainty. |
| Kelly Fraction (Binary) | Theoretical growth-optimal bet size. | Position-sizing intuition. | Applying full Kelly under estimation error. |

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
- Design one topic-specific analysis for apis, json, conditional probability, and bayes intuition instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Implement a small reproducible example for apis, json, conditional probability, and bayes intuition and explain one assumption that could fail in markets.

## Daily Interview Drill
### Q: Why are base rates important when interpreting signals?
A: Because rare events and noisy predictors can easily fool you if you ignore the starting probability of what you are trying to predict.

## Reflection Question
What from apis, json, conditional probability, and bayes intuition is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
