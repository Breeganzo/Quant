import { createClient } from "@supabase/supabase-js";

export const DEFAULT_PROGRESS = {
  days: {},
  weeklyReviews: {},
};

const SUPABASE_URL = (import.meta.env.VITE_SUPABASE_URL || "").trim();
const SUPABASE_ANON_KEY = (import.meta.env.VITE_SUPABASE_ANON_KEY || "").trim();
const PROGRESS_TABLE = (import.meta.env.VITE_SUPABASE_PROGRESS_TABLE || "study_progress").trim();

let cachedClient = null;

export function hasRemoteSyncConfig() {
  return Boolean(SUPABASE_URL && SUPABASE_ANON_KEY);
}

export function getSupabaseClient() {
  if (!hasRemoteSyncConfig()) {
    return null;
  }
  if (!cachedClient) {
    cachedClient = createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
      auth: {
        persistSession: true,
        autoRefreshToken: true,
        detectSessionInUrl: true,
      },
    });
  }
  return cachedClient;
}

function parseTimestamp(value) {
  if (!value || typeof value !== "string") {
    return 0;
  }
  const parsed = Date.parse(value);
  return Number.isNaN(parsed) ? 0 : parsed;
}

function pickLatest(localEntry = {}, remoteEntry = {}) {
  const localTs = parseTimestamp(localEntry.updatedAt);
  const remoteTs = parseTimestamp(remoteEntry.updatedAt);
  return remoteTs > localTs ? remoteEntry : localEntry;
}

export function normalizeProgress(progress) {
  if (!progress || typeof progress !== "object") {
    return { ...DEFAULT_PROGRESS };
  }
  return {
    days: progress.days && typeof progress.days === "object" ? progress.days : {},
    weeklyReviews:
      progress.weeklyReviews && typeof progress.weeklyReviews === "object"
        ? progress.weeklyReviews
        : {},
  };
}

export function hasProgressData(progress) {
  const normalized = normalizeProgress(progress);
  return (
    Object.keys(normalized.days).length > 0 ||
    Object.keys(normalized.weeklyReviews).length > 0
  );
}

export function mergeProgress(localProgress, remoteProgress) {
  const local = normalizeProgress(localProgress);
  const remote = normalizeProgress(remoteProgress);

  const dayKeys = new Set([
    ...Object.keys(local.days),
    ...Object.keys(remote.days),
  ]);
  const mergedDays = {};
  for (const key of dayKeys) {
    mergedDays[key] = pickLatest(local.days[key], remote.days[key]);
  }

  const reviewKeys = new Set([
    ...Object.keys(local.weeklyReviews),
    ...Object.keys(remote.weeklyReviews),
  ]);
  const mergedReviews = {};
  for (const key of reviewKeys) {
    const localEntry = local.weeklyReviews[key];
    const remoteEntry = remote.weeklyReviews[key];
    if (
      localEntry &&
      typeof localEntry === "object" &&
      remoteEntry &&
      typeof remoteEntry === "object"
    ) {
      mergedReviews[key] = pickLatest(localEntry, remoteEntry);
    } else {
      mergedReviews[key] = remoteEntry ?? localEntry;
    }
  }

  return {
    days: mergedDays,
    weeklyReviews: mergedReviews,
  };
}

export async function fetchRemoteProgress(client, userId) {
  const { data, error } = await client
    .from(PROGRESS_TABLE)
    .select("progress")
    .eq("user_id", userId)
    .maybeSingle();

  if (error) {
    throw error;
  }

  return normalizeProgress(data?.progress);
}

export async function saveRemoteProgress(client, userId, progress) {
  const normalized = normalizeProgress(progress);
  const { error } = await client.from(PROGRESS_TABLE).upsert(
    {
      user_id: userId,
      progress: normalized,
      updated_at: new Date().toISOString(),
    },
    {
      onConflict: "user_id",
    }
  );

  if (error) {
    throw error;
  }
}

export async function signUpWithEmail(client, email, password) {
  const { error } = await client.auth.signUp({ email, password });
  if (error) {
    throw error;
  }
}

export async function signInWithEmail(client, email, password) {
  const { error } = await client.auth.signInWithPassword({ email, password });
  if (error) {
    throw error;
  }
}

export async function signOutUser(client) {
  const { error } = await client.auth.signOut();
  if (error) {
    throw error;
  }
}
