# Week 05 Tue: Linear regression as an ML baseline

**Estimated time:** 10 hours

## Daily Mission
This day belongs to the week theme "ML Foundations I: supervised learning, regression, features, and train-test discipline". Your objective is to understand, apply, and communicate linear regression as an ml baseline in a way a quant team would trust.

## Continuity Map
- Previous day focus: Prediction problems in finance: what are we forecasting?
- Today's focus: Linear regression as an ML baseline
- Next day bridge: Feature engineering from price and volume data

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
Linear regression as an ML baseline is part of real quant work inside ml foundations i: supervised learning, regression, features, and train-test discipline research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Least-squares linear parameter estimate.
2. Technical frame: Build linear regression as an ml baseline from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: OLS Coefficients, Residual, R-Squared).
3. Market interpretation: Baseline factor/feature sensitivity model.. Run one compact, reproducible example for linear regression as an ml baseline and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Unstable estimates under multicollinearity.

## Real-World Solved Case (Step-by-Step)
- Step 1 (Problem framing): Define the desk decision and why linear regression as an ml baseline is relevant.
- Step 2 (Data and assumptions): Use `curriculum/datasets/real_market_prices.csv`, state one data-quality assumption and one regime-risk assumption.
- Step 3 (Method): Apply OLS Coefficients or a directly related workflow on a reproducible sample.
- Step 4 (Result): Report one quantitative output and one practical interpretation for research, trading, or risk.
- Step 5 (Caveat): Document one failure mode: Unstable estimates under multicollinearity.
- Step 6 (Robustness): Re-run with one alternate window, parameter, or benchmark and compare conclusions.

## Deep Study Prompts (10-Hour Track)
- What assumption is easiest to violate in live markets and how would you detect that early?
- Which output would you show a PM or risk manager first, and why?
- Which alternate explanation could produce similar numbers but imply a different action?
- What metric could improve while hidden risk still worsens?

## Practice Problems
- Explain linear regression as an ml baseline in one paragraph without jargon.
- Write down one topic-specific formula or workflow for linear regression as an ml baseline from memory.
- Connect linear regression as an ml baseline to one realistic trading, portfolio, risk, or research decision.

## 10-Hour Deliverables
- Produce 2-3 pages of notes with intuition, formal definitions, formulas, and one solved real-world case.
- Complete all notebook labs plus one extension experiment with changed assumptions or parameters.
- Add at least two error-log entries with specific correction rules and review dates.
- Record a 2-minute spoken explanation and a 1-minute risk caveat explanation for interview practice.
- Write a short desk memo: decision, evidence, risk caveat, and next test.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind linear regression as an ml baseline?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: OLS Coefficients
$$\hat\beta=(X^TX)^{-1}X^Ty$$
Plain-English interpretation: Least-squares linear parameter estimate.
Interview pitfall: Unstable estimates under multicollinearity.

### Formula 2: Residual
$$e_i=y_i-\hat y_i$$
Plain-English interpretation: Unexplained model component.
Interview pitfall: Ignoring residual autocorrelation.

### Formula 3: R-Squared
$$R^2=1-\frac{\sum e_i^2}{\sum (y_i-\bar y)^2}$$
Plain-English interpretation: Variance explained fraction.
Interview pitfall: Using R^2 alone for forecast model quality.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| OLS Coefficients | Least-squares linear parameter estimate. | Baseline factor/feature sensitivity model. | Unstable estimates under multicollinearity. |
| Residual | Unexplained model component. | Model misspecification diagnostics. | Ignoring residual autocorrelation. |
| R-Squared | Variance explained fraction. | Quick baseline fit summary. | Using R^2 alone for forecast model quality. |

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
- Design one topic-specific analysis for linear regression as an ml baseline instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Train a baseline classifier/regressor for linear regression as an ml baseline on market-derived features and report one robust metric beyond accuracy.
- Add comments that explain the intent of each major transformation and why it matters for quant decisions.
- Print one table and one metric summary that could be shown in a desk review.
- Add one stress or sensitivity variation and compare baseline versus stressed output.
- End with a one-paragraph interpretation describing actionability and limitations.

## Interview Drill
- Q1: Explain linear regression as an ml baseline to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from linear regression as an ml baseline is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
