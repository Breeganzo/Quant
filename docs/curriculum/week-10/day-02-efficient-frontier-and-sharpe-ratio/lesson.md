# Week 10 Tue: Efficient frontier and Sharpe ratio

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Finance Core II: portfolio theory, CAPM, factor investing, and optimization". Your objective is to understand, apply, and communicate efficient frontier and sharpe ratio in a way a quant team would trust.

## Continuity Map
- Previous day focus: Markowitz portfolio intuition
- Today's focus: Efficient frontier and Sharpe ratio
- Next day bridge: CAPM and beta intuition

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
Efficient frontier and Sharpe ratio is part of real quant work inside finance core ii: portfolio theory, capm, factor investing, and optimization research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: describe efficient frontier and sharpe ratio in plain language before touching formulas.
2. Technical frame: Build efficient frontier and sharpe ratio from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment.
3. Market interpretation: Run one compact, reproducible example for efficient frontier and sharpe ratio and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: identify one way this concept is commonly misused in research or trading discussion.

## Practice Problems
- Explain efficient frontier and sharpe ratio in one paragraph without jargon.
- Write down one topic-specific formula or workflow for efficient frontier and sharpe ratio from memory.
- Connect efficient frontier and sharpe ratio to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind efficient frontier and sharpe ratio?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Portfolio Variance
$$\sigma_p^2=w^T\Sigma w$$
Plain-English interpretation: Total risk from weights and covariance matrix.
Interview pitfall: Using unstable covariance estimates without shrinkage.

### Formula 2: CAPM Expected Return
$$\mathbb{E}[R_i]=R_f+\beta_i(\mathbb{E}[R_m]-R_f)$$
Plain-English interpretation: Expected return from market beta exposure.
Interview pitfall: Treating CAPM as a complete model.

### Formula 3: Marginal Risk Contribution
$$\mathrm{MRC}_i=\frac{w_i(\Sigma w)_i}{\sigma_p}$$
Plain-English interpretation: Asset-level contribution to portfolio risk.
Interview pitfall: Ignoring concentration from correlated exposures.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Portfolio Variance | Total risk from weights and covariance matrix. | Optimize risk-aware allocations. | Using unstable covariance estimates without shrinkage. |
| CAPM Expected Return | Expected return from market beta exposure. | Baseline required-return sanity checks. | Treating CAPM as a complete model. |
| Marginal Risk Contribution | Asset-level contribution to portfolio risk. | Risk budgeting and constraint design. | Ignoring concentration from correlated exposures. |

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
- Design one topic-specific analysis for efficient frontier and sharpe ratio instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Compute a risk-aware allocation for efficient frontier and sharpe ratio and explain one concentration risk from the resulting weights.

## Interview Drill
- Q1: Explain efficient frontier and sharpe ratio to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from efficient frontier and sharpe ratio is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
