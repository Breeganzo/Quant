# Week 01 Thu: Descriptive statistics, sampling intuition, and visualizing market data

**Estimated time:** 4 hours

## Study Blocks
- Block 1 (45 min): Understand mean, median, variance, and standard deviation.
- Block 2 (60 min): Relate volatility to risk and noise.
- Block 3 (45 min): Study outliers, skew, and why averages can mislead.
- Block 4 (60 min): Use pandas and plots for descriptive analysis.
- Block 5 (30 min): Practice and interview drill.

## Why It Matters In Quant
Before any model, a quant needs to understand the shape of the data: center, spread, skew, and outliers.

## Learning Overview
A quant should not fit a model to data before first understanding the shape of the data. Descriptive statistics are the first diagnostic layer.

This day builds the habit of asking: where is the center, how wide is the spread, are there outliers, and how much trust should I place in the average?

## Core Concepts
### Mean and median
- Simple explanation: The mean is the average. The median is the middle value after sorting.
- Technical depth: The sample mean is sensitive to extreme values, while the median is more robust when data contain outliers.
- Finance example: A few crisis days can drag the mean return down sharply even if most days were calm.

### Variance and standard deviation
- Simple explanation: These measure how spread out the data are. Standard deviation is easier to interpret because it is in the same units as the original data.
- Technical depth: For returns, standard deviation is commonly used as a volatility proxy. High volatility means outcomes vary more around the average.
- Finance example: Two assets can have the same average return but very different standard deviations, leading to very different risk profiles.

### Sampling uncertainty
- Simple explanation: A sample average is only an estimate. A different sample might give a different number.
- Technical depth: In finance, short samples are noisy. Apparent performance may be mostly sampling variation rather than genuine edge.
- Finance example: A backtest with 20 trades may look amazing mostly because of luck.

## Worked Examples
- Returns [0.01, 0.02, -0.01, 0.00] have mean 0.005 and sample standard deviation about 0.0129.
- One outlier return of -0.15 can change the sample mean materially even if the rest of the series is calm.
- Histograms reveal clustering, skew, and tails better than a single average number.

## Practice Questions With Answers
### Question: Why can two assets with the same mean return still feel very different to hold?
Answer: Because their volatility and downside behavior can differ a lot, changing drawdown and risk management demands.

### Question: Why is standard deviation often preferred over variance in communication?
Answer: Because it is in the same scale as the original data, making it easier to interpret.

### Question: Why should a quant look at plots before modeling?
Answer: Plots can reveal trends, outliers, missing values, and changing volatility that summary statistics alone may hide.

## Coding Task
Create a pandas Series of 20 toy returns and calculate mean, median, standard deviation, min, max, and a histogram.

## Daily Interview Drill
### Q: What does volatility mean in practice?
A: It is a measure of dispersion in returns and is often used as a simple proxy for how noisy or risky an asset is.

### Q: Why is the sample mean dangerous in finance?
A: Because financial data are noisy, non-stationary, and heavily influenced by outliers and regime changes.

## Reflection Question
When I look at a return series, do I immediately ask how noisy it is and whether the average is trustworthy?

## Completion Checklist
- I completed each study block or consciously rescheduled it.
- I rewrote the key formulas or concepts from memory.
- I finished the coding lab and checked the output.
- I added at least one item to the error log if something was unclear.
- I practiced at least one interview answer aloud.
