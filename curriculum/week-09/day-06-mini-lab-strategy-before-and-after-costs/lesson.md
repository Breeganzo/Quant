# Week 09 Sat: Mini lab: strategy before and after costs

**Estimated time:** 10 hours

## Daily Mission
This day belongs to the week theme "Finance Core I: market microstructure, execution, slippage, and transaction costs". Your objective is to understand, apply, and communicate mini lab: strategy before and after costs in a way a quant team would trust.

## Continuity Map
- Previous day focus: Turnover, holding period, and capacity intuition
- Today's focus: Mini lab: strategy before and after costs
- Next day bridge: Review and trading diary

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 60 min | Closed-book recall and formula rewrite. |
| Session 2 | 60 min | Weak-topic reteach with solved examples. |
| Session 3 | 60 min | Data refresh and exploratory diagnostics rerun. |
| Session 4 | 60 min | Notebook baseline implementation pass. |
| Session 5 | 60 min | Notebook extension challenge and parameter stress tests. |
| Session 6 | 60 min | Weekly mini-project or capstone build increment. |
| Session 7 | 60 min | Mini-project review and risk caveat documentation. |
| Session 8 | 60 min | Interview rehearsal with timed answer structure. |
| Session 9 | 60 min | Revision board updates and confidence rescoring. |
| Session 10 | 60 min | Weekly wrap memo and next-week transition planning. |

## Why It Matters In Quant
Mini lab: strategy before and after costs is part of real quant work inside finance core i: market microstructure, execution, slippage, and transaction costs research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Reference price between best bid and ask.
2. Technical frame: Build mini lab: strategy before and after costs from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: Mid Price, Effective Spread, Turnover).
3. Market interpretation: Execution quality benchmarking.. Run one compact, reproducible example for mini lab: strategy before and after costs and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Comparing fills to stale mid prices.

## Real-World Solved Case (Step-by-Step)
- Step 1 (Problem framing): Define the desk decision and why mini lab: strategy before and after costs is relevant.
- Step 2 (Data and assumptions): Use `curriculum/datasets/real_market_prices.csv`, state one data-quality assumption and one regime-risk assumption.
- Step 3 (Method): Apply Mid Price or a directly related workflow on a reproducible sample.
- Step 4 (Result): Report one quantitative output and one practical interpretation for research, trading, or risk.
- Step 5 (Caveat): Document one failure mode: Comparing fills to stale mid prices.
- Step 6 (Robustness): Re-run with one alternate window, parameter, or benchmark and compare conclusions.

## Deep Study Prompts (10-Hour Track)
- What assumption is easiest to violate in live markets and how would you detect that early?
- Which output would you show a PM or risk manager first, and why?
- Which alternate explanation could produce similar numbers but imply a different action?
- What metric could improve while hidden risk still worsens?

## Practice Problems
- Explain mini lab: strategy before and after costs in one paragraph without jargon.
- Write down one topic-specific formula or workflow for mini lab: strategy before and after costs from memory.
- Connect mini lab: strategy before and after costs to one realistic trading, portfolio, risk, or research decision.

## 10-Hour Deliverables
- Produce 2-3 pages of notes with intuition, formal definitions, formulas, and one solved real-world case.
- Complete all notebook labs plus one extension experiment with changed assumptions or parameters.
- Add at least two error-log entries with specific correction rules and review dates.
- Record a 2-minute spoken explanation and a 1-minute risk caveat explanation for interview practice.
- Write a short desk memo: decision, evidence, risk caveat, and next test.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind mini lab: strategy before and after costs?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Mid Price
$$m_t=\frac{\mathrm{bid}_t+\mathrm{ask}_t}{2}$$
Plain-English interpretation: Reference price between best bid and ask.
Interview pitfall: Comparing fills to stale mid prices.

### Formula 2: Effective Spread
$$\mathrm{EffSpread}_t=2\cdot\left|\frac{p_t^{exec}-m_t}{m_t}\right|$$
Plain-English interpretation: Realized transaction cost proxy.
Interview pitfall: Ignoring direction and sign conventions.

### Formula 3: Turnover
$$\mathrm{TO}_t=\frac{1}{2}\sum_i|w_{i,t}-w_{i,t-1}|$$
Plain-English interpretation: Fraction of portfolio traded on rebalance.
Interview pitfall: Reporting gross turnover without cost translation.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Mid Price | Reference price between best bid and ask. | Execution quality benchmarking. | Comparing fills to stale mid prices. |
| Effective Spread | Realized transaction cost proxy. | Estimate execution drag in backtests. | Ignoring direction and sign conventions. |
| Turnover | Fraction of portfolio traded on rebalance. | Capacity and cost control. | Reporting gross turnover without cost translation. |

## Common Mistakes and Fixes
- Mistake: copying formulas without defining each symbol. Fix: annotate each term in plain language.
- Mistake: reporting one number without context. Fix: compare to benchmark or alternate scenario.
- Mistake: reading model output as certainty. Fix: include one failure mode and one robustness check.
- Mistake: skipping assumptions. Fix: list assumptions before interpretation.

## Revision Sprint
- Re-solve one earlier problem from memory before checking notes.
- Review yesterday's weak point and state whether it is fixed.
- Schedule the next spaced repetition date before ending the session.

## Real-World Data Lab
- Use yfinance first for SPY, QQQ, TLT, and GLD when internet is available.
- If available, validate against a Robinhood-style export CSV for consistency checks.
- Fall back to curriculum/datasets/real_market_prices.csv for reproducible runs.
- Design one topic-specific analysis for mini lab: strategy before and after costs instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Simulate one execution or turnover scenario for mini lab: strategy before and after costs and quantify its cost impact.
- Add comments that explain the intent of each major transformation and why it matters for quant decisions.
- Print one table and one metric summary that could be shown in a desk review.
- Add one stress or sensitivity variation and compare baseline versus stressed output.
- End with a one-paragraph interpretation describing actionability and limitations.

## Interview Drill
- Q1: Explain mini lab: strategy before and after costs to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from mini lab: strategy before and after costs is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.

## Saturday Revision Protocol
1. Rebuild your week summary from memory before opening notes.
2. Rework two weak problems from your error log with corrected reasoning.
3. Refresh formula sheet entries and mark confidence 0-5 per formula.
4. Prepare one interview-style explanation for the week's hardest concept.
