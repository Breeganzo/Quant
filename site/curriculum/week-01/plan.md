# Week 01: Reset Foundations: Python, returns, probability intuition, and market map

**Dates:** 2026-04-20 to 2026-04-26

## Learning Objectives
- Rebuild confidence with core arithmetic, compounding, expected value, and descriptive statistics.
- Reconnect Python basics to finance examples instead of abstract exercises.
- Understand what quants, traders, and risk teams actually do across markets.

## Daily Schedule
### Mon: Reset your toolkit: numbers, variables, returns, and compounding
- Why it matters in quant: Quants constantly translate market moves into numbers. If returns and compounding are shaky, every later topic like portfolio optimization, forecasting, and risk measurement becomes confusing.
- Core explanation: Simple view: a return tells you how much an asset changed relative to where it started. If a stock goes from 100 to 105, the simple return is 5 percent. Compounding means today's gain changes tomorrow's base. Technical view: simple return is (P_t / P_(t-1)) - 1. Multi-period wealth evolves multiplicatively as W_t = W_0 * product(1 + r_t).
- Worked example: If prices are 100, 103, 101, 104 then returns are 3.0 percent, about -1.94 percent, and about 2.97 percent. One 3 percent gain and one 3 percent loss do not cancel perfectly because they act on different bases.
- Practice problems:
- Compute the simple return from 50 to 55.
- Starting with 1000, apply returns of 10 percent and then -5 percent. What is final wealth?
- Why is compounding important when evaluating trading performance?
- Coding task: In Python, create a list of 5 prices, convert them into returns, and calculate final wealth from an initial capital of 1000.
- Reflection: Did I understand returns as changes in relative terms, or was I still thinking only in absolute rupees or dollars?

### Tue: Functions, control flow, probability intuition, and expected value
- Why it matters in quant: Quant code is built from reusable functions, and quant decisions often reduce to expected value under uncertainty.
- Core explanation: Simple view: a function is a machine that takes input and gives output. Expected value is the weighted average outcome if we repeat a gamble many times. Technical view: for discrete outcomes, E[X] = sum p_i x_i. In trading, expected value helps separate lucky wins from positive-edge decisions.
- Worked example: A trade wins 60 percent of the time with +2 and loses 40 percent with -1. Expected value is 0.6*2 + 0.4*(-1) = 0.8. That does not guarantee each trade wins, but the average payoff is positive.
- Practice problems:
- Write a function that accepts buy price and sell price and returns the percentage return.
- Compute expected value for a strategy with 30 percent chance of +5 and 70 percent chance of -1.
- Why can a strategy with many wins still have negative expected value?
- Coding task: Write a Python function for expected value of a discrete strategy and test it on 3 toy trading setups.
- Reflection: Do I naturally ask what the average payoff is, or do I get distracted by single wins and losses?

### Wed: Vectors, matrices, and linear algebra intuition for portfolios and ML
- Why it matters in quant: Portfolio weights, factor exposures, and ML features are easiest to understand as vectors and matrices.
- Core explanation: Simple view: a vector is an ordered list of numbers, like portfolio weights across assets. A matrix is a table of numbers, like data for many assets and many features. Technical view: if w is a weight vector and r is an asset return vector, portfolio return is w^T r. Covariance matrices measure how assets move together.
- Worked example: If portfolio weights are [0.5, 0.3, 0.2] and returns are [0.02, -0.01, 0.03], the portfolio return is 0.5*0.02 + 0.3*(-0.01) + 0.2*0.03 = 0.013 or 1.3 percent.
- Practice problems:
- Interpret a weight vector of [0.6, 0.4].
- Compute a 2-asset portfolio return with weights [0.7, 0.3] and returns [0.01, 0.04].
- Why does covariance matter in diversification?
- Coding task: Use NumPy arrays to compute 3 portfolio returns from a matrix of asset returns and a vector of weights.
- Reflection: Can I explain a portfolio as a weighted combination of assets without getting lost in notation?

### Thu: Descriptive statistics, sampling intuition, and visualizing market data
- Why it matters in quant: Before any model, a quant needs to understand the shape of the data: center, spread, skew, and outliers.
- Core explanation: Simple view: mean tells you the average, standard deviation tells you how spread out values are, and a plot helps you spot structure. Technical view: for returns, volatility is often approximated by standard deviation. Sampling variation means the sample average is only an estimate of the true average.
- Worked example: Two assets can have the same mean return but very different standard deviations. The lower-volatility asset is usually easier to size and risk-manage.
- Practice problems:
- Compute mean and sample standard deviation for returns [0.01, 0.02, -0.01, 0.00].
- Why can one extreme outlier distort the mean?
- What does a histogram of returns help you see?
- Coding task: Create a pandas Series of 20 toy returns and calculate mean, median, standard deviation, min, max, and a histogram.
- Reflection: When I look at a return series, do I immediately ask how noisy it is and whether the average is trustworthy?

### Fri: Market structure, asset classes, risk, return, and what quants actually do
- Why it matters in quant: You need a mental map of markets before learning pricing, forecasting, and strategy research.
- Core explanation: Simple view: markets connect buyers and sellers. Asset classes include equities, fixed income, FX, commodities, and derivatives. Technical view: each asset class has different return drivers, risks, liquidity, and microstructure. Quant roles sit across research, trading, structuring, risk, and execution.
- Worked example: A quant researcher on the buy-side might test a momentum signal for equities, while a sell-side derivatives quant might build or calibrate an option pricing model for a bank's trading desk.
- Practice problems:
- Name 5 asset classes and one major risk for each.
- Explain the difference between return and risk in simple terms.
- Why do transaction costs matter more in fast trading strategies?
- Coding task: Build a markdown table in a notebook comparing 5 asset classes, their return drivers, and their main risks.
- Reflection: Which part of finance feels most interesting right now: markets, trading, risk, or pricing?

### Sat: Revision, spaced repetition, and first market diary notebook
- Why it matters in quant: Weekend revision is where short-term exposure becomes long-term memory.
- Core explanation: Simple view: spaced repetition means revisiting concepts before you forget them. Error logs stop you from making the same mistake again. Technical view: review after 1 day, 3 days, 7 days, and 14 days for weak items. Track not just what you got wrong, but why.
- Worked example: If you mixed up standard deviation and variance on Thursday, write the exact confusion, correct it, and schedule the next review date.
- Practice problems:
- Rewrite the 5 most important formulas from Week 1 without looking.
- List 3 concepts that still feel fuzzy and explain what exactly is confusing.
- Summarize Week 1 in one page.
- Coding task: Create a notebook section called 'market diary' and record one asset, one news item, one risk, and one numerical observation.
- Reflection: What did I understand best this week, and what did I only feel like I understood?

### Sun: Week 1 quiz and mini project: build a simple return and risk dashboard
- Why it matters in quant: A quant portfolio grows through small finished artifacts, not only reading.
- Core explanation: Simple view: combine your week's ideas into one small project. The goal is not sophistication yet; it is correctness and clarity. Technical view: take a price series, compute returns, summary statistics, cumulative wealth, and short written interpretation.
- Worked example: Use a toy series of 30 prices, convert to returns, compute mean, standard deviation, cumulative wealth from 100, and write whether the series looks smooth or noisy.
- Practice problems:
- Explain simple return, expected value, vectorized portfolio return, and standard deviation from memory.
- State one reason averages can be misleading in finance.
- State one difference between buy-side and sell-side quant work.
- Coding task: Finish the mini project notebook and write a 150-word conclusion aimed at a master's admissions reviewer.
- Reflection: If I had to show one thing from this week to a recruiter, would I be comfortable defending it?

## Concept Lessons
- Simple and multi-period returns
- Compounding and wealth paths
- Expected value and uncertainty
- Vectors and portfolio arithmetic
- Mean, volatility, and sampling intuition
- Market structure and asset classes

## Practice Tasks
- Compute returns by hand before coding them.
- Translate each finance formula into plain English and then back into notation.
- Keep an error log from Day 1 onward.
- Write one short market observation every day.

## Quiz / Checkpoint
By Sunday you should be able to explain return, compounding, expected value, volatility, and buy-side versus sell-side in your own words without notes.

## Weekend Revision and Mini Project
Build a simple return and risk dashboard from a toy price series, then write a short interpretation.

## Admissions Track
Write a one-paragraph baseline statement describing why you want Quant Finance after your AI master's and what skill gaps you are closing now.

## Interview / Job Track
Practice introducing yourself in 60 seconds: AI background, rebuilding math, target quant finance path.

## Interview Prep Questions and Model Answers
### Q: What is the difference between absolute price change and return?
A: Absolute price change is measured in currency units, like a stock moving from 100 to 105. Return scales that change by the starting price, so the same move becomes 5 percent. Quants prefer returns because they are comparable across instruments with different price levels.

### Q: Why does compounding matter in trading performance?
A: Trading performance builds on the current capital base, not the original base every day. That means gains and losses multiply over time. A strategy that ignores compounding can misstate growth, drawdown, and recovery needs.

### Q: How would you explain expected value to a trader?
A: Expected value is the average payoff if the same decision could be repeated many times under similar conditions. A trader can still lose on a single trade with positive expected value, but over a large sample that setup should be favorable if the assumptions are right.

### Q: What is the practical difference between buy-side and sell-side quant work?
A: Buy-side quants usually work closer to alpha generation, portfolio construction, and PnL ownership at hedge funds, prop firms, or asset managers. Sell-side quants at banks are more often focused on pricing, structuring, execution tools, risk, and supporting client or desk activity.

