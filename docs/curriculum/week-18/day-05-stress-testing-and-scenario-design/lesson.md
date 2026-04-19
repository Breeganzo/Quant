# Week 18 Fri: Stress testing and scenario design

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "ML for Quant II: volatility, EWMA, GARCH intuition, risk forecasting, and stress testing". Your objective is to understand, apply, and communicate stress testing and scenario design in a way a quant team would trust.

## Continuity Map
- Previous day focus: Forecast evaluation for risk models
- Today's focus: Stress testing and scenario design
- Next day bridge: Mini lab: volatility forecast comparison

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
Stress testing and scenario design is part of real quant work inside ml for quant ii: volatility, ewma, garch intuition, risk forecasting, and stress testing research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Loss quantile under distribution assumptions.
2. Technical frame: Build stress testing and scenario design from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: Parametric VaR, Expected Shortfall, Stress Loss).
3. Market interpretation: Daily risk-limit reporting.. Run one compact, reproducible example for stress testing and scenario design and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Assuming normal tails in crisis regimes.

## Practice Problems
- Explain stress testing and scenario design in one paragraph without jargon.
- Write down one topic-specific formula or workflow for stress testing and scenario design from memory.
- Connect stress testing and scenario design to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind stress testing and scenario design?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Parametric VaR
$$VaR_{\alpha}=\mu+z_{\alpha}\sigma$$
Plain-English interpretation: Loss quantile under distribution assumptions.
Interview pitfall: Assuming normal tails in crisis regimes.

### Formula 2: Expected Shortfall
$$ES_{\alpha}=\mathbb{E}[L\mid L>VaR_{\alpha}]$$
Plain-English interpretation: Average loss beyond VaR threshold.
Interview pitfall: Relying on short history for ES.

### Formula 3: Stress Loss
$$L_{stress}=w^T r_{scenario}$$
Plain-English interpretation: Portfolio loss under explicit scenario vector.
Interview pitfall: Using stress vectors not tied to plausible regimes.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Parametric VaR | Loss quantile under distribution assumptions. | Daily risk-limit reporting. | Assuming normal tails in crisis regimes. |
| Expected Shortfall | Average loss beyond VaR threshold. | Tail-risk governance. | Relying on short history for ES. |
| Stress Loss | Portfolio loss under explicit scenario vector. | Scenario-based resilience checks. | Using stress vectors not tied to plausible regimes. |

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
- Design one topic-specific analysis for stress testing and scenario design instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Compare at least two volatility/risk forecasts for stress testing and scenario design and discuss one stress weakness.

## Interview Drill
- Q1: Explain stress testing and scenario design to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from stress testing and scenario design is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
