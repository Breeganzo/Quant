# Week 02 Thu: Correlation, covariance, and diversification

**Estimated time:** 6 hours

## Session Plan
| Session | Duration | Focus |
| --- | --- | --- |
| Session 1 | 45 min | Understand correlation and covariance intuitively. |
| Session 2 | 55 min | Compute co-movement measures from returns. |
| Session 3 | 55 min | Link co-movement to diversification. |
| Session 4 | 55 min | Practice interpretation and code. |
| Session 5 | 30 min | Interview recap. |

## Why It Matters In Quant
Correlation, covariance, and diversification is part of real quant work inside data and linear algebra: numpy, pandas, visualization, diversification, and sql basics research, trading, or risk workflows.

## Learning Overview
Diversification is not magic. It works because assets do not move perfectly together all the time.

Today is about understanding co-movement well enough to explain why diversification can reduce risk even when every asset is risky on its own.

## Continuity
- Start by recalling what from yesterday is still unclear.
- Use today's topic to fix at least one weak area from your error log.
- End by writing a one-paragraph bridge to tomorrow's topic.

## Core Concepts
### Correlation
- Simple explanation: Correlation measures how strongly two variables tend to move together.
- Technical depth: It is a standardized measure of linear co-movement between -1 and 1.
- Finance example: Two equity ETFs may have high positive correlation, while stocks and bonds may sometimes have lower correlation.

### Covariance
- Simple explanation: Covariance measures whether two variables move together, but it is not scaled.
- Technical depth: Covariance appears naturally in portfolio variance formulas because it captures how joint movements contribute to total risk.
- Finance example: Portfolio risk is lower when component assets have lower or negative covariance.

### Diversification logic
- Simple explanation: If assets do not all rise and fall together, combining them can smooth the overall path.
- Technical depth: Portfolio variance depends on both individual variances and pairwise covariances, not just average volatility.
- Finance example: A mixed portfolio of assets can have lower volatility than its components if co-movement is low enough.

## Worked Examples
- Compare two assets with similar volatility but different correlation to a third asset.
- Show how a two-asset portfolio can be less volatile than both standalone assets if correlation is low enough.
- Interpret a correlation matrix economically rather than mechanically.

## Practice Questions With Answers
### Question: Why is correlation alone not enough for portfolio variance?
Answer: Because actual risk contribution also depends on each asset's own volatility and weight, not only the correlation sign and magnitude.

### Question: Why can diversification fail in crises?
Answer: Because correlations often rise during stress, making assets move together more than expected.

### Question: What is the intuition behind covariance in a portfolio?
Answer: It captures whether two assets amplify or offset each other's moves.

## Daily Quiz (Closed-Book)
1. Explain today's core intuition from memory.
2. Write one formula/workflow and define all symbols/steps.
3. Give one use case and one realistic failure mode.

## Interview-Ready Formula Sheet
### Formula 1: Covariance
$$\mathrm{Cov}(X,Y)=\frac{1}{n-1}\sum_i(x_i-\bar x)(y_i-\bar y)$$
Plain-English interpretation: Joint variation around means.
Notation check: Miscaligned timestamps inflate noise.

### Formula 2: Correlation
$$\rho_{XY}=\frac{\mathrm{Cov}(X,Y)}{\sigma_X\sigma_Y}$$
Plain-English interpretation: Scale-free co-movement in [-1,1].
Notation check: Confusing correlation with causation.

### Formula 3: 2-Asset Variance
$$\sigma_p^2=w_1^2\sigma_1^2+w_2^2\sigma_2^2+2w_1w_2\rho_{12}\sigma_1\sigma_2$$
Plain-English interpretation: Risk decomposition for two-asset mix.
Notation check: Ignoring correlation regime shifts.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Covariance | Joint variation around means. | Diversification diagnostics. | Miscaligned timestamps inflate noise. |
| Correlation | Scale-free co-movement in [-1,1]. | Asset clustering and hedging checks. | Confusing correlation with causation. |
| 2-Asset Variance | Risk decomposition for two-asset mix. | Show diversification impact directly. | Ignoring correlation regime shifts. |

## Extended Study (to complete a full 6-hour day)
1. Rewrite each core concept in your own words without looking at notes.
2. Add one extra worked example using different numbers or assumptions.
3. Explain one failure mode where this concept can be misapplied in trading or risk work.
4. Add one short paragraph linking this concept to your weekly project objective.

## Real-World Data Application
1. Pull SPY, QQQ, TLT, and GLD with yfinance when internet is available.
2. If available, compare with a Robinhood-style export CSV for source consistency.
3. Use `curriculum/datasets/real_market_prices.csv` as reproducible fallback.
4. Compute log returns, annualized volatility, and Sharpe ratio across symbols.
5. Build one cumulative growth chart and one correlation table.
6. Write one practical portfolio/risk insight from the data.

## Coding Task
Build a cleaned feature table for correlation, covariance, and diversification and show one validation check that catches a data issue.

## Daily Interview Drill
### Q: Why does low correlation help a portfolio?
A: Because when assets do not move perfectly together, their fluctuations partially offset and reduce overall variance.

## Reflection Question
What from correlation, covariance, and diversification is now evidence-backed in your notes, and what still needs a focused retry?

## Completion Checklist
- I completed the planned study blocks or adjusted them honestly.
- I rewrote the main ideas from memory.
- I finished the notebook cells and checked the outputs.
- I logged at least one weak spot in the error log.
- I practiced at least one interview answer aloud.
