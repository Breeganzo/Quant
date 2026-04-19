# Week 15 Mon: Momentum intuition and empirical logic

**Estimated time:** 10 hours

## Daily Mission
This day belongs to the week theme "Signals I: momentum, mean reversion, cross-sectional signals, and attribution". Your objective is to understand, apply, and communicate momentum intuition and empirical logic in a way a quant team would trust.

## Continuity Map
- Week kickoff: establish baseline intuition and key definitions before moving into formal detail.
- Today's focus: Momentum intuition and empirical logic
- Next day bridge: Mean reversion intuition and failure modes

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
Momentum intuition and empirical logic is part of real quant work inside signals i: momentum, mean reversion, cross-sectional signals, and attribution research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Trend strength over lookback.
2. Technical frame: Build momentum intuition and empirical logic from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: Momentum Signal, Reversion z-Score, Signal Blend).
3. Market interpretation: Cross-sectional ranking inputs.. Run one compact, reproducible example for momentum intuition and empirical logic and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Ignoring regime-dependent crash risk.

## Real-World Solved Case (Step-by-Step)
- Step 1 (Problem framing): Define the desk decision and why momentum intuition and empirical logic is relevant.
- Step 2 (Data and assumptions): Use `curriculum/datasets/real_market_prices.csv`, state one data-quality assumption and one regime-risk assumption.
- Step 3 (Method): Apply Momentum Signal or a directly related workflow on a reproducible sample.
- Step 4 (Result): Report one quantitative output and one practical interpretation for research, trading, or risk.
- Step 5 (Caveat): Document one failure mode: Ignoring regime-dependent crash risk.
- Step 6 (Robustness): Re-run with one alternate window, parameter, or benchmark and compare conclusions.

## Deep Study Prompts (10-Hour Track)
- What assumption is easiest to violate in live markets and how would you detect that early?
- Which output would you show a PM or risk manager first, and why?
- Which alternate explanation could produce similar numbers but imply a different action?
- What metric could improve while hidden risk still worsens?

## Practice Problems
- Explain momentum intuition and empirical logic in one paragraph without jargon.
- Write down one topic-specific formula or workflow for momentum intuition and empirical logic from memory.
- Connect momentum intuition and empirical logic to one realistic trading, portfolio, risk, or research decision.

## 10-Hour Deliverables
- Produce 2-3 pages of notes with intuition, formal definitions, formulas, and one solved real-world case.
- Complete all notebook labs plus one extension experiment with changed assumptions or parameters.
- Add at least two error-log entries with specific correction rules and review dates.
- Record a 2-minute spoken explanation and a 1-minute risk caveat explanation for interview practice.
- Write a short desk memo: decision, evidence, risk caveat, and next test.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind momentum intuition and empirical logic?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Momentum Signal
$$m_t=\frac{P_t}{P_{t-k}}-1$$
Plain-English interpretation: Trend strength over lookback.
Interview pitfall: Ignoring regime-dependent crash risk.

### Formula 2: Reversion z-Score
$$z_t=\frac{x_t-\mu_t}{\sigma_t}$$
Plain-English interpretation: Deviation from local equilibrium.
Interview pitfall: Using unstable rolling moments.

### Formula 3: Signal Blend
$$s_t=\sum_j\omega_j s_{j,t}$$
Plain-English interpretation: Weighted multi-signal aggregate.
Interview pitfall: Blending without normalization.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Momentum Signal | Trend strength over lookback. | Cross-sectional ranking inputs. | Ignoring regime-dependent crash risk. |
| Reversion z-Score | Deviation from local equilibrium. | Entry/exit threshold rules. | Using unstable rolling moments. |
| Signal Blend | Weighted multi-signal aggregate. | Diversify alpha sources. | Blending without normalization. |

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
- Design one topic-specific analysis for momentum intuition and empirical logic instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Build and compare at least two signal variants for momentum intuition and empirical logic and explain why one is more robust.
- Add comments that explain the intent of each major transformation and why it matters for quant decisions.
- Print one table and one metric summary that could be shown in a desk review.
- Add one stress or sensitivity variation and compare baseline versus stressed output.
- End with a one-paragraph interpretation describing actionability and limitations.

## Interview Drill
- Q1: Explain momentum intuition and empirical logic to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from momentum intuition and empirical logic is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
