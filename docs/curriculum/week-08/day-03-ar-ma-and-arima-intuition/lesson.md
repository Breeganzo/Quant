# Week 08 Wed: AR, MA, and ARIMA intuition

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Time Series I: stationarity, AR/MA/ARIMA intuition, walk-forward testing, and forecasting". Your objective is to understand, apply, and communicate ar, ma, and arima intuition in a way a quant team would trust.

## Continuity Map
- Previous day focus: Stationarity, trends, seasonality, and differencing
- Today's focus: AR, MA, and ARIMA intuition
- Next day bridge: Autocorrelation, partial autocorrelation, and lag structure

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
AR, MA, and ARIMA intuition is part of real quant work inside time series i: stationarity, ar/ma/arima intuition, walk-forward testing, and forecasting research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Unified AR/MA with differencing.
2. Technical frame: Build ar, ma, and arima intuition from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: ARIMA Model, AIC, Forecast Error).
3. Market interpretation: Baseline univariate forecasting.. Run one compact, reproducible example for ar, ma, and arima intuition and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Choosing orders without diagnostics.

## Practice Problems
- Explain ar, ma, and arima intuition in one paragraph without jargon.
- Write down one topic-specific formula or workflow for ar, ma, and arima intuition from memory.
- Connect ar, ma, and arima intuition to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind ar, ma, and arima intuition?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: ARIMA Model
$$\Phi(B)(1-B)^d x_t=\Theta(B)\epsilon_t$$
Plain-English interpretation: Unified AR/MA with differencing.
Interview pitfall: Choosing orders without diagnostics.

### Formula 2: AIC
$$AIC=2k-2\ln(\hat L)$$
Plain-English interpretation: Complexity-adjusted fit criterion.
Interview pitfall: Treating AIC winner as deploy-ready.

### Formula 3: Forecast Error
$$e_t=x_t-\hat x_t$$
Plain-English interpretation: Realized minus predicted value.
Interview pitfall: Ignoring autocorrelation in residuals.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| ARIMA Model | Unified AR/MA with differencing. | Baseline univariate forecasting. | Choosing orders without diagnostics. |
| AIC | Complexity-adjusted fit criterion. | Model order comparison. | Treating AIC winner as deploy-ready. |
| Forecast Error | Realized minus predicted value. | Residual diagnostics and calibration. | Ignoring autocorrelation in residuals. |

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
- Design one topic-specific analysis for ar, ma, and arima intuition instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Construct a lag-based pipeline for ar, ma, and arima intuition and compare one forecast baseline to one improved variant.

## Interview Drill
- Q1: Explain ar, ma, and arima intuition to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from ar, ma, and arima intuition is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
