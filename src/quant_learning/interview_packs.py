from __future__ import annotations

from typing import Any


def build_interview_pack(week_number: int, title: str, concepts: list[str]) -> list[dict[str, Any]]:
    if week_number == 1:
        return [
            {
                "question": "What is the difference between absolute price change and return?",
                "answer": (
                    "Absolute price change is measured in currency units, like a stock moving from 100 to 105. "
                    "Return scales that change by the starting price, so the same move becomes 5 percent. "
                    "Quants prefer returns because they are comparable across instruments with different price levels."
                ),
            },
            {
                "question": "Why does compounding matter in trading performance?",
                "answer": (
                    "Trading performance builds on the current capital base, not the original base every day. "
                    "That means gains and losses multiply over time. A strategy that ignores compounding can misstate growth, drawdown, and recovery needs."
                ),
            },
            {
                "question": "How would you explain expected value to a trader?",
                "answer": (
                    "Expected value is the average payoff if the same decision could be repeated many times under similar conditions. "
                    "A trader can still lose on a single trade with positive expected value, but over a large sample that setup should be favorable if the assumptions are right."
                ),
            },
            {
                "question": "What is the practical difference between buy-side and sell-side quant work?",
                "answer": (
                    "Buy-side quants usually work closer to alpha generation, portfolio construction, and PnL ownership at hedge funds, prop firms, or asset managers. "
                    "Sell-side quants at banks are more often focused on pricing, structuring, execution tools, risk, and supporting client or desk activity."
                ),
            },
        ]

    concept_a = concepts[0] if concepts else "this topic"
    concept_b = concepts[1] if len(concepts) > 1 else concept_a
    concept_c = concepts[2] if len(concepts) > 2 else title
    return [
        {
            "question": f"Explain {concept_a.lower()} in plain English.",
            "answer": (
                f"{concept_a} should first be explained as an intuitive idea before any notation. "
                f"In quant work it matters because it shapes how we measure, compare, or model financial behavior inside {title.lower()} tasks."
            ),
        },
        {
            "question": f"What is a common mistake when applying {concept_b.lower()} in finance?",
            "answer": (
                f"A common mistake is to use {concept_b.lower()} mechanically while ignoring assumptions, data quality, or market frictions. "
                f"In finance, even a mathematically correct method can fail if the data are noisy, the sample is unstable, or the implementation is unrealistic."
            ),
        },
        {
            "question": f"How would you test whether your work on {title.lower()} is robust?",
            "answer": (
                f"I would start with a simple baseline, check sensitivity to assumptions, inspect subperiod stability, and verify that results survive realistic costs or constraints. "
                f"If the topic involves prediction or backtesting, I would also guard against leakage and ensure evaluation is aligned with how the model would be used live."
            ),
        },
        {
            "question": f"Why does {concept_c.lower()} matter for a quant trader or quant researcher?",
            "answer": (
                f"{concept_c} matters because it changes either signal quality, risk control, implementation quality, or communication with a desk or portfolio manager. "
                f"A useful quant answer should always connect the concept to a real decision rather than leaving it as theory only."
            ),
        },
    ]

