# Week 18 Mon: Volatility clustering and stylized facts

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "ML for Quant II: volatility, EWMA, GARCH intuition, risk forecasting, and stress testing". Your objective is to understand, apply, and communicate volatility clustering and stylized facts in a way a quant team would trust.

## Continuity Map
- Week kickoff: establish baseline intuition and key definitions before moving into formal detail.
- Today's focus: Volatility clustering and stylized facts
- Next day bridge: Rolling volatility and EWMA

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
Volatility clustering and stylized facts is part of real quant work inside ml for quant ii: volatility, ewma, garch intuition, risk forecasting, and stress testing research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Within-cluster dispersion minimization.
2. Technical frame: Build volatility clustering and stylized facts from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: K-Means Objective, Silhouette Score, Distance Metric).
3. Market interpretation: Group assets by behavior.. Run one compact, reproducible example for volatility clustering and stylized facts and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Ignoring scale normalization before clustering.

## Practice Problems
- Explain volatility clustering and stylized facts in one paragraph without jargon.
- Write down one topic-specific formula or workflow for volatility clustering and stylized facts from memory.
- Connect volatility clustering and stylized facts to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind volatility clustering and stylized facts?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: K-Means Objective
$$\min_{C}\sum_{k}\sum_{x_i\in C_k}||x_i-\mu_k||^2$$
Plain-English interpretation: Within-cluster dispersion minimization.
Interview pitfall: Ignoring scale normalization before clustering.

### Formula 2: Silhouette Score
$$s_i=\frac{b_i-a_i}{\max(a_i,b_i)}$$
Plain-English interpretation: Cluster separation/compactness measure.
Interview pitfall: Using one metric as definitive truth.

### Formula 3: Distance Metric
$$d(x,y)=\sqrt{\sum_j(x_j-y_j)^2}$$
Plain-English interpretation: Similarity proxy in feature space.
Interview pitfall: Choosing metric inconsistent with data geometry.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| K-Means Objective | Within-cluster dispersion minimization. | Group assets by behavior. | Ignoring scale normalization before clustering. |
| Silhouette Score | Cluster separation/compactness measure. | Choose cluster count. | Using one metric as definitive truth. |
| Distance Metric | Similarity proxy in feature space. | Asset regime grouping. | Choosing metric inconsistent with data geometry. |

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
- Design one topic-specific analysis for volatility clustering and stylized facts instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Compare at least two volatility/risk forecasts for volatility clustering and stylized facts and discuss one stress weakness.

## Interview Drill
- Q1: Explain volatility clustering and stylized facts to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from volatility clustering and stylized facts is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
