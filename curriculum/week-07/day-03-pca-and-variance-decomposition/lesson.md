# Week 07 Wed: PCA and variance decomposition

**Estimated time:** 6 hours

## Daily Mission
This day belongs to the week theme "Unsupervised Learning: clustering, PCA, latent structure, and factor intuition". Your objective is to understand, apply, and communicate pca and variance decomposition in a way a quant team would trust.

## Continuity Map
- Previous day focus: Clustering assets and regimes
- Today's focus: PCA and variance decomposition
- Next day bridge: Factor intuition and common risk drivers

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
PCA and variance decomposition is part of real quant work inside unsupervised learning: clustering, pca, latent structure, and factor intuition research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: Feature co-movement matrix.
2. Technical frame: Build pca and variance decomposition from intuition to implementation: define the core mechanism, map it to measurable outputs, and state one assumption that can break in live deployment. (key formulas/workflows: Covariance Matrix, Eigen Decomposition, Explained Variance Ratio).
3. Market interpretation: Basis for PCA decomposition.. Run one compact, reproducible example for pca and variance decomposition and explain both the signal and the main failure mode a quant team should watch.
4. Failure mode check: Failing to center features first.

## Practice Problems
- Explain pca and variance decomposition in one paragraph without jargon.
- Write down one topic-specific formula or workflow for pca and variance decomposition from memory.
- Connect pca and variance decomposition to one realistic trading, portfolio, risk, or research decision.

## 6-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind pca and variance decomposition?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Covariance Matrix
$$\Sigma=\frac{1}{n-1}X^TX$$
Plain-English interpretation: Feature co-movement matrix.
Interview pitfall: Failing to center features first.

### Formula 2: Eigen Decomposition
$$\Sigma v_j=\lambda_j v_j$$
Plain-English interpretation: Principal direction/variance pair.
Interview pitfall: Interpreting sign of eigenvectors as absolute truth.

### Formula 3: Explained Variance Ratio
$$EVR_j=\frac{\lambda_j}{\sum_k\lambda_k}$$
Plain-English interpretation: Share of variance per component.
Interview pitfall: Keeping components without out-of-sample validation.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Covariance Matrix | Feature co-movement matrix. | Basis for PCA decomposition. | Failing to center features first. |
| Eigen Decomposition | Principal direction/variance pair. | Identify dominant latent factors. | Interpreting sign of eigenvectors as absolute truth. |
| Explained Variance Ratio | Share of variance per component. | Dimension reduction selection. | Keeping components without out-of-sample validation. |

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
- Design one topic-specific analysis for pca and variance decomposition instead of reusing generic volatility-only metrics.
- Document one implementation risk and one robustness check before finalizing conclusions.

## Coding Task
Train a baseline classifier/regressor for pca and variance decomposition on market-derived features and report one robust metric beyond accuracy.

## Interview Drill
- Q1: Explain pca and variance decomposition to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, risk, or research quality.

## Reflection Prompt
What from pca and variance decomposition is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
