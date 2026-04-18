from __future__ import annotations

import textwrap
from typing import Any


def _md(text: str) -> str:
    return textwrap.dedent(text).strip() + "\n"


MONTH1_EXTRA_DAY_DETAILS: dict[int, dict[str, dict[str, Any]]] = {
    2: {
        "Mon": {
            "estimated_time": "4 hours",
            "study_blocks": [
                ("Block 1", "45 min", "Understand arrays, shapes, and vectorization."),
                ("Block 2", "55 min", "Compare loops with array-based finance calculations."),
                ("Block 3", "55 min", "Apply vectorization to return and portfolio work."),
                ("Block 4", "55 min", "Complete coding drills and rewrite concepts."),
                ("Block 5", "30 min", "Interview recap and error log."),
            ],
            "overview": [
                "NumPy matters because quant work becomes painful and slow if every calculation is written as a manual loop. Arrays let you express the mathematical structure directly.",
                "The practical habit today is to stop treating market data as isolated numbers and start seeing it as organized numerical objects that can be transformed efficiently.",
            ],
            "concepts": [
                {
                    "title": "Arrays as financial objects",
                    "simple": "An array is a structured collection of numbers. In quant work those numbers might be prices, returns, weights, signals, or volumes.",
                    "technical": "NumPy arrays support vectorized operations, broadcasting, and matrix-style computations that are much faster and clearer than many explicit Python loops.",
                    "finance_example": "A daily return vector across 100 assets is naturally stored as one array.",
                },
                {
                    "title": "Vectorization",
                    "simple": "Vectorization means applying the same operation to many values at once.",
                    "technical": "Instead of looping through each asset return manually, array operations act on the whole structure in one expression.",
                    "finance_example": "Computing portfolio returns over many days becomes one matrix multiplication rather than repeated manual sums.",
                },
                {
                    "title": "Shape and dimension discipline",
                    "simple": "You need to know whether data are one-dimensional or two-dimensional before using them correctly.",
                    "technical": "Shape mismatches are a common source of quant coding bugs, especially in ML pipelines and portfolio analytics.",
                    "finance_example": "A weight vector and a return matrix must align properly for portfolio calculations to be correct.",
                },
            ],
            "worked_examples": [
                "Transform a vector of prices into returns with one array expression.",
                "Compute portfolio returns from a 3-day by 3-asset return matrix and one weight vector.",
                "Compare a loop-based sum with a dot product to show they mean the same thing conceptually.",
            ],
            "practice_with_answers": [
                {
                    "question": "Why is vectorization useful in quant finance?",
                    "answer": "It keeps code closer to the math, reduces manual error, and scales better when data become large.",
                },
                {
                    "question": "What does shape mean for an array?",
                    "answer": "Shape tells you how many rows and columns or dimensions the array has, which determines what operations are valid.",
                },
                {
                    "question": "Why can shape mistakes be dangerous in finance code?",
                    "answer": "Because a mismatched operation may silently produce the wrong result, which can distort signals, risk, or portfolio calculations.",
                },
            ],
            "interview_drill": [
                {
                    "question": "Why do quants use NumPy instead of plain Python lists for many calculations?",
                    "answer": "Because NumPy arrays support faster, clearer numerical operations and map naturally to vectors and matrices used in finance.",
                }
            ],
            "code_cells": [
                {
                    "markdown": "## Code Lab 1: Vectorized returns",
                    "code": _md(
                        """\
                        import numpy as np

                        prices = np.array([100, 102, 101, 104, 106], dtype=float)
                        returns = prices[1:] / prices[:-1] - 1
                        print("Prices:", prices)
                        print("Returns:", np.round(returns, 4))
                        """
                    ),
                },
                {
                    "markdown": "## Code Lab 2: Matrix of returns and portfolio weights",
                    "code": _md(
                        """\
                        returns_matrix = np.array(
                            [
                                [0.01, -0.02, 0.03],
                                [0.02, 0.01, -0.01],
                                [-0.01, 0.00, 0.02],
                            ]
                        )
                        weights = np.array([0.5, 0.3, 0.2])
                        portfolio_returns = returns_matrix @ weights
                        print(np.round(portfolio_returns, 4))
                        """
                    ),
                },
                {
                    "markdown": "## Code Lab 3: Loop versus vectorized calculation",
                    "code": _md(
                        """\
                        loop_result = []
                        for row in returns_matrix:
                            loop_result.append(sum(row * weights))

                        print("Loop result:", np.round(loop_result, 4))
                        print("Vectorized result:", np.round(portfolio_returns, 4))
                        """
                    ),
                },
            ],
        },
        "Tue": {
            "estimated_time": "4 hours",
            "study_blocks": [
                ("Block 1", "45 min", "Learn DataFrame structure and indexing."),
                ("Block 2", "55 min", "Clean missing values and basic data problems."),
                ("Block 3", "55 min", "Join and reshape simple market tables."),
                ("Block 4", "55 min", "Code drills and small cleaning exercises."),
                ("Block 5", "30 min", "Reflection and interview recap."),
            ],
            "overview": [
                "Most quant work is not glamorous modeling. A large part is understanding tables, cleaning messy inputs, and making sure what you model is actually what you think you are modeling.",
                "Today is about becoming comfortable with pandas as the day-to-day language of practical financial data handling.",
            ],
            "concepts": [
                {
                    "title": "DataFrames as structured market tables",
                    "simple": "A DataFrame is like a spreadsheet with labeled rows and columns.",
                    "technical": "pandas DataFrames provide indexing, grouping, joining, missing-value handling, and time-series functionality used heavily in research workflows.",
                    "finance_example": "You might store dates, prices, returns, sectors, and volumes in one table and transform it before modeling.",
                },
                {
                    "title": "Missing values and bad data",
                    "simple": "Real market data often has gaps, duplicate records, or inconsistent labels.",
                    "technical": "Cleaning decisions matter because dropped rows, forward fills, or wrong joins can change backtest outputs.",
                    "finance_example": "A missing price on one date can distort return calculations unless handled explicitly.",
                },
                {
                    "title": "Joins and alignment",
                    "simple": "A join combines tables using a common key such as date or ticker.",
                    "technical": "Misaligned joins are a common source of subtle leakage and incorrect analysis in finance data pipelines.",
                    "finance_example": "Joining returns with a factor table on the wrong date can accidentally use future information.",
                },
            ],
            "worked_examples": [
                "Build a price table with a missing value and inspect how `pct_change` behaves.",
                "Join a price table with a sector table and explain why index alignment matters.",
                "Compare dropping missing data with a fill strategy and note the trade-off.",
            ],
            "practice_with_answers": [
                {
                    "question": "Why is missing data dangerous in return calculations?",
                    "answer": "Because missing values can create false jumps, incorrect percentage changes, or unintended row drops if handled casually.",
                },
                {
                    "question": "What is one common join mistake in finance data?",
                    "answer": "Joining on the wrong date key and accidentally aligning today's feature with tomorrow's outcome.",
                },
                {
                    "question": "Why do labels matter in pandas?",
                    "answer": "Because labeled indices and columns make transformations safer and easier to interpret than raw position-only arrays.",
                },
            ],
            "interview_drill": [
                {
                    "question": "What is the difference between a DataFrame and a NumPy array in practice?",
                    "answer": "A DataFrame has labels and richer data-wrangling features, while a NumPy array is more lightweight and numerically focused.",
                }
            ],
            "code_cells": [
                {
                    "markdown": "## Code Lab 1: Build and inspect a price table",
                    "code": _md(
                        """\
                        import pandas as pd

                        prices = pd.DataFrame(
                            {
                                "date": pd.date_range("2026-01-01", periods=5, freq="D"),
                                "asset_a": [100, 101, None, 103, 104],
                                "asset_b": [50, 49, 50, 51, 52],
                            }
                        ).set_index("date")
                        print(prices)
                        print("\\nMissing values:")
                        print(prices.isna().sum())
                        """
                    ),
                },
                {
                    "markdown": "## Code Lab 2: Clean and compute returns",
                    "code": _md(
                        """\
                        cleaned = prices.ffill()
                        returns = cleaned.pct_change().dropna()
                        print(cleaned)
                        print("\\nReturns:")
                        print(returns.round(4))
                        """
                    ),
                },
                {
                    "markdown": "## Code Lab 3: Join with simple metadata",
                    "code": _md(
                        """\
                        metadata = pd.DataFrame(
                            {
                                "ticker": ["asset_a", "asset_b"],
                                "sector": ["equity", "commodity_proxy"],
                            }
                        )
                        melted = cleaned.reset_index().melt(id_vars="date", var_name="ticker", value_name="price")
                        merged = melted.merge(metadata, on="ticker", how="left")
                        print(merged.head())
                        """
                    ),
                },
            ],
        },
        "Wed": {
            "estimated_time": "4 hours",
            "study_blocks": [
                ("Block 1", "45 min", "Learn why plots are part of research, not decoration."),
                ("Block 2", "55 min", "Plot price, return, and rolling statistics."),
                ("Block 3", "55 min", "Interpret visual patterns carefully."),
                ("Block 4", "55 min", "Code charting drills."),
                ("Block 5", "30 min", "Interview recap and notes."),
            ],
            "overview": [
                "Visualization is part of quantitative reasoning. A good chart can reveal a bug, an outlier, a regime change, or a structure that summary numbers missed.",
                "The main goal today is to stop plotting mechanically and start asking what each visual tells you about the data-generating process.",
            ],
            "concepts": [
                {
                    "title": "Price plots versus return plots",
                    "simple": "Prices show levels over time, while returns show changes over time.",
                    "technical": "Price charts can reveal trends and regime shifts, but returns are more suitable for many statistical analyses because they are more comparable across assets.",
                    "finance_example": "A steadily rising price series may still hide unstable return volatility.",
                },
                {
                    "title": "Rolling statistics",
                    "simple": "Rolling metrics summarize how averages or volatility behave over a moving window.",
                    "technical": "Rolling means and rolling standard deviations help identify local behavior, changing regimes, and volatility clustering.",
                    "finance_example": "A strategy may look stable overall while a rolling volatility chart shows hidden turbulence.",
                },
                {
                    "title": "Visual interpretation with caution",
                    "simple": "A chart is evidence, not proof.",
                    "technical": "Patterns in charts can be informative but may also be driven by noise, scaling choices, or short samples.",
                    "finance_example": "Apparent mean reversion in a tiny sample may disappear out of sample.",
                },
            ],
            "worked_examples": [
                "Plot prices, returns, and rolling volatility for one toy asset.",
                "Show how an outlier day is obvious in a return series but not always in a price chart.",
                "Compare the same data on two chart scales and discuss interpretation risk.",
            ],
            "practice_with_answers": [
                {
                    "question": "Why are rolling statistics useful in finance?",
                    "answer": "Because market behavior changes over time, so one full-sample average often hides local shifts in trend or risk.",
                },
                {
                    "question": "Why should a quant avoid over-trusting charts?",
                    "answer": "Because visual patterns can be sample-specific, scale-dependent, or just noise.",
                },
                {
                    "question": "What can a return histogram reveal?",
                    "answer": "It can reveal skew, fat tails, clustering near zero, or outliers that matter for risk and modeling.",
                },
            ],
            "interview_drill": [
                {
                    "question": "What is the first chart you would make for a new financial series?",
                    "answer": "Usually I would inspect both the price series and the return series, then add a rolling volatility view to understand stability.",
                }
            ],
            "code_cells": [
                {
                    "markdown": "## Code Lab 1: Plot a toy market series",
                    "code": _md(
                        """\
                        import pandas as pd
                        import matplotlib.pyplot as plt

                        prices = pd.Series([100, 101, 102, 101, 103, 104, 106, 105, 107, 108], name="price")
                        returns = prices.pct_change().dropna()
                        rolling_vol = returns.rolling(3).std()

                        fig, axes = plt.subplots(3, 1, figsize=(8, 7))
                        prices.plot(ax=axes[0], title="Price")
                        returns.plot(ax=axes[1], title="Returns")
                        rolling_vol.plot(ax=axes[2], title="Rolling 3-period volatility")
                        plt.tight_layout()
                        plt.show()
                        """
                    ),
                },
                {
                    "markdown": "## Code Lab 2: Histogram and descriptive view",
                    "code": _md(
                        """\
                        fig, ax = plt.subplots(figsize=(6, 4))
                        returns.hist(ax=ax, bins=5)
                        ax.set_title("Return histogram")
                        plt.tight_layout()
                        plt.show()

                        print(returns.describe().round(4))
                        """
                    ),
                },
            ],
        },
        "Thu": {
            "estimated_time": "4 hours",
            "study_blocks": [
                ("Block 1", "45 min", "Understand correlation and covariance intuitively."),
                ("Block 2", "55 min", "Compute co-movement measures from returns."),
                ("Block 3", "55 min", "Link co-movement to diversification."),
                ("Block 4", "55 min", "Practice interpretation and code."),
                ("Block 5", "30 min", "Interview recap."),
            ],
            "overview": [
                "Diversification is not magic. It works because assets do not move perfectly together all the time.",
                "Today is about understanding co-movement well enough to explain why diversification can reduce risk even when every asset is risky on its own.",
            ],
            "concepts": [
                {
                    "title": "Correlation",
                    "simple": "Correlation measures how strongly two variables tend to move together.",
                    "technical": "It is a standardized measure of linear co-movement between -1 and 1.",
                    "finance_example": "Two equity ETFs may have high positive correlation, while stocks and bonds may sometimes have lower correlation.",
                },
                {
                    "title": "Covariance",
                    "simple": "Covariance measures whether two variables move together, but it is not scaled.",
                    "technical": "Covariance appears naturally in portfolio variance formulas because it captures how joint movements contribute to total risk.",
                    "finance_example": "Portfolio risk is lower when component assets have lower or negative covariance.",
                },
                {
                    "title": "Diversification logic",
                    "simple": "If assets do not all rise and fall together, combining them can smooth the overall path.",
                    "technical": "Portfolio variance depends on both individual variances and pairwise covariances, not just average volatility.",
                    "finance_example": "A mixed portfolio of assets can have lower volatility than its components if co-movement is low enough.",
                },
            ],
            "worked_examples": [
                "Compare two assets with similar volatility but different correlation to a third asset.",
                "Show how a two-asset portfolio can be less volatile than both standalone assets if correlation is low enough.",
                "Interpret a correlation matrix economically rather than mechanically.",
            ],
            "practice_with_answers": [
                {
                    "question": "Why is correlation alone not enough for portfolio variance?",
                    "answer": "Because actual risk contribution also depends on each asset's own volatility and weight, not only the correlation sign and magnitude.",
                },
                {
                    "question": "Why can diversification fail in crises?",
                    "answer": "Because correlations often rise during stress, making assets move together more than expected.",
                },
                {
                    "question": "What is the intuition behind covariance in a portfolio?",
                    "answer": "It captures whether two assets amplify or offset each other's moves.",
                },
            ],
            "interview_drill": [
                {
                    "question": "Why does low correlation help a portfolio?",
                    "answer": "Because when assets do not move perfectly together, their fluctuations partially offset and reduce overall variance.",
                }
            ],
            "code_cells": [
                {
                    "markdown": "## Code Lab 1: Correlation and covariance matrix",
                    "code": _md(
                        """\
                        import pandas as pd

                        returns = pd.DataFrame(
                            {
                                "asset_a": [0.01, 0.02, -0.01, 0.01, 0.00],
                                "asset_b": [0.00, 0.01, -0.02, 0.02, 0.01],
                                "asset_c": [0.02, -0.01, 0.01, 0.00, 0.03],
                            }
                        )
                        print("Correlation:")
                        print(returns.corr().round(3))
                        print("\\nCovariance:")
                        print(returns.cov().round(5))
                        """
                    ),
                },
                {
                    "markdown": "## Code Lab 2: Two-asset portfolio variance intuition",
                    "code": _md(
                        """\
                        import numpy as np

                        weights = np.array([0.5, 0.5])
                        cov_2 = returns[["asset_a", "asset_b"]].cov().values
                        portfolio_variance = weights @ cov_2 @ weights
                        print("Portfolio volatility:", round(np.sqrt(portfolio_variance), 4))
                        """
                    ),
                },
            ],
        },
        "Fri": {
            "estimated_time": "4 hours",
            "study_blocks": [
                ("Block 1", "45 min", "Learn weight vectors and rebalancing intuition."),
                ("Block 2", "55 min", "Understand cumulative performance tracking."),
                ("Block 3", "55 min", "Learn where SQL fits in a quant workflow."),
                ("Block 4", "55 min", "Run code labs on portfolio tables and SQL queries."),
                ("Block 5", "30 min", "Interview recap."),
            ],
            "overview": [
                "A quant researcher needs both portfolio mechanics and data retrieval discipline. Today combines those two practical skills.",
                "The goal is to understand how weights translate into performance and why SQL remains useful even when much of the analysis happens in Python.",
            ],
            "concepts": [
                {
                    "title": "Portfolio weights and rebalancing",
                    "simple": "Weights tell you how much of the portfolio is assigned to each asset. Rebalancing resets those weights after markets move.",
                    "technical": "Without rebalancing, weights drift as relative asset performance changes. That changes exposures and risk over time.",
                    "finance_example": "A 60/40 portfolio does not stay 60/40 if equities rally strongly and no rebalance is performed.",
                },
                {
                    "title": "Cumulative performance",
                    "simple": "Cumulative performance tracks how wealth evolves when returns compound over time.",
                    "technical": "A cumulative wealth index is typically formed by chaining gross returns period by period.",
                    "finance_example": "Two strategies with the same average return can produce very different wealth paths if their volatility differs.",
                },
                {
                    "title": "SQL in quant research",
                    "simple": "SQL is a way to query structured data stored in tables.",
                    "technical": "Even if modeling is done in Python, SQL is often used to filter, group, aggregate, and join historical market or transaction datasets efficiently.",
                    "finance_example": "You might query daily prices for a ticker universe before moving the result into pandas for analysis.",
                },
            ],
            "worked_examples": [
                "Track a two-asset portfolio with and without rebalancing.",
                "Build a simple wealth index from daily portfolio returns.",
                "Use SQL-style queries on a toy price table with DuckDB.",
            ],
            "practice_with_answers": [
                {
                    "question": "Why does a portfolio drift if you do not rebalance?",
                    "answer": "Because winners and losers change their portfolio weights mechanically as their values change.",
                },
                {
                    "question": "Why is SQL still useful for a quant?",
                    "answer": "Because many research workflows start by pulling or filtering large structured datasets before numerical analysis begins.",
                },
                {
                    "question": "What is a simple cumulative wealth index?",
                    "answer": "It is the compounded value of starting capital after applying each period's gross return in sequence.",
                },
            ],
            "interview_drill": [
                {
                    "question": "Where would SQL fit in a quant pipeline?",
                    "answer": "Usually in data retrieval, filtering, joining, and aggregation before features, models, or backtests are built in Python.",
                }
            ],
            "code_cells": [
                {
                    "markdown": "## Code Lab 1: Portfolio drift and cumulative wealth",
                    "code": _md(
                        """\
                        import pandas as pd

                        returns = pd.DataFrame(
                            {
                                "equity": [0.02, -0.01, 0.03, 0.01],
                                "bond": [0.00, 0.01, -0.005, 0.002],
                            }
                        )
                        weights = pd.Series({"equity": 0.6, "bond": 0.4})
                        portfolio_returns = returns.mul(weights, axis=1).sum(axis=1)
                        wealth = 100 * (1 + portfolio_returns).cumprod()
                        print(portfolio_returns.round(4))
                        print(wealth.round(2))
                        """
                    ),
                },
                {
                    "markdown": "## Code Lab 2: SQL on a toy market table with DuckDB",
                    "code": _md(
                        """\
                        import duckdb

                        con = duckdb.connect()
                        con.register("returns", returns.reset_index(names="day"))
                        query = '''
                            SELECT
                                AVG(equity) AS avg_equity_return,
                                AVG(bond) AS avg_bond_return
                            FROM returns
                        '''
                        print(con.execute(query).df())
                        """
                    ),
                },
            ],
        },
        "Sat": {
            "estimated_time": "2 hours",
            "study_blocks": [
                ("Block 1", "25 min", "Week 2 recall from memory."),
                ("Block 2", "35 min", "SQL and data-cleaning drill."),
                ("Block 3", "35 min", "Error log and concept map."),
                ("Block 4", "25 min", "Interview practice."),
            ],
            "overview": [
                "This weekend block keeps Week 2 practical. Instead of learning a large new topic, you consolidate the data workflow habits that will support every later quant project.",
            ],
            "concepts": [
                {
                    "title": "Revision through active data tasks",
                    "simple": "The best review is to clean, compute, and explain again without copying old work.",
                    "technical": "Retrieval plus application is stronger than passive re-reading for building durable technical fluency.",
                    "finance_example": "Recomputing a correlation matrix from scratch is better review than staring at yesterday's output.",
                }
            ],
            "worked_examples": [
                "Rewrite a simple SQL query from memory.",
                "Recreate a small price-cleaning pipeline without looking at notes.",
            ],
            "practice_with_answers": [
                {
                    "question": "What is one sign you truly understand a data workflow?",
                    "answer": "You can rebuild it cleanly from memory and explain why each step exists.",
                }
            ],
            "interview_drill": [
                {
                    "question": "What is one common data-handling mistake in quant research?",
                    "answer": "Misalignment across dates or assets, which can quietly contaminate results.",
                }
            ],
            "code_cells": [
                {
                    "markdown": "## Code Lab: Quick review drill",
                    "code": _md(
                        """\
                        import pandas as pd

                        review = pd.DataFrame(
                            {
                                "ticker": ["A", "A", "B", "B"],
                                "price": [100, 101, 50, 52],
                            }
                        )
                        review["return_guess"] = review.groupby("ticker")["price"].pct_change()
                        print(review)
                        """
                    ),
                }
            ],
        },
        "Sun": {
            "estimated_time": "2 hours",
            "study_blocks": [
                ("Block 1", "20 min", "Mini-project planning."),
                ("Block 2", "55 min", "Build comparison notebook."),
                ("Block 3", "20 min", "Write interpretation."),
                ("Block 4", "25 min", "Weekly review and interview summary."),
            ],
            "overview": [
                "The Week 2 mini-project turns your data skills into a simple research artifact: compare three assets and explain diversification with evidence.",
            ],
            "concepts": [
                {
                    "title": "Mini-project framing",
                    "simple": "The project should connect data cleaning, return computation, correlation, and interpretation in one clean notebook.",
                    "technical": "A strong beginner project shows a full analytical chain from raw table to insight, not just isolated code cells.",
                    "finance_example": "A three-asset comparison can already demonstrate why co-movement matters for portfolio thinking.",
                }
            ],
            "worked_examples": [
                "Compare three toy assets with different volatility and correlation profiles.",
                "Write one paragraph on which pair looks most diversifying and why.",
            ],
            "practice_with_answers": [
                {
                    "question": "What makes the Week 2 project stronger than just a chart dump?",
                    "answer": "A clear question, clean data handling, an interpretable correlation result, and an honest written conclusion.",
                }
            ],
            "interview_drill": [
                {
                    "question": "How would you describe this project in one line?",
                    "answer": "I built a small data-to-insight notebook showing how return co-movement affects diversification across three assets.",
                }
            ],
            "code_cells": [
                {
                    "markdown": "## Code Lab: Project starter preview",
                    "code": _md(
                        """\
                        import pandas as pd

                        project_prices = pd.DataFrame(
                            {
                                "asset_a": [100, 101, 103, 104, 105, 106],
                                "asset_b": [50, 50.5, 50, 51, 51.5, 52],
                                "asset_c": [80, 79, 81, 80, 82, 83],
                            }
                        )
                        project_returns = project_prices.pct_change().dropna()
                        print(project_returns.corr().round(3))
                        """
                    ),
                }
            ],
        },
    },
    3: {
        "Mon": {
            "estimated_time": "4 hours",
            "study_blocks": [
                ("Block 1", "45 min", "Rebuild algebra basics."),
                ("Block 2", "55 min", "Practice fractions, powers, and rearrangement."),
                ("Block 3", "55 min", "Learn exponents and logs in finance language."),
                ("Block 4", "55 min", "Code simple growth and log examples."),
                ("Block 5", "30 min", "Interview recap."),
            ],
            "overview": [
                "Quant finance becomes painful very quickly if algebra feels shaky. This day is about regaining control of the symbols so later probability, optimization, and ML feel manageable.",
                "You are not trying to be flashy here. You are building fluency with the manipulations that appear constantly in formulas, scaling laws, and growth calculations.",
            ],
            "concepts": [
                {
                    "title": "Equations and rearrangement",
                    "simple": "An equation states that two expressions are equal, and rearranging means solving for the quantity you care about.",
                    "technical": "Many finance formulas are useful only after algebraic rearrangement, such as isolating a rate, return, or weight.",
                    "finance_example": "If final wealth and initial wealth are known, algebra lets you solve for the return needed to get there.",
                },
                {
                    "title": "Exponents",
                    "simple": "Exponents represent repeated multiplication.",
                    "technical": "Compounding, discounting, and growth models often use powers because repeated percentage changes are multiplicative.",
                    "finance_example": "Annual compounding over multiple years is naturally written with an exponent.",
                },
                {
                    "title": "Logarithms",
                    "simple": "A logarithm answers the question: what power do I raise a number to get another number?",
                    "technical": "Logs are useful for turning multiplication into addition and for understanding log returns and growth rates.",
                    "finance_example": "Continuous compounding and log-return thinking both depend on logarithms.",
                },
            ],
            "worked_examples": [
                "Solve for the return needed to grow 100 to 121 in two equal compounded steps.",
                "Use a log to estimate how many periods are needed to double at a given rate.",
            ],
            "practice_with_answers": [
                {
                    "question": "Why do exponents show up in compounding?",
                    "answer": "Because repeating the same growth factor many times is repeated multiplication, which is what exponents represent compactly.",
                },
                {
                    "question": "Why are logarithms useful in quant finance?",
                    "answer": "Because they simplify multiplicative growth and support continuous-compounding and log-return interpretations.",
                },
            ],
            "interview_drill": [
                {
                    "question": "Why should a quant care about logs early?",
                    "answer": "Because logs appear in growth, scaling, probability, and continuous-time finance models, and they simplify many multiplicative relationships.",
                }
            ],
            "code_cells": [
                {
                    "markdown": "## Code Lab 1: Compounding and logs",
                    "code": _md(
                        """\
                        import numpy as np

                        initial = 100
                        rate = 0.08
                        years = 5
                        final = initial * (1 + rate) ** years
                        log_growth = np.log(final / initial)

                        print("Final value:", round(final, 2))
                        print("Log growth:", round(log_growth, 4))
                        """
                    ),
                },
                {
                    "markdown": "## Code Lab 2: Solve doubling time approximately",
                    "code": _md(
                        """\
                        doubling_time = np.log(2) / np.log(1 + rate)
                        print("Approximate doubling time:", round(doubling_time, 2), "years")
                        """
                    ),
                },
            ],
        },
        "Tue": {
            "estimated_time": "4 hours",
            "study_blocks": [
                ("Block 1", "45 min", "Learn slope intuition."),
                ("Block 2", "55 min", "Understand derivatives as sensitivity."),
                ("Block 3", "55 min", "Connect derivatives to finance and optimization."),
                ("Block 4", "55 min", "Code slope examples."),
                ("Block 5", "30 min", "Interview recap."),
            ],
            "overview": [
                "Calculus starts becoming useful once you stop seeing the derivative as a scary symbol and start seeing it as a sensitivity measure.",
                "In quant finance, sensitivity is everywhere: how price changes when yield changes, how option value changes when volatility changes, or how loss changes when a model parameter changes.",
            ],
            "concepts": [
                {
                    "title": "Slope as rate of change",
                    "simple": "Slope tells you how much one quantity changes when another changes.",
                    "technical": "The derivative captures the local rate of change of a function with respect to its input.",
                    "finance_example": "A bond price changing when yield changes is a sensitivity problem.",
                },
                {
                    "title": "Derivative as local approximation",
                    "simple": "A derivative approximates what happens for a very small change.",
                    "technical": "It is the limit of the difference quotient as the input change goes to zero.",
                    "finance_example": "Option Greeks are local sensitivity measures, not full descriptions of all possible moves.",
                },
                {
                    "title": "Optimization intuition",
                    "simple": "Derivatives help locate points where a function stops increasing and may turn around.",
                    "technical": "Critical points occur when the first derivative is zero or undefined, and second-derivative intuition helps assess local curvature.",
                    "finance_example": "Optimization problems in portfolio or ML settings often rely on sensitivity reasoning.",
                },
            ],
            "worked_examples": [
                "Find the slope of a line and interpret it economically.",
                "Use a simple quadratic function to discuss where the derivative becomes zero.",
            ],
            "practice_with_answers": [
                {
                    "question": "Why are derivatives important in finance?",
                    "answer": "Because finance constantly asks how one value changes with another, which is exactly what sensitivity measures capture.",
                },
                {
                    "question": "What does it mean if a derivative is positive?",
                    "answer": "It means the function is locally increasing as the input rises.",
                },
            ],
            "interview_drill": [
                {
                    "question": "How would you explain a derivative without calculus jargon?",
                    "answer": "It measures how sensitive one quantity is to a small change in another quantity.",
                }
            ],
            "code_cells": [
                {
                    "markdown": "## Code Lab 1: Numerical slope",
                    "code": _md(
                        """\
                        def f(x):
                            return x**2 + 2*x

                        x = 3
                        h = 1e-5
                        derivative_estimate = (f(x + h) - f(x)) / h
                        print("Numerical derivative near x=3:", round(derivative_estimate, 4))
                        """
                    ),
                },
                {
                    "markdown": "## Code Lab 2: Sensitivity table",
                    "code": _md(
                        """\
                        import pandas as pd

                        xs = pd.Series([0, 1, 2, 3, 4], name="x")
                        ys = xs.apply(f)
                        print(pd.DataFrame({"x": xs, "f_x": ys}))
                        """
                    ),
                },
            ],
        },
        "Wed": {
            "estimated_time": "4 hours",
            "study_blocks": [
                ("Block 1", "45 min", "Understand accumulation and area intuition."),
                ("Block 2", "55 min", "Relate integrals to totals and averages."),
                ("Block 3", "55 min", "Connect accumulation to finance."),
                ("Block 4", "55 min", "Code approximation examples."),
                ("Block 5", "30 min", "Interview recap."),
            ],
            "overview": [
                "Integrals are easier to digest when seen as accumulation rather than as abstract notation.",
                "In finance, accumulation ideas appear in continuous-time reasoning, total exposure, and moving from local change to total effect.",
            ],
            "concepts": [
                {
                    "title": "Integral as accumulation",
                    "simple": "An integral adds up many tiny pieces to get a total.",
                    "technical": "Definite integrals can be viewed as limits of sums over small intervals.",
                    "finance_example": "Accumulating a continuously changing growth rate over time leads naturally to integral thinking.",
                },
                {
                    "title": "Area intuition",
                    "simple": "The area under a curve is one geometric way to understand a definite integral.",
                    "technical": "This geometric picture is useful even when the interpretation is not literally area.",
                    "finance_example": "If instantaneous returns or rates vary through time, the total effect is an accumulated quantity.",
                },
                {
                    "title": "Local change to total effect",
                    "simple": "If the derivative tells you local change, the integral helps recover the total accumulated change.",
                    "technical": "Differentiation and integration are linked by the fundamental theorem of calculus.",
                    "finance_example": "Sensitivity and accumulation are two sides of the same modeling story.",
                },
            ],
            "worked_examples": [
                "Approximate the area under a simple curve with rectangles.",
                "Interpret a constant rate over time as repeated accumulation.",
            ],
            "practice_with_answers": [
                {
                    "question": "What is the simplest intuition for an integral?",
                    "answer": "It adds up many tiny contributions to get a total accumulated quantity.",
                },
                {
                    "question": "How is integration related to finance?",
                    "answer": "Finance often studies quantities that evolve continuously, so accumulation over time naturally leads to integral thinking.",
                },
            ],
            "interview_drill": [
                {
                    "question": "How would you explain the link between derivatives and integrals?",
                    "answer": "Derivatives describe local change, while integrals accumulate those local changes into a total effect.",
                }
            ],
            "code_cells": [
                {
                    "markdown": "## Code Lab 1: Rectangle approximation",
                    "code": _md(
                        """\
                        import numpy as np

                        xs = np.linspace(0, 2, 100)
                        fx = xs**2
                        area_approx = np.sum(fx[:-1] * np.diff(xs))
                        print("Approximate area under x^2 from 0 to 2:", round(area_approx, 4))
                        """
                    ),
                },
                {
                    "markdown": "## Code Lab 2: Compare with exact value",
                    "code": _md(
                        """\
                        exact_area = (2**3) / 3
                        print("Exact area:", round(exact_area, 4))
                        """
                    ),
                },
            ],
        },
        "Thu": {
            "estimated_time": "4 hours",
            "study_blocks": [
                ("Block 1", "45 min", "Learn probability rules and events."),
                ("Block 2", "55 min", "Understand random variables and distributions."),
                ("Block 3", "55 min", "Connect probabilities to payoffs."),
                ("Block 4", "55 min", "Code simple discrete simulations."),
                ("Block 5", "30 min", "Interview recap."),
            ],
            "overview": [
                "Probability is not an optional side topic in quant finance. It is the language for uncertainty, risk, forecasting, and expected outcomes.",
                "Today focuses on intuitive foundations rather than advanced formalism, but the goal is still technical correctness.",
            ],
            "concepts": [
                {
                    "title": "Events and probabilities",
                    "simple": "An event is something that may happen, and probability measures how likely it is.",
                    "technical": "Probabilities satisfy basic rules such as non-negativity, normalization, and additivity under disjoint events.",
                    "finance_example": "A positive-return day or a default event can be treated as events in a probability model.",
                },
                {
                    "title": "Random variables",
                    "simple": "A random variable assigns a number to each uncertain outcome.",
                    "technical": "Returns, losses, and payoffs are often modeled as random variables in finance.",
                    "finance_example": "A one-day portfolio return is a random variable because it is not known in advance.",
                },
                {
                    "title": "Distribution thinking",
                    "simple": "A distribution describes the range of possible values and how likely they are.",
                    "technical": "Good decisions in finance depend on the whole distribution, not just the average.",
                    "finance_example": "A strategy with the same average return can still be worse if it has much fatter downside tails.",
                },
            ],
            "worked_examples": [
                "List the outcomes and probabilities of a simple trade.",
                "Create a toy payoff distribution and compute the expected payoff.",
            ],
            "practice_with_answers": [
                {
                    "question": "Why does a quant care about distributions and not only means?",
                    "answer": "Because risk, drawdown, and extreme outcomes live in the distribution's spread and tails, not only in its average.",
                },
                {
                    "question": "What is a random variable in one sentence?",
                    "answer": "It is a numerical representation of an uncertain outcome.",
                },
            ],
            "interview_drill": [
                {
                    "question": "Why is expected value not enough by itself?",
                    "answer": "Because two payoffs can have the same expectation but very different risk and tail behavior.",
                }
            ],
            "code_cells": [
                {
                    "markdown": "## Code Lab 1: Discrete payoff distribution",
                    "code": _md(
                        """\
                        import numpy as np

                        outcomes = np.array([3, 1, -2])
                        probabilities = np.array([0.2, 0.5, 0.3])
                        print("Expected payoff:", np.sum(outcomes * probabilities))
                        """
                    ),
                },
                {
                    "markdown": "## Code Lab 2: Simulate repeated draws",
                    "code": _md(
                        """\
                        rng = np.random.default_rng(0)
                        samples = rng.choice(outcomes, size=1000, p=probabilities)
                        print("Sample mean:", round(samples.mean(), 4))
                        print("Sample std:", round(samples.std(), 4))
                        """
                    ),
                },
            ],
        },
        "Fri": {
            "estimated_time": "4 hours",
            "study_blocks": [
                ("Block 1", "45 min", "Learn JSON and API response structure."),
                ("Block 2", "55 min", "Understand conditional probability and Bayes intuition."),
                ("Block 3", "55 min", "Connect evidence updating to finance decisions."),
                ("Block 4", "55 min", "Code a small response-parsing and Bayes example."),
                ("Block 5", "30 min", "Interview recap."),
            ],
            "overview": [
                "A modern quant often pulls or inspects data from APIs, but the deeper idea today is evidence updating. Bayes intuition teaches you not to overreact to one observation without considering base rates.",
                "That habit is useful in markets, model evaluation, and research interpretation.",
            ],
            "concepts": [
                {
                    "title": "APIs and JSON",
                    "simple": "An API is a way for one program to request data from another. JSON is a common text format used to return structured data.",
                    "technical": "Understanding nested structures, keys, and parsing is enough to begin inspecting API outputs in finance workflows.",
                    "finance_example": "A market-data endpoint may return timestamps, prices, and metadata in JSON format before you convert them into a table.",
                },
                {
                    "title": "Conditional probability",
                    "simple": "Conditional probability asks how likely an event is given that another event has happened.",
                    "technical": "P(A|B) measures the probability of A under the condition that B is known.",
                    "finance_example": "The probability of loss given a volatility spike is a conditional question.",
                },
                {
                    "title": "Bayes intuition",
                    "simple": "Bayes updates beliefs when new evidence arrives, but it does not ignore the prior baseline.",
                    "technical": "Posterior belief combines prior belief with the likelihood of the new evidence.",
                    "finance_example": "One strong signal should update your confidence, but not erase the base rate of noisy market behavior.",
                },
            ],
            "worked_examples": [
                "Parse a toy JSON response representing daily prices.",
                "Use a simple Bayes-style disease-test style analogy and then connect it to noisy trading signals.",
            ],
            "practice_with_answers": [
                {
                    "question": "Why is Bayes intuition useful in trading research?",
                    "answer": "Because it teaches you to combine new evidence with prior uncertainty instead of overreacting to one signal or one backtest result.",
                },
                {
                    "question": "What is conditional probability in simple terms?",
                    "answer": "It is the probability of one event after you already know another event has happened.",
                },
            ],
            "interview_drill": [
                {
                    "question": "Why are base rates important when interpreting signals?",
                    "answer": "Because rare events and noisy predictors can easily fool you if you ignore the starting probability of what you are trying to predict.",
                }
            ],
            "code_cells": [
                {
                    "markdown": "## Code Lab 1: Parse a toy JSON response",
                    "code": _md(
                        """\
                        import pandas as pd

                        response = {
                            "ticker": "XYZ",
                            "prices": [
                                {"date": "2026-01-01", "close": 100},
                                {"date": "2026-01-02", "close": 102},
                                {"date": "2026-01-03", "close": 101},
                            ],
                        }
                        df = pd.DataFrame(response["prices"])
                        print(df)
                        """
                    ),
                },
                {
                    "markdown": "## Code Lab 2: Simple Bayes update",
                    "code": _md(
                        """\
                        prior = 0.10
                        likelihood_if_true = 0.70
                        likelihood_if_false = 0.20

                        posterior = (likelihood_if_true * prior) / (
                            likelihood_if_true * prior + likelihood_if_false * (1 - prior)
                        )
                        print("Posterior probability:", round(posterior, 4))
                        """
                    ),
                },
            ],
        },
        "Sat": {
            "estimated_time": "2 hours",
            "study_blocks": [
                ("Block 1", "25 min", "Math recall drill."),
                ("Block 2", "35 min", "Probability and Bayes recap."),
                ("Block 3", "35 min", "Error log and formula rewrite."),
                ("Block 4", "25 min", "Interview practice."),
            ],
            "overview": [
                "Today is about making the new math vocabulary stick. You should be able to explain exponents, logs, derivatives, integrals, probability, and Bayes at a clean beginner level after this revision block.",
            ],
            "concepts": [
                {
                    "title": "Integrated recall",
                    "simple": "The goal is to connect the week's ideas rather than memorize them in isolation.",
                    "technical": "Algebra, calculus, and probability support each other in quantitative reasoning, especially when moving between formulas and interpretations.",
                    "finance_example": "A pricing or risk formula is easier to understand when you can interpret the algebra, the sensitivity, and the uncertainty together.",
                }
            ],
            "worked_examples": [
                "Rewrite one formula from each weekday topic without notes.",
            ],
            "practice_with_answers": [
                {
                    "question": "What is the real sign that math is improving?",
                    "answer": "You can restate the idea in plain English, do a simple calculation, and connect it to a finance use case without freezing.",
                }
            ],
            "interview_drill": [
                {
                    "question": "What math topic from this week feels most useful for quant work?",
                    "answer": "A good answer is whichever concept you can explain with both intuition and a finance example, such as expected value, derivative as sensitivity, or Bayes-style updating.",
                }
            ],
            "code_cells": [
                {
                    "markdown": "## Code Lab: Quick formula recap",
                    "code": _md(
                        """\
                        import numpy as np

                        print("log(2):", round(np.log(2), 4))
                        print("exp(1):", round(np.exp(1), 4))
                        """
                    ),
                }
            ],
        },
        "Sun": {
            "estimated_time": "2 hours",
            "study_blocks": [
                ("Block 1", "20 min", "Project framing."),
                ("Block 2", "55 min", "Monte Carlo simulation build."),
                ("Block 3", "20 min", "Interpretation and reflection."),
                ("Block 4", "25 min", "Weekly review."),
            ],
            "overview": [
                "The Week 3 project ties math to uncertainty. A Monte Carlo notebook is one of the cleanest beginner ways to see how probability, expected value, and sampling variation interact.",
            ],
            "concepts": [
                {
                    "title": "Monte Carlo intuition",
                    "simple": "Monte Carlo means simulating many possible outcomes to understand a distribution.",
                    "technical": "Even when analytic answers exist, simulation helps build intuition for variability, tail risk, and the gap between expected and realized outcomes.",
                    "finance_example": "Repeatedly simulating a trading payoff shows why a positive edge still produces streaks of losses.",
                }
            ],
            "worked_examples": [
                "Simulate 1000 paths of a simple discrete trading payoff.",
                "Compare the simulated sample mean with the theoretical expected value.",
            ],
            "practice_with_answers": [
                {
                    "question": "Why is Monte Carlo useful for beginners in quant finance?",
                    "answer": "Because it makes uncertainty concrete and shows the distribution of possible outcomes instead of only one formula.",
                }
            ],
            "interview_drill": [
                {
                    "question": "What does a Monte Carlo simulation help you see that a single expected value does not?",
                    "answer": "It shows dispersion, tail outcomes, streaks, and the range of realistic sample paths.",
                }
            ],
            "code_cells": [
                {
                    "markdown": "## Code Lab: Monte Carlo preview",
                    "code": _md(
                        """\
                        import numpy as np

                        rng = np.random.default_rng(42)
                        outcomes = np.array([2.0, -1.0])
                        probabilities = np.array([0.6, 0.4])
                        samples = rng.choice(outcomes, size=1000, p=probabilities)
                        print("Simulated mean:", round(samples.mean(), 4))
                        """
                    ),
                }
            ],
        },
    },
    4: {
        "Mon": {
            "estimated_time": "4 hours",
            "study_blocks": [
                ("Block 1", "45 min", "Learn samples, populations, estimators."),
                ("Block 2", "55 min", "Understand bias and variance intuition."),
                ("Block 3", "55 min", "Relate estimator quality to finance datasets."),
                ("Block 4", "55 min", "Code sampling examples."),
                ("Block 5", "30 min", "Interview recap."),
            ],
            "overview": [
                "Statistics becomes far more useful once you understand that sample numbers are not truth. They are estimates produced from noisy limited data.",
                "That mindset is essential in finance because historical samples are often short, unstable, and regime-dependent.",
            ],
            "concepts": [
                {
                    "title": "Population versus sample",
                    "simple": "The population is the full underlying process. The sample is the subset you actually observe.",
                    "technical": "In finance we almost never observe the full truth, so we rely on sample estimates of quantities like mean return or volatility.",
                    "finance_example": "Your backtest uses a historical sample, not the full future distribution of returns.",
                },
                {
                    "title": "Estimators",
                    "simple": "An estimator is a rule for turning data into an estimate.",
                    "technical": "Sample mean and sample variance are estimators of underlying population moments.",
                    "finance_example": "A historical Sharpe ratio is an estimate, not a permanent property of a strategy.",
                },
                {
                    "title": "Bias and variance",
                    "simple": "Bias means systematic error; variance means how much the estimate moves around across samples.",
                    "technical": "Good estimation balances systematic accuracy and stability.",
                    "finance_example": "A strategy metric from a tiny sample may have huge variance even if the estimator itself is unbiased.",
                },
            ],
            "worked_examples": [
                "Compare two small samples from the same distribution and show different means.",
                "Explain why a noisy estimator can lead to overconfident portfolio choices.",
            ],
            "practice_with_answers": [
                {
                    "question": "Why is a sample mean not the same as the true expected return?",
                    "answer": "Because it is based on limited noisy observations and may differ materially from the underlying long-run average.",
                },
                {
                    "question": "What is the intuition behind estimator variance?",
                    "answer": "If you repeated the sampling process many times, a high-variance estimator would jump around a lot from sample to sample.",
                },
            ],
            "interview_drill": [
                {
                    "question": "Why are small samples dangerous in finance?",
                    "answer": "Because noisy estimates can look strong by chance and drive bad decisions about models, signals, or portfolios.",
                }
            ],
            "code_cells": [
                {
                    "markdown": "## Code Lab 1: Sampling variability",
                    "code": _md(
                        """\
                        import numpy as np

                        rng = np.random.default_rng(0)
                        sample_1 = rng.normal(0.01, 0.02, size=20)
                        sample_2 = rng.normal(0.01, 0.02, size=20)
                        print("Sample 1 mean:", round(sample_1.mean(), 4))
                        print("Sample 2 mean:", round(sample_2.mean(), 4))
                        """
                    ),
                },
                {
                    "markdown": "## Code Lab 2: Repeated-estimate spread",
                    "code": _md(
                        """\
                        estimates = [rng.normal(0.01, 0.02, size=20).mean() for _ in range(500)]
                        print("Mean of estimates:", round(np.mean(estimates), 4))
                        print("Std of estimates:", round(np.std(estimates), 4))
                        """
                    ),
                },
            ],
        },
        "Tue": {
            "estimated_time": "4 hours",
            "study_blocks": [
                ("Block 1", "45 min", "Confidence interval intuition."),
                ("Block 2", "55 min", "Hypothesis testing as evidence check."),
                ("Block 3", "55 min", "Common misuse in finance."),
                ("Block 4", "55 min", "Code interval examples."),
                ("Block 5", "30 min", "Interview recap."),
            ],
            "overview": [
                "Confidence intervals and tests are often memorized badly. Today the goal is not symbolic overload. The goal is to understand what level of uncertainty remains around an estimate.",
                "That matters in finance because weak evidence can easily be mistaken for edge.",
            ],
            "concepts": [
                {
                    "title": "Confidence interval intuition",
                    "simple": "A confidence interval gives a plausible range for an unknown quantity based on the sample.",
                    "technical": "It reflects sampling uncertainty around an estimator under model assumptions.",
                    "finance_example": "A strategy with a positive sample mean may still have a wide interval that includes weak or negative true edge.",
                },
                {
                    "title": "Hypothesis testing",
                    "simple": "A test asks whether the evidence is strong enough to challenge a baseline claim.",
                    "technical": "In many settings the baseline claim is a null hypothesis such as zero mean effect.",
                    "finance_example": "You may test whether a signal's average return differs meaningfully from zero.",
                },
                {
                    "title": "Evidence versus certainty",
                    "simple": "A test result is evidence, not proof.",
                    "technical": "Statistical significance does not automatically imply economic significance or robustness.",
                    "finance_example": "A tiny effect can be statistically noticeable in a large sample yet useless after costs.",
                },
            ],
            "worked_examples": [
                "Construct a rough interval around a sample mean.",
                "Explain why a narrow interval is different from a profitable strategy.",
            ],
            "practice_with_answers": [
                {
                    "question": "Why is statistical significance not enough in finance?",
                    "answer": "Because trading viability also depends on effect size, costs, risk, stability, and implementation realism.",
                },
                {
                    "question": "What does a wide confidence interval suggest?",
                    "answer": "It suggests high uncertainty about the true parameter given the sample and assumptions.",
                },
            ],
            "interview_drill": [
                {
                    "question": "How would you explain a confidence interval simply?",
                    "answer": "It is a range of plausible values for the unknown quantity based on what the sample tells us.",
                }
            ],
            "code_cells": [
                {
                    "markdown": "## Code Lab 1: Rough confidence interval",
                    "code": _md(
                        """\
                        import numpy as np

                        sample = np.array([0.01, 0.02, -0.01, 0.00, 0.03, 0.01, -0.02, 0.02])
                        mean = sample.mean()
                        std = sample.std(ddof=1)
                        se = std / np.sqrt(len(sample))
                        ci_low = mean - 1.96 * se
                        ci_high = mean + 1.96 * se
                        print(round(mean, 4), round(ci_low, 4), round(ci_high, 4))
                        """
                    ),
                }
            ],
        },
        "Wed": {
            "estimated_time": "4 hours",
            "study_blocks": [
                ("Block 1", "45 min", "Regression intuition."),
                ("Block 2", "55 min", "Slope, intercept, residuals, fit quality."),
                ("Block 3", "55 min", "Interpret coefficients economically."),
                ("Block 4", "55 min", "Code a tiny OLS example."),
                ("Block 5", "30 min", "Interview recap."),
            ],
            "overview": [
                "Regression is a foundational bridge between statistics, ML, and finance. It gives you a language for relationships, sensitivity, and residual noise.",
                "Today is about interpreting regression meaningfully, not memorizing a formula without context.",
            ],
            "concepts": [
                {
                    "title": "Regression as best-fit relationship",
                    "simple": "Regression tries to describe how one variable changes on average with another.",
                    "technical": "OLS chooses coefficients that minimize the sum of squared residuals.",
                    "finance_example": "You might regress an asset's returns on market returns to estimate beta-like sensitivity.",
                },
                {
                    "title": "Residuals",
                    "simple": "Residuals are what the model did not explain.",
                    "technical": "They are the differences between observed values and fitted values.",
                    "finance_example": "Large residuals may suggest omitted drivers, noise, or regime changes.",
                },
                {
                    "title": "Interpretation over blind fitting",
                    "simple": "A coefficient means something only if the setup makes economic sense.",
                    "technical": "Regression can quantify a relationship, but not every estimated relationship is causal or stable.",
                    "finance_example": "A positive regression coefficient on a short sample is not automatically a tradable edge.",
                },
            ],
            "worked_examples": [
                "Fit a line to market and asset returns.",
                "Interpret the slope as sensitivity and the residuals as unexplained movement.",
            ],
            "practice_with_answers": [
                {
                    "question": "What does the slope coefficient mean in a simple regression?",
                    "answer": "It represents the expected change in the target for a one-unit change in the input, on average within the sample.",
                },
                {
                    "question": "Why are residuals useful?",
                    "answer": "They show what the model failed to explain and can reveal noise, missing structure, or instability.",
                },
            ],
            "interview_drill": [
                {
                    "question": "How would you explain regression to a non-specialist?",
                    "answer": "It is a way to quantify the average relationship between variables and see how much noise remains around that relationship.",
                }
            ],
            "code_cells": [
                {
                    "markdown": "## Code Lab 1: Simple linear regression",
                    "code": _md(
                        """\
                        import numpy as np
                        from sklearn.linear_model import LinearRegression

                        x = np.array([[0.01], [0.02], [-0.01], [0.03], [0.00]])
                        y = np.array([0.012, 0.018, -0.008, 0.028, 0.002])

                        model = LinearRegression()
                        model.fit(x, y)
                        print("Intercept:", round(float(model.intercept_), 4))
                        print("Slope:", round(float(model.coef_[0]), 4))
                        """
                    ),
                },
                {
                    "markdown": "## Code Lab 2: Residuals",
                    "code": _md(
                        """\
                        predictions = model.predict(x)
                        residuals = y - predictions
                        print(np.round(residuals, 5))
                        """
                    ),
                },
            ],
        },
        "Thu": {
            "estimated_time": "4 hours",
            "study_blocks": [
                ("Block 1", "45 min", "Optimization intuition."),
                ("Block 2", "55 min", "Objective functions and constraints."),
                ("Block 3", "55 min", "Portfolio examples."),
                ("Block 4", "55 min", "Code simple constrained search."),
                ("Block 5", "30 min", "Interview recap."),
            ],
            "overview": [
                "Optimization is simply the art of choosing the best feasible option under a clear objective and constraints.",
                "In finance, constraints matter as much as objectives because real portfolios are not free to do anything.",
            ],
            "concepts": [
                {
                    "title": "Objective function",
                    "simple": "An objective function measures what you are trying to maximize or minimize.",
                    "technical": "Examples include maximizing expected return, minimizing variance, or minimizing prediction error.",
                    "finance_example": "A portfolio optimizer might minimize volatility for a given return target.",
                },
                {
                    "title": "Constraints",
                    "simple": "Constraints limit what choices are allowed.",
                    "technical": "Constraints can include weights summing to one, no shorting, leverage limits, or turnover caps.",
                    "finance_example": "A portfolio with no-shorting cannot assign negative weights.",
                },
                {
                    "title": "Trade-offs",
                    "simple": "Optimization is usually about balancing competing goals.",
                    "technical": "Higher return may come with higher risk, and cleaner predictions may require more model complexity.",
                    "finance_example": "A high-return portfolio may be unacceptable if it violates risk or concentration limits.",
                },
            ],
            "worked_examples": [
                "Pick portfolio weights from a small grid to minimize simple variance under constraints.",
                "Explain how the answer changes if short selling is allowed versus forbidden.",
            ],
            "practice_with_answers": [
                {
                    "question": "Why are constraints essential in finance optimization?",
                    "answer": "Because the mathematically best answer is often unrealistic or risky if not limited by practical rules.",
                },
                {
                    "question": "What is an objective function in plain language?",
                    "answer": "It is the score you are trying to make as good as possible.",
                },
            ],
            "interview_drill": [
                {
                    "question": "How would you explain optimization simply?",
                    "answer": "It is choosing the best available option after defining what 'best' means and what rules cannot be broken.",
                }
            ],
            "code_cells": [
                {
                    "markdown": "## Code Lab 1: Brute-force portfolio search",
                    "code": _md(
                        """\
                        import numpy as np

                        cov = np.array([[0.04, 0.01], [0.01, 0.02]])
                        candidates = np.linspace(0, 1, 11)
                        results = []

                        for w in candidates:
                            weights = np.array([w, 1 - w])
                            variance = weights @ cov @ weights
                            results.append((w, variance))

                        best = min(results, key=lambda x: x[1])
                        print("Best weight in asset 1:", best[0])
                        print("Minimum variance:", round(best[1], 4))
                        """
                    ),
                }
            ],
        },
        "Fri": {
            "estimated_time": "4 hours",
            "study_blocks": [
                ("Block 1", "45 min", "Portfolio theory intuition."),
                ("Block 2", "55 min", "Efficient frontier and Sharpe ratio."),
                ("Block 3", "55 min", "Estimation fragility and caution."),
                ("Block 4", "55 min", "Code small portfolio comparisons."),
                ("Block 5", "30 min", "Interview recap."),
            ],
            "overview": [
                "Portfolio theory is one of the core languages of quant finance. Even if later practice becomes more complex, the risk-return framework remains central.",
                "You should come away knowing not just what the efficient frontier and Sharpe ratio are, but also why naive use can be misleading.",
            ],
            "concepts": [
                {
                    "title": "Mean-variance thinking",
                    "simple": "Portfolio theory weighs expected return against risk.",
                    "technical": "Risk is often approximated by variance or standard deviation, and diversification enters through covariance.",
                    "finance_example": "Two portfolios with the same expected return can differ sharply in volatility.",
                },
                {
                    "title": "Efficient frontier",
                    "simple": "The efficient frontier is the set of portfolios offering the best return for a given level of risk.",
                    "technical": "It is generated by optimization under expected-return and covariance assumptions.",
                    "finance_example": "A portfolio below the frontier is inefficient because another available portfolio dominates it.",
                },
                {
                    "title": "Sharpe ratio intuition",
                    "simple": "Sharpe ratio measures return per unit of risk.",
                    "technical": "It compares excess return to volatility, but it depends on estimated inputs and does not capture every risk type.",
                    "finance_example": "A smooth-looking strategy can have a high Sharpe yet still hide tail or liquidity risk.",
                },
            ],
            "worked_examples": [
                "Compare two portfolios by mean, volatility, and Sharpe-style intuition.",
                "Explain why estimated expected returns are often the weakest input.",
            ],
            "practice_with_answers": [
                {
                    "question": "What does a high Sharpe ratio suggest?",
                    "answer": "It suggests strong average return relative to volatility, but it does not guarantee robustness or protection from tail risk.",
                },
                {
                    "question": "Why is the efficient frontier fragile in practice?",
                    "answer": "Because it depends heavily on estimated returns and covariances, which are noisy and unstable.",
                },
            ],
            "interview_drill": [
                {
                    "question": "How would you explain the efficient frontier simply?",
                    "answer": "It is the set of portfolios that are hardest to improve because each one offers the best known return for its level of risk.",
                }
            ],
            "code_cells": [
                {
                    "markdown": "## Code Lab 1: Compare simple portfolios",
                    "code": _md(
                        """\
                        import numpy as np

                        mean_returns = np.array([0.10, 0.06])
                        cov = np.array([[0.04, 0.01], [0.01, 0.02]])

                        candidate_weights = [np.array([0.2, 0.8]), np.array([0.5, 0.5]), np.array([0.8, 0.2])]

                        for weights in candidate_weights:
                            expected_return = weights @ mean_returns
                            vol = np.sqrt(weights @ cov @ weights)
                            sharpe_like = expected_return / vol
                            print(np.round(weights, 2), round(expected_return, 4), round(vol, 4), round(sharpe_like, 4))
                        """
                    ),
                }
            ],
        },
        "Sat": {
            "estimated_time": "2 hours",
            "study_blocks": [
                ("Block 1", "20 min", "Capstone plan."),
                ("Block 2", "55 min", "Implement exploratory asset-allocation notebook."),
                ("Block 3", "20 min", "Interpret results."),
                ("Block 4", "25 min", "Interview practice."),
            ],
            "overview": [
                "This is the first proper Month 1 capstone build session. The job is not to create a perfect optimizer, but to combine returns, volatility, correlation, and portfolio logic into one coherent piece of work.",
            ],
            "concepts": [
                {
                    "title": "Capstone integration",
                    "simple": "A capstone should combine the week's ideas rather than repeating one isolated topic.",
                    "technical": "This one brings together descriptive statistics, covariance, and simple portfolio comparison.",
                    "finance_example": "A small asset-allocation study mirrors the early structure of real portfolio research.",
                }
            ],
            "worked_examples": [
                "Test a few candidate weights and compare return-risk trade-offs.",
            ],
            "practice_with_answers": [
                {
                    "question": "What makes a capstone useful for applications?",
                    "answer": "It shows you can frame a question, implement analysis, interpret results, and communicate limitations.",
                }
            ],
            "interview_drill": [
                {
                    "question": "How would you describe this capstone briefly?",
                    "answer": "I built an exploratory asset-allocation study comparing a few simple portfolios using return, volatility, and correlation logic.",
                }
            ],
            "code_cells": [
                {
                    "markdown": "## Code Lab: Capstone preview",
                    "code": _md(
                        """\
                        import pandas as pd

                        capstone_prices = pd.DataFrame(
                            {
                                "equity": [100, 102, 101, 104, 106, 107],
                                "bond": [100, 100.5, 101, 101.5, 101.3, 101.8],
                                "gold": [100, 99, 100.5, 101, 102, 103],
                            }
                        )
                        capstone_returns = capstone_prices.pct_change().dropna()
                        print(capstone_returns.head())
                        """
                    ),
                }
            ],
        },
        "Sun": {
            "estimated_time": "2 hours",
            "study_blocks": [
                ("Block 1", "20 min", "Finalize capstone notebook."),
                ("Block 2", "50 min", "Write conclusion and limitation note."),
                ("Block 3", "25 min", "Monthly assessment and tracker update."),
                ("Block 4", "25 min", "Interview Q&A review."),
            ],
            "overview": [
                "Month 1 finishes with communication, not just calculation. The capstone becomes valuable only when you can explain what it did, what it found, and what its limits are.",
            ],
            "concepts": [
                {
                    "title": "Communication as quant skill",
                    "simple": "A good quant result must be understandable to another human.",
                    "technical": "Professional research output includes methodology, result, risk, and limitation communication.",
                    "finance_example": "A PM or admissions reviewer cares about whether your logic is clear and defensible, not just whether your notebook runs.",
                }
            ],
            "worked_examples": [
                "Write a short conclusion comparing two portfolios and naming one limitation.",
            ],
            "practice_with_answers": [
                {
                    "question": "What should a capstone conclusion include?",
                    "answer": "The question, method, main result, and at least one limitation or next step.",
                }
            ],
            "interview_drill": [
                {
                    "question": "What limitation would you mention first for a beginner portfolio study?",
                    "answer": "Usually the small sample size, simplified assumptions, and lack of real transaction costs or broader asset history.",
                }
            ],
            "code_cells": [
                {
                    "markdown": "## Code Lab: Capstone summary view",
                    "code": _md(
                        """\
                        import pandas as pd

                        capstone_prices = pd.DataFrame(
                            {
                                "equity": [100, 102, 101, 104, 106, 107, 109, 110],
                                "bond": [100, 100.4, 100.8, 101.0, 101.3, 101.5, 101.6, 101.9],
                                "gold": [100, 99.5, 100.5, 101.0, 102.0, 101.8, 102.5, 103.0],
                            }
                        )
                        capstone_returns = capstone_prices.pct_change().dropna()
                        summary = capstone_returns.describe().round(4)
                        print(summary)
                        """
                    ),
                }
            ],
        },
    },
}


MONTH1_PROJECT_SPECS: dict[int, dict[str, Any]] = {
    2: {
        "title_markdown": _md(
            """\
            # Week 2 Mini Project: Three-Asset Diversification Notebook

            Build a clean notebook that:

            - loads a small three-asset price table
            - computes returns
            - compares volatility and correlation
            - discusses diversification clearly
            """
        ),
        "code_cells": [
            {
                "markdown": "## Step 1: Toy price data",
                "code": _md(
                    """\
                    import pandas as pd
                    import matplotlib.pyplot as plt

                    prices = pd.DataFrame(
                        {
                            "asset_a": [100, 102, 101, 104, 106, 107, 109],
                            "asset_b": [50, 50.2, 50.5, 50.4, 51.0, 51.1, 51.3],
                            "asset_c": [80, 79, 81, 80.5, 82, 81.5, 83],
                        }
                    )
                    print(prices)
                    """
                ),
            },
            {
                "markdown": "## Step 2: Returns and co-movement",
                "code": _md(
                    """\
                    returns = prices.pct_change().dropna()
                    print(returns.round(4))
                    print("\\nVolatility:")
                    print(returns.std().round(4))
                    print("\\nCorrelation:")
                    print(returns.corr().round(3))
                    """
                ),
            },
            {
                "markdown": "## Step 3: Plot normalized prices",
                "code": _md(
                    """\
                    normalized = prices / prices.iloc[0] * 100
                    normalized.plot(figsize=(8, 4), title="Normalized price paths")
                    plt.tight_layout()
                    plt.show()
                    """
                ),
            },
        ],
        "closing_markdown": _md(
            """\
            ## Suggested conclusion

            Explain:

            - which asset looked most volatile
            - which pair looked least correlated
            - why that matters for diversification
            - one limitation of the toy dataset
            """
        ),
    },
    3: {
        "title_markdown": _md(
            """\
            # Week 3 Mini Project: Monte Carlo Trade Simulation

            This notebook turns the week's math into a simulation artifact:

            - define a simple trade payoff distribution
            - simulate many repeated trades
            - compare theoretical and simulated outcomes
            - reflect on uncertainty and variance
            """
        ),
        "code_cells": [
            {
                "markdown": "## Step 1: Theoretical setup",
                "code": _md(
                    """\
                    import numpy as np
                    import matplotlib.pyplot as plt

                    outcomes = np.array([2.0, -1.0])
                    probabilities = np.array([0.6, 0.4])
                    expected_value = np.sum(outcomes * probabilities)
                    print("Expected value:", expected_value)
                    """
                ),
            },
            {
                "markdown": "## Step 2: Simulate many trades",
                "code": _md(
                    """\
                    rng = np.random.default_rng(123)
                    trades = rng.choice(outcomes, size=1000, p=probabilities)
                    cumulative_pnl = trades.cumsum()
                    print("Simulated average payoff:", round(trades.mean(), 4))
                    """
                ),
            },
            {
                "markdown": "## Step 3: Visualize outcome and cumulative path",
                "code": _md(
                    """\
                    fig, axes = plt.subplots(2, 1, figsize=(8, 6))
                    axes[0].hist(trades, bins=3)
                    axes[0].set_title("Trade payoff distribution")
                    axes[1].plot(cumulative_pnl)
                    axes[1].set_title("Cumulative PnL path")
                    plt.tight_layout()
                    plt.show()
                    """
                ),
            },
        ],
        "closing_markdown": _md(
            """\
            ## Suggested conclusion

            Explain why a positive expected value does not prevent short losing streaks, and relate the simulation output back to decision-making under uncertainty.
            """
        ),
    },
    4: {
        "title_markdown": _md(
            """\
            # Week 4 Capstone: Exploratory Asset Allocation Study

            Build a small but polished portfolio notebook that:

            - computes returns from three assets
            - summarizes volatility and correlations
            - compares simple candidate portfolios
            - explains the trade-offs clearly
            """
        ),
        "code_cells": [
            {
                "markdown": "## Step 1: Build the price table",
                "code": _md(
                    """\
                    import pandas as pd
                    import numpy as np
                    import matplotlib.pyplot as plt

                    prices = pd.DataFrame(
                        {
                            "equity": [100, 102, 101, 104, 106, 107, 109, 110],
                            "bond": [100, 100.4, 100.8, 101.0, 101.3, 101.5, 101.6, 101.9],
                            "gold": [100, 99.5, 100.5, 101.0, 102.0, 101.8, 102.5, 103.0],
                        }
                    )
                    returns = prices.pct_change().dropna()
                    print(returns.round(4))
                    """
                ),
            },
            {
                "markdown": "## Step 2: Candidate portfolios",
                "code": _md(
                    """\
                    candidate_portfolios = {
                        "balanced": np.array([0.4, 0.4, 0.2]),
                        "growth": np.array([0.7, 0.2, 0.1]),
                        "defensive": np.array([0.2, 0.6, 0.2]),
                    }

                    rows = []
                    cov = returns.cov().values
                    mean_returns = returns.mean().values

                    for name, weights in candidate_portfolios.items():
                        expected_return = weights @ mean_returns
                        vol = np.sqrt(weights @ cov @ weights)
                        rows.append(
                            {
                                "portfolio": name,
                                "expected_return": expected_return,
                                "volatility": vol,
                                "return_to_risk": expected_return / vol,
                            }
                        )

                    summary = pd.DataFrame(rows)
                    print(summary.round(4))
                    """
                ),
            },
            {
                "markdown": "## Step 3: Visualize normalized prices",
                "code": _md(
                    """\
                    normalized = prices / prices.iloc[0] * 100
                    normalized.plot(figsize=(8, 4), title="Normalized assets")
                    plt.tight_layout()
                    plt.show()
                    """
                ),
            },
        ],
        "closing_markdown": _md(
            """\
            ## Suggested conclusion

            Comment on:

            - which portfolio looked most aggressive
            - which looked most defensive
            - how correlation shaped the result
            - what would need to improve before treating this as a serious investment process
            """
        ),
    },
}


def has_detailed_day(week_number: int, day_label: str) -> bool:
    return day_label in MONTH1_EXTRA_DAY_DETAILS.get(week_number, {})


def render_detailed_day_markdown(week_number: int, day: dict[str, Any]) -> str:
    detail = MONTH1_EXTRA_DAY_DETAILS[week_number][day["day"]]
    lines: list[str] = [
        f"# Week {week_number:02d} {day['day']}: {day['topic']}",
        "",
        f"**Estimated time:** {detail['estimated_time']}",
        "",
        "## Session Plan",
        "| Session | Duration | Focus |",
        "| --- | --- | --- |",
    ]
    for index, (_, duration, focus) in enumerate(detail["study_blocks"], start=1):
        lines.append(f"| Session {index} | {duration} | {focus} |")
    lines.extend(["", "## Why It Matters In Quant", day["why"], "", "## Learning Overview"])
    for paragraph in detail["overview"]:
        lines.extend([paragraph, ""])
    lines.extend(
        [
            "## Continuity",
            "- Start by recalling what from yesterday is still unclear.",
            "- Use today's topic to fix at least one weak area from your error log.",
            "- End by writing a one-paragraph bridge to tomorrow's topic.",
            "",
        ]
    )
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
    lines.extend(["", "## Practice Questions With Answers"])
    for item in detail["practice_with_answers"]:
        lines.extend([f"### Question: {item['question']}", f"Answer: {item['answer']}", ""])
    lines.extend(
        [
            "## Extended Study (to complete a full 4-hour day)",
            "1. Rewrite each core concept in your own words without looking at notes.",
            "2. Add one extra worked example using different numbers or assumptions.",
            "3. Explain one failure mode where this concept can be misapplied in trading or risk work.",
            "4. Add one short paragraph linking this concept to your weekly project objective.",
            "",
        ]
    )
    lines.extend(["## Coding Task", day["coding_task"], "", "## Daily Interview Drill"])
    for qa in detail["interview_drill"]:
        lines.extend([f"### Q: {qa['question']}", f"A: {qa['answer']}", ""])
    lines.extend(
        [
            "## Reflection Question",
            day["reflection"],
            "",
            "## Completion Checklist",
            "- I completed the planned study blocks or adjusted them honestly.",
            "- I rewrote the main ideas from memory.",
            "- I finished the notebook cells and checked the outputs.",
            "- I logged at least one weak spot in the error log.",
            "- I practiced at least one interview answer aloud.",
        ]
    )
    return "\n".join(lines) + "\n"


def detailed_day_notebook_spec(week_number: int, day: dict[str, Any]) -> dict[str, Any]:
    detail = MONTH1_EXTRA_DAY_DETAILS[week_number][day["day"]]
    intro = [
        f"# Week {week_number} {day['day']}: {day['topic']}",
        "",
        f"Estimated time: {detail['estimated_time']}",
        "",
        "## Why this matters",
        day["why"],
        "",
        "## Session plan",
    ]
    for index, (_, duration, focus) in enumerate(detail["study_blocks"], start=1):
        intro.append(f"- Session {index} ({duration}): {focus}")
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
    intro.extend(
        [
            "## Continuity prompt",
            "- What from yesterday's topic still needs reinforcement?",
            "- What should tomorrow build on from today?",
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


def project_notebook_spec(week_number: int) -> dict[str, Any]:
    return MONTH1_PROJECT_SPECS[week_number]
