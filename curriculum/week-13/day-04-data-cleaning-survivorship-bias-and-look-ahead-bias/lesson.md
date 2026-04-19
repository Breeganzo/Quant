# Week 13 Thu: Data cleaning, survivorship bias, and look-ahead bias

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Quant Workflow I: idea generation, research logs, labels, and data hygiene". Your objective is to understand, apply, and communicate data cleaning, survivorship bias, and look-ahead bias in a way a quant team would trust.

## Continuity Map
- Previous day focus: Label design and target horizon choice
- Today's focus: Data cleaning, survivorship bias, and look-ahead bias
- Next day bridge: Research logging and experiment notebooks

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 60 min | Theory deep dive: definitions, intuition, and assumptions. |
| Session 2 | 60 min | Formula and workflow lab with topic-specific derivations. |
| Session 3 | 60 min | Worked examples with interpretation and failure-mode checks. |
| Session 4 | 60 min | Notebook implementation and output interpretation. |
| Session 5 | 60 min | Interview-style quiz and closed-book retrieval. |
| Session 6 | 60 min | Revision sprint, error-log update, and summary memo. |

## Why It Matters In Quant
Data cleaning, survivorship bias, and look-ahead bias is part of real quant work inside quant workflow i: idea generation, research logs, labels, and data hygiene research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Temporal-causality violation indicator.
2. Technical frame: Build data cleaning, survivorship bias, and look-ahead bias from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: Leakage Flag, Coverage Ratio, Survivorship Gap).
3. Market interpretation: Pipeline data audit.. Run one compact, reproducible example for data cleaning, survivorship bias, and look-ahead bias and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Using post-event data in training.

## Practice Problems
- Explain data cleaning, survivorship bias, and look-ahead bias in one paragraph without jargon.
- Write down one topic-specific formula or workflow for data cleaning, survivorship bias, and look-ahead bias from memory.
- Connect data cleaning, survivorship bias, and look-ahead bias to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

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
