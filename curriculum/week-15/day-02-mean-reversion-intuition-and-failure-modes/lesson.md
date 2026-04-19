# Week 15 Tue: Mean reversion intuition and failure modes

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Signals I: momentum, mean reversion, cross-sectional signals, and attribution". Your objective is to understand, apply, and communicate mean reversion intuition and failure modes in a way a quant team would trust.

## Continuity Map
- Previous day focus: Momentum intuition and empirical logic
- Today's focus: Mean reversion intuition and failure modes
- Next day bridge: Cross-sectional ranking signals

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
Mean reversion intuition and failure modes is part of real quant work inside signals i: momentum, mean reversion, cross-sectional signals, and attribution research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Trend strength over lookback.
2. Technical frame: Build mean reversion intuition and failure modes from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: Momentum Signal, Reversion z-Score, Signal Blend).
3. Market interpretation: Cross-sectional ranking inputs.. Run one compact, reproducible example for mean reversion intuition and failure modes and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Ignoring regime-dependent crash risk.

## Practice Problems
- Explain mean reversion intuition and failure modes in one paragraph without jargon.
- Write down one topic-specific formula or workflow for mean reversion intuition and failure modes from memory.
- Connect mean reversion intuition and failure modes to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind mean reversion intuition and failure modes?
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
- Design one topic-specific analysis for mean reversion intuition and failure modes instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Build and compare at least two signal variants for mean reversion intuition and failure modes and explain why one is more robust.

## Interview Drill
- Q1: Explain mean reversion intuition and failure modes to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from mean reversion intuition and failure modes is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
