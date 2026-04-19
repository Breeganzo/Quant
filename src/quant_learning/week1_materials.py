from __future__ import annotations

import textwrap
from typing import Any

from quant_learning.topic_specific_content import (
    formula_entries_for_week,
    real_world_lab_lines_for_week,
)


def _md(text: str) -> str:
    return textwrap.dedent(text).strip() + "\n"


def _ten_hour_study_blocks(day_label: str) -> list[tuple[str, str, str]]:
    if day_label in {"Mon", "Tue", "Wed", "Thu", "Fri"}:
        return [
            ("Block 1", "60 min", "Concept briefing and key-assumption mapping."),
            ("Block 2", "60 min", "Formula/workflow derivation and notation rewrite."),
            ("Block 3", "60 min", "Solved real-world case walkthrough."),
            ("Block 4", "60 min", "Data checks and exploratory diagnostics."),
            ("Block 5", "60 min", "Core notebook implementation with comments."),
            ("Block 6", "60 min", "Extension coding task and sensitivity variation."),
            ("Block 7", "60 min", "Risk caveat and robustness scenario testing."),
            ("Block 8", "60 min", "Interview-style quiz answers and defense drill."),
            ("Block 9", "60 min", "Revision sprint and error-log updates."),
            ("Block 10", "60 min", "Desk memo summary and tomorrow transition plan."),
        ]

    return [
        ("Block 1", "60 min", "Closed-book recall and formula rewrite."),
        ("Block 2", "60 min", "Weak-topic reteach with solved examples."),
        ("Block 3", "60 min", "Data refresh and diagnostics rerun."),
        ("Block 4", "60 min", "Notebook baseline implementation."),
        ("Block 5", "60 min", "Notebook extension and stress tests."),
        ("Block 6", "60 min", "Mini-project build increment."),
        ("Block 7", "60 min", "Mini-project risk caveat documentation."),
        ("Block 8", "60 min", "Interview rehearsal with timed answers."),
        ("Block 9", "60 min", "Revision board confidence rescoring."),
        ("Block 10", "60 min", "Weekly memo and next-week bridge notes."),
    ]


WEEK1_DAY_DETAILS: dict[str, dict[str, Any]] = {
    "Mon": {
        "estimated_time": "6 hours",
        "study_blocks": [
            ("Block 1", "45 min", "Reset notation: prices, returns, percentages, and variables."),
            ("Block 2", "60 min", "Learn simple return, gross return, and compounding intuition."),
            ("Block 3", "45 min", "Work through hand-calculated examples and common traps."),
            ("Block 4", "60 min", "Implement returns and wealth paths in Python and pandas."),
            ("Block 5", "30 min", "Practice, reflect, and do a short interview drill."),
        ],
        "overview": [
            "This day rebuilds the language of quantitative finance from the ground up. Before models, factors, or machine learning, you need a precise way to describe how money changes over time.",
            "The main habit to build is to stop thinking only in absolute price differences and start thinking in relative changes, wealth paths, and compounding. That shift is foundational for backtesting, portfolio tracking, and risk reporting.",
        ],
        "concepts": [
            {
                "title": "Price change versus return",
                "simple": "If a stock moves from 100 to 105, the price change is 5, but the return is 5 divided by 100, which is 5 percent. Returns let us compare moves across assets with different price levels.",
                "technical": "For a one-period simple return, use r_t = P_t / P_(t-1) - 1. The gross return is 1 + r_t = P_t / P_(t-1).",
                "finance_example": "A 5-point move means something very different for a stock priced at 20 than for a stock priced at 500. Returns normalize that difference.",
            },
            {
                "title": "Compounding and the wealth path",
                "simple": "Once your capital changes, the next day's gain or loss applies to the new amount, not the old amount. That is why growth is multiplicative.",
                "technical": "If wealth starts at W_0, then after returns r_1, r_2, ..., r_t, wealth is W_t = W_0 * product(1 + r_i).",
                "finance_example": "A loss of 50 percent requires a later gain of 100 percent just to get back to the starting point.",
            },
            {
                "title": "Why arithmetic intuition can mislead",
                "simple": "A gain of 10 percent and a loss of 10 percent do not cancel out because the second move happens on a different base.",
                "technical": "The path 100 -> 110 -> 99 gives returns of +10 percent and -10 percent, but total wealth falls by 1 percent.",
                "finance_example": "This is why traders care about drawdowns and recovery periods, not just average daily returns.",
            },
        ],
        "worked_examples": [
            "Asset A: 50 -> 55. Simple return = 10 percent.",
            "Portfolio capital: 1000 -> after +10 percent becomes 1100 -> after -5 percent becomes 1045. Net return is not 5 percent; it is 4.5 percent.",
            "Path dependency: +20 percent then -20 percent produces 96 from 100, not 100.",
        ],
        "practice_with_answers": [
            {
                "question": "A stock moves from 80 to 92. What is the simple return?",
                "answer": "Return = 92 / 80 - 1 = 0.15, so 15 percent.",
            },
            {
                "question": "You start with 2000 and earn returns of 5 percent, 3 percent, and -2 percent. What is final wealth?",
                "answer": "2000 * 1.05 * 1.03 * 0.98 = 2119.32.",
            },
            {
                "question": "Why is a 30 percent loss harder to recover from than it first sounds?",
                "answer": "Because the required recovery is measured from the reduced base. After falling from 100 to 70, you need 30 / 70 = 42.86 percent to get back to 100.",
            },
        ],
        "interview_drill": [
            {
                "question": "Why do quants work with returns instead of raw prices?",
                "answer": "Returns make moves comparable across assets and line up naturally with portfolio aggregation, statistics, and risk analysis.",
            },
            {
                "question": "What does compounding change in performance analysis?",
                "answer": "It makes the order of gains and losses matter because capital evolves multiplicatively over time.",
            },
        ],
        "code_cells": [
            {
                "markdown": "## Code Lab 1: Prices to returns and wealth",
                "code": _md(
                    """\
                    import pandas as pd

                    prices = pd.Series([100, 103, 101, 104, 107], name="price")
                    returns = prices.pct_change().dropna()
                    gross_returns = 1 + returns
                    wealth = 1000 * gross_returns.cumprod()

                    print("Prices:")
                    print(prices.to_string(index=False))
                    print("\\nReturns:")
                    print((returns * 100).round(2).to_string(index=False))
                    print("\\nGross returns:")
                    print(gross_returns.round(4).to_string(index=False))
                    print("\\nWealth path:")
                    print(wealth.round(2).to_string(index=False))
                    """
                ),
            },
            {
                "markdown": "## Code Lab 2: Path dependency",
                "code": _md(
                    """\
                    import pandas as pd

                    paths = pd.DataFrame(
                        {
                            "scenario": ["up then down", "down then up"],
                            "r1": [0.10, -0.10],
                            "r2": [-0.10, 0.10],
                        }
                    )
                    paths["final_wealth_from_100"] = 100 * (1 + paths["r1"]) * (1 + paths["r2"])
                    print(paths)
                    """
                ),
            },
        ],
    },
    "Tue": {
        "estimated_time": "6 hours",
        "study_blocks": [
            ("Block 1", "45 min", "Review Python functions and reusable finance logic."),
            ("Block 2", "60 min", "Learn control flow and payoff rules."),
            ("Block 3", "60 min", "Build probability intuition and expected value."),
            ("Block 4", "45 min", "Connect payoff asymmetry to trading setups."),
            ("Block 5", "30 min", "Code, reflect, and interview drill."),
        ],
        "overview": [
            "Today is about two habits: writing clean reusable code and thinking in probabilities instead of stories. Both are central in quant research.",
            "A quant is constantly turning a financial question into a function, a decision rule, or an expected payoff under uncertainty. That is why functions and expected value belong together on the same day.",
        ],
        "concepts": [
            {
                "title": "Functions as reusable research building blocks",
                "simple": "A function is a named block of logic that you can call again with different inputs. This helps keep research clean, testable, and less error-prone.",
                "technical": "A function maps inputs to outputs. In quant work, small functions for returns, drawdowns, expected value, or signal transforms keep the pipeline modular.",
                "finance_example": "Instead of recomputing a return formula manually in many cells, a function lets you standardize the calculation across assets.",
            },
            {
                "title": "Control flow as rule logic",
                "simple": "Control flow decides what the program should do under different conditions.",
                "technical": "Conditionals like if/else mirror rule-based finance logic: if a signal crosses a threshold, enter; otherwise stay flat.",
                "finance_example": "A stop-loss or risk cap is basically a decision rule embedded in code.",
            },
            {
                "title": "Expected value and asymmetric payoffs",
                "simple": "Expected value is the average outcome if the same uncertain setup is repeated many times.",
                "technical": "For discrete outcomes x_i with probabilities p_i, E[X] = sum p_i x_i. A positive hit rate alone is not enough; payoff size matters.",
                "finance_example": "A strategy can win 70 percent of the time and still lose money if the average loss is much larger than the average gain.",
            },
        ],
        "worked_examples": [
            "A trade with 60 percent chance of +2 and 40 percent chance of -1 has expected value 0.8.",
            "A trade with 80 percent chance of +1 and 20 percent chance of -5 has expected value -0.2 despite a high win rate.",
            "A function `simple_return(buy, sell)` is a reusable way to turn prices into decisions or labels.",
        ],
        "practice_with_answers": [
            {
                "question": "Why might a strategy with many winning trades still have negative expected value?",
                "answer": "Because the losses may be much larger than the wins. Expected value depends on both probability and payoff magnitude.",
            },
            {
                "question": "What does an if/else statement represent in a trading rule?",
                "answer": "It represents a conditional action, such as buy if a signal exceeds a threshold and otherwise do nothing or reduce exposure.",
            },
            {
                "question": "A setup has outcomes +4 with probability 0.25 and -1 with probability 0.75. What is expected value?",
                "answer": "0.25 * 4 + 0.75 * (-1) = 0.25.",
            },
        ],
        "interview_drill": [
            {
                "question": "How is expected value different from the most likely outcome?",
                "answer": "Expected value is the average weighted outcome over many repetitions, while the most likely outcome is just the single highest-probability event.",
            },
            {
                "question": "Why do quants care about payoff asymmetry?",
                "answer": "Because good trading ideas are about the full payoff distribution, not just the percentage of winning trades.",
            },
        ],
        "code_cells": [
            {
                "markdown": "## Code Lab 1: A reusable return function",
                "code": _md(
                    """\
                    def simple_return(buy_price: float, sell_price: float) -> float:
                        return sell_price / buy_price - 1

                    print(round(simple_return(100, 105), 4))
                    print(round(simple_return(50, 45), 4))
                    """
                ),
            },
            {
                "markdown": "## Code Lab 2: Expected value across strategies",
                "code": _md(
                    """\
                    import pandas as pd

                    strategies = pd.DataFrame(
                        {
                            "name": ["balanced", "high_hit_rate_bad_payoff", "convex_payoff"],
                            "win_prob": [0.6, 0.8, 0.3],
                            "win_payoff": [2.0, 1.0, 5.0],
                            "loss_prob": [0.4, 0.2, 0.7],
                            "loss_payoff": [-1.0, -5.0, -1.0],
                        }
                    )
                    strategies["expected_value"] = (
                        strategies["win_prob"] * strategies["win_payoff"]
                        + strategies["loss_prob"] * strategies["loss_payoff"]
                    )
                    print(strategies[["name", "expected_value"]])
                    """
                ),
            },
            {
                "markdown": "## Code Lab 3: Small simulation",
                "code": _md(
                    """\
                    import numpy as np

                    rng = np.random.default_rng(42)
                    simulated = rng.choice([2.0, -1.0], size=20, p=[0.6, 0.4])
                    print(simulated)
                    print("Sample mean:", simulated.mean())
                    """
                ),
            },
        ],
    },
    "Wed": {
        "estimated_time": "6 hours",
        "study_blocks": [
            ("Block 1", "45 min", "Learn scalars, vectors, and matrices through finance objects."),
            ("Block 2", "60 min", "Understand the dot product as portfolio return."),
            ("Block 3", "60 min", "Use matrices for scenarios, features, and multiple assets."),
            ("Block 4", "45 min", "Preview covariance and diversification."),
            ("Block 5", "30 min", "Code and interview drill."),
        ],
        "overview": [
            "Linear algebra becomes easier when you stop treating it as abstract symbols and start seeing it as organized financial information.",
            "Portfolio weights, factor exposures, feature tables, and historical return panels all become clearer once you think in vectors and matrices.",
        ],
        "concepts": [
            {
                "title": "Scalars, vectors, and matrices",
                "simple": "A scalar is one number, a vector is an ordered list of numbers, and a matrix is a table of numbers.",
                "technical": "In quant work, vectors often store weights, returns, or factor exposures, while matrices store many observations across time or assets.",
                "finance_example": "A portfolio of three assets with weights [0.5, 0.3, 0.2] is naturally represented as a vector.",
            },
            {
                "title": "Dot product as weighted sum",
                "simple": "The dot product multiplies matching entries and adds them. In finance that gives a weighted return or exposure.",
                "technical": "If w is a weight vector and r is a return vector, portfolio return is w^T r.",
                "finance_example": "A portfolio return is just the sum of each asset's return times its portfolio weight.",
            },
            {
                "title": "Matrices as data structures",
                "simple": "A matrix helps store many assets over many dates or many features for many observations.",
                "technical": "An n by p matrix may represent n observations and p features for machine learning, or p assets over n dates for portfolio analytics.",
                "finance_example": "A return matrix with rows as days and columns as assets is the standard input to covariance and optimization work.",
            },
        ],
        "worked_examples": [
            "Weights [0.5, 0.3, 0.2] with returns [0.02, -0.01, 0.03] produce a portfolio return of 0.013 or 1.3 percent.",
            "A 3 by 2 feature matrix can represent 3 assets and 2 features such as momentum and volatility.",
            "Covariance is a matrix summary of how asset returns move together over time.",
        ],
        "practice_with_answers": [
            {
                "question": "What does a weight vector mean economically?",
                "answer": "It tells you what fraction of the portfolio is allocated to each asset or strategy component.",
            },
            {
                "question": "Why is the dot product useful in quant work?",
                "answer": "Because many quantities are weighted sums: portfolio return, factor exposure, and expected payoff all fit that pattern.",
            },
            {
                "question": "Why does covariance show up naturally after matrices?",
                "answer": "Because once returns are organized in a matrix, covariance measures the pairwise co-movement across columns or assets.",
            },
        ],
        "interview_drill": [
            {
                "question": "How would you explain a vector to a trader?",
                "answer": "It is just an organized list of related numbers, like a set of portfolio weights or factor exposures.",
            },
            {
                "question": "What is the finance interpretation of a dot product?",
                "answer": "It is usually a weighted sum, most commonly a portfolio return from weights and asset returns.",
            },
        ],
        "code_cells": [
            {
                "markdown": "## Code Lab 1: Dot product and portfolio returns",
                "code": _md(
                    """\
                    import numpy as np

                    weights = np.array([0.5, 0.3, 0.2])
                    asset_returns = np.array([0.02, -0.01, 0.03])
                    portfolio_return = weights @ asset_returns

                    print("Portfolio return:", round(portfolio_return, 4))
                    """
                ),
            },
            {
                "markdown": "## Code Lab 2: Return matrix across multiple days",
                "code": _md(
                    """\
                    import numpy as np
                    import pandas as pd

                    returns_matrix = np.array(
                        [
                            [0.01, -0.01, 0.02],
                            [0.00, 0.02, -0.01],
                            [0.03, -0.02, 0.01],
                        ]
                    )
                    df = pd.DataFrame(returns_matrix, columns=["asset_a", "asset_b", "asset_c"])
                    df["portfolio_return"] = returns_matrix @ np.array([0.5, 0.3, 0.2])
                    print(df)
                    """
                ),
            },
            {
                "markdown": "## Code Lab 3: Covariance preview",
                "code": _md(
                    """\
                    print(df[["asset_a", "asset_b", "asset_c"]].cov())
                    """
                ),
            },
        ],
    },
    "Thu": {
        "estimated_time": "6 hours",
        "study_blocks": [
            ("Block 1", "45 min", "Understand mean, median, variance, and standard deviation."),
            ("Block 2", "60 min", "Relate volatility to risk and noise."),
            ("Block 3", "45 min", "Study outliers, skew, and why averages can mislead."),
            ("Block 4", "60 min", "Use pandas and plots for descriptive analysis."),
            ("Block 5", "30 min", "Practice and interview drill."),
        ],
        "overview": [
            "A quant should not fit a model to data before first understanding the shape of the data. Descriptive statistics are the first diagnostic layer.",
            "This day builds the habit of asking: where is the center, how wide is the spread, are there outliers, and how much trust should I place in the average?",
        ],
        "concepts": [
            {
                "title": "Mean and median",
                "simple": "The mean is the average. The median is the middle value after sorting.",
                "technical": "The sample mean is sensitive to extreme values, while the median is more robust when data contain outliers.",
                "finance_example": "A few crisis days can drag the mean return down sharply even if most days were calm.",
            },
            {
                "title": "Variance and standard deviation",
                "simple": "These measure how spread out the data are. Standard deviation is easier to interpret because it is in the same units as the original data.",
                "technical": "For returns, standard deviation is commonly used as a volatility proxy. High volatility means outcomes vary more around the average.",
                "finance_example": "Two assets can have the same average return but very different standard deviations, leading to very different risk profiles.",
            },
            {
                "title": "Sampling uncertainty",
                "simple": "A sample average is only an estimate. A different sample might give a different number.",
                "technical": "In finance, short samples are noisy. Apparent performance may be mostly sampling variation rather than genuine edge.",
                "finance_example": "A backtest with 20 trades may look amazing mostly because of luck.",
            },
        ],
        "worked_examples": [
            "Returns [0.01, 0.02, -0.01, 0.00] have mean 0.005 and sample standard deviation about 0.0129.",
            "One outlier return of -0.15 can change the sample mean materially even if the rest of the series is calm.",
            "Histograms reveal clustering, skew, and tails better than a single average number.",
        ],
        "practice_with_answers": [
            {
                "question": "Why can two assets with the same mean return still feel very different to hold?",
                "answer": "Because their volatility and downside behavior can differ a lot, changing drawdown and risk management demands.",
            },
            {
                "question": "Why is standard deviation often preferred over variance in communication?",
                "answer": "Because it is in the same scale as the original data, making it easier to interpret.",
            },
            {
                "question": "Why should a quant look at plots before modeling?",
                "answer": "Plots can reveal trends, outliers, missing values, and changing volatility that summary statistics alone may hide.",
            },
        ],
        "interview_drill": [
            {
                "question": "What does volatility mean in practice?",
                "answer": "It is a measure of dispersion in returns and is often used as a simple proxy for how noisy or risky an asset is.",
            },
            {
                "question": "Why is the sample mean dangerous in finance?",
                "answer": "Because financial data are noisy, non-stationary, and heavily influenced by outliers and regime changes.",
            },
        ],
        "code_cells": [
            {
                "markdown": "## Code Lab 1: Summary statistics",
                "code": _md(
                    """\
                    import pandas as pd

                    returns = pd.Series([0.01, 0.02, -0.01, 0.00, 0.03, -0.02, 0.01], name="returns")
                    summary = pd.Series(
                        {
                            "mean": returns.mean(),
                            "median": returns.median(),
                            "std": returns.std(),
                            "min": returns.min(),
                            "max": returns.max(),
                        }
                    )
                    print(summary.round(4))
                    """
                ),
            },
            {
                "markdown": "## Code Lab 2: Visualization",
                "code": _md(
                    """\
                    import matplotlib.pyplot as plt

                    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
                    returns.plot(ax=axes[0], title="Toy return series")
                    returns.hist(ax=axes[1], bins=5)
                    axes[1].set_title("Histogram")
                    plt.tight_layout()
                    plt.show()
                    """
                ),
            },
        ],
    },
    "Fri": {
        "estimated_time": "6 hours",
        "study_blocks": [
            ("Block 1", "45 min", "Understand what markets are and who participates."),
            ("Block 2", "60 min", "Learn major asset classes and return drivers."),
            ("Block 3", "45 min", "Map core risk types and why implementation matters."),
            ("Block 4", "60 min", "Clarify quant roles: buy-side, sell-side, risk, strats, and investment banking."),
            ("Block 5", "30 min", "Code table-building and interview drill."),
        ],
        "overview": [
            "A lot of confusion in early quant learning comes from knowing formulas without knowing the market context they belong to. This day fixes that.",
            "The goal is not to master every asset class in one day. The goal is to build a clean mental map of markets, roles, and why quants are paid to solve specific problems.",
        ],
        "concepts": [
            {
                "title": "Market structure",
                "simple": "Markets match buyers and sellers. Prices move because participants update beliefs, manage risk, or need liquidity.",
                "technical": "Market structure includes venues, order types, liquidity conditions, and how trades are executed.",
                "finance_example": "A highly liquid index future behaves very differently from a small illiquid stock.",
            },
            {
                "title": "Asset classes and risk drivers",
                "simple": "Different instruments are moved by different forces: earnings for equities, rates for bonds, macro and flows for FX, supply and demand for commodities.",
                "technical": "Each asset class has distinct payoff structures, liquidity patterns, and risk exposures.",
                "finance_example": "An equity drawdown, a bond duration shock, and an FX carry unwind are different risk stories.",
            },
            {
                "title": "Buy-side, sell-side, and investment banking",
                "simple": "Buy-side manages money and seeks returns. Sell-side serves clients, prices products, runs trading desks, and manages bank-side exposures. Investment banking is more deal-oriented than model-oriented.",
                "technical": "Buy-side quants focus more on alpha, portfolio construction, and PnL. Sell-side quants often support pricing, structuring, risk, execution, and desk infrastructure.",
                "finance_example": "A hedge fund researcher testing a factor signal and a bank derivatives quant calibrating an options model are both quants, but their incentives and workflows differ.",
            },
        ],
        "worked_examples": [
            "Equity example: stock returns depend on earnings, valuation, macro sensitivity, and sentiment.",
            "Bond example: price sensitivity to rates is linked to duration and convexity.",
            "Transaction costs matter more in high-turnover strategies because gross edge is repeatedly eaten by spread and slippage.",
        ],
        "practice_with_answers": [
            {
                "question": "Why is investment banking not the same as quant trading?",
                "answer": "Investment banking is centered on deals, capital raising, valuation, and client execution, while quant trading focuses on models, risk, pricing, and systematic decision making.",
            },
            {
                "question": "What is one major risk driver for fixed income?",
                "answer": "Interest rates and the shape of the yield curve are central drivers, along with credit risk for credit products.",
            },
            {
                "question": "Why do transaction costs matter more in short-horizon strategies?",
                "answer": "Because frequent trading causes costs to accumulate and can easily overwhelm a small raw edge.",
            },
        ],
        "interview_drill": [
            {
                "question": "What is the clearest difference between buy-side and sell-side quant work?",
                "answer": "Buy-side is more directly tied to alpha and portfolio performance, while sell-side is more tied to pricing, client support, structuring, execution, and desk risk.",
            },
            {
                "question": "Why should a quant understand market structure early?",
                "answer": "Because signals only matter if they can actually be implemented in the market without unrealistic assumptions.",
            },
        ],
        "code_cells": [
            {
                "markdown": "## Code Lab 1: Asset class map",
                "code": _md(
                    """\
                    import pandas as pd

                    asset_map = pd.DataFrame(
                        {
                            "asset_class": ["Equities", "Fixed Income", "FX", "Commodities", "Options"],
                            "return_driver": [
                                "earnings and valuation",
                                "rates and credit spreads",
                                "macro and carry",
                                "supply, demand, macro",
                                "underlying move and volatility",
                            ],
                            "main_risk": [
                                "equity drawdown",
                                "duration and credit risk",
                                "macro shocks",
                                "supply shock",
                                "nonlinear exposure",
                            ],
                        }
                    )
                    print(asset_map)
                    """
                ),
            },
            {
                "markdown": "## Code Lab 2: Simple turnover-cost example",
                "code": _md(
                    """\
                    gross_alpha_per_trade = 0.0015
                    cost_per_trade = 0.0008
                    trades_per_month = 40

                    monthly_gross = gross_alpha_per_trade * trades_per_month
                    monthly_net = (gross_alpha_per_trade - cost_per_trade) * trades_per_month

                    print("Monthly gross return contribution:", round(monthly_gross, 4))
                    print("Monthly net return contribution:", round(monthly_net, 4))
                    """
                ),
            },
        ],
    },
    "Sat": {
        "estimated_time": "6 hours",
        "study_blocks": [
            ("Block 1", "45 min", "Active recall and formula rewrite from memory."),
            ("Block 2", "55 min", "Error log deep clean and spaced repetition schedule update."),
            ("Block 3", "50 min", "Market diary with one chart and one quantitative observation."),
            ("Block 4", "50 min", "Code labs plus one extension variation on your own."),
            ("Block 5", "60 min", "Interview recap, weak-point drill, and short written memo."),
        ],
        "overview": [
            "Weekend work should not feel like a weak leftover. It is where consolidation happens.",
            "Today is about building a repeatable revision system so weak points do not quietly accumulate until later quantitative topics become overwhelming.",
        ],
        "concepts": [
            {
                "title": "Spaced repetition",
                "simple": "Review material just before you would naturally forget it.",
                "technical": "A practical sequence for weak concepts is 1 day, 3 days, 7 days, and 14 days after first exposure.",
                "finance_example": "If compounding felt shaky on Monday, it should appear again in the review schedule instead of being assumed solved.",
            },
            {
                "title": "Error logs",
                "simple": "An error log records what you got wrong, why it happened, and what the corrected idea is.",
                "technical": "The goal is not to collect mistakes passively, but to convert them into future review prompts and cleaner mental models.",
                "finance_example": "Mixing up price change and return is a conceptual error worth logging immediately because it contaminates many later topics.",
            },
            {
                "title": "Market diary",
                "simple": "A market diary turns passive reading into structured observation.",
                "technical": "Each entry should include instrument, driver, risk, and one numerical observation or chart comment.",
                "finance_example": "You might note that bond yields rose, equity futures fell, and the likely link was rate expectations.",
            },
        ],
        "worked_examples": [
            "Weak concept: standard deviation vs variance. Mistake: confusing the squared unit issue. Correction: variance is squared deviation, standard deviation is the square root and easier to interpret.",
            "Market diary entry: asset = S&P 500 ETF, driver = rate-sensitive growth sentiment, risk = macro surprise, numeric note = daily move and volume spike.",
        ],
        "practice_with_answers": [
            {
                "question": "What should an error log entry contain besides the wrong answer?",
                "answer": "It should contain the exact misconception, the corrected idea, and the next review date.",
            },
            {
                "question": "Why is active recall stronger than re-reading?",
                "answer": "Because pulling an idea from memory reveals whether it is actually learned rather than merely familiar.",
            },
        ],
        "interview_drill": [
            {
                "question": "How do you keep yourself from repeating the same mistakes?",
                "answer": "I use an error log with scheduled reviews and I force myself to restate weak concepts from memory before re-reading notes.",
            },
        ],
        "code_cells": [
            {
                "markdown": "## Code Lab 1: Review schedule generator",
                "code": _md(
                    """\
                    import pandas as pd

                    concepts = pd.DataFrame(
                        {
                            "concept": ["returns", "expected_value", "dot_product", "standard_deviation"],
                            "first_study_date": pd.to_datetime(["2026-04-20", "2026-04-21", "2026-04-22", "2026-04-23"]),
                        }
                    )

                    concepts["review_1d"] = concepts["first_study_date"] + pd.Timedelta(days=1)
                    concepts["review_3d"] = concepts["first_study_date"] + pd.Timedelta(days=3)
                    concepts["review_7d"] = concepts["first_study_date"] + pd.Timedelta(days=7)
                    print(concepts)
                    """
                ),
            },
            {
                "markdown": "## Code Lab 2: Error log starter",
                "code": _md(
                    """\
                    error_log = pd.DataFrame(
                        [
                            {
                                "concept": "compounding",
                                "mistake": "treated +10% and -10% as cancelling out",
                                "correction": "returns compound on changing capital base",
                                "next_review": "2026-04-27",
                            }
                        ]
                    )
                    print(error_log)
                    """
                ),
            },
        ],
    },
    "Sun": {
        "estimated_time": "6 hours",
        "study_blocks": [
            ("Block 1", "45 min", "Closed-book quiz and formula retrieval from memory."),
            ("Block 2", "70 min", "Mini-project build and extension with one extra metric."),
            ("Block 3", "55 min", "Interpretation write-up with failure-mode analysis."),
            ("Block 4", "50 min", "Interview practice and weekly review."),
        ],
        "overview": [
            "The first weekend project is deliberately simple. The point is to prove that you can move from concept to code to interpretation in one clean artifact.",
            "You are not being judged on complexity yet. You are building the habit of finishing, documenting, and explaining quantitative work.",
        ],
        "concepts": [
            {
                "title": "Project framing",
                "simple": "A good small project has a clear input, a few correct calculations, and a clean interpretation.",
                "technical": "The first project should include a price series, return conversion, summary statistics, cumulative wealth, and an economic comment.",
                "finance_example": "Even a toy risk-return dashboard can demonstrate clarity, reproducibility, and communication discipline.",
            },
            {
                "title": "Evaluation and interpretation",
                "simple": "A chart or number becomes useful only when you explain what it means.",
                "technical": "Interpret average return, volatility, drawdown-like behavior, and data limitations rather than presenting raw outputs only.",
                "finance_example": "If the wealth curve looks smooth but the sample is tiny, that limitation must be stated.",
            },
            {
                "title": "Portfolio communication",
                "simple": "Recruiters and admissions reviewers care about whether you can explain your work clearly.",
                "technical": "A short conclusion should include the objective, method, result, and one limitation or next step.",
                "finance_example": "This is the seed of a later master's project summary or interview walkthrough.",
            },
        ],
        "worked_examples": [
            "Compute returns from a toy 30-day price series.",
            "Summarize mean return, volatility, min, max, and final wealth from 100.",
            "Write a short note on whether the series appears smooth, noisy, or regime-changing.",
        ],
        "practice_with_answers": [
            {
                "question": "What makes a beginner quant project strong even if it is simple?",
                "answer": "Correctness, reproducibility, and clear interpretation. Simplicity is fine if the logic is sound.",
            },
            {
                "question": "What should you include in a short project conclusion?",
                "answer": "The goal, what you computed, what the results suggest, and one limitation or next step.",
            },
        ],
        "interview_drill": [
            {
                "question": "How would you present this Week 1 project in an interview?",
                "answer": "I would say I built a small return-and-risk dashboard from a toy price series to demonstrate correct handling of returns, compounding, descriptive statistics, and communication. Then I would mention one limitation and what I would extend next.",
            },
        ],
        "code_cells": [
            {
                "markdown": "## Code Lab: Mini-project core build",
                "code": _md(
                    """\
                    import numpy as np
                    import pandas as pd
                    import matplotlib.pyplot as plt

                    prices = pd.Series(
                        [100, 101, 102, 101, 103, 104, 103, 105, 107, 106, 108, 109, 111, 110, 112],
                        name="price",
                    )
                    returns = prices.pct_change().dropna()
                    wealth = 100 * (1 + returns).cumprod()

                    summary = pd.Series(
                        {
                            "mean_return": returns.mean(),
                            "volatility": returns.std(),
                            "min_return": returns.min(),
                            "max_return": returns.max(),
                            "final_wealth": wealth.iloc[-1],
                        }
                    )
                    print(summary.round(4))

                    fig, axes = plt.subplots(2, 1, figsize=(8, 6))
                    prices.plot(ax=axes[0], title="Price series")
                    wealth.plot(ax=axes[1], title="Wealth from 100")
                    plt.tight_layout()
                    plt.show()
                    """
                ),
            },
        ],
    },
}


def week1_interview_pack() -> list[dict[str, str]]:
    return [
        {
            "question": "What is the difference between a price series and a return series?",
            "answer": "A price series shows levels over time, while a return series shows relative changes from one period to the next. Returns are more useful for comparison, statistics, and portfolio analysis.",
        },
        {
            "question": "Why is compounding such a big deal in quantitative trading?",
            "answer": "Because capital changes over time, so gains and losses hit a moving base. The order of returns changes the final wealth path and drawdown profile.",
        },
        {
            "question": "Can a high win-rate strategy still be bad?",
            "answer": "Yes. If the occasional losses are much larger than the frequent wins, expected value can still be negative.",
        },
        {
            "question": "How do vectors and matrices show up in finance?",
            "answer": "Weights, returns, factor exposures, and feature tables are all naturally represented as vectors or matrices. This is why linear algebra shows up so early in quant work.",
        },
        {
            "question": "What is the difference between buy-side and sell-side quant roles?",
            "answer": "Buy-side quants are usually closer to alpha, portfolio construction, and PnL. Sell-side quants are usually closer to pricing, structuring, risk, and supporting bank trading or client workflows.",
        },
    ]


def render_week1_day_markdown(day: dict[str, Any]) -> str:
    detail = WEEK1_DAY_DETAILS[day["day"]]
    formula_entries = formula_entries_for_week(1, day["topic"])
    lab_lines = real_world_lab_lines_for_week(1, day["topic"])
    study_blocks = _ten_hour_study_blocks(day["day"])
    lines: list[str] = [
        f"# Week 01 {day['day']}: {day['topic']}",
        "",
        "**Estimated time:** 10 hours",
        "",
        "## Study Blocks",
    ]
    for label, duration, focus in study_blocks:
        lines.append(f"- {label} ({duration}): {focus}")

    lines.extend(["", "## Why It Matters In Quant", day["why"], "", "## Learning Overview"])
    for paragraph in detail["overview"]:
        lines.extend([paragraph, ""])

    lines.append("## Core Concepts")
    for concept in detail["concepts"]:
        lines.extend(
            [
                f"### {concept['title']}",
                f"- Simple explanation: {concept['simple']}",
                f"- Technical depth: {concept['technical']}",
                f"- Finance example: {concept['finance_example']}",
                "",
            ]
        )

    lines.extend(["## Worked Examples"])
    for example in detail["worked_examples"]:
        lines.append(f"- {example}")

    lines.extend(
        [
            "",
            "## Solved Real-World Flow",
            "- Define one concrete desk decision that this topic informs.",
            "- Use reproducible market data and state one data-quality check.",
            "- Apply one core formula/workflow and report one numerical output.",
            "- Add one risk caveat and one robustness check before trusting the conclusion.",
        ]
    )

    lines.extend(["", "## Practice Questions With Answers"])
    for item in detail["practice_with_answers"]:
        lines.extend(
            [
                f"### Question: {item['question']}",
                f"Answer: {item['answer']}",
                "",
            ]
        )

    lines.extend(
        [
            "## Daily Quiz (Closed-Book)",
            "1. State the main intuition in your own words without notes.",
            "2. Write one key formula/workflow from memory and define all symbols.",
            "3. Give one practical quant use case and one failure mode.",
            "",
            "## Interview-Ready Formula Sheet",
        ]
    )

    for idx, entry in enumerate(formula_entries, start=1):
        lines.extend(
            [
                f"### Formula {idx}: {entry['name']}",
                f"$${entry['equation']}$$",
                f"Plain-English interpretation: {entry['meaning']}",
                f"Notation check: {entry['pitfall']}",
                "",
            ]
        )

    lines.extend(
        [
            "## Formula Organization Table",
            "| Formula/Workflow | Meaning | Finance Use Case | Common Misread |",
            "| --- | --- | --- | --- |",
        ]
    )
    for entry in formula_entries:
        lines.append(
            f"| {entry['name']} | {entry['meaning']} | {entry['use_case']} | {entry['pitfall']} |"
        )

    lines.extend(["", "## Real-World Data Application"])
    for item in lab_lines:
        lines.append(f"- {item}")
    lines.append("")

    lines.extend(["## Coding Task", day["coding_task"], "", "## Daily Interview Drill"])
    for qa in detail["interview_drill"]:
        lines.extend(
            [
                f"### Q: {qa['question']}",
                f"A: {qa['answer']}",
                "",
            ]
        )

    lines.extend(
        [
            "## Reflection Question",
            day["reflection"],
            "",
            "## Completion Checklist",
            "- I completed each study block or consciously rescheduled it.",
            "- I rewrote the key formulas or concepts from memory.",
            "- I finished the coding lab and checked the output.",
            "- I added at least one item to the error log if something was unclear.",
            "- I practiced at least one interview answer aloud.",
            "- I documented one actionable desk-style takeaway and one follow-up experiment.",
        ]
    )
    return "\n".join(lines) + "\n"


def week1_day_notebook_specs(day: dict[str, Any]) -> dict[str, Any]:
    detail = WEEK1_DAY_DETAILS[day["day"]]
    study_blocks = _ten_hour_study_blocks(day["day"])
    intro = [
        f"# Week 1 {day['day']}: {day['topic']}",
        "",
        "Estimated time: 10 hours",
        "",
        "## Why this matters",
        day["why"],
        "",
        "## Study blocks",
    ]
    for label, duration, focus in study_blocks:
        intro.append(f"- {label} ({duration}): {focus}")
    intro.extend(["", "## Concept notes"])
    for concept in detail["concepts"]:
        intro.extend(
            [
                f"### {concept['title']}",
                concept["simple"],
                "",
                f"Technical note: {concept['technical']}",
                "",
                f"Finance example: {concept['finance_example']}",
                "",
            ]
        )

    practice = ["## Practice recap"]
    for item in detail["practice_with_answers"]:
        practice.extend([f"- {item['question']}", f"  Suggested answer: {item['answer']}"])

    interview = ["## Interview drill"]
    for qa in detail["interview_drill"]:
        interview.extend([f"- Q: {qa['question']}", f"  A: {qa['answer']}"])

    return {
        "title_markdown": "\n".join(intro),
        "practice_markdown": "\n".join(practice),
        "interview_markdown": "\n".join(interview),
        "code_cells": detail["code_cells"],
    }


def week1_project_notebook_spec() -> dict[str, Any]:
    return {
        "title_markdown": _md(
            """\
            # Week 1 Mini Project: Return and Risk Dashboard

            This notebook turns the first week's concepts into a finished artifact:

            - convert prices to returns
            - compute a wealth path
            - summarize return and risk
            - visualize the series
            - write a short interpretation
            """
        ),
        "code_cells": [
            {
                "markdown": "## Step 1: Create a toy price series",
                "code": _md(
                    """\
                    import pandas as pd
                    import matplotlib.pyplot as plt

                    prices = pd.Series(
                        [100, 101, 100, 102, 103, 105, 104, 107, 109, 108, 111, 113, 112, 114, 116, 115, 117, 118, 120, 119],
                        name="price",
                    )
                    print(prices.head())
                    """
                ),
            },
            {
                "markdown": "## Step 2: Convert prices into returns and wealth",
                "code": _md(
                    """\
                    returns = prices.pct_change().dropna()
                    wealth = 100 * (1 + returns).cumprod()

                    print("Return summary:")
                    print(returns.describe().round(4))
                    """
                ),
            },
            {
                "markdown": "## Step 3: Create a dashboard plot",
                "code": _md(
                    """\
                    fig, axes = plt.subplots(3, 1, figsize=(9, 8))
                    prices.plot(ax=axes[0], title="Price Series")
                    returns.plot(ax=axes[1], title="Return Series")
                    wealth.plot(ax=axes[2], title="Wealth from 100")
                    plt.tight_layout()
                    plt.show()
                    """
                ),
            },
            {
                "markdown": "## Step 4: Build a small summary table",
                "code": _md(
                    """\
                    summary = pd.DataFrame(
                        {
                            "metric": ["mean_return", "volatility", "min_return", "max_return", "final_wealth"],
                            "value": [
                                returns.mean(),
                                returns.std(),
                                returns.min(),
                                returns.max(),
                                wealth.iloc[-1],
                            ],
                        }
                    )
                    print(summary.round(4))
                    """
                ),
            },
        ],
        "closing_markdown": _md(
            """\
            ## Suggested write-up

            A good 150-word conclusion should mention:

            - what the project tried to show
            - how prices were converted into returns
            - what the volatility and wealth path suggest
            - one limitation, such as the toy nature of the data
            """
        ),
    }
