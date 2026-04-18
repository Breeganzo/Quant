# Quant Learning System

This repository provides a 24-week quant finance and ML learning system with:

- a full 6-month (24-week) roadmap
- day-by-day continuity across all weeks
- expanded daily lesson plans with session-based study flow
- notebook-based practice for every day and weekly project
- standalone daily quiz artifacts (`quiz.md` + `quiz.json`) with answer guides
- explicit daily formula drills and closed-book quiz/revision structure
- PDF export for offline study
- a React tracker site ready for GitHub Pages deployment
- local progress persistence in browser storage

## Prerequisites

- Python 3.11 or 3.12
- uv
- Node.js 18+
- npm

## One-Time Setup + Full Verification

Run the exact flow below from repo root:

```bash
cd "/Users/anto/Quant Learning"
uv sync
uv run quant-bootstrap
uv run quant-export-pdfs
uv run quant-smoke-check
cd site
npm install
npm run build
```

What this does:

- `quant-bootstrap`: builds roadmap JSON, week plans, day lesson markdown, templates, docs references, and notebooks
- `quant-export-pdfs`: exports markdown to `curriculum/pdfs/`
- `quant-smoke-check`: verifies 24-week integrity and key artifacts (including Months 2-6)
- `npm run build`: syncs content and builds static site to `docs/`

Optional deep validation (runs every generated notebook):

```bash
cd "/Users/anto/Quant Learning"
uv run quant-verify-notebooks --timeout 180
```

This writes `exports/notebook-validation.json` with pass/fail results per notebook.

## Where The Notebooks Are

If you are browsing locally, notebooks are here:

- `curriculum/week-01/notebooks/`
- `curriculum/week-02/notebooks/`
- ...
- `curriculum/week-24/notebooks/`

If you are browsing the deployed site, notebook assets are copied under:

- `docs/curriculum/week-XX/notebooks/`

Real-world dataset used by daily notebook labs:

- `curriculum/datasets/real_market_prices.csv`

## Notebook Access

Website behavior:

- Notebook buttons in the site open an in-app notebook viewer by default.
- The viewer is read-only for study; use the download action or VS Code web when you want to edit.

Notebook source locations:

- `curriculum/week-01/notebooks/` ... `curriculum/week-24/notebooks/`
- deployed static copy: `docs/curriculum/week-XX/notebooks/`

If you fork or rename the repo, update `site/.env.local` with `VITE_GITHUB_REPO` and `VITE_GITHUB_BRANCH` so the VS Code web links stay correct.

## Run Website Locally (Development)

From repo root:

```bash
cd site
npm install
npm run dev
```

Open this URL in your browser:

- `http://localhost:5173/Quant_Practise/`

Notes:

- Day pages render lesson content directly in the app.
- Notebook buttons open in-app notebook viewer by default, with optional VS Code action.
- Progress updates autosave in browser storage.

## Preview Production Build Locally

```bash
cd site
npm run preview
```

Then open the URL printed by Vite (typically also under `/Quant_Practise/`).

## Progress Persistence

Progress is always stored in browser localStorage:

- completion status
- confidence score
- day notes

This persists across `npm run dev` restarts on the same browser profile and device.

If you want backup/transfer, use the app's export/import progress JSON buttons.

## Cross-Device Persistent Memory (Supabase Optional)

If you want progress to sync across multiple devices and browsers, enable Supabase cloud sync.

1. Copy environment template:

```bash
cd "/Users/anto/Quant Learning/site"
cp .env.example .env.local
```

2. Fill in:

- `VITE_SUPABASE_URL`
- `VITE_SUPABASE_ANON_KEY`
- `VITE_SITE_BASE` (set this to your deployed subpath, for example `/Quant_Practise/`)

If your static host does not inject build-time env vars, set Supabase at runtime in:

- `site/public/runtime-config.js`

3. In Supabase SQL editor, run the script from `site/supabase/schema.sql`.

Equivalent SQL:

```sql
create table if not exists public.study_progress (
	id uuid primary key default gen_random_uuid(),
	user_id uuid not null unique references auth.users(id) on delete cascade,
	progress jsonb not null default '{}'::jsonb,
	updated_at timestamptz not null default now()
);

alter table public.study_progress enable row level security;

create policy "Users can read own progress"
	on public.study_progress
	for select
	using (auth.uid() = user_id);

create policy "Users can insert own progress"
	on public.study_progress
	for insert
	with check (auth.uid() = user_id);

create policy "Users can update own progress"
	on public.study_progress
	for update
	using (auth.uid() = user_id)
	with check (auth.uid() = user_id);
```

4. Start the site and sign in from the dashboard Cloud Sync panel.

Behavior:

- if cloud sync is not configured, app works fully in local-only mode
- when you sign in, local and cloud progress are merged and then synced automatically
- cloud sync keeps progress consistent across signed-in devices

## GitHub Pages Output

- Production build output is written to `docs/`
- Site base path is configured as `/Quant/` in `site/vite.config.js`

## Host on GitHub Pages

1. Build the site:

```bash
cd "/Users/anto/Quant Learning/site"
npm install
npm run build
```

2. Commit and push the updated `docs/` folder.
3. In GitHub repo settings, enable Pages and set source to branch `main` / folder `docs`.
4. Open the published URL.

Important: GitHub Pages is static hosting. Progress is browser-local by default; cross-device persistence requires optional backend sync (for example, Supabase as shown above).

## Why Daily Markdown Files Exist

Day-level markdown files are required source content for:

- PDF generation (`quant-export-pdfs`)
- in-app day lesson rendering on the website
- regeneration consistency when curriculum is rebuilt

So daily markdown is not redundant, even if you mainly consume PDFs.

## Curriculum Coverage Status

- Weeks 1-24: roadmap + weekly plans generated
- Weeks 1-24: daily lesson markdown generated
- Weeks 1-24: daily quiz markdown/json generated
- Weeks 1-24: day notebook files and weekly project notebooks generated
- Weeks 1-24: notebooks include real-data labs using `curriculum/datasets/real_market_prices.csv`

## Daily Artifact Guarantee

Every day (all 168 days) is generated with:

- theory lesson markdown: `lesson.md`
- theory PDF: `lesson.pdf`
- daily quiz markdown: `quiz.md`
- daily quiz PDF: `quiz.pdf`
- structured quiz JSON with answer guide: `quiz.json`
- daily notebook: `day-XX-*.ipynb`

## Repository Layout

- `curriculum/`: roadmap, weekly plans, day lessons, notebooks, generated PDFs
- `site/`: React app source
- `docs/`: static build output for GitHub Pages
- `src/quant_learning/`: bootstrap, export, smoke-check code
- `templates/`: checklist and review templates
- `references/`: benchmarking, system flow, and career notes

## Suggested Weekly Time Budget

- Monday-Friday: `8 hours/day`
- Saturday: `8 hours`
- Sunday: `8 hours`
- Total: about `56 hours/week`
