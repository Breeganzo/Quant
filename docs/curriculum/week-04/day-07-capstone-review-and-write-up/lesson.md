# Week 04 Sun: Capstone review and write-up

**Estimated time:** 10 hours

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 60 min | Closed-book retrieval and formula rewrite. |
| Session 2 | 60 min | Weak-topic reteach with solved examples. |
| Session 3 | 60 min | Data refresh and diagnostics rerun. |
| Session 4 | 60 min | Notebook baseline pass. |
| Session 5 | 60 min | Notebook extension and stress tests. |
| Session 6 | 60 min | Project build increment. |
| Session 7 | 60 min | Project risk caveat and robustness note. |
| Session 8 | 60 min | Interview rehearsal under time limit. |
| Session 9 | 60 min | Revision board confidence rescoring. |
| Session 10 | 60 min | Weekly transition memo and gap plan. |

## Why It Matters In Quant
Capstone review and write-up is part of real quant work inside math rebuild ii: statistics, inference, regression, optimization, and portfolio theory research, trading, or risk workflows.

## Learning Overview
Month 1 finishes with communication, not just calculation. The capstone becomes valuable only when you can explain what it did, what it found, and what its limits are.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### Communication as quant skill
- Simple explanation: A good quant result must be understandable to another human.
- Technical depth: Professional research output includes methodology, result, risk, and limitation communication.
- Finance example: A PM or admissions reviewer cares about whether your logic is clear and defensible, not just whether your notebook runs.

## Worked Examples
- Write a short conclusion comparing two portfolios and naming one limitation.

## Practice Questions With Answers
### Question: What should a capstone conclusion include?
Answer: The question, method, main result, and at least one limitation or next step.

## Daily Quiz (Closed-Book)
1. Explain today's core intuition from memory.
2. Write one formula/workflow and define all symbols/steps.
3. Give one use case and one realistic failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Net Return
$$r_t^{net}=r_t^{gross}-cost_t$$
Plain-English interpretation: Performance after implementation frictions.
Notation check: Presenting gross-only metrics.

### Formula 2: Out-of-Sample RMSE
$$RMSE_{OOS}=\sqrt{\frac{1}{n}\sum_i(\hat y_i-y_i)^2}$$
Plain-English interpretation: Forecast quality on unseen data.
Notation check: Leaking test data into tuning.

### Formula 3: Max Drawdown
$$MDD=\min_t\left(\frac{W_t}{\max_{s\le t}W_s}-1\right)$$
Plain-English interpretation: Worst path-dependent loss.
Notation check: Reporting return with no drawdown context.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Net Return | Performance after implementation frictions. | Final report realism. | Presenting gross-only metrics. |
| Out-of-Sample RMSE | Forecast quality on unseen data. | Capstone model comparison. | Leaking test data into tuning. |
| Max Drawdown | Worst path-dependent loss. | Risk defense in presentations. | Reporting return with no drawdown context. |

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
- Design one topic-specific analysis for capstone review and write-up instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Implement a small reproducible example for capstone review and write-up and explain one assumption that could fail in markets.

## Daily Interview Drill
### Q: What limitation would you mention first for a beginner portfolio study?
A: Usually the small sample size, simplified assumptions, and lack of real transaction costs or broader asset history.

## Reflection Question
What from capstone review and write-up is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
