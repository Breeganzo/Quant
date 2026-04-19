# Week 03 Thu: Probability rules, random variables, and distributions

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
Probability rules, random variables, and distributions is part of real quant work inside math rebuild i: algebra, calculus intuition, probability rules, apis, and monte carlo thinking research, trading, or risk workflows.

## Learning Overview
Probability is not an optional side topic in quant finance. It is the language for uncertainty, risk, forecasting, and expected outcomes.

Today focuses on intuitive foundations rather than advanced formalism, but the goal is still technical correctness.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### Events and probabilities
- Simple explanation: An event is something that may happen, and probability measures how likely it is.
- Technical depth: Probabilities satisfy basic rules such as non-negativity, normalization, and additivity under disjoint events.
- Finance example: A positive-return day or a default event can be treated as events in a probability model.

### Random variables
- Simple explanation: A random variable assigns a number to each uncertain outcome.
- Technical depth: Returns, losses, and payoffs are often modeled as random variables in finance.
- Finance example: A one-day portfolio return is a random variable because it is not known in advance.

### Distribution thinking
- Simple explanation: A distribution describes the range of possible values and how likely they are.
- Technical depth: Good decisions in finance depend on the whole distribution, not just the average.
- Finance example: A strategy with the same average return can still be worse if it has much fatter downside tails.

## Worked Examples
- List the outcomes and probabilities of a simple trade.
- Create a toy payoff distribution and compute the expected payoff.

## Practice Questions With Answers
### Question: Why does a quant care about distributions and not only means?
Answer: Because risk, drawdown, and extreme outcomes live in the distribution's spread and tails, not only in its average.

### Question: What is a random variable in one sentence?
Answer: It is a numerical representation of an uncertain outcome.

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
- Design one topic-specific analysis for probability rules, random variables, and distributions instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Implement a small reproducible example for probability rules, random variables, and distributions and explain one assumption that could fail in markets.

## Daily Interview Drill
### Q: Why is expected value not enough by itself?
A: Because two payoffs can have the same expectation but very different risk and tail behavior.

## Reflection Question
What from probability rules, random variables, and distributions is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
