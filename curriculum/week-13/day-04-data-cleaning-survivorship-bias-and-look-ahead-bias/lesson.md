# Week 13 Thu: Data cleaning, survivorship bias, and look-ahead bias

**Estimated time:** 10 hours

## Daily Mission
This day belongs to the week theme "Quant Workflow I: idea generation, research logs, labels, and data hygiene". Your objective is to understand, apply, and communicate data cleaning, survivorship bias, and look-ahead bias in a way a quant team would trust.

## Continuity Map
- Previous day focus: Label design and target horizon choice
- Today's focus: Data cleaning, survivorship bias, and look-ahead bias
- Next day bridge: Research logging and experiment notebooks

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 60 min | Concept briefing: definitions, intuition, and assumptions. |
| Session 2 | 60 min | Formula derivation and notation fluency practice. |
| Session 3 | 60 min | Solved real-world case study with step-by-step reasoning. |
| Session 4 | 60 min | Data quality checks and exploratory diagnostics. |
| Session 5 | 60 min | Core notebook implementation and baseline output analysis. |
| Session 6 | 60 min | Extended coding challenge with variations and sensitivity checks. |
| Session 7 | 60 min | Risk/failure-mode simulation and robustness interpretation. |
| Session 8 | 60 min | Interview quiz: answer structure and technical defense drills. |
| Session 9 | 60 min | Revision sprint and error-log corrections from weak points. |
| Session 10 | 60 min | Desk-style summary memo and next-session action plan. |

## Why It Matters In Quant
Data cleaning, survivorship bias, and look-ahead bias is part of real quant work inside quant workflow i: idea generation, research logs, labels, and data hygiene research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Temporal-causality violation indicator.
2. Technical frame: Build data cleaning, survivorship bias, and look-ahead bias from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: Leakage Flag, Coverage Ratio, Survivorship Gap).
3. Market interpretation: Pipeline data audit.. Run one compact, reproducible example for data cleaning, survivorship bias, and look-ahead bias and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Using post-event data in training.

## Real-World Solved Case (Step-by-Step)
- Step 1 (Problem framing): Define the desk decision and why data cleaning, survivorship bias, and look-ahead bias is relevant.
- Step 2 (Data and assumptions): Use `curriculum/datasets/real_market_prices.csv`, state one data-quality assumption and one regime-risk assumption.
- Step 3 (Method): Apply Leakage Flag or a directly related workflow on a reproducible sample.
- Step 4 (Result): Report one quantitative output and one practical interpretation for research, trading, or risk.
- Step 5 (Caveat): Document one failure mode: Using post-event data in training.
- Step 6 (Robustness): Re-run with one alternate window, parameter, or benchmark and compare conclusions.

## Deep Study Prompts (10-Hour Track)
- What assumption is easiest to violate in live markets and how would you detect that early?
- Which output would you show a PM or risk manager first, and why?
- Which alternate explanation could produce similar numbers but imply a different action?
- What metric could improve while hidden risk still worsens?

## Practice Problems
- Explain data cleaning, survivorship bias, and look-ahead bias in one paragraph without jargon.
- Write down one topic-specific formula or workflow for data cleaning, survivorship bias, and look-ahead bias from memory.
- Connect data cleaning, survivorship bias, and look-ahead bias to one realistic trading, portfolio, risk, or research decision.

## 10-Hour Deliverables
- Produce 2-3 pages of notes with intuition, formal definitions, formulas, and one solved real-world case.
- Complete all notebook labs plus one extension experiment with changed assumptions or parameters.
- Add at least two error-log entries with specific correction rules and review dates.
- Record a 2-minute spoken explanation and a 1-minute risk caveat explanation for interview practice.
- Write a short desk memo: decision, evidence, risk caveat, and next test.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind data cleaning, survivorship bias, and look-ahead bias?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Leakage Flag
$$Leakage=\mathbb{1}(t_{feature}>t_{label})$$
Plain-English interpretation: Temporal-causality violation indicator.
Interview pitfall: Using post-event data in training.

### Formula 2: Coverage Ratio
$$Coverage=\frac{N_{usable}}{N_{raw}}$$
Plain-English interpretation: Share of valid observations after cleaning.
Interview pitfall: Dropping rows without bias review.

### Formula 3: Survivorship Gap
$$SG=\bar r_{survivors}-\bar r_{full\ universe}$$
Plain-English interpretation: Return distortion from missing dead assets.
Interview pitfall: Backtests on survivor-only symbols.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Leakage Flag | Temporal-causality violation indicator. | Pipeline data audit. | Using post-event data in training. |
| Coverage Ratio | Share of valid observations after cleaning. | Track data attrition risk. | Dropping rows without bias review. |
| Survivorship Gap | Return distortion from missing dead assets. | Universe construction sanity checks. | Backtests on survivor-only symbols. |

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
- Design one topic-specific analysis for data cleaning, survivorship bias, and look-ahead bias instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Create a hypothesis test workflow for data cleaning, survivorship bias, and look-ahead bias and log one anti-leakage guardrail.
- Add comments that explain the intent of each major transformation and why it matters for quant decisions.
- Print one table and one metric summary that could be shown in a desk review.
- Add one stress or sensitivity variation and compare baseline versus stressed output.
- End with a one-paragraph interpretation describing actionability and limitations.

## Interview Drill
- Q1: Explain data cleaning, survivorship bias, and look-ahead bias to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from data cleaning, survivorship bias, and look-ahead bias is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
