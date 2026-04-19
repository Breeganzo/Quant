# Week 08 Tue: Stationarity, trends, seasonality, and differencing

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Time Series I: stationarity, AR/MA/ARIMA intuition, walk-forward testing, and forecasting". Your objective is to understand, apply, and communicate stationarity, trends, seasonality, and differencing in a way a quant team would trust.

## Continuity Map
- Previous day focus: What makes time series different from tabular data?
- Today's focus: Stationarity, trends, seasonality, and differencing
- Next day bridge: AR, MA, and ARIMA intuition

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
Stationarity, trends, seasonality, and differencing is part of real quant work inside time series i: stationarity, ar/ma/arima intuition, walk-forward testing, and forecasting research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: describe stationarity, trends, seasonality, and differencing in plain language before touching formulas.
2. Technical frame: Build stationarity, trends, seasonality, and differencing from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment.
3. Market interpretation: Run one compact, reproducible example for stationarity, trends, seasonality, and differencing and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: identify one way this concept is commonly misused in research or trading discussion.

## Practice Problems
- Explain stationarity, trends, seasonality, and differencing in one paragraph without jargon.
- Write down one topic-specific formula or workflow for stationarity, trends, seasonality, and differencing from memory.
- Connect stationarity, trends, seasonality, and differencing to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind stationarity, trends, seasonality, and differencing?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: AR(1)
$$x_t=c+\phi x_{t-1}+\epsilon_t$$
Plain-English interpretation: Current value depends on one lag plus noise.
Interview pitfall: Ignoring non-stationarity before fitting AR models.

### Formula 2: EWMA Variance
$$\sigma_t^2=\lambda\sigma_{t-1}^2+(1-\lambda)r_{t-1}^2$$
Plain-English interpretation: Recency-weighted volatility estimate.
Interview pitfall: Choosing decay factor without validation.

### Formula 3: RMSE
$$\mathrm{RMSE}=\sqrt{\frac{1}{n}\sum_{i=1}^{n}(\hat y_i-y_i)^2}$$
Plain-English interpretation: Average forecast error magnitude in original units.
Interview pitfall: Comparing RMSE across differently scaled targets.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| AR(1) | Current value depends on one lag plus noise. | Baseline dependence and mean-reversion diagnostics. | Ignoring non-stationarity before fitting AR models. |
| EWMA Variance | Recency-weighted volatility estimate. | Adaptive risk forecasting. | Choosing decay factor without validation. |
| RMSE | Average forecast error magnitude in original units. | Compare forecasting pipelines. | Comparing RMSE across differently scaled targets. |

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
- Design one topic-specific analysis for stationarity, trends, seasonality, and differencing instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Construct a lag-based pipeline for stationarity, trends, seasonality, and differencing and compare one forecast baseline to one improved variant.

## Interview Drill
- Q1: Explain stationarity, trends, seasonality, and differencing to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from stationarity, trends, seasonality, and differencing is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
