# Week 08 Fri: Walk-forward validation and forecast error metrics

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Time Series I: stationarity, AR/MA/ARIMA intuition, walk-forward testing, and forecasting". Your objective is to understand, apply, and communicate walk-forward validation and forecast error metrics in a way a quant team would trust.

## Continuity Map
- Previous day focus: Autocorrelation, partial autocorrelation, and lag structure
- Today's focus: Walk-forward validation and forecast error metrics
- Next day bridge: Capstone build day

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
Walk-forward validation and forecast error metrics is part of real quant work inside time series i: stationarity, ar/ma/arima intuition, walk-forward testing, and forecasting research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Time-respecting evaluation.
2. Technical frame: Build walk-forward validation and forecast error metrics from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: Walk-Forward Split, RMSE, MAPE).
3. Market interpretation: Avoid look-ahead leakage.. Run one compact, reproducible example for walk-forward validation and forecast error metrics and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Using random shuffle on time series.

## Practice Problems
- Explain walk-forward validation and forecast error metrics in one paragraph without jargon.
- Write down one topic-specific formula or workflow for walk-forward validation and forecast error metrics from memory.
- Connect walk-forward validation and forecast error metrics to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind walk-forward validation and forecast error metrics?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Walk-Forward Split
$$Train_{1:t}\rightarrow Test_{t+1:t+h}$$
Plain-English interpretation: Time-respecting evaluation.
Interview pitfall: Using random shuffle on time series.

### Formula 2: RMSE
$$RMSE=\sqrt{\frac{1}{n}\sum_i(\hat y_i-y_i)^2}$$
Plain-English interpretation: Quadratic forecast error magnitude.
Interview pitfall: Comparing RMSE on different scales.

### Formula 3: MAPE
$$MAPE=\frac{100}{n}\sum_i\left|\frac{y_i-\hat y_i}{y_i}\right|$$
Plain-English interpretation: Relative forecast error percentage.
Interview pitfall: Undefined behavior near zero targets.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Walk-Forward Split | Time-respecting evaluation. | Avoid look-ahead leakage. | Using random shuffle on time series. |
| RMSE | Quadratic forecast error magnitude. | Compare forecast pipelines. | Comparing RMSE on different scales. |
| MAPE | Relative forecast error percentage. | Interpretability for stakeholders. | Undefined behavior near zero targets. |

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
- Design one topic-specific analysis for walk-forward validation and forecast error metrics instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Construct a lag-based pipeline for walk-forward validation and forecast error metrics and compare one forecast baseline to one improved variant.

## Interview Drill
- Q1: Explain walk-forward validation and forecast error metrics to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from walk-forward validation and forecast error metrics is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
