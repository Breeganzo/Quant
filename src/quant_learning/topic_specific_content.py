from __future__ import annotations

import textwrap


def _code(block: str) -> str:
    return textwrap.dedent(block).strip() + "\n"


def domain_for_week(week_number: int) -> str:
    mapping = {
        1: "foundations",
        2: "data",
        3: "math_stats",
        4: "math_stats",
        5: "ml_foundations",
        6: "ml_foundations",
        7: "ml_foundations",
        8: "time_series",
        9: "microstructure",
        10: "portfolio",
        11: "fixed_income",
        12: "derivatives",
        13: "research_design",
        14: "backtesting",
        15: "signals",
        16: "stat_arb",
        17: "ml_foundations",
        18: "volatility_risk",
        19: "ai_workflow",
        20: "ai_workflow",
        21: "applications",
        22: "interview_drills",
        23: "communication",
        24: "capstone",
    }
    return mapping.get(week_number, "foundations")


def formula_entries_for_week(week_number: int) -> list[dict[str, str]]:
    domain = domain_for_week(week_number)

    if domain == "data":
        return [
            {
                "name": "Simple Return",
                "equation": "r_t = \\frac{P_t}{P_{t-1}} - 1",
                "meaning": "Relative one-period price change used for comparable analytics.",
                "use_case": "Build aligned return tables before joins and cleaning.",
                "pitfall": "Mixing simple and log returns in one pipeline.",
            },
            {
                "name": "Covariance",
                "equation": "\\mathrm{Cov}(X,Y)=\\frac{1}{n-1}\\sum_{i=1}^{n}(x_i-\\bar x)(y_i-\\bar y)",
                "meaning": "Joint variation of two series around their means.",
                "use_case": "Diversification diagnostics before portfolio construction.",
                "pitfall": "Ignoring missing-value alignment before computing covariance.",
            },
            {
                "name": "Correlation",
                "equation": "\\rho_{XY}=\\frac{\\mathrm{Cov}(X,Y)}{\\sigma_X\\sigma_Y}",
                "meaning": "Scale-free co-movement measure in [-1, 1].",
                "use_case": "Screen assets for complementary behavior.",
                "pitfall": "Interpreting correlation as causation.",
            },
        ]

    if domain == "math_stats":
        return [
            {
                "name": "Expected Value",
                "equation": "\\mathbb{E}[X]=\\sum_i p_i x_i",
                "meaning": "Probability-weighted average outcome across scenarios.",
                "use_case": "Evaluate expected payoff of a repeated decision rule.",
                "pitfall": "Ignoring tail risk while focusing only on mean payoff.",
            },
            {
                "name": "Bayes Rule",
                "equation": "P(A\\mid B)=\\frac{P(B\\mid A)P(A)}{P(B)}",
                "meaning": "Posterior update from prior belief and evidence likelihood.",
                "use_case": "Revise signal confidence after new market evidence.",
                "pitfall": "Neglecting base rates.",
            },
            {
                "name": "OLS Slope",
                "equation": "\\hat\\beta=\\frac{\\sum (x_i-\\bar x)(y_i-\\bar y)}{\\sum (x_i-\\bar x)^2}",
                "meaning": "Best linear sensitivity estimate under squared-error loss.",
                "use_case": "Estimate directional relation between factor and return.",
                "pitfall": "Assuming stability without checking residual behavior.",
            },
        ]

    if domain == "ml_foundations":
        return [
            {
                "name": "Logistic Link",
                "equation": "p(y=1\\mid x)=\\frac{1}{1+e^{-z}},\\ z=w^Tx+b",
                "meaning": "Maps linear score to class probability.",
                "use_case": "Probability of positive next-period return event.",
                "pitfall": "Treating probability as certainty near threshold.",
            },
            {
                "name": "Cross-Entropy Loss",
                "equation": "L=-\\frac{1}{n}\\sum_{i=1}^n [y_i\\log p_i + (1-y_i)\\log(1-p_i)]",
                "meaning": "Penalizes confident wrong classifications strongly.",
                "use_case": "Train classification baselines for risk events.",
                "pitfall": "Evaluating only loss without class-balance diagnostics.",
            },
            {
                "name": "F1 Score",
                "equation": "F1=2\\cdot\\frac{\\mathrm{Precision}\\cdot\\mathrm{Recall}}{\\mathrm{Precision}+\\mathrm{Recall}}",
                "meaning": "Balances false-positive and false-negative tradeoff.",
                "use_case": "Model selection under class imbalance.",
                "pitfall": "Using accuracy alone on imbalanced labels.",
            },
        ]

    if domain == "time_series":
        return [
            {
                "name": "AR(1)",
                "equation": "x_t=c+\\phi x_{t-1}+\\epsilon_t",
                "meaning": "Current value depends on one lag plus noise.",
                "use_case": "Baseline dependence and mean-reversion diagnostics.",
                "pitfall": "Ignoring non-stationarity before fitting AR models.",
            },
            {
                "name": "EWMA Variance",
                "equation": "\\sigma_t^2=\\lambda\\sigma_{t-1}^2+(1-\\lambda)r_{t-1}^2",
                "meaning": "Recency-weighted volatility estimate.",
                "use_case": "Adaptive risk forecasting.",
                "pitfall": "Choosing decay factor without validation.",
            },
            {
                "name": "RMSE",
                "equation": "\\mathrm{RMSE}=\\sqrt{\\frac{1}{n}\\sum_{i=1}^{n}(\\hat y_i-y_i)^2}",
                "meaning": "Average forecast error magnitude in original units.",
                "use_case": "Compare forecasting pipelines.",
                "pitfall": "Comparing RMSE across differently scaled targets.",
            },
        ]

    if domain == "microstructure":
        return [
            {
                "name": "Mid Price",
                "equation": "m_t=\\frac{\\mathrm{bid}_t+\\mathrm{ask}_t}{2}",
                "meaning": "Reference price between best bid and ask.",
                "use_case": "Execution quality benchmarking.",
                "pitfall": "Comparing fills to stale mid prices.",
            },
            {
                "name": "Effective Spread",
                "equation": "\\mathrm{EffSpread}_t=2\\cdot\\left|\\frac{p_t^{exec}-m_t}{m_t}\\right|",
                "meaning": "Realized transaction cost proxy.",
                "use_case": "Estimate execution drag in backtests.",
                "pitfall": "Ignoring direction and sign conventions.",
            },
            {
                "name": "Turnover",
                "equation": "\\mathrm{TO}_t=\\frac{1}{2}\\sum_i|w_{i,t}-w_{i,t-1}|",
                "meaning": "Fraction of portfolio traded on rebalance.",
                "use_case": "Capacity and cost control.",
                "pitfall": "Reporting gross turnover without cost translation.",
            },
        ]

    if domain == "portfolio":
        return [
            {
                "name": "Portfolio Variance",
                "equation": "\\sigma_p^2=w^T\\Sigma w",
                "meaning": "Total risk from weights and covariance matrix.",
                "use_case": "Optimize risk-aware allocations.",
                "pitfall": "Using unstable covariance estimates without shrinkage.",
            },
            {
                "name": "CAPM Expected Return",
                "equation": "\\mathbb{E}[R_i]=R_f+\\beta_i(\\mathbb{E}[R_m]-R_f)",
                "meaning": "Expected return from market beta exposure.",
                "use_case": "Baseline required-return sanity checks.",
                "pitfall": "Treating CAPM as a complete model.",
            },
            {
                "name": "Marginal Risk Contribution",
                "equation": "\\mathrm{MRC}_i=\\frac{w_i(\\Sigma w)_i}{\\sigma_p}",
                "meaning": "Asset-level contribution to portfolio risk.",
                "use_case": "Risk budgeting and constraint design.",
                "pitfall": "Ignoring concentration from correlated exposures.",
            },
        ]

    if domain == "fixed_income":
        return [
            {
                "name": "Bond Price",
                "equation": "P=\\sum_{t=1}^{T}\\frac{CF_t}{(1+y)^t}",
                "meaning": "Present value of discounted cash flows.",
                "use_case": "Mark-to-model pricing for plain-vanilla bonds.",
                "pitfall": "Mixing compounding conventions.",
            },
            {
                "name": "Modified Duration",
                "equation": "D_{mod}=\\frac{D_{mac}}{1+y}",
                "meaning": "Approximate percentage price sensitivity to yield.",
                "use_case": "Rate-shock risk estimation.",
                "pitfall": "Using duration alone for large yield moves.",
            },
            {
                "name": "Convexity",
                "equation": "C=\\frac{1}{P}\\sum_{t=1}^{T}\\frac{CF_t\\,t(t+1)}{(1+y)^{t+2}}",
                "meaning": "Second-order sensitivity adjustment to yield moves.",
                "use_case": "Improve rate-shock approximation accuracy.",
                "pitfall": "Ignoring convexity in stressed scenarios.",
            },
        ]

    if domain == "derivatives":
        return [
            {
                "name": "Call Payoff",
                "equation": "\\mathrm{Payoff}_{call}=\\max(S_T-K,0)",
                "meaning": "Upside above strike with limited downside (premium aside).",
                "use_case": "Directional convex exposure design.",
                "pitfall": "Confusing payoff with profit (ignoring premium).",
            },
            {
                "name": "Put Payoff",
                "equation": "\\mathrm{Payoff}_{put}=\\max(K-S_T,0)",
                "meaning": "Downside protection structure at maturity.",
                "use_case": "Hedging drawdown risk.",
                "pitfall": "Ignoring time decay before maturity.",
            },
            {
                "name": "Delta",
                "equation": "\\Delta=\\frac{\\partial V}{\\partial S}",
                "meaning": "First-order option value sensitivity to underlying.",
                "use_case": "Hedge ratio sizing.",
                "pitfall": "Assuming delta is constant across moves and time.",
            },
        ]

    if domain == "research_design":
        return [
            {
                "name": "Information Coefficient",
                "equation": "IC=\\mathrm{Corr}(signal_t, r_{t+1})",
                "meaning": "Association between signal and future return.",
                "use_case": "Early alpha hypothesis screening.",
                "pitfall": "Treating a single-period IC as stable edge.",
            },
            {
                "name": "t-Statistic",
                "equation": "t=\\frac{\\hat\\alpha}{SE(\\hat\\alpha)}",
                "meaning": "Effect size scaled by estimation uncertainty.",
                "use_case": "Assess hypothesis significance.",
                "pitfall": "Ignoring multiple-testing inflation.",
            },
            {
                "name": "Hit Rate",
                "equation": "\\mathrm{HitRate}=\\frac{\\#(sign(\\hat r_t)=sign(r_t))}{N}",
                "meaning": "Directional correctness frequency.",
                "use_case": "Classify forecast usefulness.",
                "pitfall": "High hit rate with poor payoff asymmetry.",
            },
        ]

    if domain == "backtesting":
        return [
            {
                "name": "Strategy Return with Costs",
                "equation": "r_t^{strat}=w_{t-1}^Tr_t-c_t",
                "meaning": "Net return after implementation frictions.",
                "use_case": "Realistic backtest evaluation.",
                "pitfall": "Ignoring costs in reported performance.",
            },
            {
                "name": "Max Drawdown",
                "equation": "MDD=\\min_t\\left(\\frac{W_t}{\\max_{s\\le t}W_s}-1\\right)",
                "meaning": "Worst peak-to-trough capital decline.",
                "use_case": "Risk limit calibration.",
                "pitfall": "Reporting Sharpe without drawdown context.",
            },
            {
                "name": "Turnover",
                "equation": "\\mathrm{TO}_t=\\frac{1}{2}\\sum_i|w_{i,t}-w_{i,t-1}|",
                "meaning": "Trading intensity proxy for cost pressure.",
                "use_case": "Capacity and slippage monitoring.",
                "pitfall": "High-turnover alpha that vanishes net of costs.",
            },
        ]

    if domain == "signals":
        return [
            {
                "name": "Momentum Signal",
                "equation": "m_t=\\frac{P_t}{P_{t-k}}-1",
                "meaning": "Past trend strength over lookback k.",
                "use_case": "Cross-sectional ranking strategies.",
                "pitfall": "Ignoring crash risk in reversals.",
            },
            {
                "name": "Mean-Reversion z-Score",
                "equation": "z_t=\\frac{x_t-\\mu_t}{\\sigma_t}",
                "meaning": "Deviation from local mean in standard units.",
                "use_case": "Entry/exit bands for reversal trades.",
                "pitfall": "Using unstable rolling windows.",
            },
            {
                "name": "Alpha Attribution",
                "equation": "\\alpha_t=r_t^{strat}-\\beta_t r_t^{mkt}",
                "meaning": "Residual performance after market exposure.",
                "use_case": "Diagnose true signal contribution.",
                "pitfall": "Assuming constant beta through regimes.",
            },
        ]

    if domain == "stat_arb":
        return [
            {
                "name": "Spread",
                "equation": "s_t=y_t-\\beta x_t",
                "meaning": "Relative value residual after hedge ratio adjustment.",
                "use_case": "Pairs trading mean-reversion setup.",
                "pitfall": "Skipping hedge-ratio estimation stability checks.",
            },
            {
                "name": "Spread z-Score",
                "equation": "z_t=\\frac{s_t-\\mu_s}{\\sigma_s}",
                "meaning": "Normalized spread deviation signal.",
                "use_case": "Rule-based entry and exit bands.",
                "pitfall": "Using static moments in regime shifts.",
            },
            {
                "name": "Half-Life",
                "equation": "\\mathrm{HL}= -\\frac{\\ln 2}{\\ln \\phi}",
                "meaning": "Expected mean-reversion speed from AR(1) phi.",
                "use_case": "Set holding horizon expectations.",
                "pitfall": "Estimating phi on non-stationary spread.",
            },
        ]

    if domain == "volatility_risk":
        return [
            {
                "name": "Realized Volatility",
                "equation": "\\sigma_{ann}=\\sqrt{252}\\cdot\\mathrm{Std}(r_t)",
                "meaning": "Sample-based annualized risk estimate.",
                "use_case": "Position sizing and stress planning.",
                "pitfall": "Ignoring clustering and regime changes.",
            },
            {
                "name": "EWMA Volatility",
                "equation": "\\sigma_t^2=\\lambda\\sigma_{t-1}^2+(1-\\lambda)r_{t-1}^2",
                "meaning": "Recency-weighted volatility forecasting.",
                "use_case": "Adaptive VaR pipelines.",
                "pitfall": "Decay hyperparameter not validated out-of-sample.",
            },
            {
                "name": "GARCH(1,1)",
                "equation": "\\sigma_t^2=\\omega+\\alpha r_{t-1}^2+\\beta\\sigma_{t-1}^2",
                "meaning": "Conditional variance with persistence and shocks.",
                "use_case": "Risk forecast under volatility clustering.",
                "pitfall": "Assuming model stability across crises.",
            },
        ]

    if domain == "ai_workflow":
        return [
            {
                "name": "Precision",
                "equation": "\\mathrm{Precision}=\\frac{TP}{TP+FP}",
                "meaning": "How often flagged items are truly correct.",
                "use_case": "Quality control of extracted insights.",
                "pitfall": "High precision with very low coverage.",
            },
            {
                "name": "Recall",
                "equation": "\\mathrm{Recall}=\\frac{TP}{TP+FN}",
                "meaning": "How many true items are captured.",
                "use_case": "Guardrail calibration for missed risks.",
                "pitfall": "High recall with noisy false positives.",
            },
            {
                "name": "Hallucination Rate",
                "equation": "HR=\\frac{\\#\\text{unsupported claims}}{\\#\\text{total claims}}",
                "meaning": "Share of generated statements lacking evidence.",
                "use_case": "LLM workflow safety monitoring.",
                "pitfall": "No citation checks in production research notes.",
            },
        ]

    if domain == "applications":
        return [
            {
                "name": "Program Fit Score",
                "equation": "Fit=w_1\\cdot curriculum+w_2\\cdot career+w_3\\cdot cost",
                "meaning": "Weighted ranking of degree options.",
                "use_case": "Prioritize application targets.",
                "pitfall": "Ignoring downside constraints like debt burden.",
            },
            {
                "name": "Scholarship Ratio",
                "equation": "SR=\\frac{grant}{tuition+living}",
                "meaning": "Funding share of full program cost.",
                "use_case": "Financial feasibility comparison.",
                "pitfall": "Comparing grants without total-cost normalization.",
            },
            {
                "name": "Narrative Evidence Coverage",
                "equation": "NEC=\\frac{\\#supported claims}{\\#total claims}",
                "meaning": "How much of SOP narrative is evidence-backed.",
                "use_case": "Strengthen application credibility.",
                "pitfall": "Aspirational claims without portfolio evidence.",
            },
        ]

    if domain == "interview_drills":
        return [
            {
                "name": "Expected Value",
                "equation": "\\mathbb{E}[X]=\\sum_i p_i x_i",
                "meaning": "Core quantitative interview staple.",
                "use_case": "Fast probability reasoning under pressure.",
                "pitfall": "Forgetting payoff asymmetry.",
            },
            {
                "name": "z-Score",
                "equation": "z=\\frac{x-\\mu}{\\sigma}",
                "meaning": "Standardized distance from mean.",
                "use_case": "Outlier checks in data screens.",
                "pitfall": "Using unstable sigma estimates.",
            },
            {
                "name": "OLS Beta",
                "equation": "\\hat\\beta=(X^TX)^{-1}X^Ty",
                "meaning": "Closed-form linear estimate.",
                "use_case": "Regression interview derivation drills.",
                "pitfall": "Ignoring multicollinearity and conditioning.",
            },
        ]

    if domain == "communication":
        return [
            {
                "name": "Evidence Coverage",
                "equation": "EC=\\frac{\\#claims\ with\ evidence}{\\#claims}",
                "meaning": "Share of statements supported by data or outputs.",
                "use_case": "Case-study defense quality.",
                "pitfall": "Narrative claims without references.",
            },
            {
                "name": "Clarity Ratio",
                "equation": "CR=\\frac{\\#clear\ action\ points}{\\#total\ points}",
                "meaning": "How actionable the communication is.",
                "use_case": "Improve portfolio presentation readability.",
                "pitfall": "Dense reports without decision guidance.",
            },
            {
                "name": "Limitation Disclosure Rate",
                "equation": "LDR=\\frac{\\#explicit\ limitations}{\\#major\ findings}",
                "meaning": "Transparency level of model/report caveats.",
                "use_case": "Credible interview and stakeholder communication.",
                "pitfall": "Overstating confidence by hiding caveats.",
            },
        ]

    if domain == "capstone":
        return [
            {
                "name": "Net Strategy Return",
                "equation": "r_t^{net}=r_t^{gross}-cost_t",
                "meaning": "Performance after implementation assumptions.",
                "use_case": "Final capstone realism checks.",
                "pitfall": "Reporting only gross backtest outcomes.",
            },
            {
                "name": "Out-of-Sample RMSE",
                "equation": "RMSE_{OOS}=\\sqrt{\\frac{1}{n}\\sum(\\hat y_i-y_i)^2}",
                "meaning": "Forecast quality on unseen evaluation window.",
                "use_case": "Model comparison in final report.",
                "pitfall": "Tuning decisions leaked from test set.",
            },
            {
                "name": "Max Drawdown",
                "equation": "MDD=\\min_t\\left(\\frac{W_t}{\\max_{s\\le t}W_s}-1\\right)",
                "meaning": "Worst capital drop in deployment-like simulation.",
                "use_case": "Risk section of capstone defense.",
                "pitfall": "Ignoring path dependency in risk narrative.",
            },
        ]

    return [
        {
            "name": "Log Return",
            "equation": "\\ell_t=\\ln\\left(\\frac{P_t}{P_{t-1}}\\right)",
            "meaning": "Additive return representation across time.",
            "use_case": "Multi-period analytics.",
            "pitfall": "Mixing with simple returns without context.",
        },
        {
            "name": "Annualized Volatility",
            "equation": "\\sigma_{ann}=\\sqrt{252}\\cdot\\mathrm{Std}(r_t)",
            "meaning": "Daily uncertainty scaled to annual horizon.",
            "use_case": "Risk budgeting.",
            "pitfall": "Mismatched frequency assumptions.",
        },
        {
            "name": "Sharpe Ratio",
            "equation": "S=\\frac{R_{ann}-R_f}{\\sigma_{ann}}",
            "meaning": "Excess return per risk unit.",
            "use_case": "Strategy comparison.",
            "pitfall": "Ignoring regime instability.",
        },
    ]


def coding_task_for_topic(week_number: int, topic: str) -> str:
    domain = domain_for_week(week_number)
    topic_lower = topic.lower()

    templates = {
        "data": "Build a cleaned feature table for {topic} and show one validation check that catches a data issue.",
        "math_stats": "Implement a small reproducible example for {topic} and explain one assumption that could fail in markets.",
        "ml_foundations": "Train a baseline classifier/regressor for {topic} on market-derived features and report one robust metric beyond accuracy.",
        "time_series": "Construct a lag-based pipeline for {topic} and compare one forecast baseline to one improved variant.",
        "microstructure": "Simulate one execution or turnover scenario for {topic} and quantify its cost impact.",
        "portfolio": "Compute a risk-aware allocation for {topic} and explain one concentration risk from the resulting weights.",
        "fixed_income": "Price a simple bond setup for {topic} and measure sensitivity to a yield shock.",
        "derivatives": "Implement payoff and sensitivity calculations for {topic} and interpret one hedging implication.",
        "research_design": "Create a hypothesis test workflow for {topic} and log one anti-leakage guardrail.",
        "backtesting": "Backtest a toy rule for {topic} with transaction costs and report net metrics.",
        "signals": "Build and compare at least two signal variants for {topic} and explain why one is more robust.",
        "stat_arb": "Estimate spread/z-score style metrics for {topic} and define one disciplined entry/exit rule.",
        "volatility_risk": "Compare at least two volatility/risk forecasts for {topic} and discuss one stress weakness.",
        "ai_workflow": "Build a small AI-assisted workflow for {topic} with explicit citation and hallucination checks.",
        "applications": "Create a scoring matrix for {topic} and justify one decision using evidence weights.",
        "interview_drills": "Solve one timed coding/math drill for {topic} and write a concise interview-quality explanation.",
        "communication": "Prepare an evidence-first one-page artifact for {topic} that includes limitations and next steps.",
        "capstone": "Implement one capstone-grade module for {topic} with validation outputs and a limitation note.",
        "foundations": "Implement one notebook cell or small script focused on {topic} with clear interpretation.",
    }

    template = templates.get(domain, templates["foundations"])
    return template.format(topic=topic_lower)


def real_world_lab_lines_for_week(week_number: int, topic: str) -> list[str]:
    domain = domain_for_week(week_number)
    topic_lower = topic.lower()

    if domain in {
        "data",
        "math_stats",
        "ml_foundations",
        "time_series",
        "microstructure",
        "portfolio",
        "fixed_income",
        "derivatives",
        "research_design",
        "backtesting",
        "signals",
        "stat_arb",
        "volatility_risk",
        "capstone",
    }:
        return [
            "Use yfinance first for SPY, QQQ, TLT, and GLD when internet is available.",
            "If available, validate against a Robinhood-style export CSV for consistency checks.",
            "Fall back to curriculum/datasets/real_market_prices.csv for reproducible runs.",
            f"Design one topic-specific analysis for {topic_lower} instead of reusing generic volatility-only metrics.",
            "Document one implementation risk and one robustness check before finalizing conclusions.",
        ]

    if domain == "ai_workflow":
        return [
            "Create a small citation table with source, claim, and verification status.",
            "Measure hallucination risk using unsupported-claim ratio on a short generated memo.",
            "Log at least one guardrail that prevented an incorrect conclusion.",
            f"Tie the workflow back to {topic_lower} with one concrete business/research decision.",
        ]

    if domain == "applications":
        return [
            "Build an application matrix with program, cost, scholarship, curriculum fit, and career fit.",
            "Score options transparently using weighted criteria.",
            "Write one evidence-backed reason for your top choice and one downside risk.",
            f"Link the matrix directly to today's topic: {topic_lower}.",
        ]

    if domain == "interview_drills":
        return [
            "Run one timed drill and record completion time and accuracy.",
            "Write a two-minute spoken answer script with one equation and one risk caveat.",
            "Log one weakness that appeared under time pressure and schedule a targeted retry.",
        ]

    if domain == "communication":
        return [
            "Create a claim-evidence table for your presentation/case write-up.",
            "Add one explicit limitations section with at least three concrete caveats.",
            "Convert analysis outputs into decision-ready bullet points for a stakeholder.",
        ]

    return [
        "Use curriculum/datasets/real_market_prices.csv as reproducible fallback data.",
        "Build one table and one chart supporting a decision.",
        "Document one limitation and one robustness check.",
    ]


def quiz_python_drill_for_week(week_number: int, topic: str) -> dict[str, str]:
    domain = domain_for_week(week_number)

    if domain in {"data", "math_stats", "portfolio"}:
        return {
            "task": "Load market data and compute a correlation/covariance diagnostic tied to today's topic.",
            "solution": _code(
                """
                from pathlib import Path
                import pandas as pd

                market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
                prices = market.pivot(index="date", columns="symbol", values="close").dropna()
                returns = prices.pct_change().dropna()
                print(returns.corr().round(3))
                print("\\nCovariance:")
                print(returns.cov().round(6))
                """
            ),
        }

    if domain == "ml_foundations":
        return {
            "task": "Train a simple classification baseline and report precision/recall/F1.",
            "solution": _code(
                """
                from pathlib import Path
                import pandas as pd
                from sklearn.linear_model import LogisticRegression
                from sklearn.metrics import classification_report
                from sklearn.model_selection import train_test_split

                market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
                prices = market.pivot(index="date", columns="symbol", values="close").dropna()
                returns = prices.pct_change().dropna()
                X = returns.shift(1).dropna()
                y = (returns["SPY"].loc[X.index] > 0).astype(int)
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=False)
                model = LogisticRegression(max_iter=500)
                model.fit(X_train, y_train)
                pred = model.predict(X_test)
                print(classification_report(y_test, pred, digits=3))
                """
            ),
        }

    if domain == "time_series":
        return {
            "task": "Compute lag autocorrelation and rolling mean/volatility diagnostics.",
            "solution": _code(
                """
                from pathlib import Path
                import pandas as pd

                market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
                spy = market[market["symbol"] == "SPY"].sort_values("date").set_index("date")["close"]
                ret = spy.pct_change().dropna()
                diag = pd.DataFrame(
                    {
                        "ret": ret,
                        "lag1": ret.shift(1),
                        "roll_mean_20": ret.rolling(20).mean(),
                        "roll_vol_20": ret.rolling(20).std(),
                    }
                ).dropna()
                print("Lag-1 autocorr:", round(diag["ret"].corr(diag["lag1"]), 4))
                print(diag.tail())
                """
            ),
        }

    if domain == "microstructure":
        return {
            "task": "Estimate turnover and a simple cost proxy from a toy rebalance schedule.",
            "solution": _code(
                """
                import pandas as pd

                weights = pd.DataFrame(
                    {
                        "SPY": [0.40, 0.35, 0.30],
                        "QQQ": [0.30, 0.35, 0.35],
                        "TLT": [0.20, 0.20, 0.25],
                        "GLD": [0.10, 0.10, 0.10],
                    },
                    index=["t0", "t1", "t2"],
                )
                turnover = 0.5 * weights.diff().abs().sum(axis=1).fillna(0.0)
                cost_bps = 8
                est_cost = turnover * (cost_bps / 10000)
                print(pd.DataFrame({"turnover": turnover, "estimated_cost": est_cost}))
                """
            ),
        }

    if domain == "fixed_income":
        return {
            "task": "Price a simple fixed-coupon bond and compute duration approximation.",
            "solution": _code(
                """
                import numpy as np

                face = 100
                coupon = 0.04
                y = 0.035
                n = 5
                cashflows = np.array([face * coupon] * (n - 1) + [face * (1 + coupon)])
                times = np.arange(1, n + 1)
                discount = (1 + y) ** times
                price = (cashflows / discount).sum()
                macaulay = ((times * cashflows / discount).sum()) / price
                mod_duration = macaulay / (1 + y)
                print("Price:", round(float(price), 4))
                print("Modified duration:", round(float(mod_duration), 4))
                """
            ),
        }

    if domain == "derivatives":
        return {
            "task": "Build option payoff vectors and estimate delta numerically at one point.",
            "solution": _code(
                """
                import numpy as np

                k = 100
                s_grid = np.linspace(70, 130, 13)
                call = np.maximum(s_grid - k, 0)
                put = np.maximum(k - s_grid, 0)
                s0 = 101
                eps = 0.5
                call_price = lambda s: max(s - k, 0)
                delta = (call_price(s0 + eps) - call_price(s0 - eps)) / (2 * eps)
                print("Call payoff:", call)
                print("Put payoff:", put)
                print("Delta estimate near S=101:", round(float(delta), 4))
                """
            ),
        }

    if domain in {"research_design", "signals", "stat_arb", "backtesting"}:
        return {
            "task": "Construct a simple signal and evaluate one risk-aware performance diagnostic.",
            "solution": _code(
                """
                from pathlib import Path
                import pandas as pd

                market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
                prices = market.pivot(index="date", columns="symbol", values="close").dropna()
                ret = prices.pct_change().dropna()
                signal = ret["SPY"].rolling(20).mean().shift(1).dropna()
                aligned = ret.loc[signal.index, "SPY"]
                strat = aligned * signal.apply(lambda x: 1 if x > 0 else -1)
                ann_ret = strat.mean() * 252
                ann_vol = strat.std() * (252 ** 0.5)
                print({"ann_return": round(float(ann_ret), 4), "ann_vol": round(float(ann_vol), 4)})
                """
            ),
        }

    if domain == "volatility_risk":
        return {
            "task": "Compare rolling volatility and EWMA volatility estimates.",
            "solution": _code(
                """
                from pathlib import Path
                import pandas as pd

                market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
                spy = market[market["symbol"] == "SPY"].sort_values("date").set_index("date")["close"]
                ret = spy.pct_change().dropna()
                roll = ret.rolling(20).std()
                ewma = ret.pow(2).ewm(alpha=0.06, adjust=False).mean().pow(0.5)
                out = pd.DataFrame({"roll20": roll, "ewma": ewma}).dropna()
                print(out.tail())
                """
            ),
        }

    if domain == "ai_workflow":
        return {
            "task": "Score a small AI-generated memo for citation support and hallucination risk.",
            "solution": _code(
                """
                import pandas as pd

                memo = pd.DataFrame(
                    [
                        {"claim": "Signal improved Sharpe by 20%", "supported": 1},
                        {"claim": "Model generalizes across all regimes", "supported": 0},
                        {"claim": "Turnover fell after constraints", "supported": 1},
                    ]
                )
                hallucination_rate = 1 - memo["supported"].mean()
                print(memo)
                print("Hallucination rate:", round(float(hallucination_rate), 3))
                """
            ),
        }

    if domain == "applications":
        return {
            "task": "Build a program-fit and cost matrix and rank options by weighted score.",
            "solution": _code(
                """
                import pandas as pd

                options = pd.DataFrame(
                    {
                        "program": ["A", "B", "C"],
                        "curriculum_fit": [0.9, 0.8, 0.7],
                        "career_fit": [0.8, 0.9, 0.7],
                        "cost_score": [0.6, 0.4, 0.9],
                    }
                )
                w = {"curriculum_fit": 0.45, "career_fit": 0.35, "cost_score": 0.20}
                options["fit_score"] = (
                    options["curriculum_fit"] * w["curriculum_fit"]
                    + options["career_fit"] * w["career_fit"]
                    + options["cost_score"] * w["cost_score"]
                )
                print(options.sort_values("fit_score", ascending=False))
                """
            ),
        }

    if domain == "interview_drills":
        return {
            "task": "Run a short timed drill set and compute accuracy by topic category.",
            "solution": _code(
                """
                import pandas as pd

                drills = pd.DataFrame(
                    {
                        "topic": ["probability", "stats", "python", "sql", "markets"],
                        "correct": [1, 0, 1, 1, 0],
                        "minutes": [6, 8, 7, 5, 9],
                    }
                )
                print(drills)
                print("Accuracy:", round(float(drills["correct"].mean()), 3))
                print("Mean minutes:", round(float(drills["minutes"].mean()), 2))
                """
            ),
        }

    if domain == "communication":
        return {
            "task": "Convert a project summary into a claim-evidence table and compute evidence coverage.",
            "solution": _code(
                """
                import pandas as pd

                table = pd.DataFrame(
                    [
                        {"claim": "Model improves net return", "evidence": "backtest_table", "supported": 1},
                        {"claim": "Robust in all regimes", "evidence": "none", "supported": 0},
                        {"claim": "Costs are manageable", "evidence": "turnover_cost_chart", "supported": 1},
                    ]
                )
                coverage = table["supported"].mean()
                print(table)
                print("Evidence coverage:", round(float(coverage), 3))
                """
            ),
        }

    if domain == "capstone":
        return {
            "task": "Train a simple out-of-sample baseline and report RMSE with one risk caveat.",
            "solution": _code(
                """
                from pathlib import Path
                import pandas as pd
                from sklearn.linear_model import LinearRegression
                from sklearn.metrics import mean_squared_error

                market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
                prices = market.pivot(index="date", columns="symbol", values="close").dropna()
                ret = prices.pct_change().dropna()
                X = ret.shift(1).dropna()
                y = ret["SPY"].loc[X.index]
                split = int(len(X) * 0.7)
                model = LinearRegression()
                model.fit(X.iloc[:split], y.iloc[:split])
                pred = model.predict(X.iloc[split:])
                rmse = mean_squared_error(y.iloc[split:], pred) ** 0.5
                print("Out-of-sample RMSE:", round(float(rmse), 6))
                """
            ),
        }

    return {
        "task": "Compute log returns and summarize annualized return/risk with one caveat.",
        "solution": _code(
            """
            from pathlib import Path
            import pandas as pd

            market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
            prices = market.pivot(index="date", columns="symbol", values="close").dropna()
            ret = prices.pct_change().dropna()
            ann_ret = ret.mean() * 252
            ann_vol = ret.std() * (252 ** 0.5)
            print(pd.DataFrame({"ann_return": ann_ret, "ann_vol": ann_vol}).round(4))
            """
        ),
    }


def notebook_code_cells_for_week(week_number: int, topic: str) -> list[dict[str, str]]:
    drill = quiz_python_drill_for_week(week_number, topic)
    topic_lower = topic.lower()

    return [
        {
            "markdown": "## Code Lab 1: Topic-specific implementation",
            "code": drill["solution"],
        },
        {
            "markdown": "## Code Lab 2: Assumption register",
            "code": _code(
                f"""
                import pandas as pd

                assumptions = pd.DataFrame(
                    [
                        {{"topic": {topic!r}, "assumption": "Data is representative", "status": "needs verification"}},
                        {{"topic": {topic!r}, "assumption": "No leakage in pipeline", "status": "needs test"}},
                        {{"topic": {topic!r}, "assumption": "Costs are realistic", "status": "needs calibration"}},
                    ]
                )
                print(assumptions)
                """
            ),
        },
        {
            "markdown": "## Code Lab 3: Sensitivity or stress note",
            "code": _code(
                f"""
                import pandas as pd

                stress = pd.DataFrame(
                    [
                        {{"scenario": "base", "impact": "baseline output"}},
                        {{"scenario": "adverse", "impact": "degradation expected"}},
                        {{"scenario": "extreme", "impact": "failure boundary"}},
                    ]
                )
                print("Topic:", {topic_lower!r})
                print(stress)
                """
            ),
        },
        {
            "markdown": "## Code Lab 4: Study-note structure for revision",
            "code": _code(
                f"""
                study_note = {{
                    "topic": {topic!r},
                    "main_formula_or_workflow": "",
                    "what_worked": "",
                    "failure_mode": "",
                    "next_review_date": "",
                }}
                print(study_note)
                """
            ),
        },
    ]
