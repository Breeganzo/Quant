# Week 09 Fri: Turnover, holding period, and capacity intuition

**Estimated time:** 8 hours

## Daily Mission
This day belongs to the week theme "Finance Core I: market microstructure, execution, slippage, and transaction costs". Your objective is to understand, apply, and communicate turnover, holding period, and capacity intuition in a way a quant team would trust.

## Continuity Map
- Previous day focus: Transaction costs and slippage models
- Today's focus: Turnover, holding period, and capacity intuition
- Next day bridge: Mini lab: strategy before and after costs

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
Turnover, holding period, and capacity intuition is part of real quant work inside finance core i: market microstructure, execution, slippage, and transaction costs research, trading, or risk workflows.

## Concept Build (Intuition -> Technical -> Market Use)
1. Intuition: describe turnover, holding period, and capacity intuition in plain language before touching formulas.
2. Technical frame: Start with intuition for turnover, holding period, and capacity intuition, then restate it using the formal quantitative language used in finance and ML.
3. Market interpretation: Build one small finance example around turnover, holding period, and capacity intuition and explain what the output would mean for a trader or risk analyst.
4. Failure mode check: identify one way this concept is commonly misused in research or trading discussion.

## Practice Problems
- Explain turnover, holding period, and capacity intuition in one paragraph without jargon.
- Write down the main formula or workflow for turnover, holding period, and capacity intuition from memory.
- Connect turnover, holding period, and capacity intuition to one trading, portfolio, or risk problem.

## 8-Hour Deliverables
- Produce one page of notes with intuition, formulas, and one market example in your own words.
- Complete all notebook cells and annotate each output with what it means financially.
- Add one error-log entry with a scheduled review date.
- Record a 60-90 second spoken explanation of the concept as interview practice.

## Daily Quiz (Closed-Book)
1. What is the core intuition behind turnover, holding period, and capacity intuition?
2. Write one formula or workflow from memory and define each term.
3. Give one practical quant use case and one failure mode.

## Formula Sheet Drill
- Expected value: E[X] = sum_i p_i x_i
- Variance: Var(X) = E[(X - E[X])^2]
- Covariance and correlation: Cov(X,Y), Corr(X,Y) = Cov(X,Y)/(sigma_X sigma_Y)
- Compounding: W_t = W_0 * product(1 + r_t)
- Topic-specific formula: write one formula central to turnover, holding period, and capacity intuition and explain every symbol.

## Formula Organization Table
| Formula/Workflow | Meaning | Finance Use Case | Common Misread |
| --- | --- | --- | --- |
| Topic-specific formula | Core relationship for today's topic | Strategy/risk interpretation | Memorizing symbols without interpretation |
| Expected value | Probability-weighted average outcome | Comparing asymmetric payoff setups | Ignoring payoff magnitude |
| Volatility proxy | Dispersion of returns around average | Position sizing and risk budgeting | Treating low volatility as no risk |

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
- Open the local market dataset at `curriculum/datasets/real_market_prices.csv`.
- Build a small panel for SPY, QQQ, TLT, and GLD and compute daily returns.
- Compare cumulative performance and volatility across symbols.
- Write one practical takeaway for position sizing or diversification.

## Coding Task
Implement one notebook cell or small script focused on: turnover, holding period, and capacity intuition.

## Interview Drill
- Q1: Explain turnover, holding period, and capacity intuition to a non-technical stakeholder in 3 sentences.
- Q2: Give one failure case where this concept can produce misleading confidence.
- Q3: Show one concrete link from this concept to trading, portfolio construction, or risk control.

## Reflection Prompt
What from turnover, holding period, and capacity intuition felt truly clear, and what still needs a slower revisit?

## Completion Checklist
- I can explain the concept from memory without reading notes.
- I completed at least one coding exercise tied to the day topic.
- I wrote one realistic finance use case in my own words.
- I recorded at least one weak area in my error log.
- I set the next review date using spaced repetition.
