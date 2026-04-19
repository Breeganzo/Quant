import { useEffect, useMemo, useRef, useState } from "react";
import ReactMarkdown from "react-markdown";
import rehypeKatex from "rehype-katex";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";
import { Link, NavLink, Route, Routes, useLocation, useNavigate, useParams } from "react-router-dom";
import "katex/dist/katex.min.css";
import {
  DEFAULT_PROGRESS,
  fetchRemoteProgress,
  getSupabaseClient,
  hasProgressData,
  mergeProgress,
  normalizeProgress,
  saveRemoteProgress,
  signInWithEmail,
  signOutUser,
  signUpWithEmail,
} from "./progressSync";

const STORAGE_KEY = "quant-learning-progress-v2";
const GITHUB_REPO = (import.meta.env.VITE_GITHUB_REPO || "Breeganzo/Quant").trim();
const GITHUB_BRANCH = (import.meta.env.VITE_GITHUB_BRANCH || "main").trim();

function withBase(path) {
  if (!path) return "";
  return `${import.meta.env.BASE_URL}${path}`.replace(/([^:]\/)\/+/g, "$1");
}

function withNotebookViewer(path) {
  if (!path) return "";
  const normalized = path.replace(/^\/+/, "");
  return `/notebook/${encodeURIComponent(normalized)}`;
}

function withVSCodeWeb(path) {
  if (!path) return "";
  const normalized = path.replace(/^\/+/, "");
  return `https://vscode.dev/github/${GITHUB_REPO}/blob/${GITHUB_BRANCH}/${normalized}`;
}

function withGitHubBlob(path) {
  if (!path) return "";
  const normalized = path.replace(/^\/+/, "");
  return `https://github.com/${GITHUB_REPO}/blob/${GITHUB_BRANCH}/${normalized}`;
}

function withAdditionalReading(weekNumber) {
  const readingPath = withBase("references/additional-reading.md");
  return `${readingPath}#week-${String(weekNumber).padStart(2, "0")}`;
}

function loadProgress() {
  try {
    const raw = window.localStorage.getItem(STORAGE_KEY);
    return raw ? normalizeProgress(JSON.parse(raw)) : { ...DEFAULT_PROGRESS };
  } catch {
    return { ...DEFAULT_PROGRESS };
  }
}

function saveProgress(progress) {
  window.localStorage.setItem(STORAGE_KEY, JSON.stringify(normalizeProgress(progress)));
}

function dayKey(week, dayIndex) {
  return `week-${String(week).padStart(2, "0")}-day-${String(dayIndex).padStart(2, "0")}`;
}

function monthLabel(week) {
  return `Month ${Math.ceil(week / 4)}`;
}

function useCurriculum() {
  const [data, setData] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch(withBase("curriculum/roadmap.json"))
      .then((res) => {
        if (!res.ok) throw new Error("Failed to load roadmap.json");
        return res.json();
      })
      .then(setData)
      .catch((err) => setError(err.message));
  }, []);

  return { data, error };
}

function useMarkdown(path) {
  const [content, setContent] = useState("");
  const [status, setStatus] = useState(path ? "loading" : "idle");

  useEffect(() => {
    if (!path) {
      setStatus("idle");
      setContent("");
      return;
    }

    let cancelled = false;
    setStatus("loading");

    fetch(withBase(path))
      .then((res) => {
        if (!res.ok) throw new Error(`Failed to load ${path}`);
        return res.text();
      })
      .then((text) => {
        if (!cancelled) {
          setContent(text);
          setStatus("ready");
        }
      })
      .catch(() => {
        if (!cancelled) {
          setContent("");
          setStatus("error");
        }
      });

    return () => {
      cancelled = true;
    };
  }, [path]);

  return { content, status };
}

function useNotebook(path) {
  const [notebook, setNotebook] = useState(null);
  const [status, setStatus] = useState(path ? "loading" : "idle");
  const [error, setError] = useState("");

  useEffect(() => {
    if (!path) {
      setStatus("idle");
      setNotebook(null);
      setError("");
      return;
    }

    let cancelled = false;
    setStatus("loading");
    setError("");

    fetch(withBase(path))
      .then((res) => {
        if (!res.ok) throw new Error(`Failed to load notebook: ${path}`);
        return res.json();
      })
      .then((data) => {
        if (!cancelled) {
          setNotebook(data);
          setStatus("ready");
        }
      })
      .catch((err) => {
        if (!cancelled) {
          setNotebook(null);
          setStatus("error");
          setError(err.message);
        }
      });

    return () => {
      cancelled = true;
    };
  }, [path]);

  return { notebook, status, error };
}

function summarizeNotebook(notebook) {
  const cells = Array.isArray(notebook?.cells) ? notebook.cells : [];
  const markdownCells = cells.filter((cell) => cell.cell_type === "markdown").length;
  const codeCells = cells.filter((cell) => cell.cell_type === "code").length;

  return {
    totalCells: cells.length,
    markdownCells,
    codeCells,
  };
}

function extractNotebookOutline(notebook) {
  const cells = Array.isArray(notebook?.cells) ? notebook.cells : [];

  return cells.map((cell, index) => {
    const source = Array.isArray(cell.source) ? cell.source.join("") : String(cell.source || "");
    const headingMatch = source.match(/^#{1,6}\s+(.+)$/m);
    const firstLine = source
      .split(/\r?\n/)
      .map((line) => line.trim())
      .find(Boolean);
    const fallbackLabel = cell.cell_type === "code" ? `Code cell ${index + 1}` : `Markdown cell ${index + 1}`;
    const label = (headingMatch?.[1] || firstLine || fallbackLabel).replace(/\s+/g, " ");

    return {
      id: `notebook-cell-${index + 1}`,
      label: label.length > 80 ? `${label.slice(0, 77)}...` : label,
      type: cell.cell_type === "code" ? "Code" : "Markdown",
      index: index + 1,
    };
  });
}

function App() {
  const { data, error } = useCurriculum();
  const [progress, setProgress] = useState(loadProgress);
  const [authStatus, setAuthStatus] = useState("disabled");
  const [authUser, setAuthUser] = useState(null);
  const [syncStatus, setSyncStatus] = useState("local");
  const [syncMessage, setSyncMessage] = useState("Cloud sync is disabled in this build.");
  const supabase = useMemo(() => getSupabaseClient(), []);
  const remoteSyncEnabled = Boolean(supabase);
  const progressRef = useRef(progress);
  const skipNextCloudWriteRef = useRef(false);
  const cloudReadyRef = useRef(false);

  useEffect(() => {
    progressRef.current = progress;
  }, [progress]);

  useEffect(() => {
    saveProgress(progress);
  }, [progress]);

  useEffect(() => {
    if (!supabase) {
      setAuthStatus("disabled");
      setSyncStatus("local");
      setSyncMessage("Cloud sync is disabled in this build.");
      return;
    }

    let active = true;
    setAuthStatus("loading");

    supabase.auth.getSession().then(({ data: sessionData, error: sessionError }) => {
      if (!active) {
        return;
      }
      if (sessionError) {
        setAuthStatus("error");
        setSyncStatus("error");
        setSyncMessage(`Cloud auth error: ${sessionError.message}`);
        return;
      }
      const user = sessionData.session?.user ?? null;
      setAuthUser(user);
      setAuthStatus(user ? "signed_in" : "signed_out");
      setSyncStatus(user ? "syncing" : "local");
      setSyncMessage(
        user
          ? "Cloud account found. Syncing progress now..."
          : "Signed out. Progress still autosaves locally."
      );
    });

    const {
      data: { subscription },
    } = supabase.auth.onAuthStateChange((_event, session) => {
      const user = session?.user ?? null;
      setAuthUser(user);
      setAuthStatus(user ? "signed_in" : "signed_out");
      setSyncStatus(user ? "syncing" : "local");
      setSyncMessage(
        user
          ? "Signed in. Syncing progress now..."
          : "Signed out. Progress still autosaves locally."
      );
      cloudReadyRef.current = false;
      skipNextCloudWriteRef.current = false;
    });

    return () => {
      active = false;
      subscription.unsubscribe();
    };
  }, [supabase]);

  useEffect(() => {
    if (!supabase || !authUser) {
      return;
    }

    let cancelled = false;

    async function hydrateCloudProgress() {
      setSyncStatus("syncing");
      setSyncMessage("Loading cloud progress...");
      try {
        const localProgress = normalizeProgress(progressRef.current);
        const remoteProgress = await fetchRemoteProgress(supabase, authUser.id);
        const remoteHasData = hasProgressData(remoteProgress);
        const localHasData = hasProgressData(localProgress);
        let merged = localProgress;

        if (remoteHasData) {
          merged = mergeProgress(localProgress, remoteProgress);
          if (!cancelled) {
            skipNextCloudWriteRef.current = true;
            setProgress(merged);
          }
          await saveRemoteProgress(supabase, authUser.id, merged);
          if (!cancelled) {
            setSyncMessage("Cloud sync active. Local and remote progress merged successfully.");
          }
        } else if (localHasData) {
          await saveRemoteProgress(supabase, authUser.id, localProgress);
          if (!cancelled) {
            setSyncMessage("Cloud sync active. Existing local progress was uploaded.");
          }
        } else if (!cancelled) {
          setSyncMessage("Cloud sync active. Start editing lessons to create your first cloud save.");
        }

        if (!cancelled) {
          cloudReadyRef.current = true;
          setSyncStatus("ready");
        }
      } catch (cloudError) {
        if (!cancelled) {
          setSyncStatus("error");
          setSyncMessage(`Cloud sync failed: ${cloudError.message}`);
        }
      }
    }

    hydrateCloudProgress();
    return () => {
      cancelled = true;
    };
  }, [supabase, authUser]);

  useEffect(() => {
    if (!supabase || !authUser || !cloudReadyRef.current) {
      return;
    }

    if (skipNextCloudWriteRef.current) {
      skipNextCloudWriteRef.current = false;
      return;
    }

    const timeoutId = window.setTimeout(async () => {
      try {
        setSyncStatus("syncing");
        await saveRemoteProgress(supabase, authUser.id, progressRef.current);
        setSyncStatus("ready");
        setSyncMessage(`Cloud sync active. Last cloud save: ${new Date().toLocaleTimeString()}.`);
      } catch (cloudError) {
        setSyncStatus("error");
        setSyncMessage(`Cloud sync failed: ${cloudError.message}`);
      }
    }, 700);

    return () => {
      window.clearTimeout(timeoutId);
    };
  }, [progress, supabase, authUser]);

  async function handleSignUp(email, password) {
    if (!supabase) {
      throw new Error("Cloud sync is not configured.");
    }
    setSyncStatus("syncing");
    setSyncMessage("Creating your account...");
    await signUpWithEmail(supabase, email, password);
    setSyncStatus("ready");
    setSyncMessage("Account created. Check your inbox if email confirmation is enabled.");
  }

  async function handleSignIn(email, password) {
    if (!supabase) {
      throw new Error("Cloud sync is not configured.");
    }
    setSyncStatus("syncing");
    setSyncMessage("Signing in...");
    await signInWithEmail(supabase, email, password);
  }

  async function handleSignOut() {
    if (!supabase) {
      return;
    }
    await signOutUser(supabase);
  }

  const roadmap = data?.roadmap ?? [];
  const fullTrackReady =
    roadmap.length === 24
    && roadmap.every((week) => week.daily_schedule.every((day) => day.lesson_markdown_path && day.lesson_pdf_path && day.notebook_path));

  if (error) {
    return <div className="shell"><p className="error-card">{error}</p></div>;
  }

  if (!data) {
    return <div className="shell"><p className="loading-card">Loading your learning system...</p></div>;
  }

  return (
    <div className="shell">
      <Sidebar roadmap={roadmap} progress={progress} />
      <main className="content">
        <Hero data={data} roadmap={roadmap} progress={progress} fullTrackReady={fullTrackReady} />
        <Routes>
          <Route
            path="/"
            element={(
              <Overview
                data={data}
                roadmap={roadmap}
                progress={progress}
                setProgress={setProgress}
                remoteSync={{
                  enabled: remoteSyncEnabled,
                  authStatus,
                  userEmail: authUser?.email || "",
                  syncStatus,
                  syncMessage,
                  onSignIn: handleSignIn,
                  onSignOut: handleSignOut,
                  onSignUp: handleSignUp,
                }}
              />
            )}
          />
          <Route path="/week/:weekNumber" element={<WeekPage roadmap={roadmap} progress={progress} setProgress={setProgress} />} />
          <Route
            path="/week/:weekNumber/day/:dayIndex"
            element={(
              <DayPage
                roadmap={roadmap}
                progress={progress}
                setProgress={setProgress}
                remoteSync={{ enabled: remoteSyncEnabled, syncStatus }}
              />
            )}
          />
          <Route path="/notebook/:encodedPath" element={<NotebookPage roadmap={roadmap} />} />
        </Routes>
      </main>
    </div>
  );
}

function Sidebar({ roadmap, progress }) {
  return (
    <aside className="sidebar">
      <div className="brand-block">
        <div className="brand-kicker">Quant Learning</div>
        <h1>Quant Sprint Studio</h1>
        <p>Six-month execution system with daily theory, code, and interview drills.</p>
      </div>
      <nav className="week-nav">
        <NavLink to="/" className="nav-home">
          Dashboard
        </NavLink>
        {Array.from({ length: 6 }, (_, i) => i + 1).map((month) => {
          const weeks = roadmap.filter((item) => Math.ceil(item.week / 4) === month);
          return (
            <div key={month} className="month-group">
              <div className="month-label">{`Month ${month}`}</div>
              {weeks.map((week) => {
                const complete = week.daily_schedule.filter((day) => {
                  const key = dayKey(week.week, day.day_index);
                  return progress.days?.[key]?.status === "done";
                }).length;
                return (
                  <NavLink key={week.week} to={`/week/${week.week}`} className="week-link">
                    <span>{`Week ${week.week}`}</span>
                    <small>{`${complete}/${week.daily_schedule.length}`}</small>
                  </NavLink>
                );
              })}
            </div>
          );
        })}
      </nav>
    </aside>
  );
}

function Hero({ data, roadmap, progress, fullTrackReady }) {
  const totalDays = roadmap.reduce((acc, week) => acc + week.daily_schedule.length, 0);
  const completedDays = Object.values(progress.days ?? {}).filter((item) => item.status === "done").length;

  return (
    <section className="hero">
      <div>
        <div className="hero-chip">2026 Fresh Build</div>
        <h2>Train like a quant desk, not a passive course.</h2>
        <p>
          The full 24-week roadmap now runs as a true 6-hour daily loop: concept brief, formula intuition,
          executable notebook work, practical lab blocks, and interview-style quiz checkpoints. Every week
          ships with a clear project direction so your portfolio compounds while you study.
        </p>
      </div>
      <div className="hero-stats">
        <StatCard label="Completed days" value={`${completedDays}/${totalDays}`} />
        <StatCard label="Weekday budget" value={data.weekly_time_budget["Mon-Fri"]} />
        <StatCard label="Weekend budget" value={`${data.weekly_time_budget.Sat} + ${data.weekly_time_budget.Sun}`} />
        <StatCard label="24-week detail" value={fullTrackReady ? "Ready" : "In progress"} />
      </div>
    </section>
  );
}

function StatCard({ label, value }) {
  return (
    <div className="stat-card">
      <span>{label}</span>
      <strong>{value}</strong>
    </div>
  );
}

function Overview({ data, roadmap, progress, setProgress, remoteSync }) {
  const navigate = useNavigate();
  const monthOneWeeks = roadmap.filter((week) => week.week <= 4);
  const weeksByMonth = useMemo(() => {
    const grouped = new Map();
    roadmap.forEach((week) => {
      const key = monthLabel(week.week);
      if (!grouped.has(key)) grouped.set(key, []);
      grouped.get(key).push(week);
    });
    return grouped;
  }, [roadmap]);

  function exportProgress() {
    const blob = new Blob([JSON.stringify(progress, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = "quant-learning-progress.json";
    link.click();
    URL.revokeObjectURL(url);
  }

  function importProgress(event) {
    const file = event.target.files?.[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = () => {
      try {
        const parsed = JSON.parse(String(reader.result));
        setProgress(parsed);
      } catch {
        window.alert("Could not import progress JSON.");
      }
    };
    reader.readAsText(file);
  }

  return (
    <div className="page-grid">
      <section className="panel">
        <div className="panel-head">
          <h3>Execution Launchpad</h3>
          <button className="primary-button" onClick={() => navigate("/week/1")}>
            Start Week 1
          </button>
        </div>
        <p className="panel-copy">
          Weeks 1-4 are highlighted here as the fastest starting path. The full six-month track now includes daily
          lesson files, weekly plans, and notebook artifacts through Week 24.
        </p>
        <div className="week-card-grid">
          {monthOneWeeks.map((week) => (
            <WeekSummaryCard key={week.week} week={week} progress={progress} />
          ))}
        </div>
      </section>

      <section className="panel">
        <div className="panel-head">
          <h3>Progress Tools</h3>
        </div>
        <div className="button-row">
          <button className="secondary-button" onClick={exportProgress}>
            Export Progress JSON
          </button>
          <label className="secondary-button file-label">
            Import Progress
            <input type="file" accept="application/json" onChange={importProgress} />
          </label>
          <a className="secondary-button" href={withBase("curriculum/pdfs/24-week-roadmap.pdf")} target="_blank" rel="noreferrer">
            Open Roadmap PDF
          </a>
        </div>
        <p className="panel-copy">
          Progress always autosaves in your browser. Cloud sync is optional and can keep progress consistent across signed-in devices.
        </p>
      </section>

      <CloudSyncPanel remoteSync={remoteSync} />

      <section className="panel span-2">
        <div className="panel-head">
          <h3>24-Week Path</h3>
        </div>
        <div className="month-stack">
          {[...weeksByMonth.entries()].map(([month, weeks]) => (
            <div key={month} className="month-panel">
              <div className="month-panel-head">
                <strong>{month}</strong>
                <span>{weeks[0].dates} to {weeks[weeks.length - 1].dates}</span>
              </div>
              <div className="roadmap-lines">
                {weeks.map((week) => (
                  <Link key={week.week} to={`/week/${week.week}`} className="roadmap-line">
                    <span>{`Week ${week.week}`}</span>
                    <b>{week.title}</b>
                    <small>{week.checkpoint}</small>
                  </Link>
                ))}
              </div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}

function CloudSyncPanel({ remoteSync }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [formError, setFormError] = useState("");

  async function submit(handler) {
    setFormError("");
    try {
      await handler(email.trim(), password);
      setPassword("");
    } catch (err) {
      setFormError(err.message || "Cloud auth request failed.");
    }
  }

  if (!remoteSync.enabled) {
    return (
      <section className="panel">
        <div className="panel-head">
          <h3>Cloud Sync (Optional)</h3>
        </div>
        <p className="panel-copy">
          Cloud sync is disabled. Add VITE_SUPABASE_URL and VITE_SUPABASE_ANON_KEY in site/.env.local, or set
          site/public/runtime-config.js for static hosting, to enable cross-device progress persistence.
        </p>
      </section>
    );
  }

  return (
    <section className="panel">
      <div className="panel-head">
        <h3>Cloud Sync</h3>
      </div>
      <p className="panel-copy">{remoteSync.syncMessage}</p>
      {remoteSync.authStatus === "signed_in" ? (
        <div className="cloud-sync-stack">
          <p className="panel-copy">Signed in as {remoteSync.userEmail || "your account"}.</p>
          <div className="button-row">
            <button className="secondary-button" onClick={remoteSync.onSignOut}>
              Sign Out
            </button>
          </div>
        </div>
      ) : (
        <div className="cloud-sync-stack">
          <label>
            Email
            <input
              className="cloud-input"
              type="email"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
              placeholder="you@example.com"
            />
          </label>
          <label>
            Password
            <input
              className="cloud-input"
              type="password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
              placeholder="At least 6 characters"
            />
          </label>
          <div className="button-row">
            <button
              className="primary-button"
              onClick={() => submit(remoteSync.onSignIn)}
              disabled={remoteSync.authStatus === "loading" || remoteSync.syncStatus === "syncing"}
            >
              Sign In
            </button>
            <button
              className="secondary-button"
              onClick={() => submit(remoteSync.onSignUp)}
              disabled={remoteSync.authStatus === "loading" || remoteSync.syncStatus === "syncing"}
            >
              Create Account
            </button>
          </div>
          {formError ? <p className="error-inline">{formError}</p> : null}
        </div>
      )}
    </section>
  );
}

function WeekSummaryCard({ week, progress }) {
  const done = week.daily_schedule.filter((day) => {
    const key = dayKey(week.week, day.day_index);
    return progress.days?.[key]?.status === "done";
  }).length;

  return (
    <Link to={`/week/${week.week}`} className="week-summary-card">
      <div className="week-summary-top">
        <span>{`Week ${week.week}`}</span>
        <small>{`${done}/${week.daily_schedule.length} done`}</small>
      </div>
      <strong>{week.title}</strong>
      <p>{week.dates}</p>
    </Link>
  );
}

function WeekPage({ roadmap, progress, setProgress }) {
  const { weekNumber } = useParams();
  const week = roadmap.find((item) => item.week === Number(weekNumber));

  if (!week) return <div className="panel"><p>Week not found.</p></div>;

  return (
    <div className="page-grid">
      <section className="panel span-2">
        <div className="panel-head">
          <div>
            <span className="eyebrow">{week.dates}</span>
            <h3>{`Week ${week.week}: ${week.title}`}</h3>
          </div>
          <div className="button-row">
            <a className="secondary-button" href={withBase(week.weekly_plan_pdf_path)} target="_blank" rel="noreferrer">
              Weekly PDF
            </a>
            {week.weekly_project_notebook_path ? (
              <>
                <Link className="secondary-button" to={withNotebookViewer(week.weekly_project_notebook_path)}>
                  Project Notebook
                </Link>
                <a className="secondary-button" href={withVSCodeWeb(week.weekly_project_notebook_path)} target="_blank" rel="noreferrer">
                  Open in VS Code
                </a>
                <a className="secondary-button" href={withGitHubBlob(week.weekly_project_notebook_path)} target="_blank" rel="noreferrer">
                  Open in GitHub
                </a>
              </>
            ) : null}
          </div>
        </div>

        <div className="week-meta-grid">
          <PanelList title="Objectives" items={week.objectives} />
          <PanelList title="Practice Tasks" items={week.practice_tasks} />
        </div>

        <div className="week-meta-grid">
          <div className="sub-panel">
            <h4>Checkpoint</h4>
            <p>{week.checkpoint}</p>
          </div>
          <div className="sub-panel">
            <h4>Weekend Project</h4>
            <p>{week.weekend_project}</p>
          </div>
          <div className="sub-panel">
            <h4>Admissions Track</h4>
            <p>{week.admissions_track}</p>
          </div>
          <div className="sub-panel">
            <h4>Interview Track</h4>
            <p>{week.interview_track}</p>
          </div>
        </div>
      </section>

      <section className="panel span-2">
        <div className="panel-head">
          <h3>Daily Path</h3>
        </div>
        <div className="day-card-grid">
          {week.daily_schedule.map((day) => {
            const key = dayKey(week.week, day.day_index);
            const saved = progress.days?.[key] ?? {};
            return (
              <div key={key} className="day-card">
                <div className="day-card-top">
                  <span>{`${day.day} · ${day.estimated_time}`}</span>
                  <StatusPill status={saved.status || "not_started"} />
                </div>
                <strong>{day.topic}</strong>
                <p>{day.why}</p>
                <div className="button-row compact">
                  {day.lesson_markdown_path ? (
                    <Link className="primary-button compact" to={`/week/${week.week}/day/${day.day_index}`}>
                      Open Day
                    </Link>
                  ) : (
                    <span className="secondary-button compact disabled-button">
                      Detail coming
                    </span>
                  )}
                  {day.lesson_pdf_path ? (
                    <a className="secondary-button compact" href={withBase(day.lesson_pdf_path)} target="_blank" rel="noreferrer">
                      PDF
                    </a>
                  ) : null}
                  {day.notebook_path ? (
                    <Link className="secondary-button compact" to={withNotebookViewer(day.notebook_path)}>
                      Notebook
                    </Link>
                  ) : null}
                </div>
              </div>
            );
          })}
        </div>
      </section>

      <section className="panel span-2">
        <div className="panel-head">
          <h3>Interview Questions</h3>
        </div>
        <div className="qa-stack">
          {week.interview_questions.map((item) => (
            <div key={item.question} className="qa-card">
              <strong>{item.question}</strong>
              <p>{item.answer}</p>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}

function DayPage({ roadmap, progress, setProgress, remoteSync }) {
  const { weekNumber, dayIndex } = useParams();
  const location = useLocation();
  const week = roadmap.find((item) => item.week === Number(weekNumber));
  const day = week?.daily_schedule.find((item) => item.day_index === Number(dayIndex));

  const key = week && day ? dayKey(week.week, day.day_index) : "";
  const saved = key ? progress.days?.[key] ?? { status: "not_started", confidence: 0, notes: "" } : null;
  const { content, status } = useMarkdown(day?.lesson_markdown_path);
  const previousDay = week?.daily_schedule.find((item) => item.day_index === Number(dayIndex) - 1);
  const nextDay = week?.daily_schedule.find((item) => item.day_index === Number(dayIndex) + 1);

  if (!week || !day || !saved) return <div className="panel"><p>Lesson not found.</p></div>;
  const detailedDayAvailable = Boolean(day.lesson_markdown_path);

  function updateDay(patch) {
    const next = {
      ...progress,
      days: {
        ...(progress.days ?? {}),
        [key]: {
          ...saved,
          ...patch,
          updatedAt: new Date().toISOString(),
        },
      },
    };
    setProgress(next);
  }

  return (
    <div className="page-grid day-layout">
      <section className="panel lesson-side">
        <div className="panel-head">
          <div>
            <span className="eyebrow">{location.pathname.replace("/week/", "Week ").replace("/day/", " · Day ")}</span>
            <h3>{day.topic}</h3>
          </div>
          <StatusPill status={saved.status || "not_started"} />
        </div>

        <div className="day-nav-row">
          <Link className="secondary-button compact" to="/">
            Back to Dashboard
          </Link>
          <Link className="secondary-button compact" to={`/week/${week.week}`}>
            Back to Week {week.week}
          </Link>
          {previousDay ? (
            <Link className="secondary-button compact" to={`/week/${week.week}/day/${previousDay.day_index}`}>
              Previous Day
            </Link>
          ) : null}
          {nextDay ? (
            <Link className="secondary-button compact" to={`/week/${week.week}/day/${nextDay.day_index}`}>
              Next Day
            </Link>
          ) : null}
        </div>

        <div className="week-meta-grid">
          <div className="sub-panel">
            <h4>Study Controls</h4>
            <div className="control-stack">
              <label>
                Status
                <select value={saved.status || "not_started"} onChange={(e) => updateDay({ status: e.target.value })}>
                  <option value="not_started">Not started</option>
                  <option value="in_progress">In progress</option>
                  <option value="done">Done</option>
                </select>
              </label>

              <label>
                Confidence: {saved.confidence || 0}/5
                <input
                  type="range"
                  min="0"
                  max="5"
                  step="1"
                  value={saved.confidence || 0}
                  onChange={(e) => updateDay({ confidence: Number(e.target.value) })}
                />
              </label>

              <label>
                Notes
                <textarea
                  rows="8"
                  value={saved.notes || ""}
                  onChange={(e) => updateDay({ notes: e.target.value })}
                  placeholder="Write what clicked, what was confusing, and what to review later."
                />
              </label>
              <p className="panel-copy">
                Progress autosaves locally. {saved.updatedAt ? `Last saved: ${new Date(saved.updatedAt).toLocaleString()}` : "Update any field to create the first save point."}
              </p>
              {remoteSync?.enabled ? (
                <p className="panel-copy">
                  Cloud sync status: {remoteSync.syncStatus === "ready" ? "Connected" : remoteSync.syncStatus}
                </p>
              ) : null}
            </div>
          </div>

          <div className="sub-panel">
            <h4>Daily Study Actions</h4>
            <p className="panel-copy">
              Use these actions in order: read the lesson, review the theory PDF, answer the quiz, work through the notebook, then review additional references.
            </p>
            <div className="daily-action-grid">
              {detailedDayAvailable ? (
                <>
                  <a className="secondary-button" href="#daily-content">
                    Read Daily Content
                  </a>
                  <a className="secondary-button" href={withBase(day.lesson_pdf_path)} target="_blank" rel="noreferrer">
                    Open Theory PDF
                  </a>
                  {day.quiz_markdown_path || day.quiz_pdf_path ? (
                    <a
                      className="secondary-button"
                      href={withBase(day.quiz_markdown_path || day.quiz_pdf_path)}
                      target="_blank"
                      rel="noreferrer"
                    >
                      Open Daily Quiz
                    </a>
                  ) : (
                    <span className="secondary-button disabled-button">Daily Quiz Unavailable</span>
                  )}
                  <Link className="secondary-button" to={withNotebookViewer(day.notebook_path)}>
                    Open Daily Notebook
                  </Link>
                  <a className="secondary-button" href={withVSCodeWeb(day.notebook_path)} target="_blank" rel="noreferrer">
                    Open Notebook in VS Code
                  </a>
                  <a className="secondary-button" href={withGitHubBlob(day.notebook_path)} target="_blank" rel="noreferrer">
                    Open Notebook in GitHub
                  </a>
                  <a className="secondary-button" href={withAdditionalReading(week.week)} target="_blank" rel="noreferrer">
                    Additional Reading
                  </a>
                </>
              ) : (
                <span className="secondary-button disabled-button">Detailed daily lesson coming next phase</span>
              )}
            </div>
          </div>

          <div className="sub-panel">
            <h4>Day Navigation</h4>
            <div className="day-links">
              {week.daily_schedule.map((item) => (
                <Link key={item.day_index} to={`/week/${week.week}/day/${item.day_index}`} className={`day-jump ${item.day_index === day.day_index ? "active" : ""}`}>
                  {item.day}
                </Link>
              ))}
            </div>
          </div>
        </div>
      </section>

      <section id="daily-content" className="panel lesson-main">
        {!detailedDayAvailable ? (
          <div className="sub-panel">
            <h4>Daily Lesson File Missing</h4>
            <p>
              The day path exists in the roadmap but the corresponding lesson file could not be loaded. Re-run the
              bootstrap and export commands to regenerate content.
            </p>
          </div>
        ) : null}
        {status === "loading" ? <p>Loading lesson content...</p> : null}
        {status === "error" ? <p>Could not load this lesson file.</p> : null}
        {status === "ready" ? (
          <div className="markdown-shell">
            <ReactMarkdown remarkPlugins={[remarkGfm, remarkMath]} rehypePlugins={[rehypeKatex]}>{content}</ReactMarkdown>
          </div>
        ) : null}
      </section>
    </div>
  );
}

function PanelList({ title, items }) {
  return (
    <div className="sub-panel">
      <h4>{title}</h4>
      <ul className="clean-list">
        {items.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </div>
  );
}

function StatusPill({ status }) {
  return <span className={`status-pill ${status}`}>{status.replace("_", " ")}</span>;
}

function NotebookPage({ roadmap }) {
  const { encodedPath } = useParams();
  const decodedPath = encodedPath ? decodeURIComponent(encodedPath) : "";
  const { notebook, status, error } = useNotebook(decodedPath);
  const notebookSummary = useMemo(() => summarizeNotebook(notebook), [notebook]);
  const notebookOutline = useMemo(() => extractNotebookOutline(notebook), [notebook]);

  const relatedWeek = roadmap.find((week) =>
    week.daily_schedule.some((day) => day.notebook_path === decodedPath) ||
    week.weekly_project_notebook_path === decodedPath ||
    week.weekly_overview_notebook_path === decodedPath
  );

  return (
    <div className="page-grid">
      <section className="panel span-2 notebook-panel">
        <div className="panel-head">
          <div>
            <span className="eyebrow">Notebook Viewer</span>
            <h3>{decodedPath || "Notebook"}</h3>
          </div>
          <div className="button-row">
            <a className="secondary-button" href={withBase(decodedPath)} target="_blank" rel="noreferrer">
              Download .ipynb
            </a>
            <a className="secondary-button" href={withVSCodeWeb(decodedPath)} target="_blank" rel="noreferrer">
              Open in VS Code
            </a>
            <a className="secondary-button" href={withGitHubBlob(decodedPath)} target="_blank" rel="noreferrer">
              Open in GitHub
            </a>
            <Link className="secondary-button" to="/">
              Dashboard
            </Link>
            {relatedWeek ? (
              <Link className="secondary-button" to={`/week/${relatedWeek.week}`}>
                Back to Week {relatedWeek.week}
              </Link>
            ) : null}
          </div>
        </div>

        {relatedWeek ? (
          <p className="panel-copy">
            Week {relatedWeek.week}: Theory is in day lessons, notebook practice is here, revision and quiz prompts are in lesson sections, and weekly mini-project/capstone is linked from the week/day pages.
          </p>
        ) : null}
        <p className="panel-copy">Use this viewer for study flow, then open in VS Code when you want to edit the notebook directly.</p>

        {status === "ready" ? (
          <div className="week-meta-grid notebook-meta-grid">
            <div className="sub-panel">
              <h4>Notebook Summary</h4>
              <p>{`${notebookSummary.totalCells} cells · ${notebookSummary.markdownCells} markdown · ${notebookSummary.codeCells} code`}</p>
            </div>
            <div className="sub-panel">
              <h4>Study Flow</h4>
              <p>The outline below helps you move through theory, formulas, real-data checks, and project notes in order.</p>
            </div>
          </div>
        ) : null}

        {status === "ready" && notebookOutline.length > 0 ? (
          <div className="sub-panel notebook-outline">
            <h4>Notebook Map</h4>
            <div className="notebook-outline-list">
              {notebookOutline.map((item) => (
                <a key={item.id} href={`#${item.id}`} className="notebook-outline-item">
                  <span>{`Cell ${item.index}`}</span>
                  <strong>{item.label}</strong>
                  <small>{item.type}</small>
                </a>
              ))}
            </div>
          </div>
        ) : null}

        {status === "loading" ? <p>Loading notebook...</p> : null}
        {status === "error" ? <p>Could not load notebook. {error}</p> : null}
        {status === "ready" && Array.isArray(notebook?.cells) ? (
          <div className="notebook-cells">
            {notebook.cells.map((cell, index) => (
              <article id={`notebook-cell-${index + 1}`} key={`${index}-${cell.cell_type || "cell"}`} className="notebook-cell">
                <div className="notebook-cell-head">
                  <strong>Cell {index + 1}</strong>
                  <span>{cell.cell_type === "code" ? "Code" : "Markdown"}</span>
                </div>
                {cell.cell_type === "markdown" ? (
                  <div className="markdown-shell">
                    <ReactMarkdown
                      remarkPlugins={[remarkGfm, remarkMath]}
                      rehypePlugins={[rehypeKatex]}
                    >
                      {Array.isArray(cell.source) ? cell.source.join("") : String(cell.source || "")}
                    </ReactMarkdown>
                  </div>
                ) : (
                  <pre className="notebook-code"><code>{Array.isArray(cell.source) ? cell.source.join("") : String(cell.source || "")}</code></pre>
                )}
              </article>
            ))}
          </div>
        ) : null}
      </section>
    </div>
  );
}

export default App;
