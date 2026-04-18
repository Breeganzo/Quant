from __future__ import annotations

from pathlib import Path

from quant_learning.content import load_curriculum


def main() -> None:
    data = load_curriculum()
    assert len(data["roadmap"]) == 24, "Expected 24 roadmap weeks"
    assert data["roadmap"][0]["week"] == 1, "First week missing"
    assert Path("curriculum/week-01/notebooks/week-01-foundations.ipynb").exists()
    assert Path("curriculum/week-01/notebooks/day-01-reset-your-toolkit-numbers-variables-returns-and-compounding.ipynb").exists()
    assert Path("curriculum/week-01/notebooks/week-01-mini-project.ipynb").exists()
    assert Path("curriculum/week-04/notebooks/week-04-capstone.ipynb").exists()
    assert Path("curriculum/pdfs/24-week-roadmap.pdf").exists()
    assert Path("docs/index.html").exists()
    print(
        "Smoke check passed:",
        f"weeks={len(data['roadmap'])}",
        f"docs_ready={Path('docs/index.html').exists()}",
        f"month1_notebooks_ready={Path('curriculum/week-04/notebooks/week-04-capstone.ipynb').exists()}",
    )
