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


def _entry(name: str, equation: str, meaning: str, use_case: str, pitfall: str) -> dict[str, str]:
    return {
        "name": name,
        "equation": equation,
        "meaning": meaning,
        "use_case": use_case,
        "pitfall": pitfall,
    }


def _topic_formula_entries(topic: str) -> list[dict[str, str]] | None:
    t = topic.lower()

    if "returns" in t or "compounding" in t:
        return [
            _entry(
                "Simple Return",
                "r_t=\\frac{P_t}{P_{t-1}}-1",
                "One-period relative price change.",
                "Baseline daily performance attribution.",
                "Comparing assets without handling frequency or missing days.",
            ),
            _entry(
                "Log Return",
                "\\ell_t=\\ln\\left(\\frac{P_t}{P_{t-1}}\\right)",
                "Additive return representation across time.",
                "Multi-period return decomposition.",
                "Mixing log and simple returns in one report.",
            ),
            _entry(
                "Compounded Wealth",
                "W_T=W_0\\prod_{t=1}^{T}(1+r_t)",
                "Capital path under sequential returns.",
                "Backtest equity-curve reconstruction.",
                "Averaging returns instead of compounding them.",
            ),
        ]

    if "expected value" in t or "probability" in t:
        return [
            _entry(
                "Expected Value",
                "\\mathbb{E}[X]=\\sum_i p_i x_i",
                "Probability-weighted average payoff.",
                "Filter positive-edge trading setups.",
                "Ignoring payoff asymmetry and tails.",
            ),
            _entry(
                "Variance",
                "\\mathrm{Var}(X)=\\mathbb{E}[(X-\\mu)^2]",
                "Spread around expected payoff.",
                "Risk-adjusted strategy comparison.",
                "Using only mean without uncertainty.",
            ),
            _entry(
                "Kelly Fraction (Binary)",
                "f^*=\\frac{bp-q}{b}",
                "Theoretical growth-optimal bet size.",
                "Position-sizing intuition.",
                "Applying full Kelly under estimation error.",
            ),
        ]

    if "vectors" in t or "matrices" in t or "linear algebra" in t:
        return [
            _entry(
                "Portfolio Return",
                "r_p=w^Tr",
                "Weight-return dot product.",
                "Fast multi-asset return aggregation.",
                "Misaligned weight and return ordering.",
            ),
            _entry(
                "Portfolio Variance",
                "\\sigma_p^2=w^T\\Sigma w",
                "Total covariance-weighted risk.",
                "Diversification and sizing decisions.",
                "Using unstable covariance without checks.",
            ),
            _entry(
                "Covariance Matrix",
                "\\Sigma=\\mathbb{E}[(r-\\mu)(r-\\mu)^T]",
                "Cross-asset co-movement structure.",
                "Risk model construction.",
                "Treating covariance as static across regimes.",
            ),
        ]

    if "descriptive statistics" in t or "sampling" in t or "visualizing" in t:
        return [
            _entry(
                "Sample Mean",
                "\\bar x=\\frac{1}{n}\\sum_{i=1}^n x_i",
                "Average observed value.",
                "Return-level baseline estimate.",
                "Assuming mean is robust to outliers.",
            ),
            _entry(
                "Sample Standard Deviation",
                "s=\\sqrt{\\frac{1}{n-1}\\sum_{i=1}^n(x_i-\\bar x)^2}",
                "Observed variability estimate.",
                "Volatility proxy from sample returns.",
                "Comparing volatility across mismatched windows.",
            ),
            _entry(
                "z-Score",
                "z=\\frac{x-\\mu}{\\sigma}",
                "Distance from mean in sigma units.",
                "Outlier and regime diagnostics.",
                "Using unstable rolling moments.",
            ),
        ]

    if "market structure" in t and "asset classes" in t:
        return [
            _entry(
                "Bid-Ask Spread",
                "\\mathrm{Spread}=Ask-Bid",
                "Execution friction at top of book.",
                "Liquidity-aware strategy design.",
                "Ignoring spread impact in high-turnover rules.",
            ),
            _entry(
                "Turnover",
                "\\mathrm{TO}_t=\\frac{1}{2}\\sum_i|w_{i,t}-w_{i,t-1}|",
                "Portfolio trading intensity.",
                "Capacity and cost budgeting.",
                "Reporting gross alpha without turnover context.",
            ),
            _entry(
                "Sharpe Ratio",
                "S=\\frac{R_{ann}-R_f}{\\sigma_{ann}}",
                "Excess return per volatility unit.",
                "Risk-adjusted cross-asset comparison.",
                "Comparing Sharpe without drawdown context.",
            ),
        ]

    if "numpy" in t or "vectorization" in t:
        return [
            _entry(
                "Vectorized Return",
                "r=\\frac{P_{1:}}{P_{:-1}}-1",
                "Batch return transform over arrays.",
                "Replace loop-heavy feature extraction.",
                "Off-by-one index mismatches.",
            ),
            _entry(
                "Dot Product",
                "w\\cdot r=\\sum_i w_i r_i",
                "Linear weighted aggregation.",
                "Portfolio and factor combination.",
                "Shape mismatch between vectors.",
            ),
            _entry(
                "Broadcasting Rule",
                "(m\\times n)\\odot(n,)\\rightarrow(m\\times n)",
                "Dimension-safe elementwise scaling.",
                "Scale features by column constants.",
                "Silent broadcast along wrong axis.",
            ),
        ]

    if "pandas" in t or "dataframes" in t or "joins" in t:
        return [
            _entry(
                "Missingness Rate",
                "MR=\\frac{\\#\\text{missing cells}}{\\#\\text{total cells}}",
                "Fraction of absent observations.",
                "Data quality monitoring before modeling.",
                "Forward-filling without documenting bias.",
            ),
            _entry(
                "Join Cardinality",
                "Rows_{out}=Rows_A\\bowtie Rows_B",
                "Row-growth behavior after merge.",
                "Prevent duplicate explosion in joins.",
                "Assuming one-to-one keys without checks.",
            ),
            _entry(
                "Coverage by Symbol",
                "Coverage_i=\\frac{\\#dates_i}{\\#dates_{max}}",
                "Relative data history length per asset.",
                "Universe eligibility filtering.",
                "Comparing assets with unequal history.",
            ),
        ]

    if "plotting" in t or "exploratory data analysis" in t:
        return [
            _entry(
                "Rolling Mean",
                "\\mu_t^{(k)}=\\frac{1}{k}\\sum_{j=0}^{k-1}x_{t-j}",
                "Local average trend estimate.",
                "Trend regime visualization.",
                "Interpreting noisy short windows as trends.",
            ),
            _entry(
                "Rolling Volatility",
                "\\sigma_t^{(k)}=\\mathrm{Std}(x_{t-k+1:t})",
                "Local risk estimate over a window.",
                "Volatility clustering diagnostics.",
                "Comparing windows with different lengths.",
            ),
            _entry(
                "Drawdown",
                "DD_t=\\frac{W_t}{\\max_{s\\le t}W_s}-1",
                "Current loss from running peak.",
                "Risk narrative beyond volatility.",
                "Reporting return without drawdown path.",
            ),
        ]

    if "correlation" in t or "covariance" in t or "diversification" in t:
        return [
            _entry(
                "Covariance",
                "\\mathrm{Cov}(X,Y)=\\frac{1}{n-1}\\sum_i(x_i-\\bar x)(y_i-\\bar y)",
                "Joint variation around means.",
                "Diversification diagnostics.",
                "Miscaligned timestamps inflate noise.",
            ),
            _entry(
                "Correlation",
                "\\rho_{XY}=\\frac{\\mathrm{Cov}(X,Y)}{\\sigma_X\\sigma_Y}",
                "Scale-free co-movement in [-1,1].",
                "Asset clustering and hedging checks.",
                "Confusing correlation with causation.",
            ),
            _entry(
                "2-Asset Variance",
                "\\sigma_p^2=w_1^2\\sigma_1^2+w_2^2\\sigma_2^2+2w_1w_2\\rho_{12}\\sigma_1\\sigma_2",
                "Risk decomposition for two-asset mix.",
                "Show diversification impact directly.",
                "Ignoring correlation regime shifts.",
            ),
        ]

    if "rebalancing" in t or "portfolio weights" in t:
        return [
            _entry(
                "Portfolio Return",
                "r_{p,t}=\\sum_i w_{i,t-1}r_{i,t}",
                "Weighted one-step return.",
                "Portfolio backtest baseline.",
                "Using contemporaneous (leaky) weights.",
            ),
            _entry(
                "Turnover",
                "\\mathrm{TO}_t=\\frac{1}{2}\\sum_i|w_{i,t}-w_{i,t-1}|",
                "Rebalance trading requirement.",
                "Estimate execution cost pressure.",
                "Ignoring transaction costs in alpha claims.",
            ),
            _entry(
                "Cumulative Wealth",
                "W_t=W_0\\prod_{j=1}^{t}(1+r_{p,j})",
                "Compounded capital path.",
                "Compare portfolio design trajectories.",
                "Averaging returns instead of compounding.",
            ),
        ]

    if "calculus" in t or "derivatives and sensitivity" in t:
        return [
            _entry(
                "First Derivative",
                "f'(x)=\\lim_{h\\to0}\\frac{f(x+h)-f(x)}{h}",
                "Instantaneous slope/sensitivity.",
                "Rate sensitivity intuition for pricing.",
                "Treating finite difference as exact.",
            ),
            _entry(
                "Second Derivative",
                "f''(x)=\\frac{d^2 f}{dx^2}",
                "Curvature and local convexity.",
                "Risk asymmetry discussions.",
                "Ignoring nonlinearity in stressed moves.",
            ),
            _entry(
                "Elasticity",
                "\\epsilon=\\frac{d y}{d x}\\cdot\\frac{x}{y}",
                "Percent sensitivity ratio.",
                "Compare sensitivities across scales.",
                "Using at points where y\\approx0.",
            ),
        ]

    if "integrals" in t or "accumulation" in t:
        return [
            _entry(
                "Definite Integral",
                "\\int_a^b f(x)dx",
                "Accumulated quantity over interval.",
                "Cumulative signal/flow interpretation.",
                "Forgetting integration bounds context.",
            ),
            _entry(
                "Fundamental Theorem",
                "\\frac{d}{dx}\\int_a^x f(t)dt=f(x)",
                "Derivative-integral inverse link.",
                "Map instantaneous vs accumulated effects.",
                "Mixing variable symbols and limits.",
            ),
            _entry(
                "Cumulative Log Return",
                "\\sum_t \\ell_t = \\ln\\left(\\frac{P_T}{P_0}\\right)",
                "Log-return additivity across time.",
                "Long-horizon growth decomposition.",
                "Mixing with simple-return aggregation.",
            ),
        ]

    if "bayes" in t or "conditional probability" in t:
        return [
            _entry(
                "Conditional Probability",
                "P(A|B)=\\frac{P(A\\cap B)}{P(B)}",
                "Probability of A given B occurred.",
                "Signal conditioning from evidence.",
                "Ignoring denominator event rarity.",
            ),
            _entry(
                "Bayes Rule",
                "P(A|B)=\\frac{P(B|A)P(A)}{P(B)}",
                "Prior-to-posterior belief update.",
                "Revise conviction after new data.",
                "Base-rate neglect.",
            ),
            _entry(
                "Likelihood Ratio",
                "LR=\\frac{P(B|A)}{P(B|\\neg A)}",
                "Relative evidence strength.",
                "Compare competing hypotheses.",
                "Treating LR as probability.",
            ),
        ]

    if "confidence intervals" in t or "hypothesis testing" in t:
        return [
            _entry(
                "Confidence Interval (Mean)",
                "\\bar x \\pm t_{n-1,\\alpha/2}\\cdot\\frac{s}{\\sqrt{n}}",
                "Range of plausible mean values.",
                "Uncertainty-aware return estimates.",
                "Treating interval as probability for fixed parameter.",
            ),
            _entry(
                "t-Statistic",
                "t=\\frac{\\bar x-\\mu_0}{s/\\sqrt{n}}",
                "Signal-to-noise vs null mean.",
                "Edge significance checks.",
                "Ignoring dependence/autocorrelation.",
            ),
            _entry(
                "p-Value",
                "p=P(T\\ge |t_{obs}|\\mid H_0)",
                "Extremeness under null model.",
                "Reject/retain null decision support.",
                "Confusing p with effect size.",
            ),
        ]

    if "ols" in t or "linear regression" in t:
        return [
            _entry(
                "OLS Coefficients",
                "\\hat\\beta=(X^TX)^{-1}X^Ty",
                "Least-squares linear parameter estimate.",
                "Baseline factor/feature sensitivity model.",
                "Unstable estimates under multicollinearity.",
            ),
            _entry(
                "Residual",
                "e_i=y_i-\\hat y_i",
                "Unexplained model component.",
                "Model misspecification diagnostics.",
                "Ignoring residual autocorrelation.",
            ),
            _entry(
                "R-Squared",
                "R^2=1-\\frac{\\sum e_i^2}{\\sum (y_i-\\bar y)^2}",
                "Variance explained fraction.",
                "Quick baseline fit summary.",
                "Using R^2 alone for forecast model quality.",
            ),
        ]

    if "optimization" in t or "constrained" in t:
        return [
            _entry(
                "Constrained Objective",
                "\\min_w f(w)\\ \text{s.t.}\\ Aw=b,\\ w\\ge0",
                "Target with feasibility constraints.",
                "Portfolio optimization setup.",
                "Ignoring feasibility checks before solving.",
            ),
            _entry(
                "Lagrangian",
                "\\mathcal{L}(w,\\lambda)=f(w)+\\lambda^T(Aw-b)",
                "Constraint-aware objective transform.",
                "Solve equality-constrained problems.",
                "Not verifying KKT conditions post-solve.",
            ),
            _entry(
                "KKT Stationarity",
                "\\nabla_w\\mathcal{L}=0",
                "Necessary optimality condition.",
                "Audit optimization solution quality.",
                "Stopping at numerical output without diagnostics.",
            ),
        ]

    if "decision trees" in t or "rule-based splits" in t:
        return [
            _entry(
                "Gini Impurity",
                "G=1-\\sum_k p_k^2",
                "Class-mix impurity at node.",
                "Split quality scoring.",
                "Overfitting deep trees without pruning.",
            ),
            _entry(
                "Information Gain",
                "IG=H(parent)-\\sum_j\\frac{n_j}{n}H(child_j)",
                "Entropy reduction from split.",
                "Feature split selection.",
                "Bias toward high-cardinality features.",
            ),
            _entry(
                "Tree Depth",
                "Depth=\\max(path\\ length)",
                "Model complexity measure.",
                "Control variance and interpretability.",
                "Letting depth grow without validation.",
            ),
        ]

    if "random forests" in t or "bagging" in t:
        return [
            _entry(
                "Bagging Predictor",
                "\\hat y=\\frac{1}{B}\\sum_{b=1}^{B}\\hat y^{(b)}",
                "Average over bootstrapped learners.",
                "Variance reduction.",
                "Assuming bias also vanishes automatically.",
            ),
            _entry(
                "Out-of-Bag Error",
                "OOB=\\frac{1}{n}\\sum_i\\mathbb{1}(\\hat y^{OOB}_i\\ne y_i)",
                "Internal validation estimate.",
                "Quick generalization monitoring.",
                "Replacing proper temporal validation with OOB.",
            ),
            _entry(
                "Feature Importance (MDI)",
                "FI_j=\\sum_{splits\\ on\\ j}\\Delta impurity",
                "Aggregate split-gain attribution.",
                "Model interpretability screening.",
                "Treating importance as causal effect.",
            ),
        ]

    if "gradient boosting" in t:
        return [
            _entry(
                "Additive Model",
                "F_m(x)=F_{m-1}(x)+\\eta h_m(x)",
                "Sequential residual correction.",
                "Capture nonlinear structure gradually.",
                "Using too high learning rate.",
            ),
            _entry(
                "Pseudo-Residual",
                "r_{im}=-\\left[\\frac{\\partial L(y_i,F(x_i))}{\\partial F(x_i)}\\right]_{F=F_{m-1}}",
                "Gradient signal for next learner.",
                "Optimize generic differentiable losses.",
                "Ignoring loss-function mismatch to objective.",
            ),
            _entry(
                "Shrinkage",
                "\\eta\\in(0,1)",
                "Step-size regularization in boosting.",
                "Stability vs training speed control.",
                "Compensating tiny eta with too few trees.",
            ),
        ]

    if "pca" in t or "variance decomposition" in t:
        return [
            _entry(
                "Covariance Matrix",
                "\\Sigma=\\frac{1}{n-1}X^TX",
                "Feature co-movement matrix.",
                "Basis for PCA decomposition.",
                "Failing to center features first.",
            ),
            _entry(
                "Eigen Decomposition",
                "\\Sigma v_j=\\lambda_j v_j",
                "Principal direction/variance pair.",
                "Identify dominant latent factors.",
                "Interpreting sign of eigenvectors as absolute truth.",
            ),
            _entry(
                "Explained Variance Ratio",
                "EVR_j=\\frac{\\lambda_j}{\\sum_k\\lambda_k}",
                "Share of variance per component.",
                "Dimension reduction selection.",
                "Keeping components without out-of-sample validation.",
            ),
        ]

    if "clustering" in t:
        return [
            _entry(
                "K-Means Objective",
                "\\min_{C}\\sum_{k}\\sum_{x_i\\in C_k}||x_i-\\mu_k||^2",
                "Within-cluster dispersion minimization.",
                "Group assets by behavior.",
                "Ignoring scale normalization before clustering.",
            ),
            _entry(
                "Silhouette Score",
                "s_i=\\frac{b_i-a_i}{\\max(a_i,b_i)}",
                "Cluster separation/compactness measure.",
                "Choose cluster count.",
                "Using one metric as definitive truth.",
            ),
            _entry(
                "Distance Metric",
                "d(x,y)=\\sqrt{\\sum_j(x_j-y_j)^2}",
                "Similarity proxy in feature space.",
                "Asset regime grouping.",
                "Choosing metric inconsistent with data geometry.",
            ),
        ]

    if "stationarity" in t or "differencing" in t:
        return [
            _entry(
                "First Difference",
                "\\Delta x_t=x_t-x_{t-1}",
                "Removes level trends.",
                "Stabilize mean for modeling.",
                "Over-differencing useful signal away.",
            ),
            _entry(
                "AR(1)",
                "x_t=c+\\phi x_{t-1}+\\epsilon_t",
                "Lag dependence baseline.",
                "Mean-reversion diagnostics.",
                "Assuming stationarity without tests.",
            ),
            _entry(
                "ADF Regression",
                "\\Delta x_t=\\alpha+\\beta x_{t-1}+\\sum_i\\gamma_i\\Delta x_{t-i}+\\epsilon_t",
                "Unit-root test setup.",
                "Stationarity hypothesis check.",
                "Ignoring low power on short samples.",
            ),
        ]

    if "arima" in t or "ar ma" in t:
        return [
            _entry(
                "ARIMA Model",
                "\\Phi(B)(1-B)^d x_t=\\Theta(B)\\epsilon_t",
                "Unified AR/MA with differencing.",
                "Baseline univariate forecasting.",
                "Choosing orders without diagnostics.",
            ),
            _entry(
                "AIC",
                "AIC=2k-2\\ln(\\hat L)",
                "Complexity-adjusted fit criterion.",
                "Model order comparison.",
                "Treating AIC winner as deploy-ready.",
            ),
            _entry(
                "Forecast Error",
                "e_t=x_t-\\hat x_t",
                "Realized minus predicted value.",
                "Residual diagnostics and calibration.",
                "Ignoring autocorrelation in residuals.",
            ),
        ]

    if "autocorrelation" in t or "lag structure" in t:
        return [
            _entry(
                "Autocorrelation",
                "\\rho_k=\\frac{\\mathrm{Cov}(x_t,x_{t-k})}{\\mathrm{Var}(x_t)}",
                "Lag-k dependence strength.",
                "Feature lag selection.",
                "Confusing seasonal and trend effects.",
            ),
            _entry(
                "Partial Autocorrelation",
                "PACF(k)=Corr(x_t,x_{t-k}\\mid x_{t-1..t-k+1})",
                "Direct lag effect net of intermediates.",
                "AR order identification.",
                "Overfitting order from noisy PACF spikes.",
            ),
            _entry(
                "Ljung-Box",
                "Q=n(n+2)\\sum_{k=1}^{h}\\frac{\\hat\\rho_k^2}{n-k}",
                "Residual whiteness diagnostic.",
                "Model adequacy testing.",
                "Ignoring multiple-horizon checks.",
            ),
        ]

    if "walk-forward" in t or "forecast error" in t:
        return [
            _entry(
                "Walk-Forward Split",
                "Train_{1:t}\\rightarrow Test_{t+1:t+h}",
                "Time-respecting evaluation.",
                "Avoid look-ahead leakage.",
                "Using random shuffle on time series.",
            ),
            _entry(
                "RMSE",
                "RMSE=\\sqrt{\\frac{1}{n}\\sum_i(\\hat y_i-y_i)^2}",
                "Quadratic forecast error magnitude.",
                "Compare forecast pipelines.",
                "Comparing RMSE on different scales.",
            ),
            _entry(
                "MAPE",
                "MAPE=\\frac{100}{n}\\sum_i\\left|\\frac{y_i-\\hat y_i}{y_i}\\right|",
                "Relative forecast error percentage.",
                "Interpretability for stakeholders.",
                "Undefined behavior near zero targets.",
            ),
        ]

    if "decision trees" not in t and (
        "classification" in t or "confusion matrix" in t or "class imbalance" in t or "credit risk" in t
    ):
        return [
            _entry(
                "Logistic Link",
                "p(y=1|x)=\\frac{1}{1+e^{-z}}",
                "Probability mapping from linear score.",
                "Binary event prediction.",
                "Thresholding without business-cost calibration.",
            ),
            _entry(
                "Precision",
                "Precision=\\frac{TP}{TP+FP}",
                "Correctness among predicted positives.",
                "False-alarm control.",
                "Optimizing precision alone under imbalance.",
            ),
            _entry(
                "Recall",
                "Recall=\\frac{TP}{TP+FN}",
                "Coverage of true positives.",
                "Miss-risk control.",
                "Ignoring precision-recall tradeoff.",
            ),
        ]

    if "cross-validation" in t or "resampling" in t:
        return [
            _entry(
                "CV Mean Score",
                "\\bar s=\\frac{1}{K}\\sum_{k=1}^{K}s_k",
                "Average fold performance.",
                "Model ranking under resampling.",
                "Ignoring fold variance.",
            ),
            _entry(
                "CV Std",
                "s_{cv}=\\sqrt{\\frac{1}{K-1}\\sum_k(s_k-\\bar s)^2}",
                "Stability of validation scores.",
                "Robust model selection.",
                "Choosing unstable high-mean models.",
            ),
            _entry(
                "Time Split Constraint",
                "\\max(Train_t) < \\min(Test_t)",
                "Temporal causality condition.",
                "Leakage prevention.",
                "Accidentally including future labels in train.",
            ),
        ]

    if "credit spreads" in t or "default risk" in t:
        return [
            _entry(
                "Credit Spread",
                "s_{credit}=y_{corp}-y_{gov}",
                "Compensation over risk-free yield.",
                "Credit-risk pricing comparison.",
                "Ignoring liquidity premium component.",
            ),
            _entry(
                "Expected Loss",
                "EL=PD\\times LGD\\times EAD",
                "Average credit loss estimate.",
                "Risk budgeting and scenario design.",
                "Static PD/LGD assumptions across regimes.",
            ),
            _entry(
                "Hazard Approximation",
                "h\\approx\\frac{s_{credit}}{1-R}",
                "Spread-to-default intensity proxy.",
                "Quick sanity checks on spread levels.",
                "Using approximation outside assumptions.",
            ),
        ]

    if "yield curve" in t or "term structure" in t:
        return [
            _entry(
                "Discount Factor",
                "DF(T)=\\frac{1}{(1+s_T)^T}",
                "Present-value weight at maturity T.",
                "Curve construction and pricing.",
                "Mixing compounding conventions.",
            ),
            _entry(
                "Forward Rate",
                "f_{t,t+1}=\\frac{(1+s_{t+1})^{t+1}}{(1+s_t)^t}-1",
                "Implied future short rate.",
                "Term-structure expectations analysis.",
                "Interpreting forwards as unbiased forecasts.",
            ),
            _entry(
                "Term Spread",
                "TS=s_{10Y}-s_{2Y}",
                "Slope between long and short yields.",
                "Macro regime signal monitoring.",
                "Using one spread as complete macro model.",
            ),
        ]

    if "duration" in t and "interest rate" in t:
        return [
            _entry(
                "Macaulay Duration",
                "D_{mac}=\\frac{1}{P}\\sum_t t\\cdot\\frac{CF_t}{(1+y)^t}",
                "Cash-flow weighted timing measure.",
                "Interest-rate sensitivity baseline.",
                "Using duration for large non-linear shocks.",
            ),
            _entry(
                "Modified Duration",
                "D_{mod}=\\frac{D_{mac}}{1+y}",
                "Approximate %-price change per yield unit.",
                "DV01 and hedge sizing.",
                "Ignoring convexity correction.",
            ),
            _entry(
                "DV01",
                "DV01=D_{mod}\\cdot P\\cdot 10^{-4}",
                "Dollar value change for 1bp move.",
                "Rate-risk limit reporting.",
                "Comparing DV01 without position scale context.",
            ),
        ]

    if "convexity" in t:
        return [
            _entry(
                "Convexity",
                "C=\\frac{1}{P}\\sum_t\\frac{CF_t\\,t(t+1)}{(1+y)^{t+2}}",
                "Second-order yield sensitivity.",
                "Improve bond shock approximations.",
                "Ignoring convexity in volatile rate regimes.",
            ),
            _entry(
                "Price Change Approx",
                "\\frac{\\Delta P}{P}\\approx -D_{mod}\\Delta y + \\frac{1}{2}C(\\Delta y)^2",
                "Duration-convexity Taylor approximation.",
                "Scenario stress calculations.",
                "Applying for very large non-local shifts.",
            ),
            _entry(
                "Curve Shock PnL",
                "PnL\\approx -DV01\\cdot\\Delta bp + \\frac{1}{2}C\\cdot(\\Delta y)^2P",
                "PnL estimate under rate shocks.",
                "Risk reporting and hedge checks.",
                "Not separating parallel vs non-parallel moves.",
            ),
        ]

    if "forwards" in t or "futures" in t:
        return [
            _entry(
                "Forward Price",
                "F_0=S_0e^{(r-q)T}",
                "No-arbitrage carry pricing.",
                "Cash-and-carry checks.",
                "Ignoring funding/storage/dividend assumptions.",
            ),
            _entry(
                "Futures PnL",
                "PnL=\\Delta F\\cdot Contract\\ Size",
                "Linear exposure payoff change.",
                "Scenario and margin planning.",
                "Overlooking mark-to-market mechanics.",
            ),
            _entry(
                "Basis",
                "Basis=S-F",
                "Spot-futures relationship gap.",
                "Convergence and hedge diagnostics.",
                "Assuming basis is always negligible.",
            ),
        ]

    if "calls" in t or "puts" in t or "payoff diagrams" in t:
        return [
            _entry(
                "Call Payoff",
                "\\max(S_T-K,0)",
                "Upside-only terminal payoff.",
                "Directional convex exposures.",
                "Confusing payoff with net profit.",
            ),
            _entry(
                "Put Payoff",
                "\\max(K-S_T,0)",
                "Downside-protection terminal payoff.",
                "Tail-risk hedge intuition.",
                "Ignoring premium/time decay.",
            ),
            _entry(
                "Put-Call Parity",
                "C-P=S_0-Ke^{-rT}",
                "No-arbitrage relation across vanilla options.",
                "Consistency checks in pricing surfaces.",
                "Applying parity with mismatched maturities.",
            ),
        ]

    if "greeks" in t:
        return [
            _entry(
                "Delta",
                "\\Delta=\\frac{\\partial V}{\\partial S}",
                "Price sensitivity to underlying.",
                "Hedge-ratio baseline.",
                "Treating delta as constant.",
            ),
            _entry(
                "Gamma",
                "\\Gamma=\\frac{\\partial^2 V}{\\partial S^2}",
                "Delta curvature sensitivity.",
                "Re-hedging frequency intuition.",
                "Ignoring gamma in large spot moves.",
            ),
            _entry(
                "Vega",
                "Vega=\\frac{\\partial V}{\\partial \\sigma}",
                "Sensitivity to implied volatility.",
                "Volatility-risk exposure sizing.",
                "Ignoring vol-regime shifts.",
            ),
        ]

    if "volatility smile" in t or "pricing inputs" in t:
        return [
            _entry(
                "Implied Volatility",
                "\\sigma_{imp}: C_{BS}(S,K,T,r,\\sigma_{imp})=C_{mkt}",
                "Vol level that matches market option price.",
                "Surface construction.",
                "Treating implied vol as direct forecast.",
            ),
            _entry(
                "Moneyness",
                "m=\\frac{S_0}{K}",
                "Relative strike positioning.",
                "Smile/skew diagnostics.",
                "Comparing strikes without maturity context.",
            ),
            _entry(
                "Black-Scholes d1",
                "d_1=\\frac{\\ln(S_0/K)+(r+\\sigma^2/2)T}{\\sigma\\sqrt{T}}",
                "Core standardized input in BS model.",
                "Greeks and option valuation.",
                "Using wrong annualization units.",
            ),
        ]

    if "var" in t or "stress" in t or "scenarios" in t:
        return [
            _entry(
                "Parametric VaR",
                "VaR_{\\alpha}=\\mu+z_{\\alpha}\\sigma",
                "Loss quantile under distribution assumptions.",
                "Daily risk-limit reporting.",
                "Assuming normal tails in crisis regimes.",
            ),
            _entry(
                "Expected Shortfall",
                "ES_{\\alpha}=\\mathbb{E}[L\\mid L>VaR_{\\alpha}]",
                "Average loss beyond VaR threshold.",
                "Tail-risk governance.",
                "Relying on short history for ES.",
            ),
            _entry(
                "Stress Loss",
                "L_{stress}=w^T r_{scenario}",
                "Portfolio loss under explicit scenario vector.",
                "Scenario-based resilience checks.",
                "Using stress vectors not tied to plausible regimes.",
            ),
        ]

    if "hypothesis" in t or "signal design" in t or "label design" in t:
        return [
            _entry(
                "Information Coefficient",
                "IC=Corr(signal_t,r_{t+1})",
                "Signal-next-return association.",
                "Early hypothesis validation.",
                "Ignoring IC stability over time.",
            ),
            _entry(
                "Hit Rate",
                "HR=\\frac{\\#(sign(\\hat r)=sign(r))}{N}",
                "Directional correctness ratio.",
                "Quick directional predictive quality check.",
                "High hit-rate with poor payoff asymmetry.",
            ),
            _entry(
                "Label Horizon",
                "y_t=sign(P_{t+h}-P_t)",
                "Future target definition at horizon h.",
                "Align prediction objective with holding period.",
                "Choosing h without turnover/cost implications.",
            ),
        ]

    if "data-cleaning" in t or "survivorship" in t or "look-ahead" in t:
        return [
            _entry(
                "Leakage Flag",
                "Leakage=\\mathbb{1}(t_{feature}>t_{label})",
                "Temporal-causality violation indicator.",
                "Pipeline data audit.",
                "Using post-event data in training.",
            ),
            _entry(
                "Coverage Ratio",
                "Coverage=\\frac{N_{usable}}{N_{raw}}",
                "Share of valid observations after cleaning.",
                "Track data attrition risk.",
                "Dropping rows without bias review.",
            ),
            _entry(
                "Survivorship Gap",
                "SG=\\bar r_{survivors}-\\bar r_{full\\ universe}",
                "Return distortion from missing dead assets.",
                "Universe construction sanity checks.",
                "Backtests on survivor-only symbols.",
            ),
        ]

    if "backtesting" in t or "look-ahead" in t or "slippage" in t or "performance attribution" in t:
        return [
            _entry(
                "Net Strategy Return",
                "r_t^{net}=w_{t-1}^Tr_t-c_t",
                "Post-cost strategy return.",
                "Realistic backtest reporting.",
                "Publishing gross-only performance.",
            ),
            _entry(
                "Turnover",
                "TO_t=\\frac{1}{2}\\sum_i|w_{i,t}-w_{i,t-1}|",
                "Trade intensity proxy.",
                "Cost and capacity constraints.",
                "Ignoring turnover in deployment sizing.",
            ),
            _entry(
                "Max Drawdown",
                "MDD=\\min_t\\left(\\frac{W_t}{\\max_{s\\le t}W_s}-1\\right)",
                "Worst peak-to-trough decline.",
                "Risk narrative and kill-switch design.",
                "Relying on Sharpe without path risk.",
            ),
        ]

    if "momentum" in t or "mean reversion" in t or "cross-sectional ranking" in t or "signal combination" in t:
        return [
            _entry(
                "Momentum Signal",
                "m_t=\\frac{P_t}{P_{t-k}}-1",
                "Trend strength over lookback.",
                "Cross-sectional ranking inputs.",
                "Ignoring regime-dependent crash risk.",
            ),
            _entry(
                "Reversion z-Score",
                "z_t=\\frac{x_t-\\mu_t}{\\sigma_t}",
                "Deviation from local equilibrium.",
                "Entry/exit threshold rules.",
                "Using unstable rolling moments.",
            ),
            _entry(
                "Signal Blend",
                "s_t=\\sum_j\\omega_j s_{j,t}",
                "Weighted multi-signal aggregate.",
                "Diversify alpha sources.",
                "Blending without normalization.",
            ),
        ]

    if "cointegration" in t or "spread" in t or "residual" in t or "factor models" in t:
        return [
            _entry(
                "Spread",
                "s_t=y_t-\\beta x_t",
                "Hedged relative-value residual.",
                "Pairs and residual strategy setup.",
                "Using stale hedge ratio.",
            ),
            _entry(
                "Half-Life",
                "HL=-\\frac{\\ln 2}{\\ln \\phi}",
                "Mean-reversion speed estimate.",
                "Holding-period sanity checks.",
                "Estimating phi on nonstationary series.",
            ),
            _entry(
                "Factor Model",
                "r_t=\\alpha+\\beta^Tf_t+\\epsilon_t",
                "Return decomposition into factor exposures.",
                "Risk decomposition and attribution.",
                "Assuming static betas across regimes.",
            ),
        ]

    if "volatility" in t or "garch" in t or "stress testing" in t:
        return [
            _entry(
                "Realized Volatility",
                "\\sigma_{ann}=\\sqrt{252}\\cdot Std(r_t)",
                "Sample annualized risk estimate.",
                "Position sizing.",
                "Assuming homoskedasticity.",
            ),
            _entry(
                "EWMA Volatility",
                "\\sigma_t^2=\\lambda\\sigma_{t-1}^2+(1-\\lambda)r_{t-1}^2",
                "Recency-weighted risk forecast.",
                "Adaptive risk control.",
                "Unvalidated lambda choice.",
            ),
            _entry(
                "GARCH(1,1)",
                "\\sigma_t^2=\\omega+\\alpha r_{t-1}^2+\\beta\\sigma_{t-1}^2",
                "Shock and persistence volatility model.",
                "Scenario-aware risk forecasting.",
                "Ignoring structural breaks.",
            ),
        ]

    if "agentic ai" in t or "hallucination" in t or "literature summarization" in t or "code review assistants" in t:
        return [
            _entry(
                "Precision",
                "Precision=\\frac{TP}{TP+FP}",
                "Correctness of generated claims.",
                "Quality control for AI outputs.",
                "High precision with tiny coverage.",
            ),
            _entry(
                "Recall",
                "Recall=\\frac{TP}{TP+FN}",
                "Coverage of relevant claims.",
                "Avoid missed critical evidence.",
                "High recall with high hallucination.",
            ),
            _entry(
                "Hallucination Rate",
                "HR=\\frac{\\#unsupported\\ claims}{\\#total\\ claims}",
                "Unsupported-statement share.",
                "Governance of AI-assisted research.",
                "No citation-verification pipeline.",
            ),
        ]

    if "alternative data" in t or "nlp" in t or "experiment tracking" in t or "report generation" in t:
        return [
            _entry(
                "Coverage",
                "Coverage=\\frac{N_{usable}}{N_{total}}",
                "Usable fraction of alternative-data records.",
                "Data source triage.",
                "Using sparse data without coverage diagnostics.",
            ),
            _entry(
                "F1 Score",
                "F1=2\\cdot\\frac{Precision\\cdot Recall}{Precision+Recall}",
                "Balanced NLP classification metric.",
                "Sentiment model evaluation.",
                "Optimizing one metric without calibration checks.",
            ),
            _entry(
                "Run Reproducibility Rate",
                "RRR=\\frac{\\#reproducible\\ runs}{\\#total\\ runs}",
                "Experiment repeatability health metric.",
                "ML ops governance in research.",
                "No fixed seeds/data-version tagging.",
            ),
        ]

    if "program tiers" in t or "scholarship" in t or "sop" in t or "recommendation" in t or "cv" in t:
        return [
            _entry(
                "Program Fit Score",
                "Fit=w_1\\cdot curriculum+w_2\\cdot career+w_3\\cdot cost",
                "Weighted application prioritization score.",
                "Rank schools by evidence-based criteria.",
                "Using arbitrary weights without rationale.",
            ),
            _entry(
                "Scholarship Ratio",
                "SR=\\frac{grant}{tuition+living}",
                "Funding share of full program cost.",
                "Financial feasibility planning.",
                "Comparing grants without full-cost denominator.",
            ),
            _entry(
                "Narrative Evidence Coverage",
                "NEC=\\frac{\\#supported\\ claims}{\\#total\\ claims}",
                "Evidence density in SOP/CV story.",
                "Stronger application credibility.",
                "Story claims without project proof.",
            ),
        ]

    if "github" in t or "readme" in t or "networking" in t or "presentation" in t or "behavioral" in t:
        return [
            _entry(
                "Evidence Coverage",
                "EC=\\frac{\\#claims\\ with\\ evidence}{\\#claims}",
                "Share of statements backed by outputs.",
                "Portfolio and presentation quality.",
                "Narrative-heavy artifacts without proof.",
            ),
            _entry(
                "Clarity Ratio",
                "CR=\\frac{\\#actionable\\ points}{\\#total\\ points}",
                "Actionability density of communication.",
                "Improve recruiter/interviewer comprehension.",
                "Overloaded slides/readmes with no decisions.",
            ),
            _entry(
                "Limitation Disclosure Rate",
                "LDR=\\frac{\\#explicit\\ limitations}{\\#major\\ findings}",
                "Transparency metric for credibility.",
                "Defend project scope honestly.",
                "Over-claiming robustness.",
            ),
        ]

    if "mock interview" in t or "probability drills" in t or "statistics" in t or "sql" in t or "python" in t:
        return [
            _entry(
                "Expected Value",
                "\\mathbb{E}[X]=\\sum_i p_i x_i",
                "Probability-weighted expected outcome.",
                "Fast interview math checks.",
                "Ignoring payoff asymmetry.",
            ),
            _entry(
                "z-Score",
                "z=\\frac{x-\\mu}{\\sigma}",
                "Standardized deviation metric.",
                "Data sanity and outlier drills.",
                "Using unstable sigma baseline.",
            ),
            _entry(
                "OLS Beta",
                "\\hat\\beta=(X^TX)^{-1}X^Ty",
                "Closed-form linear coefficient estimate.",
                "Regression interview derivations.",
                "Forgetting conditioning and collinearity risk.",
            ),
        ]

    if "capstone" in t or "final" in t or "transition roadmap" in t:
        return [
            _entry(
                "Net Return",
                "r_t^{net}=r_t^{gross}-cost_t",
                "Performance after implementation frictions.",
                "Final report realism.",
                "Presenting gross-only metrics.",
            ),
            _entry(
                "Out-of-Sample RMSE",
                "RMSE_{OOS}=\\sqrt{\\frac{1}{n}\\sum_i(\\hat y_i-y_i)^2}",
                "Forecast quality on unseen data.",
                "Capstone model comparison.",
                "Leaking test data into tuning.",
            ),
            _entry(
                "Max Drawdown",
                "MDD=\\min_t\\left(\\frac{W_t}{\\max_{s\\le t}W_s}-1\\right)",
                "Worst path-dependent loss.",
                "Risk defense in presentations.",
                "Reporting return with no drawdown context.",
            ),
        ]

    return None


def _topic_python_drill(topic: str) -> dict[str, str] | None:
    t = topic.lower()

    if "vectors" in t or "matrices" in t or "linear algebra" in t:
        return {
            "task": "Compute portfolio return and variance from a return matrix and covariance estimate.",
            "solution": _code(
                """
                from pathlib import Path
                import numpy as np
                import pandas as pd

                market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
                prices = market.pivot(index="date", columns="symbol", values="close").dropna()
                returns = prices.pct_change().dropna()
                w = np.array([0.4, 0.3, 0.2, 0.1])
                mu = returns.mean().values
                cov = returns.cov().values
                exp_ret = float(w @ mu)
                var = float(w @ cov @ w)
                print({"expected_daily_return": round(exp_ret, 6), "daily_variance": round(var, 8)})
                """
            ),
        }

    if "confidence intervals" in t or "hypothesis testing" in t:
        return {
            "task": "Compute a 95% confidence interval for SPY daily returns and report the t-statistic vs zero.",
            "solution": _code(
                """
                from pathlib import Path
                import numpy as np
                import pandas as pd
                from scipy import stats

                market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
                spy = market[market["symbol"] == "SPY"].sort_values("date")["close"].pct_change().dropna()
                n = len(spy)
                mean = float(spy.mean())
                std = float(spy.std(ddof=1))
                se = std / np.sqrt(n)
                t_crit = stats.t.ppf(0.975, n - 1)
                ci = (mean - t_crit * se, mean + t_crit * se)
                t_stat = mean / se
                print({"mean": round(mean, 6), "ci_95": tuple(round(x, 6) for x in ci), "t_stat": round(float(t_stat), 4)})
                """
            ),
        }

    if "ols" in t or "linear regression" in t:
        return {
            "task": "Fit a linear regression of QQQ returns on lagged SPY returns and report coefficient and R^2.",
            "solution": _code(
                """
                from pathlib import Path
                import pandas as pd
                from sklearn.linear_model import LinearRegression

                market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
                prices = market.pivot(index="date", columns="symbol", values="close").dropna()
                returns = prices.pct_change().dropna()
                X = returns[["SPY"]].shift(1).dropna()
                y = returns.loc[X.index, "QQQ"]
                model = LinearRegression().fit(X, y)
                print({"beta_spy": round(float(model.coef_[0]), 6), "intercept": round(float(model.intercept_), 6), "r2": round(float(model.score(X, y)), 4)})
                """
            ),
        }

    if "optimization" in t or "constrained" in t:
        return {
            "task": "Minimize portfolio variance with long-only weights that sum to one.",
            "solution": _code(
                """
                from pathlib import Path
                import numpy as np
                import pandas as pd
                from scipy.optimize import minimize

                market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
                prices = market.pivot(index="date", columns="symbol", values="close").dropna()
                returns = prices.pct_change().dropna().iloc[:, :4]
                cov = returns.cov().values
                n = cov.shape[0]
                x0 = np.ones(n) / n
                bounds = [(0, 1)] * n
                cons = ({"type": "eq", "fun": lambda w: w.sum() - 1},)
                obj = lambda w: float(w @ cov @ w)
                res = minimize(obj, x0=x0, bounds=bounds, constraints=cons)
                print("success:", res.success)
                print("weights:", np.round(res.x, 4))
                print("variance:", round(float(res.fun), 8))
                """
            ),
        }

    if "clustering" in t:
        return {
            "task": "Cluster symbols by return and volatility features using k-means and report labels.",
            "solution": _code(
                """
                from pathlib import Path
                import pandas as pd
                from sklearn.cluster import KMeans

                market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
                prices = market.pivot(index="date", columns="symbol", values="close").dropna()
                ret = prices.pct_change().dropna()
                feats = pd.DataFrame({"mean": ret.mean(), "vol": ret.std()})
                model = KMeans(n_clusters=2, random_state=7, n_init=10)
                feats["cluster"] = model.fit_predict(feats)
                print(feats)
                """
            ),
        }

    if "pca" in t or "variance decomposition" in t:
        return {
            "task": "Run PCA on standardized returns and report explained variance ratios.",
            "solution": _code(
                """
                from pathlib import Path
                import pandas as pd
                from sklearn.decomposition import PCA
                from sklearn.preprocessing import StandardScaler

                market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
                prices = market.pivot(index="date", columns="symbol", values="close").dropna()
                ret = prices.pct_change().dropna()
                X = StandardScaler().fit_transform(ret)
                pca = PCA(n_components=min(3, X.shape[1]))
                pca.fit(X)
                print("Explained variance ratio:", [round(float(x), 4) for x in pca.explained_variance_ratio_])
                """
            ),
        }

    if "arima" in t or "stationarity" in t or "autocorrelation" in t or "walk-forward" in t:
        return {
            "task": "Build a lag-based forecast baseline and compute RMSE on the last 30 observations.",
            "solution": _code(
                """
                from pathlib import Path
                import numpy as np
                import pandas as pd

                market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
                spy = market[market["symbol"] == "SPY"].sort_values("date").set_index("date")["close"]
                r = spy.pct_change().dropna()
                lag1 = r.shift(1).dropna()
                y = r.loc[lag1.index]
                split = max(30, int(len(y) * 0.8))
                pred = lag1.iloc[split:]
                truth = y.iloc[split:]
                rmse = float(np.sqrt(((pred - truth) ** 2).mean()))
                print({"rmse": round(rmse, 6), "test_points": len(truth)})
                """
            ),
        }

    if "decision trees" in t:
        return {
            "task": "Train a decision tree classifier on lagged ETF returns and print depth and accuracy.",
            "solution": _code(
                """
                from pathlib import Path
                import pandas as pd
                from sklearn.metrics import accuracy_score
                from sklearn.model_selection import train_test_split
                from sklearn.tree import DecisionTreeClassifier

                market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
                prices = market.pivot(index="date", columns="symbol", values="close").dropna()
                returns = prices.pct_change().dropna()
                X = returns.shift(1).dropna()
                y = (returns.loc[X.index, "SPY"] > 0).astype(int)
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=False)
                model = DecisionTreeClassifier(max_depth=4, random_state=7)
                model.fit(X_train, y_train)
                pred = model.predict(X_test)
                print({"depth": model.get_depth(), "accuracy": round(float(accuracy_score(y_test, pred)), 4)})
                """
            ),
        }

    if "random forests" in t:
        return {
            "task": "Train a random forest classifier and report feature importances.",
            "solution": _code(
                """
                from pathlib import Path
                import pandas as pd
                from sklearn.ensemble import RandomForestClassifier

                market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
                prices = market.pivot(index="date", columns="symbol", values="close").dropna()
                returns = prices.pct_change().dropna()
                X = returns.shift(1).dropna()
                y = (returns.loc[X.index, "SPY"] > 0).astype(int)
                model = RandomForestClassifier(n_estimators=200, random_state=7)
                model.fit(X, y)
                print(pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False))
                """
            ),
        }

    if "gradient boosting" in t:
        return {
            "task": "Train a gradient boosting classifier and report train score.",
            "solution": _code(
                """
                from pathlib import Path
                import pandas as pd
                from sklearn.ensemble import GradientBoostingClassifier

                market = pd.read_csv(Path("curriculum/datasets/real_market_prices.csv"), parse_dates=["date"])
                prices = market.pivot(index="date", columns="symbol", values="close").dropna()
                returns = prices.pct_change().dropna()
                X = returns.shift(1).dropna()
                y = (returns.loc[X.index, "SPY"] > 0).astype(int)
                model = GradientBoostingClassifier(random_state=7)
                model.fit(X, y)
                print({"train_accuracy": round(float(model.score(X, y)), 4)})
                """
            ),
        }

    if "bond" in t or "duration" in t or "convexity" in t or "yield curve" in t:
        return {
            "task": "Price a simple bond and compute modified duration under a yield assumption.",
            "solution": _code(
                """
                import numpy as np

                face = 100
                coupon = 0.05
                y = 0.04
                n = 5
                cf = np.array([face * coupon] * (n - 1) + [face * (1 + coupon)])
                t = np.arange(1, n + 1)
                disc = (1 + y) ** t
                price = float((cf / disc).sum())
                d_mac = float((t * cf / disc).sum() / price)
                d_mod = d_mac / (1 + y)
                print({"price": round(price, 4), "mod_duration": round(d_mod, 4)})
                """
            ),
        }

    if "forwards" in t or "futures" in t or "option" in t or "greeks" in t:
        return {
            "task": "Build option payoff vectors and approximate delta around the strike.",
            "solution": _code(
                """
                import numpy as np

                k = 100
                s = np.linspace(70, 130, 13)
                call = np.maximum(s - k, 0)
                put = np.maximum(k - s, 0)
                eps = 1.0
                s0 = 100
                delta = (max(s0 + eps - k, 0) - max(s0 - eps - k, 0)) / (2 * eps)
                print("call:", call)
                print("put:", put)
                print("delta near strike:", round(float(delta), 4))
                """
            ),
        }

    if "github" in t or "readme" in t or "networking" in t or "presentation" in t or "behavioral" in t:
        return {
            "task": "Create a claim-evidence table for a portfolio story and compute evidence coverage.",
            "solution": _code(
                """
                import pandas as pd

                story = pd.DataFrame(
                    [
                        {"claim": "Signal improves net return", "evidence": "backtest table", "supported": 1},
                        {"claim": "Robust in all regimes", "evidence": "none", "supported": 0},
                        {"claim": "Risk is controlled", "evidence": "drawdown chart", "supported": 1},
                    ]
                )
                coverage = float(story["supported"].mean())
                print(story)
                print("evidence_coverage:", round(coverage, 3))
                """
            ),
        }

    return None


def formula_entries_for_week(week_number: int, topic: str = "") -> list[dict[str, str]]:
    topic_entries = _topic_formula_entries(topic) if topic else None
    if topic_entries:
        return topic_entries

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
                "equation": "EC=\\frac{\\#claims\\ with\\ evidence}{\\#claims}",
                "meaning": "Share of statements supported by data or outputs.",
                "use_case": "Case-study defense quality.",
                "pitfall": "Narrative claims without references.",
            },
            {
                "name": "Clarity Ratio",
                "equation": "CR=\\frac{\\#clear\\ action\\ points}{\\#total\\ points}",
                "meaning": "How actionable the communication is.",
                "use_case": "Improve portfolio presentation readability.",
                "pitfall": "Dense reports without decision guidance.",
            },
            {
                "name": "Limitation Disclosure Rate",
                "equation": "LDR=\\frac{\\#explicit\\ limitations}{\\#major\\ findings}",
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
    topic_drill = _topic_python_drill(topic)
    if topic_drill:
        return topic_drill

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
