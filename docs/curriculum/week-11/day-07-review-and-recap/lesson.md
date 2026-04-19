# Week 11 Sun: Review and recap

**Estimated time:** 10 hours

## Daily Mission
This day belongs to the week theme "Finance Core III: fixed income, yield curves, duration, convexity, and credit basics". Your objective is to understand, apply, and communicate review and recap in a way a quant team would trust.

## Continuity Map
- Previous day focus: Mini lab: simple bond price sensitivity
- Today's focus: Review and recap
- Week closure: consolidate this concept into your weekly project narrative.

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
Review and recap is part of real quant work inside finance core iii: fixed income, yield curves, duration, convexity, and credit basics research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Present value of discounted cash flows.
2. Technical frame: Build review and recap from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: Bond Price, Modified Duration, Convexity).
3. Market interpretation: Mark-to-model pricing for plain-vanilla bonds.. Run one compact, reproducible example for review and recap and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Mixing compounding conventions.

## Real-World Solved Case (Step-by-Step)
- Step 1 (Problem framing): Define the desk decision and why review and recap is relevant.
- Step 2 (Data and assumptions): Use `curriculum/datasets/real_market_prices.csv`, state one data-quality assumption and one regime-risk assumption.
- Step 3 (Method): Apply Bond Price or a directly related workflow on a reproducible sample.
- Step 4 (Result): Report one quantitative output and one practical interpretation for research, trading, or risk.
- Step 5 (Caveat): Document one failure mode: Mixing compounding conventions.
- Step 6 (Robustness): Re-run with one alternate window, parameter, or benchmark and compare conclusions.

## Deep Study Prompts (10-Hour Track)
- What assumption is easiest to violate in live markets and how would you detect that early?
- Which output would you show a PM or risk manager first, and why?
- Which alternate explanation could produce similar numbers but imply a different action?
- What metric could improve while hidden risk still worsens?

## Practice Problems
- Explain review and recap in one paragraph without jargon.
- Write down one topic-specific formula or workflow for review and recap from memory.
- Connect review and recap to one realistic trading, portfolio, risk, or research decision.

## 10-Hour Deliverables
- Produce 2-3 pages of notes with intuition, formal definitions, formulas, and one solved real-world case.
- Complete all notebook labs plus one extension experiment with changed assumptions or parameters.
- Add at least two error-log entries with specific correction rules and review dates.
- Record a 2-minute spoken explanation and a 1-minute risk caveat explanation for interview practice.
- Write a short desk memo: decision, evidence, risk caveat, and next test.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind review and recap?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Bond Price
$$P=\sum_{t=1}^{T}\frac{CF_t}{(1+y)^t}$$
Plain-English interpretation: Present value of discounted cash flows.
Interview pitfall: Mixing compounding conventions.

### Formula 2: Modified Duration
$$D_{mod}=\frac{D_{mac}}{1+y}$$
Plain-English interpretation: Approximate percentage price sensitivity to yield.
Interview pitfall: Using duration alone for large yield moves.

### Formula 3: Convexity
$$C=\frac{1}{P}\sum_{t=1}^{T}\frac{CF_t\,t(t+1)}{(1+y)^{t+2}}$$
Plain-English interpretation: Second-order sensitivity adjustment to yield moves.
Interview pitfall: Ignoring convexity in stressed scenarios.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Bond Price | Present value of discounted cash flows. | Mark-to-model pricing for plain-vanilla bonds. | Mixing compounding conventions. |
| Modified Duration | Approximate percentage price sensitivity to yield. | Rate-shock risk estimation. | Using duration alone for large yield moves. |
| Convexity | Second-order sensitivity adjustment to yield moves. | Improve rate-shock approximation accuracy. | Ignoring convexity in stressed scenarios. |

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
- Design one topic-specific analysis for review and recap instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Price a simple bond setup for review and recap and measure sensitivity to a yield shock.
- Add comments that explain the intent of each major transformation and why it matters for quant decisions.
- Print one table and one metric summary that could be shown in a desk review.
- Add one stress or sensitivity variation and compare baseline versus stressed output.
- End with a one-paragraph interpretation describing actionability and limitations.

## Interview Drill
- Q1: Explain review and recap to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from review and recap is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.

## Sunday Mini-Project Blueprint
1. Load real market data from `curriculum/datasets/real_market_prices.csv`.
2. Define a clear project question and one measurable output metric.
3. Build at least one baseline and one variation, then compare outcomes.
4. Write a short conclusion with one limitation and one next-step improvement.
