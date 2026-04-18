# Quant Learning System

This repository provides a 24-week quant finance and ML learning system with:

- a full 6-month (24-week) roadmap
- day-by-day continuity across all weeks
- expanded daily lesson plans with session-based study flow
- notebook-based practice for every day and weekly project
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

## Run Notebooks Properly (JupyterLab)

Use the project environment so notebook packages are available:

```bash
cd "/Users/anto/Quant Learning"
uv sync
uv run quant-jupyter
```

Then open notebooks in JupyterLab. The site notebook buttons are configured for local JupyterLab at:

- `http://localhost:8888/lab/tree/...`

This avoids opening raw `.ipynb` JSON in the browser.

## Run Website Locally (Development)

From repo root:

```bash
cd site
npm install
npm run dev
```

Open this URL in your browser:

- `http://localhost:5173/Quant/`

Notes:

- Day pages render lesson content directly in the app.
- Notebook buttons open local JupyterLab instead of raw JSON files.
- Progress updates autosave in browser storage.

## Preview Production Build Locally

```bash
cd site
npm run preview
```

Then open the URL printed by Vite (typically also under `/Quant/`).

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

3. Create table and policies in Supabase SQL editor:

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

## Curriculum Coverage Status

- Weeks 1-24: roadmap + weekly plans generated
- Weeks 1-24: daily lesson markdown generated
- Weeks 1-24: day notebook files and weekly project notebooks generated
- Weeks 1-24: notebooks are generated as structured study templates ready to run in JupyterLab
- Notebook execution is intentionally done interactively in JupyterLab (not during bootstrap) for reliability

## Repository Layout

- `curriculum/`: roadmap, weekly plans, day lessons, notebooks, generated PDFs
- `site/`: React app source
- `docs/`: static build output for GitHub Pages
- `src/quant_learning/`: bootstrap, export, smoke-check code
- `templates/`: checklist and review templates
- `references/`: benchmarking, system flow, and career notes

## Suggested Weekly Time Budget

- Monday-Friday: `4 hours/day`
- Saturday: `2 hours`
- Sunday: `2 hours`
- Total: about `24 hours/week`
