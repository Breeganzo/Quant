# Week 06 Sat: Mini lab: classify positive versus negative future returns

**Estimated time:** 10 hours

## Daily Mission
This day belongs to the week theme "ML Foundations II: classification, metrics, imbalance, validation, and risk use cases". Your objective is to understand, apply, and communicate mini lab: classify positive versus negative future returns in a way a quant team would trust.

## Continuity Map
- Previous day focus: Credit risk and event prediction examples
- Today's focus: Mini lab: classify positive versus negative future returns
- Next day bridge: Review and error-log day

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
Mini lab: classify positive versus negative future returns is part of real quant work inside ml foundations ii: classification, metrics, imbalance, validation, and risk use cases research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: One-period relative price change.
2. Technical frame: Build mini lab: classify positive versus negative future returns from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: Simple Return, Log Return, Compounded Wealth).
3. Market interpretation: Baseline daily performance attribution.. Run one compact, reproducible example for mini lab: classify positive versus negative future returns and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Comparing assets without handling frequency or missing days.

## Real-World Solved Case (Step-by-Step)
- Step 1 (Problem framing): Define the desk decision and why mini lab: classify positive versus negative future returns is relevant.
- Step 2 (Data and assumptions): Use `curriculum/datasets/real_market_prices.csv`, state one data-quality assumption and one regime-risk assumption.
- Step 3 (Method): Apply Simple Return or a directly related workflow on a reproducible sample.
- Step 4 (Result): Report one quantitative output and one practical interpretation for research, trading, or risk.
- Step 5 (Caveat): Document one failure mode: Comparing assets without handling frequency or missing days.
- Step 6 (Robustness): Re-run with one alternate window, parameter, or benchmark and compare conclusions.

## Deep Study Prompts (10-Hour Track)
- What assumption is easiest to violate in live markets and how would you detect that early?
- Which output would you show a PM or risk manager first, and why?
- Which alternate explanation could produce similar numbers but imply a different action?
- What metric could improve while hidden risk still worsens?

## Practice Problems
- Explain mini lab: classify positive versus negative future returns in one paragraph without jargon.
- Write down one topic-specific formula or workflow for mini lab: classify positive versus negative future returns from memory.
- Connect mini lab: classify positive versus negative future returns to one realistic trading, portfolio, risk, or research decision.

## 10-Hour Deliverables
- Produce 2-3 pages of notes with intuition, formal definitions, formulas, and one solved real-world case.
- Complete all notebook labs plus one extension experiment with changed assumptions or parameters.
- Add at least two error-log entries with specific correction rules and review dates.
- Record a 2-minute spoken explanation and a 1-minute risk caveat explanation for interview practice.
- Write a short desk memo: decision, evidence, risk caveat, and next test.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind mini lab: classify positive versus negative future returns?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Simple Return
$$r_t=\frac{P_t}{P_{t-1}}-1$$
Plain-English interpretation: One-period relative price change.
Interview pitfall: Comparing assets without handling frequency or missing days.

### Formula 2: Log Return
$$\ell_t=\ln\left(\frac{P_t}{P_{t-1}}\right)$$
Plain-English interpretation: Additive return representation across time.
Interview pitfall: Mixing log and simple returns in one report.

### Formula 3: Compounded Wealth
$$W_T=W_0\prod_{t=1}^{T}(1+r_t)$$
Plain-English interpretation: Capital path under sequential returns.
Interview pitfall: Averaging returns instead of compounding them.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Simple Return | One-period relative price change. | Baseline daily performance attribution. | Comparing assets without handling frequency or missing days. |
| Log Return | Additive return representation across time. | Multi-period return decomposition. | Mixing log and simple returns in one report. |
| Compounded Wealth | Capital path under sequential returns. | Backtest equity-curve reconstruction. | Averaging returns instead of compounding them. |

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
- Design one topic-specific analysis for mini lab: classify positive versus negative future returns instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Train a baseline classifier/regressor for mini lab: classify positive versus negative future returns on market-derived features and report one robust metric beyond accuracy.
- Add comments that explain the intent of each major transformation and why it matters for quant decisions.
- Print one table and one metric summary that could be shown in a desk review.
- Add one stress or sensitivity variation and compare baseline versus stressed output.
- End with a one-paragraph interpretation describing actionability and limitations.

## Interview Drill
- Q1: Explain mini lab: classify positive versus negative future returns to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from mini lab: classify positive versus negative future returns is now evidence-backed in your notes, and what still needs a focused retry?

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
