from __future__ import annotations

import json
import textwrap
from datetime import date, timedelta
from pathlib import Path

import nbformat as nbf
from nbclient import NotebookClient

from quant_learning.interview_packs import build_interview_pack
from quant_learning.month1_extensions import (
    detailed_day_notebook_spec,
    has_detailed_day,
    project_notebook_spec,
    render_detailed_day_markdown,
)
from quant_learning.week1_materials import (
    render_week1_day_markdown,
    week1_day_notebook_specs,
    week1_project_notebook_spec,
)


ROOT = Path(".")
CURRICULUM_DIR = ROOT / "curriculum"
DOCS_DIR = ROOT / "references"
TEMPLATES_DIR = ROOT / "templates"
START_DATE = date(2026, 4, 20)


def week_dates(week_number: int) -> str:
    start = START_DATE + timedelta(days=(week_number - 1) * 7)
    end = start + timedelta(days=6)
    return f"{start.isoformat()} to {end.isoformat()}"


def weekly_project_notebook_name(week_number: int) -> str:
    return (
        f"week-{week_number:02d}-capstone.ipynb"
        if week_number % 4 == 0
        else f"week-{week_number:02d}-mini-project.ipynb"
    )


def daily_session_plan(day_label: str) -> list[tuple[str, str, str]]:
    if day_label in {"Mon", "Tue", "Wed", "Thu", "Fri"}:
        return [
            ("Session 1", "35 min", "Recall yesterday's ideas and define today's learning outcome."),
            ("Session 2", "50 min", "Build intuition first, then formalize notation and key formulas."),
            ("Session 3", "45 min", "Work through trading, portfolio, and risk examples with interpretation."),
            ("Session 4", "50 min", "Run notebook labs, inspect outputs, and explain results in plain language."),
            ("Session 5", "20 min", "Interview drill, reflection, and error-log update."),
        ]
    return [
        ("Session 1", "25 min", "Closed-book recall and formula rewrite."),
        ("Session 2", "35 min", "High-value concept reinforcement with one worked example."),
        ("Session 3", "35 min", "Notebook review and one focused extension task."),
        ("Session 4", "25 min", "Interview-style explanation, reflection, and weekly checkpoint."),
    ]


def make_generic_day(day: str, topic: str, week_title: str, coding_task: str, reflection: str) -> dict:
    return {
        "day": day,
        "topic": topic,
        "estimated_time": "4 hours" if day in {"Mon", "Tue", "Wed", "Thu", "Fri"} else "2 hours",
        "why": f"{topic} is part of real quant work inside {week_title.lower()} research, trading, or risk workflows.",
        "core_explanation": (
            f"Start with intuition for {topic.lower()}, then restate it using the formal quantitative language used in finance and ML."
        ),
        "worked_example": f"Build one small finance example around {topic.lower()} and explain what the output would mean for a trader or risk analyst.",
        "practice_problems": [
            f"Explain {topic.lower()} in one paragraph without jargon.",
            f"Write down the main formula or workflow for {topic.lower()} from memory.",
            f"Connect {topic.lower()} to one trading, portfolio, or risk problem.",
        ],
        "coding_task": coding_task,
        "reflection": reflection,
        "session_plan": daily_session_plan(day),
    }


WEEK1_DAYS = [
    {
        "day": "Mon",
        "topic": "Reset your toolkit: numbers, variables, returns, and compounding",
        "why": "Quants constantly translate market moves into numbers. If returns and compounding are shaky, every later topic like portfolio optimization, forecasting, and risk measurement becomes confusing.",
        "core_explanation": (
            "Simple view: a return tells you how much an asset changed relative to where it started. "
            "If a stock goes from 100 to 105, the simple return is 5 percent. Compounding means today's gain changes tomorrow's base. "
            "Technical view: simple return is (P_t / P_(t-1)) - 1. Multi-period wealth evolves multiplicatively as W_t = W_0 * product(1 + r_t)."
        ),
        "worked_example": (
            "If prices are 100, 103, 101, 104 then returns are 3.0 percent, about -1.94 percent, and about 2.97 percent. "
            "One 3 percent gain and one 3 percent loss do not cancel perfectly because they act on different bases."
        ),
        "practice_problems": [
            "Compute the simple return from 50 to 55.",
            "Starting with 1000, apply returns of 10 percent and then -5 percent. What is final wealth?",
            "Why is compounding important when evaluating trading performance?",
        ],
        "coding_task": "In Python, create a list of 5 prices, convert them into returns, and calculate final wealth from an initial capital of 1000.",
        "reflection": "Did I understand returns as changes in relative terms, or was I still thinking only in absolute rupees or dollars?",
    },
    {
        "day": "Tue",
        "topic": "Functions, control flow, probability intuition, and expected value",
        "why": "Quant code is built from reusable functions, and quant decisions often reduce to expected value under uncertainty.",
        "core_explanation": (
            "Simple view: a function is a machine that takes input and gives output. Expected value is the weighted average outcome if we repeat a gamble many times. "
            "Technical view: for discrete outcomes, E[X] = sum p_i x_i. In trading, expected value helps separate lucky wins from positive-edge decisions."
        ),
        "worked_example": (
            "A trade wins 60 percent of the time with +2 and loses 40 percent with -1. Expected value is 0.6*2 + 0.4*(-1) = 0.8. "
            "That does not guarantee each trade wins, but the average payoff is positive."
        ),
        "practice_problems": [
            "Write a function that accepts buy price and sell price and returns the percentage return.",
            "Compute expected value for a strategy with 30 percent chance of +5 and 70 percent chance of -1.",
            "Why can a strategy with many wins still have negative expected value?",
        ],
        "coding_task": "Write a Python function for expected value of a discrete strategy and test it on 3 toy trading setups.",
        "reflection": "Do I naturally ask what the average payoff is, or do I get distracted by single wins and losses?",
    },
    {
        "day": "Wed",
        "topic": "Vectors, matrices, and linear algebra intuition for portfolios and ML",
        "why": "Portfolio weights, factor exposures, and ML features are easiest to understand as vectors and matrices.",
        "core_explanation": (
            "Simple view: a vector is an ordered list of numbers, like portfolio weights across assets. A matrix is a table of numbers, like data for many assets and many features. "
            "Technical view: if w is a weight vector and r is an asset return vector, portfolio return is w^T r. Covariance matrices measure how assets move together."
        ),
        "worked_example": (
            "If portfolio weights are [0.5, 0.3, 0.2] and returns are [0.02, -0.01, 0.03], the portfolio return is 0.5*0.02 + 0.3*(-0.01) + 0.2*0.03 = 0.013 or 1.3 percent."
        ),
        "practice_problems": [
            "Interpret a weight vector of [0.6, 0.4].",
            "Compute a 2-asset portfolio return with weights [0.7, 0.3] and returns [0.01, 0.04].",
            "Why does covariance matter in diversification?",
        ],
        "coding_task": "Use NumPy arrays to compute 3 portfolio returns from a matrix of asset returns and a vector of weights.",
        "reflection": "Can I explain a portfolio as a weighted combination of assets without getting lost in notation?",
    },
    {
        "day": "Thu",
        "topic": "Descriptive statistics, sampling intuition, and visualizing market data",
        "why": "Before any model, a quant needs to understand the shape of the data: center, spread, skew, and outliers.",
        "core_explanation": (
            "Simple view: mean tells you the average, standard deviation tells you how spread out values are, and a plot helps you spot structure. "
            "Technical view: for returns, volatility is often approximated by standard deviation. Sampling variation means the sample average is only an estimate of the true average."
        ),
        "worked_example": (
            "Two assets can have the same mean return but very different standard deviations. The lower-volatility asset is usually easier to size and risk-manage."
        ),
        "practice_problems": [
            "Compute mean and sample standard deviation for returns [0.01, 0.02, -0.01, 0.00].",
            "Why can one extreme outlier distort the mean?",
            "What does a histogram of returns help you see?",
        ],
        "coding_task": "Create a pandas Series of 20 toy returns and calculate mean, median, standard deviation, min, max, and a histogram.",
        "reflection": "When I look at a return series, do I immediately ask how noisy it is and whether the average is trustworthy?",
    },
    {
        "day": "Fri",
        "topic": "Market structure, asset classes, risk, return, and what quants actually do",
        "why": "You need a mental map of markets before learning pricing, forecasting, and strategy research.",
        "core_explanation": (
            "Simple view: markets connect buyers and sellers. Asset classes include equities, fixed income, FX, commodities, and derivatives. "
            "Technical view: each asset class has different return drivers, risks, liquidity, and microstructure. Quant roles sit across research, trading, structuring, risk, and execution."
        ),
        "worked_example": (
            "A quant researcher on the buy-side might test a momentum signal for equities, while a sell-side derivatives quant might build or calibrate an option pricing model for a bank's trading desk."
        ),
        "practice_problems": [
            "Name 5 asset classes and one major risk for each.",
            "Explain the difference between return and risk in simple terms.",
            "Why do transaction costs matter more in fast trading strategies?",
        ],
        "coding_task": "Build a markdown table in a notebook comparing 5 asset classes, their return drivers, and their main risks.",
        "reflection": "Which part of finance feels most interesting right now: markets, trading, risk, or pricing?",
    },
    {
        "day": "Sat",
        "topic": "Revision, spaced repetition, and first market diary notebook",
        "why": "Weekend revision is where short-term exposure becomes long-term memory.",
        "core_explanation": (
            "Simple view: spaced repetition means revisiting concepts before you forget them. Error logs stop you from making the same mistake again. "
            "Technical view: review after 1 day, 3 days, 7 days, and 14 days for weak items. Track not just what you got wrong, but why."
        ),
        "worked_example": (
            "If you mixed up standard deviation and variance on Thursday, write the exact confusion, correct it, and schedule the next review date."
        ),
        "practice_problems": [
            "Rewrite the 5 most important formulas from Week 1 without looking.",
            "List 3 concepts that still feel fuzzy and explain what exactly is confusing.",
            "Summarize Week 1 in one page.",
        ],
        "coding_task": "Create a notebook section called 'market diary' and record one asset, one news item, one risk, and one numerical observation.",
        "reflection": "What did I understand best this week, and what did I only feel like I understood?",
    },
    {
        "day": "Sun",
        "topic": "Week 1 quiz and mini project: build a simple return and risk dashboard",
        "why": "A quant portfolio grows through small finished artifacts, not only reading.",
        "core_explanation": (
            "Simple view: combine your week's ideas into one small project. The goal is not sophistication yet; it is correctness and clarity. "
            "Technical view: take a price series, compute returns, summary statistics, cumulative wealth, and short written interpretation."
        ),
        "worked_example": (
            "Use a toy series of 30 prices, convert to returns, compute mean, standard deviation, cumulative wealth from 100, and write whether the series looks smooth or noisy."
        ),
        "practice_problems": [
            "Explain simple return, expected value, vectorized portfolio return, and standard deviation from memory.",
            "State one reason averages can be misleading in finance.",
            "State one difference between buy-side and sell-side quant work.",
        ],
        "coding_task": "Finish the mini project notebook and write a 150-word conclusion aimed at a master's admissions reviewer.",
        "reflection": "If I had to show one thing from this week to a recruiter, would I be comfortable defending it?",
    },
]


WEEK_BLUEPRINTS = [
    {
        "week": 1,
        "title": "Reset Foundations: Python, returns, probability intuition, and market map",
        "objectives": [
            "Rebuild confidence with core arithmetic, compounding, expected value, and descriptive statistics.",
            "Reconnect Python basics to finance examples instead of abstract exercises.",
            "Understand what quants, traders, and risk teams actually do across markets.",
        ],
        "daily_schedule": WEEK1_DAYS,
        "concepts": [
            "Simple and multi-period returns",
            "Compounding and wealth paths",
            "Expected value and uncertainty",
            "Vectors and portfolio arithmetic",
            "Mean, volatility, and sampling intuition",
            "Market structure and asset classes",
        ],
        "practice_tasks": [
            "Compute returns by hand before coding them.",
            "Translate each finance formula into plain English and then back into notation.",
            "Keep an error log from Day 1 onward.",
            "Write one short market observation every day.",
        ],
        "checkpoint": "By Sunday you should be able to explain return, compounding, expected value, volatility, and buy-side versus sell-side in your own words without notes.",
        "weekend_project": "Build a simple return and risk dashboard from a toy price series, then write a short interpretation.",
        "admissions_track": "Write a one-paragraph baseline statement describing why you want Quant Finance after your AI master's and what skill gaps you are closing now.",
        "interview_track": "Practice introducing yourself in 60 seconds: AI background, rebuilding math, target quant finance path.",
    },
    {
        "week": 2,
        "title": "Data and Linear Algebra: NumPy, pandas, visualization, diversification, and SQL basics",
        "objectives": [
            "Use Python tools the way a quant researcher actually uses them: arrays, tables, plots, and joins.",
            "Build intuition for vectors, covariance, correlation, and diversification.",
            "Create a clean workflow for structured market data.",
        ],
        "day_topics": [
            "NumPy arrays, vectorization, and speed intuition",
            "pandas DataFrames, indexing, joins, and missing values",
            "Plotting and exploratory data analysis for prices and returns",
            "Correlation, covariance, and diversification",
            "Portfolio weights, rebalancing, cumulative performance, and SQL workflow",
            "Revision, error log, and data workflow drill",
            "Mini project: compare three assets and explain diversification",
        ],
        "concepts": [
            "Array operations and broadcasting",
            "Data cleaning",
            "Covariance matrices",
            "Diversification math",
            "SQL select, filter, group by, and joins",
        ],
        "practice_tasks": [
            "Clean a messy price table with missing values.",
            "Compare simple versus vectorized computations.",
            "Compute a correlation matrix and interpret it economically.",
            "Write 5 basic SQL queries on toy market data.",
        ],
        "checkpoint": "Can you clean a price table, compute returns, plot them, and explain why low correlation can reduce portfolio risk?",
        "weekend_project": "Create a three-asset comparison notebook with tables, plots, and a diversification conclusion.",
        "admissions_track": "Start a scholarship and university tracker with columns for country, tuition, living cost, deadline, prerequisites, and scholarship notes.",
        "interview_track": "Practice explaining covariance and diversification in plain English.",
    },
    {
        "week": 3,
        "title": "Math Rebuild I: Algebra, calculus intuition, probability rules, APIs, and Monte Carlo thinking",
        "objectives": [
            "Restart math from the base rather than pretending old knowledge is still solid.",
            "Connect algebra, calculus, and probability to pricing, optimization, and forecasting.",
            "Pull data from APIs and understand uncertainty through simulation intuition.",
        ],
        "day_topics": [
            "Algebra refresher: equations, fractions, exponents, and logs",
            "Calculus intuition: slopes, derivatives, and sensitivity",
            "Integrals, accumulation, and area intuition",
            "Probability rules, random variables, and distributions",
            "APIs, JSON, conditional probability, and Bayes intuition",
            "Revision, recall, and formula consolidation",
            "Mini project: expected value and Monte Carlo trade simulation",
        ],
        "concepts": [
            "Exponents and logarithms",
            "Derivatives as rates of change",
            "Probability spaces",
            "Conditional probability",
            "Monte Carlo intuition",
        ],
        "practice_tasks": [
            "Solve 10 algebra problems without a calculator first.",
            "Relate derivatives to option Greeks and optimization intuition.",
            "Pull and inspect one JSON payload from a finance API.",
            "Simulate repeated trade outcomes and summarize the distribution.",
        ],
        "checkpoint": "Can you explain derivative, probability, and Bayes in plain language and connect them to finance decisions?",
        "weekend_project": "Build a Monte Carlo notebook for a simple trading payoff and interpret expected value versus realized variance.",
        "admissions_track": "Draft a target-program shortlist of 12 programs across the US, UK, Europe, Singapore, and Canada.",
        "interview_track": "Start a notebook of mental math drills: logs, percentages, expected value, and conditional probability.",
    },
    {
        "week": 4,
        "title": "Math Rebuild II: Statistics, inference, regression, optimization, and portfolio theory",
        "objectives": [
            "Move from descriptive statistics to inference and modeling.",
            "Understand the basic logic of regression and optimization.",
            "Build your first portfolio-style capstone with clean documentation.",
        ],
        "day_topics": [
            "Sampling, estimators, bias, and variance",
            "Confidence intervals and hypothesis testing intuition",
            "OLS regression intuition and interpretation",
            "Optimization basics and constrained thinking",
            "Portfolio theory, efficient frontier, and Sharpe ratio intuition",
            "Capstone build day",
            "Capstone review and write-up",
        ],
        "concepts": [
            "Bias-variance trade-off",
            "Confidence intervals",
            "Linear regression",
            "Optimization constraints",
            "Portfolio risk-return trade-offs",
        ],
        "practice_tasks": [
            "Interpret regression coefficients economically.",
            "Compute a t-stat style intuition rather than memorizing symbols only.",
            "Build a simple mean-variance comparison across portfolios.",
            "Explain why backtests based on tiny samples are dangerous.",
        ],
        "checkpoint": "Can you explain regression, overfitting risk, and the efficient frontier without equations first, then with equations?",
        "weekend_project": "Capstone 1: exploratory asset allocation study.",
        "admissions_track": "Create CV version 1 with education, AI background, finance interest, and first mini projects.",
        "interview_track": "Practice regression and Sharpe ratio explanations aloud.",
        "capstone": {
            "problem_statement": "Compare a small set of assets, estimate returns and volatility, and design a basic diversified portfolio with a clear risk narrative.",
            "data_sources": "Use Yahoo Finance via yfinance or a cleaned CSV with daily prices for ETFs such as SPY, TLT, GLD, and EEM.",
            "steps": "Download data, clean missing values, compute returns, summarize descriptive statistics, compare correlations, test a few weight vectors, and write a one-page conclusion.",
            "metrics": "Annualized return, annualized volatility, Sharpe ratio, max drawdown, and clarity of written interpretation.",
            "mistakes": "Using price levels instead of returns, annualizing incorrectly, ignoring missing data, or treating one short sample as universal truth.",
        },
    },
    {
        "week": 5,
        "title": "ML Foundations I: supervised learning, regression, features, and train-test discipline",
        "objectives": [
            "Frame finance questions as prediction problems only when the setup makes sense.",
            "Understand labels, features, loss functions, and model evaluation.",
            "Learn how leakage starts before the model, during data design.",
        ],
        "day_topics": [
            "Prediction problems in finance: what are we forecasting?",
            "Linear regression as an ML baseline",
            "Feature engineering from price and volume data",
            "Train, validation, test split and leakage",
            "Regularization and overfitting intuition",
            "Mini research lab on next-day return prediction",
            "Review and checkpoint",
        ],
        "concepts": [
            "Labels and features",
            "Loss functions",
            "Train-validation-test discipline",
            "Feature leakage",
            "Regularization",
        ],
        "practice_tasks": [
            "Design good and bad labels for a return prediction problem.",
            "Build a baseline regression before trying complex models.",
            "Write down 5 examples of leakage in finance ML.",
            "Explain why weak alpha can vanish after transaction costs.",
        ],
        "checkpoint": "Can you design a small supervised learning problem in finance without leaking future information?",
        "weekend_project": "Forecast a simple target such as next-day sign or next-week return using baseline tabular features.",
        "admissions_track": "Map each target master's program to prerequisite gaps: calculus, linear algebra, probability, finance, programming.",
        "interview_track": "Practice answering: what is overfitting and why is it dangerous in finance?",
    },
    {
        "week": 6,
        "title": "ML Foundations II: classification, metrics, imbalance, validation, and risk use cases",
        "objectives": [
            "Understand classification beyond accuracy.",
            "Connect ML evaluation to finance costs and asymmetric errors.",
            "Use cross-validation carefully in non-iid settings.",
        ],
        "day_topics": [
            "Classification intuition and decision boundaries",
            "Confusion matrix, precision, recall, F1, and ROC-AUC",
            "Class imbalance and cost-sensitive decisions",
            "Cross-validation, resampling, and model stability",
            "Credit risk and event prediction examples",
            "Mini lab: classify positive versus negative future returns",
            "Review and error-log day",
        ],
        "concepts": [
            "Binary classification",
            "Evaluation metrics",
            "Imbalanced data",
            "Cross-validation",
            "Threshold selection",
        ],
        "practice_tasks": [
            "Compare accuracy with precision and recall on an imbalanced example.",
            "Explain why a 55 percent hit rate can still lose money.",
            "Run a small classification baseline and inspect threshold effects.",
            "Write one paragraph on why finance labels are noisy.",
        ],
        "checkpoint": "Can you explain when ROC-AUC is helpful and when it hides economically important errors?",
        "weekend_project": "Build a classification notebook and compare statistical metrics with simple PnL intuition.",
        "admissions_track": "Draft a recommender list: academic, professional, and backup recommender candidates.",
        "interview_track": "Practice confusion matrix interpretation without looking at notes.",
    },
    {
        "week": 7,
        "title": "Unsupervised Learning: clustering, PCA, latent structure, and factor intuition",
        "objectives": [
            "Learn when unlabeled structure matters in markets.",
            "Understand dimensionality reduction and common drivers.",
            "Connect latent structure to factor investing and regime grouping.",
        ],
        "day_topics": [
            "Unsupervised learning overview",
            "Clustering assets and regimes",
            "PCA and variance decomposition",
            "Factor intuition and common risk drivers",
            "Feature compression and dimensionality reduction",
            "Mini lab: cluster assets by behavior",
            "Review and communication practice",
        ],
        "concepts": [
            "Clustering",
            "Distance metrics",
            "Principal components",
            "Latent factors",
            "Dimensionality reduction",
        ],
        "practice_tasks": [
            "Interpret the first principal component economically.",
            "Explain why clustering can be unstable.",
            "Relate factor intuition to diversification and risk.",
            "Summarize one unsupervised finance use case.",
        ],
        "checkpoint": "Can you explain PCA as 'common movement directions' before using any matrix language?",
        "weekend_project": "Group a small asset universe by behavior and describe possible factor interpretations.",
        "admissions_track": "Update CV and GitHub README with first three mini projects.",
        "interview_track": "Practice explaining PCA and clustering in 90 seconds.",
    },
    {
        "week": 8,
        "title": "Time Series I: stationarity, AR/MA/ARIMA intuition, walk-forward testing, and forecasting",
        "objectives": [
            "Shift from iid thinking to ordered time-dependent data.",
            "Understand stationarity and why it matters for forecasting.",
            "Build a simple forecasting capstone with strong evaluation discipline.",
        ],
        "day_topics": [
            "What makes time series different from tabular data?",
            "Stationarity, trends, seasonality, and differencing",
            "AR, MA, and ARIMA intuition",
            "Autocorrelation, partial autocorrelation, and lag structure",
            "Walk-forward validation and forecast error metrics",
            "Capstone build day",
            "Capstone review and write-up",
        ],
        "concepts": [
            "Stationarity",
            "Autocorrelation",
            "AR/MA/ARIMA",
            "Walk-forward validation",
            "Forecast evaluation",
        ],
        "practice_tasks": [
            "Differentiate trend from mean reversion.",
            "Plot lags and interpret autocorrelation.",
            "Compare naive, moving-average, and AR baselines.",
            "Explain why shuffled cross-validation is wrong for time series forecasting.",
        ],
        "checkpoint": "Can you justify a walk-forward split and explain stationarity in trading language?",
        "weekend_project": "Capstone 2: baseline forecasting lab on returns or volatility proxy.",
        "admissions_track": "Write a draft paragraph for your SOP on why you are moving from AI into finance quantitatively.",
        "interview_track": "Practice AR and mean reversion intuition verbally.",
        "capstone": {
            "problem_statement": "Forecast a simple financial time series baseline and compare it against naive rules.",
            "data_sources": "Use a daily ETF series or FX pair from yfinance; for safer modeling, focus on rolling volatility or spread changes instead of raw prices.",
            "steps": "Clean the data, check stationarity visually, define a target, split with walk-forward validation, fit naive and time-series baselines, and compare errors.",
            "metrics": "MAE, RMSE, directional accuracy if relevant, and economic interpretation of forecast usefulness.",
            "mistakes": "Forecasting price levels without understanding non-stationarity, leaking future data into features, or celebrating tiny statistical gains with no economic meaning.",
        },
    },
    {
        "week": 9,
        "title": "Finance Core I: market microstructure, execution, slippage, and transaction costs",
        "objectives": [
            "Understand how real trading differs from theoretical signals.",
            "Learn how orders, liquidity, and execution quality affect strategy viability.",
            "Connect research output to trade implementation.",
        ],
        "day_topics": [
            "Market microstructure and order books",
            "Bid-ask spread, liquidity, and adverse selection",
            "Order types and execution choices",
            "Transaction costs and slippage models",
            "Turnover, holding period, and capacity intuition",
            "Mini lab: strategy before and after costs",
            "Review and trading diary",
        ],
        "concepts": [
            "Order book basics",
            "Bid-ask spread",
            "Market versus limit orders",
            "Slippage",
            "Capacity constraints",
        ],
        "practice_tasks": [
            "Explain why gross alpha is not net alpha.",
            "Estimate rough transaction costs for a high-turnover signal.",
            "Compare market and limit order trade-offs.",
            "Write a short note on why capacity matters more for some strategies than others.",
        ],
        "checkpoint": "Can you explain why a strategy that looks good in a notebook can fail in execution?",
        "weekend_project": "Add simple cost assumptions to an earlier toy signal and compare net performance.",
        "admissions_track": "Shortlist 3 professors or industry practitioners you may want recommendation letters from by 2027.",
        "interview_track": "Practice answering: what is slippage and why is it dangerous in backtests?",
    },
    {
        "week": 10,
        "title": "Finance Core II: portfolio theory, CAPM, factor investing, and optimization",
        "objectives": [
            "Understand the language of portfolio construction used across buy-side and risk roles.",
            "Connect expected return, covariance, and optimization.",
            "Introduce factor thinking before moving into cross-sectional alphas.",
        ],
        "day_topics": [
            "Markowitz portfolio intuition",
            "Efficient frontier and Sharpe ratio",
            "CAPM and beta intuition",
            "Factor investing basics",
            "Risk budgeting and constraints",
            "Mini lab: factor exposure overview",
            "Review and checkpoint",
        ],
        "concepts": [
            "Mean-variance optimization",
            "Sharpe ratio",
            "CAPM",
            "Beta and factors",
            "Risk budgeting",
        ],
        "practice_tasks": [
            "Compute beta for a toy example.",
            "Explain why estimated expected returns are fragile.",
            "Describe 3 practical portfolio constraints.",
            "Connect factor exposures to economic narratives.",
        ],
        "checkpoint": "Can you explain factor investing as a systematic bet on common drivers rather than individual stock stories?",
        "weekend_project": "Estimate simple factor exposures or factor-like group comparisons for a small asset set.",
        "admissions_track": "Begin a scholarship matrix with application opening dates, essays, and funding type.",
        "interview_track": "Practice CAPM and beta explanations without equations first.",
    },
    {
        "week": 11,
        "title": "Finance Core III: fixed income, yield curves, duration, convexity, and credit basics",
        "objectives": [
            "Build the fixed income foundation required by serious quant finance programs.",
            "Understand rate sensitivity and bond pricing intuition.",
            "Connect yield curves to macro and risk management.",
        ],
        "day_topics": [
            "Bond cash flows and discounting",
            "Yield, yield curve, and term structure intuition",
            "Duration and interest rate sensitivity",
            "Convexity and nonlinear bond behavior",
            "Credit spreads and default risk basics",
            "Mini lab: simple bond price sensitivity",
            "Review and recap",
        ],
        "concepts": [
            "Bond pricing",
            "Yield curves",
            "Duration",
            "Convexity",
            "Credit spreads",
        ],
        "practice_tasks": [
            "Explain why longer-duration bonds move more when rates change.",
            "Interpret a steep versus inverted yield curve.",
            "Compute rough price sensitivity from duration.",
            "Connect credit spreads to perceived default risk.",
        ],
        "checkpoint": "Can you explain duration in words and use it as an approximation for bond price risk?",
        "weekend_project": "Create a one-page bond sensitivity note with toy numbers.",
        "admissions_track": "Add any missing quantitative prerequisites to your application prep tracker.",
        "interview_track": "Practice bond pricing and duration questions aloud.",
    },
    {
        "week": 12,
        "title": "Finance Core IV: derivatives, options, Greeks, hedging, and risk management",
        "objectives": [
            "Build options intuition from payoff diagrams to risk sensitivities.",
            "Understand why derivatives are central to modern quant roles.",
            "Complete a capstone that links pricing intuition to risk scenarios.",
        ],
        "day_topics": [
            "Forwards, futures, and option payoffs",
            "Calls, puts, and payoff diagrams",
            "Option Greeks intuition",
            "Volatility smile and pricing inputs",
            "Risk management: VaR, stress, and scenarios",
            "Capstone build day",
            "Capstone review and write-up",
        ],
        "concepts": [
            "Derivative contracts",
            "Option payoffs",
            "Delta, gamma, vega, theta",
            "Volatility input intuition",
            "Scenario-based risk management",
        ],
        "practice_tasks": [
            "Draw basic payoff diagrams by hand.",
            "Explain delta as sensitivity rather than memorizing a Greek.",
            "Connect volatility assumptions to option value.",
            "Describe the difference between hedging and speculation.",
        ],
        "checkpoint": "Can you explain why options are nonlinear and why Greeks matter for risk control?",
        "weekend_project": "Capstone 3: options and scenario-risk mini project.",
        "admissions_track": "Write the first full draft of your CV bullet points for the first 3 capstones.",
        "interview_track": "Practice payoff and Greek intuition questions.",
        "capstone": {
            "problem_statement": "Build a mini option-risk notebook that explains payoffs, Greeks intuition, and scenario behavior for a small set of option positions.",
            "data_sources": "Use toy option parameters, public option chain snapshots if available, or synthetic examples.",
            "steps": "Define payoff functions, explore parameter changes, simulate simple scenarios, and write a risk memo explaining exposures.",
            "metrics": "Correct payoff logic, coherent scenario analysis, clarity of Greek interpretation, and quality of written communication.",
            "mistakes": "Confusing payoff with profit, ignoring premium cost, using formulas without understanding what drives sensitivity, and skipping written interpretation.",
        },
    },
    {
        "week": 13,
        "title": "Quant Workflow I: idea generation, research logs, labels, and data hygiene",
        "objectives": [
            "Move from isolated topics into a repeatable research workflow.",
            "Learn to form alpha hypotheses and document them clearly.",
            "Strengthen research hygiene before more serious backtesting.",
        ],
        "day_topics": [
            "What makes a good quant hypothesis?",
            "Signal design and economic reasoning",
            "Label design and target horizon choice",
            "Data cleaning, survivorship bias, and look-ahead bias",
            "Research logging and experiment notebooks",
            "Mini lab: define one alpha hypothesis cleanly",
            "Review and refinement",
        ],
        "concepts": [
            "Hypothesis-driven research",
            "Signal definition",
            "Data hygiene",
            "Look-ahead bias",
            "Research documentation",
        ],
        "practice_tasks": [
            "Write 3 alpha ideas and reject 2 of them with logic.",
            "List at least 5 data-quality pitfalls in quant research.",
            "Design one clean signal with clear economic story and holding period.",
            "Start a formal research log template for all future projects.",
        ],
        "checkpoint": "Can you explain one alpha idea with data source, target horizon, and failure mode?",
        "weekend_project": "Turn one weak trading idea into a structured research hypothesis document.",
        "admissions_track": "Start collecting unofficial transcripts, course syllabi, and test requirement notes for target schools.",
        "interview_track": "Practice discussing one research idea with both intuition and caution.",
    },
    {
        "week": 14,
        "title": "Quant Workflow II: backtesting architecture, position sizing, and performance attribution",
        "objectives": [
            "Learn how to test strategies in a way that does not fool you.",
            "Understand position sizing, turnover, and risk constraints.",
            "Start thinking like a PM or risk manager, not only a model builder.",
        ],
        "day_topics": [
            "Backtesting workflow from signal to trades",
            "Look-ahead, survivorship, and data snooping pitfalls",
            "Position sizing and exposure control",
            "Turnover, slippage, and implementation realism",
            "Performance attribution and diagnostics",
            "Mini lab: backtest a toy rule with costs",
            "Review and write-up",
        ],
        "concepts": [
            "Backtesting pipeline",
            "Bias pitfalls",
            "Position sizing",
            "Risk constraints",
            "Attribution",
        ],
        "practice_tasks": [
            "List every place future information can leak into a backtest.",
            "Compare equal-weight, volatility-scaled, and capped position sizing.",
            "Write a short performance attribution note for a toy strategy.",
            "State why a high Sharpe ratio can still be fragile.",
        ],
        "checkpoint": "Can you name the most common reasons a backtest overstates real performance?",
        "weekend_project": "Build a small backtest notebook with explicit assumptions and diagnostics.",
        "admissions_track": "Create a project narrative template: problem, data, method, result, limitations, and next step.",
        "interview_track": "Practice backtesting-pitfall questions.",
    },
    {
        "week": 15,
        "title": "Signals I: momentum, mean reversion, cross-sectional signals, and attribution",
        "objectives": [
            "Study classic alpha families used in practice and interviews.",
            "Understand where momentum and mean reversion come from.",
            "Compare time-series and cross-sectional thinking.",
        ],
        "day_topics": [
            "Momentum intuition and empirical logic",
            "Mean reversion intuition and failure modes",
            "Cross-sectional ranking signals",
            "Signal combination and normalization",
            "Attribution: what is actually driving PnL?",
            "Mini lab: compare momentum versus mean reversion rule",
            "Review and critique",
        ],
        "concepts": [
            "Momentum",
            "Mean reversion",
            "Cross-sectional ranking",
            "Signal normalization",
            "Performance attribution",
        ],
        "practice_tasks": [
            "Write the economic story behind one momentum and one mean reversion signal.",
            "Explain when mean reversion is more plausible than trend following.",
            "Normalize two signals with different scales.",
            "Compare the turnover implications of both strategy families.",
        ],
        "checkpoint": "Can you explain why the same raw return series may support one signal and reject another depending on horizon and costs?",
        "weekend_project": "Run a toy comparison of momentum and mean reversion on one instrument or spread.",
        "admissions_track": "Update CV and GitHub with your stronger signal and backtesting artifacts.",
        "interview_track": "Practice signal-design questions on paper.",
    },
    {
        "week": 16,
        "title": "Signals II: factor models, statistical arbitrage intuition, cointegration, and regime shifts",
        "objectives": [
            "Move from classic signals to more structured relative-value thinking.",
            "Understand statistical arbitrage only after the foundations are stable.",
            "Complete a capstone that combines signal logic with regime awareness.",
        ],
        "day_topics": [
            "Factor models and common risk decomposition",
            "Residual signals and relative-value intuition",
            "Cointegration and spread logic",
            "Regime shifts and model instability",
            "Cross-sectional portfolio construction",
            "Capstone build day",
            "Capstone review and write-up",
        ],
        "concepts": [
            "Factor models",
            "Residual returns",
            "Cointegration intuition",
            "Regime shifts",
            "Cross-sectional portfolio building",
        ],
        "practice_tasks": [
            "Explain the difference between correlation and cointegration.",
            "Describe why regimes break historical relationships.",
            "Interpret residuals as a potential signal with caution.",
            "Write a short memo on why stat arb can fail in crowded markets.",
        ],
        "checkpoint": "Can you explain factor-neutral thinking and spread intuition without overselling it as easy alpha?",
        "weekend_project": "Capstone 4: factor/signal research note with regime discussion.",
        "admissions_track": "Create a two-page project portfolio summary for applications.",
        "interview_track": "Practice factor-model and stat-arb intuition questions.",
        "capstone": {
            "problem_statement": "Research one cross-sectional or spread-based signal, evaluate it carefully, and discuss regime sensitivity.",
            "data_sources": "Use a small liquid equity ETF set, sector ETFs, or a few related instruments with public daily data.",
            "steps": "Define the signal, standardize data, test a simple portfolio rule, include transaction-cost assumptions, and analyze periods where it works or fails.",
            "metrics": "Sharpe ratio, turnover, drawdown, hit rate, stability across subperiods, and quality of failure analysis.",
            "mistakes": "Assuming stationarity, overfitting thresholds, ignoring crowding and costs, and reporting only the best period.",
        },
    },
    {
        "week": 17,
        "title": "ML for Quant I: trees, ensembles, nonlinear interactions, and model interpretation",
        "objectives": [
            "Go beyond linear baselines while keeping financial discipline.",
            "Understand when nonlinear models add value and when they just overfit.",
            "Practice interpretation and robustness checks.",
        ],
        "day_topics": [
            "Decision trees and rule-based splits",
            "Random forests and bagging intuition",
            "Gradient boosting intuition",
            "Feature importance and interpretation caveats",
            "Model risk and stability across regimes",
            "Mini lab: nonlinear tabular finance model",
            "Review and limitations",
        ],
        "concepts": [
            "Decision trees",
            "Random forests",
            "Gradient boosting",
            "Feature importance",
            "Model risk",
        ],
        "practice_tasks": [
            "Compare a linear and tree-based model on the same features.",
            "Explain why a feature importance score is not causal proof.",
            "Inspect whether the nonlinear model is stable across splits.",
            "Write down one reason complex models often fail in finance.",
        ],
        "checkpoint": "Can you defend when not to use a more complex model?",
        "weekend_project": "Build a nonlinear baseline and compare it honestly to a linear benchmark.",
        "admissions_track": "Refine SOP bullet points around AI-to-Quant transition with concrete evidence from your projects.",
        "interview_track": "Practice bias-variance and model-complexity questions.",
    },
    {
        "week": 18,
        "title": "ML for Quant II: volatility, EWMA, GARCH intuition, risk forecasting, and stress testing",
        "objectives": [
            "Treat volatility as a first-class object in trading and risk.",
            "Learn why volatility clusters and why static risk estimates fail.",
            "Connect forecasting to practical risk control.",
        ],
        "day_topics": [
            "Volatility clustering and stylized facts",
            "Rolling volatility and EWMA",
            "GARCH intuition and limitations",
            "Forecast evaluation for risk models",
            "Stress testing and scenario design",
            "Mini lab: volatility forecast comparison",
            "Review and risk memo",
        ],
        "concepts": [
            "Volatility clustering",
            "EWMA",
            "GARCH intuition",
            "Risk forecasting",
            "Stress testing",
        ],
        "practice_tasks": [
            "Explain why volatility is more predictable than returns in many settings.",
            "Compare rolling volatility and EWMA conceptually.",
            "Describe what a stress scenario should include.",
            "Write a short note on model limitations in turbulent regimes.",
        ],
        "checkpoint": "Can you explain why risk models should be challenged with scenarios, not trusted mechanically?",
        "weekend_project": "Forecast a volatility proxy and explain how you would use it in sizing or risk control.",
        "admissions_track": "Prepare a clean master spreadsheet of all application materials and deadlines.",
        "interview_track": "Practice volatility and risk questions.",
    },
    {
        "week": 19,
        "title": "Agentic AI for Quant I: research automation, literature review, idea generation, and guardrails",
        "objectives": [
            "Use AI as a disciplined research assistant rather than a shortcut machine.",
            "Learn where agentic workflows help in quant research.",
            "Build explicit safeguards against hallucination, leakage, and false confidence.",
        ],
        "day_topics": [
            "What agentic AI can and cannot do in quant",
            "Literature summarization and idea extraction",
            "Feature brainstorming and hypothesis generation",
            "Code review assistants and debugging workflow",
            "Guardrails: hallucination, leakage, benchmark cheating",
            "Mini lab: AI-assisted research memo",
            "Review and policy checklist",
        ],
        "concepts": [
            "Research automation",
            "Structured prompting",
            "Verification discipline",
            "Hallucination risk",
            "Human-in-the-loop workflows",
        ],
        "practice_tasks": [
            "Write one agent prompt to summarize a paper and one prompt to challenge the summary.",
            "List 5 ways AI can accidentally leak future information into a strategy workflow.",
            "Use AI to generate features, then manually reject weak ones.",
            "Create a personal verification checklist for all AI-assisted work.",
        ],
        "checkpoint": "Can you explain why agentic AI is strongest in support roles and weakest when asked to invent trustworthy alpha without verification?",
        "weekend_project": "Build a research memo workflow where AI proposes ideas and you verify or reject them.",
        "admissions_track": "Decide whether to position yourself as AI-for-finance, pure quant finance, or hybrid research candidate in your applications.",
        "interview_track": "Practice speaking about AI in finance with both enthusiasm and skepticism.",
    },
    {
        "week": 20,
        "title": "Agentic AI for Quant II: alternative data, NLP, experiment tracking, and robust research delivery",
        "objectives": [
            "Extend AI usage into text and alternative data with strong controls.",
            "Track experiments and decisions like a serious researcher.",
            "Complete a capstone that combines quant method with AI support responsibly.",
        ],
        "day_topics": [
            "Alternative data and when it is useful",
            "NLP and sentiment feature intuition",
            "Experiment tracking and reproducibility",
            "Research report generation with AI support",
            "Robustness checks and final validation",
            "Capstone build day",
            "Capstone review and write-up",
        ],
        "concepts": [
            "Alternative data",
            "Text features",
            "Experiment tracking",
            "Reproducibility",
            "Robust validation",
        ],
        "practice_tasks": [
            "Define one alternative data idea and one reason it may fail.",
            "Turn text into a simple numeric signal carefully.",
            "Record every experiment setting in a structured log.",
            "State which parts of the workflow rely on AI and how you verified them.",
        ],
        "checkpoint": "Can you prove that your process is reproducible and not just a one-off notebook?",
        "weekend_project": "Capstone 5: AI-assisted quant research artifact with documentation and controls.",
        "admissions_track": "Write a scholarship narrative draft emphasizing global mobility, quantitative readiness, and project-based evidence.",
        "interview_track": "Practice describing one AI-assisted project with strong guardrails.",
        "capstone": {
            "problem_statement": "Build a documented research artifact that uses AI support for one part of the workflow while keeping the core quantitative logic verifiable.",
            "data_sources": "Use price data, simple text headlines, or a synthetic research corpus plus public market data.",
            "steps": "Define the question, separate AI-assisted and fully verified steps, implement a reproducible notebook, document prompts and checks, and write a concise report.",
            "metrics": "Reproducibility, clarity of verification process, predictive or explanatory usefulness, and professionalism of final presentation.",
            "mistakes": "Letting AI invent facts, failing to version prompts or assumptions, mixing future information into features, and not keeping a manual validation trail.",
        },
    },
    {
        "week": 21,
        "title": "Admissions Track I: target programs, scholarships, SOP structure, and recommendation strategy",
        "objectives": [
            "Turn your technical progress into a master's application strategy.",
            "Match your profile to programs by prerequisites, cost, and scholarship potential.",
            "Build a strong narrative from AI to quant finance credibly.",
        ],
        "day_topics": [
            "Program tiers and fit analysis",
            "Scholarship matrix and funding logic",
            "SOP structure: past, pivot, proof, future",
            "Recommendation strategy and evidence package",
            "CV and project narrative refinement",
            "Mini lab: draft your application story",
            "Review and evidence gap check",
        ],
        "concepts": [
            "Program fit",
            "Scholarship targeting",
            "Narrative coherence",
            "Recommendation planning",
            "Evidence-led SOP writing",
        ],
        "practice_tasks": [
            "Sort schools into reach, target, and safe buckets.",
            "Write a 200-word career transition story.",
            "Create a recommender briefing sheet with your goals and evidence.",
            "Audit missing requirements like GRE, TOEFL/IELTS, or prerequisite proofs if relevant.",
        ],
        "checkpoint": "Can you explain why each target school makes sense for your background and goals?",
        "weekend_project": "Produce a draft application packet: SOP outline, CV draft, shortlist, scholarship tracker.",
        "admissions_track": "This entire week is the admissions track. Start drafting actual artifacts.",
        "interview_track": "Practice the master's admissions question: why this field, why now, why you?",
    },
    {
        "week": 22,
        "title": "Interview Prep I: probability, statistics, mental math, Python, SQL, and markets discussion",
        "objectives": [
            "Build the interview muscle needed for quant and finance roles.",
            "Strengthen speed and clarity under pressure.",
            "Review core topics from the full plan in drill format.",
        ],
        "day_topics": [
            "Probability drills and expected value",
            "Statistics and regression drills",
            "Linear algebra and optimization drills",
            "Python and NumPy drills",
            "SQL and data reasoning drills",
            "Markets and finance discussion drills",
            "Mock interview day",
        ],
        "concepts": [
            "Mental math",
            "Probabilistic reasoning",
            "Coding clarity",
            "Data querying",
            "Market communication",
        ],
        "practice_tasks": [
            "Answer 10 short probability questions without external help.",
            "Solve 5 Python mini-problems on arrays and loops.",
            "Write 5 SQL queries from scratch.",
            "Explain one current market move and one quant project clearly.",
        ],
        "checkpoint": "Can you stay calm and structured when asked short technical questions aloud?",
        "weekend_project": "Simulate a 45-minute interview with mixed math, coding, and finance questions.",
        "admissions_track": "Refine your project portfolio so it supports interviews as well as applications.",
        "interview_track": "This entire week is interview-heavy. Time every drill.",
    },
    {
        "week": 23,
        "title": "Interview Prep II: portfolio polish, GitHub presentation, networking, and mock case defense",
        "objectives": [
            "Package your work so admissions committees and employers can understand it quickly.",
            "Practice defending limitations, not just results.",
            "Build a professional public-facing project story.",
        ],
        "day_topics": [
            "GitHub cleanup and repository storytelling",
            "Project README writing and visual clarity",
            "Networking and outreach messages",
            "Case-study presentation and limitations defense",
            "Behavioral stories for finance roles",
            "Mock presentation day",
            "Review and polish",
        ],
        "concepts": [
            "Project communication",
            "Professional presentation",
            "Networking hygiene",
            "Behavioral interview structure",
            "Limitations-first thinking",
        ],
        "practice_tasks": [
            "Rewrite one project README for clarity and credibility.",
            "Draft 3 concise outreach messages to alumni or professionals.",
            "Practice answering: what would you improve if given one more month?",
            "Record a 5-minute voice explanation of one capstone.",
        ],
        "checkpoint": "Can a stranger understand your strongest project in under 3 minutes?",
        "weekend_project": "Create a portfolio landing summary across all capstones and mini projects.",
        "admissions_track": "Prepare finalized recommender briefing documents and updated CV.",
        "interview_track": "Practice defending assumptions and limitations.",
    },
    {
        "week": 24,
        "title": "Final Integration: end-to-end capstone, final assessments, and application transition plan",
        "objectives": [
            "Integrate math, finance, ML, time series, workflow, and communication into one final artifact.",
            "Assess your readiness honestly against master's and interview goals.",
            "Leave the 24-week plan with a clear next-step timeline for 2027 applications.",
        ],
        "day_topics": [
            "Choose final capstone question and scope",
            "Implement pipeline and verify assumptions",
            "Evaluate, stress test, and document limitations",
            "Prepare final report and presentation",
            "Final self-assessment and gap map",
            "Capstone presentation day",
            "Transition roadmap for 2026-2027 applications",
        ],
        "concepts": [
            "End-to-end research pipeline",
            "Validation and robustness",
            "Professional reporting",
            "Self-assessment",
            "Transition planning",
        ],
        "practice_tasks": [
            "Write the final capstone like a serious research deliverable.",
            "Compare yourself against target program prerequisites objectively.",
            "List the next 6 months of work needed before applications open.",
            "Turn your gap map into a dated action plan.",
        ],
        "checkpoint": "Can you now show evidence, not just intention, that you are preparing for a serious quant master's path?",
        "weekend_project": "Capstone 6: final end-to-end quant research and application-ready portfolio package.",
        "admissions_track": "Set an exact application calendar for September 2027 and January 2028 intakes, including recommenders and scholarship deadlines as soon as they are published.",
        "interview_track": "Run a final mock interview and record your answers for review.",
        "capstone": {
            "problem_statement": "Build one polished end-to-end quant research project with clear motivation, data handling, modeling, validation, risks, and business relevance.",
            "data_sources": "Use the cleanest public data source you have worked with during the plan, optionally combining market data with one engineered feature set or simple text signal.",
            "steps": "Define the question, build the dataset, engineer features, establish baselines, test a strategy or forecast, include cost and risk checks, write a report, and prepare a presentation.",
            "metrics": "Research clarity, code quality, validation discipline, economic reasoning, communication quality, and honesty about limitations.",
            "mistakes": "Trying to do too much, using too many models, hiding failure modes, or presenting a backtest without implementation assumptions.",
        },
    },
]


def build_roadmap() -> list[dict]:
    roadmap = []
    day_labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for blueprint in WEEK_BLUEPRINTS:
        if "daily_schedule" in blueprint:
            days = blueprint["daily_schedule"]
        else:
            days = []
            for day_label, topic in zip(day_labels, blueprint["day_topics"], strict=True):
                days.append(
                    make_generic_day(
                        day_label,
                        topic,
                        blueprint["title"],
                        coding_task=f"Implement one notebook cell or small script focused on: {topic.lower()}.",
                        reflection=f"What from {topic.lower()} felt truly clear, and what still needs a slower revisit?",
                    )
                )
        for index, day in enumerate(days, start=1):
            day["day_index"] = index
            day["estimated_time"] = "4 hours" if day["day"] in {"Mon", "Tue", "Wed", "Thu", "Fri"} else "2 hours"
            day["session_plan"] = day.get("session_plan", daily_session_plan(day["day"]))
            day["week_theme"] = blueprint["title"]
            day["previous_topic"] = days[index - 2]["topic"] if index > 1 else ""
            day["next_topic"] = days[index]["topic"] if index < len(days) else ""
            slug = slugify(day["topic"])
            day["lesson_markdown_path"] = (
                f"curriculum/week-{blueprint['week']:02d}/day-{index:02d}-{slug}/lesson.md"
            )
            day["lesson_pdf_path"] = (
                f"curriculum/pdfs/week-{blueprint['week']:02d}/day-{index:02d}-{slug}/lesson.pdf"
            )
            day["notebook_path"] = (
                f"curriculum/week-{blueprint['week']:02d}/notebooks/day-{index:02d}-{slug}.ipynb"
            )
        roadmap.append(
            {
                "week": blueprint["week"],
                "title": blueprint["title"],
                "dates": week_dates(blueprint["week"]),
                "objectives": blueprint["objectives"],
                "daily_schedule": days,
                "concepts": blueprint["concepts"],
                "practice_tasks": blueprint["practice_tasks"],
                "checkpoint": blueprint["checkpoint"],
                "weekend_project": blueprint["weekend_project"],
                "admissions_track": blueprint["admissions_track"],
                "interview_track": blueprint["interview_track"],
                "weekly_plan_markdown_path": f"curriculum/week-{blueprint['week']:02d}/plan.md",
                "weekly_plan_pdf_path": f"curriculum/pdfs/week-{blueprint['week']:02d}/plan.pdf",
                "weekly_overview_notebook_path": (
                    f"curriculum/week-{blueprint['week']:02d}/notebooks/week-{blueprint['week']:02d}-foundations.ipynb"
                ),
                "weekly_project_notebook_path": (
                    f"curriculum/week-{blueprint['week']:02d}/notebooks/"
                    f"{weekly_project_notebook_name(blueprint['week'])}"
                ),
                "interview_questions": build_interview_pack(
                    blueprint["week"], blueprint["title"], blueprint["concepts"]
                ),
                "capstone": blueprint.get("capstone"),
            }
        )
    return roadmap


def ensure_dirs() -> None:
    for path in [CURRICULUM_DIR, DOCS_DIR, TEMPLATES_DIR]:
        path.mkdir(parents=True, exist_ok=True)
    for week in range(1, 25):
        (CURRICULUM_DIR / f"week-{week:02d}").mkdir(parents=True, exist_ok=True)
        (CURRICULUM_DIR / f"week-{week:02d}" / "notebooks").mkdir(parents=True, exist_ok=True)
    for week_number in range(1, 25):
        blueprint = WEEK_BLUEPRINTS[week_number - 1]
        topics = (
            [day["topic"] for day in blueprint["daily_schedule"]]
            if "daily_schedule" in blueprint
            else blueprint["day_topics"]
        )
        for idx, topic in enumerate(topics, start=1):
            slug = slugify(topic)
            (CURRICULUM_DIR / f"week-{week_number:02d}" / f"day-{idx:02d}-{slug}").mkdir(
                parents=True, exist_ok=True
            )


def slugify(text: str) -> str:
    cleaned = "".join(ch.lower() if ch.isalnum() else "-" for ch in text)
    while "--" in cleaned:
        cleaned = cleaned.replace("--", "-")
    return cleaned.strip("-")


def write_json(roadmap: list[dict]) -> None:
    data = {
        "profile": {
            "baseline": "AI master's graduate restarting toward Quant Finance",
            "math_level": "0-1",
            "coding_level": "around 3/5 overall",
            "finance_exposure": "basic investing",
            "target_intakes": ["September 2027", "January 2028"],
        },
        "assumptions": [
            "You are restarting math almost from zero and need simple explanations before formal treatment.",
            "You can sustain about 24 hours per week.",
            "You want a scholarship-aware master's preparation track in parallel with technical training.",
            "You prefer practical portfolio-building over purely theoretical study.",
        ],
        "weekly_time_budget": {
            "Mon-Fri": "4 hours/day",
            "Sat": "2 hours",
            "Sun": "2 hours",
            "Total": "About 24 hours/week",
        },
        "roadmap": roadmap,
    }
    (CURRICULUM_DIR / "roadmap.json").write_text(json.dumps(data, indent=2), encoding="utf-8")


def roadmap_markdown(roadmap: list[dict]) -> str:
    lines = [
        "# Personalized 24-Week Quant Learning Roadmap",
        "",
        "## Assumptions",
        "- Math is being rebuilt almost from zero, so each lesson starts with intuition and then adds technical language.",
        "- Coding is good enough to move quickly once finance and math are tied back to practice.",
        "- The 24-week plan runs from 2026-04-20 to 2026-10-04 if you start on the next Monday after this build.",
        "- Weekly workload is sized for about 24 hours.",
        "",
        "## 24-Week Roadmap Table",
        "| Week | Dates | Theme | Key Outcome |",
        "| --- | --- | --- | --- |",
    ]
    for week in roadmap:
        key_outcome = week["checkpoint"].split(".")[0]
        lines.append(
            f"| {week['week']} | {week['dates']} | {week['title']} | {key_outcome} |"
        )

    lines.extend(
        [
            "",
            "## Benchmarking Against Top Programs and WorldQuant-Style Practice",
            "- Berkeley MFE: interdisciplinary finance, statistics, computing, and industry project structure.",
            "- Carnegie Mellon MSCF: financial computing, time series, machine learning, markets, and capstone orientation.",
            "- Oxford Mathematical and Computational Finance: stochastic calculus, derivatives, risk, fixed income, deep learning, and dissertation-style depth.",
            "- Columbia MSFE: optimization, stochastic models, foundations of financial engineering, deep learning, programming, and algorithmic trading orientation.",
            "- WorldQuant University MScFE: practical sequence from data and econometrics through derivatives, stochastic modeling, ML in finance, portfolio management, risk, and capstone.",
            "",
            "## Monthly Capstone Portfolio",
            "- Week 4: Exploratory asset allocation study.",
            "- Week 8: Time-series forecasting baseline lab.",
            "- Week 12: Options and scenario-risk notebook.",
            "- Week 16: Factor or cross-sectional signal research note.",
            "- Week 20: AI-assisted quant research artifact with guardrails.",
            "- Week 24: End-to-end final quant research project for applications and interviews.",
            "",
            "## Monthly Assessment Rubric",
            "| Month | Math | Programming and Data | Finance | ML/Time Series | Communication and Career | Pass Mark |",
            "| --- | --- | --- | --- | --- | --- | --- |",
            "| Month 1 | 25 | 20 | 20 | 10 | 25 | 70/100 |",
            "| Month 2 | 20 | 20 | 15 | 25 | 20 | 72/100 |",
            "| Month 3 | 15 | 15 | 35 | 15 | 20 | 75/100 |",
            "| Month 4 | 10 | 20 | 30 | 20 | 20 | 77/100 |",
            "| Month 5 | 10 | 20 | 20 | 30 | 20 | 80/100 |",
            "| Month 6 | 10 | 15 | 20 | 20 | 35 | 82/100 |",
            "",
            "## Revision System",
            "- Review weak items after 1 day, 3 days, 7 days, and 14 days.",
            "- Maintain an error log with: concept, specific mistake, corrected idea, next review date.",
            "- Every Sunday: write a 10-minute summary from memory before looking at notes.",
            "- Every capstone week: score yourself against the monthly rubric and list the next 3 corrections.",
            "",
            "## Folder Naming Convention",
            "- `curriculum/week-01/day-01-reset-your-toolkit/lesson.md`",
            "- `curriculum/week-01/notebooks/week-01-foundations.ipynb`",
            "- `curriculum/week-08/plan.md`",
            "",
            "## Required Prerequisites",
            "- Basic comfort with using a computer, terminal, and notebooks.",
            "- Willingness to do arithmetic and algebra daily.",
            "- Commitment to writing short explanations, not only code.",
            "",
            "## Optional Advanced Extensions",
            "- Stochastic calculus after Week 18 once the base is stable.",
            "- Reinforcement learning for trading after Week 20.",
            "- Advanced derivatives pricing, Monte Carlo, and PDE methods after Week 24.",
            "- C++ for quant finance after Week 24 if targeting more classical pricing or strats roles.",
        ]
    )
    return "\n".join(lines) + "\n"


def week_markdown(week: dict) -> str:
    lines = [
        f"# Week {week['week']:02d}: {week['title']}",
        "",
        f"**Dates:** {week['dates']}",
        "",
        "## Learning Objectives",
    ]
    for item in week["objectives"]:
        lines.append(f"- {item}")
    lines.extend(["", "## Daily Schedule"])
    for day in week["daily_schedule"]:
        lines.extend(
            [
                f"### {day['day']}: {day['topic']}",
                f"- Why it matters in quant: {day['why']}",
                f"- Core explanation: {day['core_explanation']}",
                f"- Worked example: {day['worked_example']}",
                "- Practice problems:",
            ]
        )
        for problem in day["practice_problems"]:
            lines.append(f"- {problem}")
        lines.append(f"- Coding task: {day['coding_task']}")
        lines.append(f"- Reflection: {day['reflection']}")
        lines.append("")

    lines.extend(["## Concept Lessons"])
    for concept in week["concepts"]:
        lines.append(f"- {concept}")
    lines.extend(["", "## Practice Tasks"])
    for task in week["practice_tasks"]:
        lines.append(f"- {task}")
    lines.extend(
        [
            "",
            "## Quiz / Checkpoint",
            week["checkpoint"],
            "",
            "## Weekend Revision and Mini Project",
            week["weekend_project"],
            "",
            "## Admissions Track",
            week["admissions_track"],
            "",
            "## Interview / Job Track",
            week["interview_track"],
        ]
    )
    if week.get("interview_questions"):
        lines.extend(["", "## Interview Prep Questions and Model Answers"])
        for item in week["interview_questions"]:
            lines.extend(
                [
                    f"### Q: {item['question']}",
                    f"A: {item['answer']}",
                    "",
                ]
            )
    if week.get("capstone"):
        capstone = week["capstone"]
        lines.extend(
            [
                "",
                "## Capstone",
                f"- Problem statement: {capstone['problem_statement']}",
                f"- Data source suggestions: {capstone['data_sources']}",
                f"- Implementation steps: {capstone['steps']}",
                f"- Evaluation metrics: {capstone['metrics']}",
                f"- Common mistakes: {capstone['mistakes']}",
            ]
        )
    return "\n".join(lines) + "\n"


def week1_day_markdown(day: dict, week_number: int, index: int) -> str:
    return render_week1_day_markdown(day)


def generic_day_markdown(week_number: int, day: dict) -> str:
    continuity_lines = ["## Continuity Map"]
    if day.get("previous_topic"):
        continuity_lines.append(f"- Previous day focus: {day['previous_topic']}")
    else:
        continuity_lines.append(
            "- Week kickoff: establish baseline intuition and key definitions before moving into formal detail."
        )
    continuity_lines.append(f"- Today's focus: {day['topic']}")
    if day.get("next_topic"):
        continuity_lines.append(f"- Next day bridge: {day['next_topic']}")
    else:
        continuity_lines.append("- Week closure: consolidate this concept into your weekly project narrative.")

    lines = [
        f"# Week {week_number:02d} {day['day']}: {day['topic']}",
        "",
        f"**Estimated time:** {day['estimated_time']}",
        "",
        "## Daily Mission",
        (
            f"This day belongs to the week theme \"{day.get('week_theme', f'Week {week_number}')}\". "
            f"Your objective is to understand, apply, and communicate {day['topic'].lower()} in a way a quant team would trust."
        ),
        "",
        *continuity_lines,
        "",
        "## Session Plan",
        "| Session | Duration | Focus |",
        "| --- | --- | --- |",
    ]
    for label, duration, focus in day.get("session_plan", daily_session_plan(day["day"])):
        lines.append(f"| {label} | {duration} | {focus} |")

    lines.extend(
        [
            "",
            "## Why It Matters In Quant",
            day["why"],
            "",
            "## Concept Build (Intuition -> Technical -> Market Use)",
            f"1. Intuition: describe {day['topic'].lower()} in plain language before touching formulas.",
            f"2. Technical frame: {day['core_explanation']}",
            f"3. Market interpretation: {day['worked_example']}",
            "4. Failure mode check: identify one way this concept is commonly misused in research or trading discussion.",
            "",
            "## Practice Problems",
        ]
    )
    for problem in day["practice_problems"]:
        lines.append(f"- {problem}")
    lines.extend(
        [
            "",
            "## 4-Hour Deliverables",
            "- Produce one page of notes with intuition, formulas, and one market example in your own words.",
            "- Complete all notebook cells and annotate each output with what it means financially.",
            "- Add one error-log entry with a scheduled review date.",
            "- Record a 60-90 second spoken explanation of the concept as interview practice.",
            "",
            "## Coding Task",
            day["coding_task"],
            "",
            "## Interview Drill",
            f"- Q1: Explain {day['topic'].lower()} to a non-technical stakeholder in 3 sentences.",
            "- Q2: Give one failure case where this concept can produce misleading confidence.",
            "- Q3: Show one concrete link from this concept to trading, portfolio construction, or risk control.",
            "",
            "## Reflection Prompt",
            day["reflection"],
            "",
            "## Completion Checklist",
            "- I can explain the concept from memory without reading notes.",
            "- I completed at least one coding exercise tied to the day topic.",
            "- I wrote one realistic finance use case in my own words.",
            "- I recorded at least one weak area in my error log.",
            "- I set the next review date using spaced repetition.",
        ]
    )
    return "\n".join(lines) + "\n"


def _nb_code(code: str) -> str:
    return textwrap.dedent(code).strip() + "\n"


def generic_day_notebook_spec(week_number: int, day: dict) -> dict:
    continuity_text = (
        f"Previous day: {day['previous_topic']}\n\n"
        if day.get("previous_topic")
        else "Previous day: week kickoff and baseline setup.\n\n"
    )
    continuity_text += (
        f"Next day: {day['next_topic']}"
        if day.get("next_topic")
        else "Next day: weekly consolidation and project integration."
    )
    intro = textwrap.dedent(
        f"""\
        # Week {week_number} {day['day']}: {day['topic']}

        Estimated time: {day['estimated_time']}

        ## Why this matters
        {day['why']}

        ## Core explanation
        {day['core_explanation']}

        ## Worked example
        {day['worked_example']}

        ## Continuity
        {continuity_text}
        """
    ).strip()
    practice = "\n".join([
        "## Practice recap",
        *[f"- {item}" for item in day["practice_problems"]],
        f"- Reflection prompt: {day['reflection']}",
        "- Deliverable: write a 100-word note connecting today's topic to a real trading or risk decision.",
    ])
    interview = textwrap.dedent(
        f"""\
        ## Interview drill
        - Q: Explain {day['topic'].lower()} and one real quant use case.
        - A: Start with intuition, provide one technical detail, and connect it to a trading, portfolio, or risk decision.
        - Q: What would go wrong if this concept is applied carelessly?
        - A: Discuss one realistic failure mode and how you would detect it.
        """
    ).strip()
    code_cells = [
        {
            "markdown": "## Code Lab 1: Build a synthetic market panel",
            "code": _nb_code(
                """\
                import numpy as np
                import pandas as pd

                rng = np.random.default_rng(42)
                dates = pd.date_range("2026-01-01", periods=120, freq="D")
                shock = rng.normal(0.0, 0.008, size=len(dates))
                drift = 0.0005
                returns = drift + shock
                prices = 100 * np.cumprod(1 + returns)

                panel = pd.DataFrame({"date": dates, "return": returns, "price": prices})
                print(panel.head())
                """
            ),
        },
        {
            "markdown": "## Code Lab 2: Core summary statistics and risk lens",
            "code": _nb_code(
                """\
                summary = {
                    "mean_return": panel["return"].mean(),
                    "volatility": panel["return"].std(),
                    "min_return": panel["return"].min(),
                    "max_return": panel["return"].max(),
                    "final_price": panel["price"].iloc[-1],
                }

                for k, v in summary.items():
                    print(k, round(float(v), 6))
                """
            ),
        },
        {
            "markdown": "## Code Lab 3: Scenario stress and interpretation",
            "code": _nb_code(
                """\
                stressed = panel.copy()
                stressed.loc[stressed.index[40:45], "return"] -= 0.02
                stressed["price"] = 100 * (1 + stressed["return"]).cumprod()

                baseline_final = panel["price"].iloc[-1]
                stressed_final = stressed["price"].iloc[-1]
                impact = stressed_final / baseline_final - 1

                print("Baseline final price:", round(float(baseline_final), 2))
                print("Stressed final price:", round(float(stressed_final), 2))
                print("Stress impact:", round(float(impact), 4))
                """
            ),
        },
        {
            "markdown": "## Code Lab 4: Study-note structure for revision",
            "code": _nb_code(
                f"""\
                study_note = {{
                    "topic": {day['topic']!r},
                    "intuition": "Write this in your own words.",
                    "formula_or_workflow": "Add one formula or step-by-step process.",
                    "finance_use_case": "Add one real trading/risk use case.",
                    "failure_mode": "Describe one pitfall.",
                    "next_review": "Set a date for spaced repetition.",
                }}

                for key, value in study_note.items():
                    print(f"{{key}}: {{value}}")
                """
            ),
        },
    ]
    return {
        "title_markdown": intro,
        "practice_markdown": practice,
        "interview_markdown": interview,
        "code_cells": code_cells,
    }


def generic_project_notebook_spec(week: dict) -> dict:
    week_number = week["week"]
    project_type = "Capstone" if week_number % 4 == 0 else "Mini Project"
    title_markdown = textwrap.dedent(
        f"""\
        # Week {week_number:02d} {project_type}: {week['title']}

        Build a concise research artifact that:

        - states the question clearly
        - creates at least one measurable output
        - compares alternatives transparently
        - documents limitations honestly
        """
    ).strip()
    closing_markdown = textwrap.dedent(
        f"""\
        ## Suggested conclusion

        Summarize:

        - what worked
        - what failed
        - how assumptions affected outcomes
        - one improvement for next week

        Weekend objective: {week['weekend_project']}

        Use this closing structure:

        1. Problem definition and motivation.
        2. Data and assumptions.
        3. Result summary with one risk caveat.
        4. What you would improve next week.
        """
    ).strip()
    code_cells = [
        {
            "markdown": "## Step 1: Create a toy score table",
            "code": _nb_code(
                """\
                import pandas as pd

                candidates = pd.DataFrame(
                    {
                        "strategy": ["baseline", "variant_a", "variant_b"],
                        "expected_return": [0.010, 0.013, 0.009],
                        "volatility": [0.020, 0.024, 0.015],
                        "max_drawdown": [0.050, 0.070, 0.040],
                    }
                )
                print(candidates)
                """
            ),
        },
        {
            "markdown": "## Step 2: Compute a simple quality score",
            "code": _nb_code(
                """\
                candidates = candidates.assign(
                    return_to_risk=candidates["expected_return"] / candidates["volatility"],
                    penalty=candidates["max_drawdown"] * 2,
                )
                candidates["quality_score"] = candidates["return_to_risk"] - candidates["penalty"]
                print(candidates.round(4))
                """
            ),
        },
        {
            "markdown": "## Step 3: Rank and interpret",
            "code": _nb_code(
                """\
                ranked = candidates.sort_values("quality_score", ascending=False)
                print(ranked[["strategy", "quality_score"]].round(4))
                """
            ),
        },
        {
            "markdown": "## Step 4: Add decision notes",
            "code": _nb_code(
                f"""\
                decision_note = {{
                    "week": {week_number},
                    "theme": {week['title']!r},
                    "best_candidate": ranked.iloc[0]["strategy"],
                    "risk_note": "Document one fragility before trusting this result.",
                    "next_iteration": "Define one concrete improvement for the next research cycle.",
                }}
                print(decision_note)
                """
            ),
        },
    ]
    return {
        "title_markdown": title_markdown + "\n",
        "code_cells": code_cells,
        "closing_markdown": closing_markdown + "\n",
    }


def templates() -> dict[str, str]:
    return {
        "daily-completion-checklist.md": textwrap.dedent(
            """\
            # Daily Completion Checklist

            - I completed the lesson and notebook work.
            - I wrote the main formula or concept from memory.
            - I solved the practice set before checking notes.
            - I finished the coding task.
            - I logged at least one mistake or confusion.
            - I rated my confidence from 0 to 5.
            """
        ),
        "weekly-review-template.md": textwrap.dedent(
            """\
            # Weekly Review Template

            - Week number:
            - Score out of 100:
            - Top 3 wins:
            - Top 3 weak spots:
            - What I misunderstood:
            - What I will change next week:
            - Which project artifact is worth keeping in my portfolio:
            """
        ),
        "monthly-milestone-template.md": textwrap.dedent(
            """\
            # Monthly Milestone Template

            - Month:
            - Rubric score:
            - Technical strengths:
            - Technical gaps:
            - Portfolio status:
            - Admissions progress:
            - Interview readiness:
            - Next 30-day plan:
            """
        ),
        "error-log-template.md": textwrap.dedent(
            """\
            # Error Log Template

            | Date | Week | Concept | Mistake | Correct Idea | Next Review Date |
            | --- | --- | --- | --- | --- | --- |
            """
        ),
        "self-evaluation-form.md": textwrap.dedent(
            """\
            # Weekly Self-Evaluation Form

            - What did I truly understand this week?
            - What only looked familiar but was not actually strong?
            - Where did I rush?
            - Which finance example finally made something click?
            - Which coding task was clean and reproducible?
            - Which topic needs a re-study next week?
            - Confidence score:
            """
        ),
    }


def benchmarking_markdown() -> str:
    return textwrap.dedent(
        """\
        # Benchmarking Notes

        This curriculum was intentionally benchmarked for breadth and difficulty against official program material from:

        - Berkeley MFE curriculum: https://mfe.haas.berkeley.edu/academics/curriculum
        - Carnegie Mellon MSCF Year One and Year Two: https://www.cmu.edu/mscf/academics/curriculum/year-one.html and https://www.cmu.edu/mscf/academics/curriculum/year-two.html
        - Oxford MSc in Mathematical and Computational Finance: https://www.ox.ac.uk/admissions/graduate/courses/msc-mathematical-and-computational-finance
        - Columbia MSFE curriculum: https://ieor.columbia.edu/msfe-curriculum
        - WorldQuant University academic catalog: https://www.wqu.edu/documents/wqu-catalog.pdf

        Design choices pulled from those benchmarks:

        - Strong math and probability rebuild before advanced finance.
        - Practical financial computing and data handling early.
        - Time-series, ML, risk, derivatives, and portfolio construction all included.
        - Capstone and project cadence modeled after applied, industry-facing programs.
        - Admissions, communication, and career readiness built in rather than delayed.
        - Agentic AI added as a support workflow with guardrails, not as a replacement for validation.
        """
    )


def system_flow_markdown() -> str:
    return textwrap.dedent(
        """\
        # System Flow

        1. Open the roadmap and select the current week.
        2. Read the weekly PDF and daily markdown lessons.
        3. Work through the weekly notebook and daily coding task.
        4. Update progress in the Streamlit dashboard.
        5. Save weak spots into the error log with a scheduled review date.
        6. Complete the weekly review every Sunday.
        7. Complete the monthly assessment after every capstone week.
        8. Use the admissions and interview tracks in parallel so technical growth becomes application evidence.

        Persistence model:

        - The app writes to `data/progress.db`.
        - Closing the browser or stopping Streamlit does not erase progress.
        - Reopening the app restores saved progress, reviews, and error logs from SQLite.
        """
    )


def career_notes_markdown() -> str:
    return textwrap.dedent(
        """\
        # Career Notes

        ## Buy-Side vs Sell-Side Quant

        - Buy-side quant: works for hedge funds, asset managers, or prop firms. The focus is usually generating alpha, portfolio construction, execution, and direct investment performance.
        - Sell-side quant: works for banks or broker-dealers. The focus is often pricing, structuring, model building, risk management, execution tools, and supporting clients or trading desks.

        ## Investment Banking vs Quant Finance

        - Investment banking is more deal-oriented: M&A, capital raises, client execution, valuation, and presentations.
        - Quant finance is more model-oriented: pricing, trading, risk, research, portfolio construction, and systematic strategies.
        - There is overlap on the sell-side because banks house both investment banking teams and quantitative teams, but the day-to-day work is very different.
        """
    )


def write_docs() -> None:
    (DOCS_DIR / "benchmarking.md").write_text(benchmarking_markdown(), encoding="utf-8")
    (DOCS_DIR / "system-flow.md").write_text(system_flow_markdown(), encoding="utf-8")
    (DOCS_DIR / "career-notes.md").write_text(career_notes_markdown(), encoding="utf-8")


def write_templates() -> None:
    for name, content in templates().items():
        (TEMPLATES_DIR / name).write_text(content, encoding="utf-8")


def write_notebook(path: Path, cells: list) -> None:
    nb = nbf.v4.new_notebook()
    nb.cells = cells
    nb.metadata["kernelspec"] = {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3",
    }
    nb.metadata["language_info"] = {"name": "python"}
    path.write_text(nbf.writes(nb), encoding="utf-8")


def create_and_execute_notebook(path: Path, cells: list) -> None:
    write_notebook(path, cells)
    try:
        executed = nbf.read(path.open("r", encoding="utf-8"), as_version=4)
        client = NotebookClient(executed, timeout=120, kernel_name="python3")
        client.execute()
        path.write_text(nbf.writes(executed), encoding="utf-8")
    except Exception as exc:  # noqa: BLE001
        print(
            f"Warning: could not execute notebook {path}. "
            f"Saved unexecuted notebook instead. Reason: {exc}"
        )


def create_curriculum_notebooks(roadmap: list[dict]) -> None:
    for week in roadmap:
        notebooks_dir = CURRICULUM_DIR / f"week-{week['week']:02d}" / "notebooks"
        notebook_writer = write_notebook
        week_overview_cells = [
            nbf.v4.new_markdown_cell(
                f"# Week {week['week']} Notebook Hub\n\nThis overview notebook points you to the daily notebooks and the weekly project notebook."
            ),
            nbf.v4.new_markdown_cell(
                "Work through the daily notebooks in order, then complete the weekly mini-project or capstone notebook at the weekend."
            ),
        ]
        notebook_writer(
            notebooks_dir / f"week-{week['week']:02d}-foundations.ipynb",
            week_overview_cells,
        )

        for index, day in enumerate(week["daily_schedule"], start=1):
            spec = (
                week1_day_notebook_specs(day)
                if week["week"] == 1
                else (
                    detailed_day_notebook_spec(week["week"], day)
                    if has_detailed_day(week["week"], day["day"])
                    else generic_day_notebook_spec(week["week"], day)
                )
            )
            slug = slugify(day["topic"])
            cells = [nbf.v4.new_markdown_cell(spec["title_markdown"])]
            for item in spec["code_cells"]:
                cells.append(nbf.v4.new_markdown_cell(item["markdown"]))
                cells.append(nbf.v4.new_code_cell(item["code"]))
            cells.append(nbf.v4.new_markdown_cell(spec["practice_markdown"]))
            cells.append(nbf.v4.new_markdown_cell(spec["interview_markdown"]))
            notebook_writer(notebooks_dir / f"day-{index:02d}-{slug}.ipynb", cells)

        if week["week"] == 1:
            project_spec = week1_project_notebook_spec()
        else:
            project_spec = (
                project_notebook_spec(week["week"])
                if week["week"] <= 4
                else generic_project_notebook_spec(week)
            )
        project_name = weekly_project_notebook_name(week["week"])
        project_cells = [nbf.v4.new_markdown_cell(project_spec["title_markdown"])]
        for item in project_spec["code_cells"]:
            project_cells.append(nbf.v4.new_markdown_cell(item["markdown"]))
            project_cells.append(nbf.v4.new_code_cell(item["code"]))
        project_cells.append(nbf.v4.new_markdown_cell(project_spec["closing_markdown"]))
        notebook_writer(notebooks_dir / project_name, project_cells)


def write_curriculum_files(roadmap: list[dict]) -> None:
    (CURRICULUM_DIR / "24-week-roadmap.md").write_text(
        roadmap_markdown(roadmap), encoding="utf-8"
    )

    for week in roadmap:
        week_dir = CURRICULUM_DIR / f"week-{week['week']:02d}"
        (week_dir / "plan.md").write_text(week_markdown(week), encoding="utf-8")

    for week in roadmap:
        for idx, day in enumerate(week["daily_schedule"], start=1):
            slug = slugify(day["topic"])
            day_dir = CURRICULUM_DIR / f"week-{week['week']:02d}" / f"day-{idx:02d}-{slug}"
            content = (
                week1_day_markdown(day, week["week"], idx)
                if week["week"] == 1
                else (
                    render_detailed_day_markdown(week["week"], day)
                    if has_detailed_day(week["week"], day["day"])
                    else generic_day_markdown(week["week"], day)
                )
            )
            (day_dir / "lesson.md").write_text(content, encoding="utf-8")


def main() -> None:
    ensure_dirs()
    roadmap = build_roadmap()
    write_json(roadmap)
    write_curriculum_files(roadmap)
    write_templates()
    write_docs()
    create_curriculum_notebooks(roadmap)
    print("Bootstrapped curriculum, templates, docs, and notebooks for all 24 weeks.")
