# Week 03 Tue: Calculus intuition: slopes, derivatives, and sensitivity

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
Calculus intuition: slopes, derivatives, and sensitivity is part of real quant work inside math rebuild i: algebra, calculus intuition, probability rules, apis, and monte carlo thinking research, trading, or risk workflows.

## Learning Overview
Calculus starts becoming useful once you stop seeing the derivative as a scary symbol and start seeing it as a sensitivity measure.

In quant finance, sensitivity is everywhere: how price changes when yield changes, how option value changes when volatility changes, or how loss changes when a model parameter changes.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### Slope as rate of change
- Simple explanation: Slope tells you how much one quantity changes when another changes.
- Technical depth: The derivative captures the local rate of change of a function with respect to its input.
- Finance example: A bond price changing when yield changes is a sensitivity problem.

### Derivative as local approximation
- Simple explanation: A derivative approximates what happens for a very small change.
- Technical depth: It is the limit of the difference quotient as the input change goes to zero.
- Finance example: Option Greeks are local sensitivity measures, not full descriptions of all possible moves.

### Optimization intuition
- Simple explanation: Derivatives help locate points where a function stops increasing and may turn around.
- Technical depth: Critical points occur when the first derivative is zero or undefined, and second-derivative intuition helps assess local curvature.
- Finance example: Optimization problems in portfolio or ML settings often rely on sensitivity reasoning.

## Worked Examples
- Find the slope of a line and interpret it economically.
- Use a simple quadratic function to discuss where the derivative becomes zero.

## Practice Questions With Answers
### Question: Why are derivatives important in finance?
Answer: Because finance constantly asks how one value changes with another, which is exactly what sensitivity measures capture.

### Question: What does it mean if a derivative is positive?
Answer: It means the function is locally increasing as the input rises.

## Daily Quiz (Closed-Book)
1. Explain today's core intuition from memory.
2. Write one formula/workflow and define all symbols/steps.
3. Give one use case and one realistic failure mode.

## Interview-Ready Formula Sheet
### Formula 1: First Derivative
$$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$$
Plain-English interpretation: Instantaneous slope/sensitivity.
Notation check: Treating finite difference as exact.

### Formula 2: Second Derivative
$$f''(x)=\frac{d^2 f}{dx^2}$$
Plain-English interpretation: Curvature and local convexity.
Notation check: Ignoring nonlinearity in stressed moves.

### Formula 3: Elasticity
$$\epsilon=\frac{d y}{d x}\cdot\frac{x}{y}$$
Plain-English interpretation: Percent sensitivity ratio.
Notation check: Using at points where y\approx0.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| First Derivative | Instantaneous slope/sensitivity. | Rate sensitivity intuition for pricing. | Treating finite difference as exact. |
| Second Derivative | Curvature and local convexity. | Risk asymmetry discussions. | Ignoring nonlinearity in stressed moves. |
| Elasticity | Percent sensitivity ratio. | Compare sensitivities across scales. | Using at points where y\approx0. |

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
- Design one topic-specific analysis for calculus intuition: slopes, derivatives, and sensitivity instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Implement a small reproducible example for calculus intuition: slopes, derivatives, and sensitivity and explain one assumption that could fail in markets.

## Daily Interview Drill
### Q: How would you explain a derivative without calculus jargon?
A: It measures how sensitive one quantity is to a small change in another quantity.

## Reflection Question
What from calculus intuition: slopes, derivatives, and sensitivity is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
