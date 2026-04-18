# Week 17 Mon: Decision trees and rule-based splits

**Estimated time:** 8 hours

## Daily Mission
This day belongs to the week theme "ML for Quant I: trees, ensembles, nonlinear interactions, and model interpretation". Your objective is to understand, apply, and communicate decision trees and rule-based splits in a way a quant team would trust.

## Continuity Map
- Week kickoff: establish baseline intuition and key definitions before moving into formal detail.
- Today's focus: Decision trees and rule-based splits
- Next day bridge: Random forests and bagging intuition

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 75 min | Theory deep dive: definitions, intuition, and assumptions. |
| Session 2 | 70 min | Formula lab: derive, rewrite, and memorize key formulas from scratch. |
| Session 3 | 70 min | Worked examples with finance interpretation and edge-case checks. |
| Session 4 | 70 min | Notebook implementation and output interpretation. |
| Session 5 | 60 min | Practice quiz and closed-book retrieval on formulas. |
| Session 6 | 50 min | Mini-project increment and result write-up. |
| Session 7 | 45 min | Revision sprint, spaced-repetition update, and error-log updates. |
| Session 8 | 40 min | Interview drill and communication rehearsal. |

## Why It Matters In Quant
Decision trees and rule-based splits is part of real quant work inside ml for quant i: trees, ensembles, nonlinear interactions, and model interpretation research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: describe decision trees and rule-based splits in plain language before touching formulas.
2. Technical frame: Start with intuition for decision trees and rule-based splits, then restate it using the formal quantitative language used in finance and ML.
3. Market interpretation: Build one small finance example around decision trees and rule-based splits and explain what the output would mean for a trader or risk analyst.
4. Failure mode check: identify one way this concept is commonly misused in research or trading discussion.

## Practice Problems
- Explain decision trees and rule-based splits in one paragraph without jargon.
- Write down the main formula or workflow for decision trees and rule-based splits from memory.
- Connect decision trees and rule-based splits to one trading, portfolio, or risk problem.

## 8-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind decision trees and rule-based splits?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Log Return
$$\ell_t = \ln\left(\frac{P_t}{P_{t-1}}\right)$$
Plain-English interpretation: Additive return representation over time.
Notation check: Define each symbol and unit before coding.

### Formula 2: Annualized Volatility
$$\sigma_{ann} = \sqrt{252} \cdot \mathrm{Std}(r_t)$$
Plain-English interpretation: Scales daily return uncertainty to annual horizon.
Notation check: Confirm return frequency matches annualization factor.

### Formula 3: Sharpe Ratio
$$S = \frac{R_{ann} - R_f}{\sigma_{ann}}$$
Plain-English interpretation: Excess return earned per unit of risk.
Notation check: Use consistent annualized units for return, risk-free rate, and volatility.

### Symbol Definitions
| Symbol | Meaning | Units | Example |
| --- | --- | --- | --- |
| $P_t$ | Price at time $t$ | USD/share | 110.50 |
| $r_t$ | Simple return | decimal | 0.012 |
| $R_{ann}$ | Annualized return | annualized decimal | 0.14 |
| $\sigma_{ann}$ | Annualized volatility | annualized decimal | 0.18 |
| $R_f$ | Risk-free rate | annualized decimal | 0.03 |
| $TO_t$ | Portfolio turnover | fraction of portfolio | 0.12 |

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Log return | Additive return representation | Multi-period analytics and model features | Mixing with simple return without context |
| Annualized volatility | Scaled daily uncertainty | Position sizing and risk budgeting | Annualizing from inconsistent data frequency |
| Sharpe ratio | Excess return per risk unit | Strategy comparison and portfolio review | Ignoring regime shifts and estimation error |

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
- Fall back to `curriculum/datasets/real_market_prices.csv` for reproducible runs.
- Build a small panel and compute log returns, annualized volatility, and Sharpe ratio.
- Compare cumulative performance across symbols and mark one stress-period observation.
- Write one practical takeaway for position sizing or diversification.

## Coding Task
Implement one notebook cell or small script focused on: decision trees and rule-based splits.

## Interview Drill
- Q1: Explain decision trees and rule-based splits to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, or risk control.

## Reflection Prompt
What from decision trees and rule-based splits felt truly clear, and what still needs a slower revisit?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic finance use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
