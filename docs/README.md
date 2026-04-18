# Quant Learning System

This repository is a practical 24-week quant finance and machine learning study system designed around:

- a beginner restart in math and finance
- your target of `Quant Finance` master's applications for `September 2027` or `January 2028`
- a practical, portfolio-driven workflow inspired by strong MFE/MSCF/MSFE curricula and WorldQuant-style applied learning
- a GitHub Pages-ready React tracker with persistent browser storage

## Start Here

```bash
uv sync
uv run quant-bootstrap
uv run quant-export-pdfs
uv run quant-smoke-check
cd site
npm install
npm run build
```

## Repository Layout

- `curriculum/`: roadmap, weekly plans, day-by-day lessons, notebooks, and generated PDFs
- `site/`: React app source for the tracker and hosted learning interface
- `docs/`: built static site for GitHub Pages plus copied curriculum assets
- `src/quant_learning/`: curriculum generation, PDF export, and utilities
- `templates/`: daily, weekly, and monthly tracking forms
- `references/`: benchmarking, workflow, and career notes copied into the site build

## Persistence

The hosted tracker stores progress in browser `localStorage`. Your completion state, confidence score, and day notes remain available when you close and reopen the site in the same browser.

## PDF Workflow

The curriculum is authored in markdown and notebook-friendly form, then exported to PDF using a pure-Python exporter so it stays easy to read offline.

## Suggested Weekly Time Budget

- Monday to Friday: `4 hours/day`
- Saturday: `2 hours`
- Sunday: `2 hours`
- Total: about `24 hours/week`

## Current Scope

This current build includes:

- the full 24-week roadmap
- weekly plans for all 24 weeks
- Month 1 fully expanded day by day
- executed notebooks for Weeks 1 to 4
- project notebooks for Weeks 1 to 4
- monthly rubrics, checklists, and spaced repetition templates
- a hosted React tracking UI with lesson, PDF, and notebook links
