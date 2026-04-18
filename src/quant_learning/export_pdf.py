from __future__ import annotations

from pathlib import Path
from typing import Iterable

from markdown_it import MarkdownIt
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer


MARKDOWN = MarkdownIt()


def markdown_to_flowables(text: str):
    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    body_style = styles["BodyText"]
    body_style.spaceAfter = 8
    bullet_style = ParagraphStyle(
        "BulletText",
        parent=body_style,
        leftIndent=18,
        bulletIndent=6,
    )
    heading_style = styles["Heading2"]

    flowables = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            flowables.append(Spacer(1, 0.2 * cm))
            continue

        if line.startswith("# "):
            flowables.append(Paragraph(line[2:], title_style))
        elif line.startswith("## "):
            flowables.append(Paragraph(line[3:], heading_style))
        elif line.startswith("### "):
            flowables.append(Paragraph(line[4:], styles["Heading3"]))
        elif line.startswith("- "):
            flowables.append(Paragraph(f"&bull; {line[2:]}", bullet_style))
        elif line.startswith("|"):
            # Render tables as monospace-ish paragraphs to keep exporter simple and reliable.
            flowables.append(Paragraph(line.replace(" ", "&nbsp;"), styles["Code"]))
        else:
            flowables.append(Paragraph(line, body_style))
    return flowables


def export_markdown_file(md_path: Path, pdf_path: Path) -> None:
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        rightMargin=1.5 * cm,
        leftMargin=1.5 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
    )
    text = md_path.read_text(encoding="utf-8")
    doc.build(markdown_to_flowables(text))


def iter_markdown_targets() -> Iterable[tuple[Path, Path]]:
    root = Path("curriculum")
    for md_path in sorted(root.rglob("*.md")):
        relative = md_path.relative_to(root)
        if relative.parts and relative.parts[0] == "pdfs":
            continue
        pdf_path = root / "pdfs" / relative.with_suffix(".pdf")
        yield md_path, pdf_path


def main() -> None:
    for md_path, pdf_path in iter_markdown_targets():
        export_markdown_file(md_path, pdf_path)
    print("Exported curriculum markdown files to curriculum/pdfs/")

