from __future__ import annotations

from pathlib import Path

from quant_learning.content import load_curriculum


def _has_day_lesson(week_number: int, day_index: int) -> bool:
    week_dir = Path(f"curriculum/week-{week_number:02d}")
    return any(week_dir.glob(f"day-{day_index:02d}-*/lesson.md"))


def _has_day_notebook(week_number: int, day_index: int) -> bool:
    notebooks_dir = Path(f"curriculum/week-{week_number:02d}/notebooks")
    return any(notebooks_dir.glob(f"day-{day_index:02d}-*.ipynb"))


def main() -> None:
    data = load_curriculum()
    assert len(data["roadmap"]) == 24, "Expected 24 roadmap weeks"
    assert data["roadmap"][0]["week"] == 1, "First week missing"
    assert data["roadmap"][-1]["week"] == 24, "Last week missing"

    for week in data["roadmap"]:
        assert week["weekly_overview_notebook_path"], f"Week {week['week']} overview notebook path missing"
        assert week["weekly_project_notebook_path"], f"Week {week['week']} project notebook path missing"
        for day in week["daily_schedule"]:
            assert day["lesson_markdown_path"], f"Week {week['week']} day lesson path missing"
            assert day["lesson_pdf_path"], f"Week {week['week']} day PDF path missing"
            assert day["notebook_path"], f"Week {week['week']} day notebook path missing"

    assert Path("curriculum/week-01/notebooks/week-01-foundations.ipynb").exists()
    assert Path("curriculum/week-01/notebooks/day-01-reset-your-toolkit-numbers-variables-returns-and-compounding.ipynb").exists()
    assert Path("curriculum/week-01/notebooks/week-01-mini-project.ipynb").exists()
    assert Path("curriculum/week-04/notebooks/week-04-capstone.ipynb").exists()
    assert Path("curriculum/week-08/notebooks/week-08-capstone.ipynb").exists()
    assert Path("curriculum/week-12/notebooks/week-12-capstone.ipynb").exists()
    assert Path("curriculum/week-16/notebooks/week-16-capstone.ipynb").exists()
    assert Path("curriculum/week-20/notebooks/week-20-capstone.ipynb").exists()
    assert Path("curriculum/week-24/notebooks/week-24-capstone.ipynb").exists()

    assert _has_day_lesson(5, 1), "Week 5 day-01 lesson missing"
    assert _has_day_lesson(9, 3), "Week 9 day-03 lesson missing"
    assert _has_day_lesson(16, 5), "Week 16 day-05 lesson missing"
    assert _has_day_lesson(24, 7), "Week 24 day-07 lesson missing"

    assert _has_day_notebook(5, 1), "Week 5 day-01 notebook missing"
    assert _has_day_notebook(11, 2), "Week 11 day-02 notebook missing"
    assert _has_day_notebook(18, 4), "Week 18 day-04 notebook missing"
    assert _has_day_notebook(24, 7), "Week 24 day-07 notebook missing"

    assert Path("curriculum/pdfs/24-week-roadmap.pdf").exists()
    assert Path("curriculum/pdfs/week-24/plan.pdf").exists()
    assert any(Path("curriculum/pdfs/week-24").glob("day-07-*/lesson.pdf")), "Week 24 day-07 PDF missing"
    assert Path("docs/index.html").exists()
    print(
        "Smoke check passed:",
        f"weeks={len(data['roadmap'])}",
        f"docs_ready={Path('docs/index.html').exists()}",
        f"month1_notebooks_ready={Path('curriculum/week-04/notebooks/week-04-capstone.ipynb').exists()}",
        f"month2_to_6_ready={Path('curriculum/week-24/notebooks/week-24-capstone.ipynb').exists()}",
    )
