# Week 03 Mon: Algebra refresher: equations, fractions, exponents, and logs

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
Algebra refresher: equations, fractions, exponents, and logs is part of real quant work inside math rebuild i: algebra, calculus intuition, probability rules, apis, and monte carlo thinking research, trading, or risk workflows.

## Learning Overview
Quant finance becomes painful very quickly if algebra feels shaky. This day is about regaining control of the symbols so later probability, optimization, and ML feel manageable.

You are not trying to be flashy here. You are building fluency with the manipulations that appear constantly in formulas, scaling laws, and growth calculations.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### Equations and rearrangement
- Simple explanation: An equation states that two expressions are equal, and rearranging means solving for the quantity you care about.
- Technical depth: Many finance formulas are useful only after algebraic rearrangement, such as isolating a rate, return, or weight.
- Finance example: If final wealth and initial wealth are known, algebra lets you solve for the return needed to get there.

### Exponents
- Simple explanation: Exponents represent repeated multiplication.
- Technical depth: Compounding, discounting, and growth models often use powers because repeated percentage changes are multiplicative.
- Finance example: Annual compounding over multiple years is naturally written with an exponent.

### Logarithms
- Simple explanation: A logarithm answers the question: what power do I raise a number to get another number?
- Technical depth: Logs are useful for turning multiplication into addition and for understanding log returns and growth rates.
- Finance example: Continuous compounding and log-return thinking both depend on logarithms.

## Worked Examples
- Solve for the return needed to grow 100 to 121 in two equal compounded steps.
- Use a log to estimate how many periods are needed to double at a given rate.

## Practice Questions With Answers
### Question: Why do exponents show up in compounding?
Answer: Because repeating the same growth factor many times is repeated multiplication, which is what exponents represent compactly.

### Question: Why are logarithms useful in quant finance?
Answer: Because they simplify multiplicative growth and support continuous-compounding and log-return interpretations.

## Daily Quiz (Closed-Book)
1. Explain today's core intuition from memory.
2. Write one formula/workflow and define all symbols/steps.
3. Give one use case and one realistic failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Expected Value
$$\mathbb{E}[X]=\sum_i p_i x_i$$
Plain-English interpretation: Probability-weighted average outcome across scenarios.
Notation check: Ignoring tail risk while focusing only on mean payoff.

### Formula 2: Bayes Rule
$$P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}$$
Plain-English interpretation: Posterior update from prior belief and evidence likelihood.
Notation check: Neglecting base rates.

### Formula 3: OLS Slope
$$\hat\beta=\frac{\sum (x_i-\bar x)(y_i-\bar y)}{\sum (x_i-\bar x)^2}$$
Plain-English interpretation: Best linear sensitivity estimate under squared-error loss.
Notation check: Assuming stability without checking residual behavior.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Expected Value | Probability-weighted average outcome across scenarios. | Evaluate expected payoff of a repeated decision rule. | Ignoring tail risk while focusing only on mean payoff. |
| Bayes Rule | Posterior update from prior belief and evidence likelihood. | Revise signal confidence after new market evidence. | Neglecting base rates. |
| OLS Slope | Best linear sensitivity estimate under squared-error loss. | Estimate directional relation between factor and return. | Assuming stability without checking residual behavior. |

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
- Design one topic-specific analysis for algebra refresher: equations, fractions, exponents, and logs instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Implement a small reproducible example for algebra refresher: equations, fractions, exponents, and logs and explain one assumption that could fail in markets.

## Daily Interview Drill
### Q: Why should a quant care about logs early?
A: Because logs appear in growth, scaling, probability, and continuous-time finance models, and they simplify many multiplicative relationships.

## Reflection Question
What from algebra refresher: equations, fractions, exponents, and logs is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
