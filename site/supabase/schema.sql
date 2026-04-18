create extension if not exists pgcrypto;

create table if not exists public.study_progress (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null unique references auth.users(id) on delete cascade,
  progress jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now()
);

alter table public.study_progress enable row level security;

drop policy if exists "Users can read own progress" on public.study_progress;
drop policy if exists "Users can insert own progress" on public.study_progress;
drop policy if exists "Users can update own progress" on public.study_progress;

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
