import { useEffect, useMemo, useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { Link, NavLink, Route, Routes, useLocation, useNavigate, useParams } from "react-router-dom";

const STORAGE_KEY = "quant-learning-progress-v2";

function withBase(path) {
  if (!path) return "";
  return `${import.meta.env.BASE_URL}${path}`.replace(/([^:]\/)\/+/g, "$1");
}

function loadProgress() {
  try {
    const raw = window.localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : { days: {}, weeklyReviews: {} };
  } catch {
    return { days: {}, weeklyReviews: {} };
  }
}

function saveProgress(progress) {
  window.localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
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

function App() {
  const { data, error } = useCurriculum();
  const [progress, setProgress] = useState(loadProgress);

  useEffect(() => {
    saveProgress(progress);
  }, [progress]);

  const roadmap = data?.roadmap ?? [];
  const monthOneComplete = roadmap.filter((week) => week.week <= 4).length === 4;

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
        <Hero data={data} roadmap={roadmap} progress={progress} monthOneComplete={monthOneComplete} />
        <Routes>
          <Route path="/" element={<Overview data={data} roadmap={roadmap} progress={progress} setProgress={setProgress} />} />
          <Route path="/week/:weekNumber" element={<WeekPage roadmap={roadmap} progress={progress} setProgress={setProgress} />} />
          <Route path="/week/:weekNumber/day/:dayIndex" element={<DayPage roadmap={roadmap} progress={progress} setProgress={setProgress} />} />
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
        <h1>Scholarship-to-Quant Roadmap</h1>
        <p>Hosted-ready study system with local progress memory.</p>
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

function Hero({ data, roadmap, progress, monthOneComplete }) {
  const totalDays = roadmap.reduce((acc, week) => acc + week.daily_schedule.length, 0);
  const completedDays = Object.values(progress.days ?? {}).filter((item) => item.status === "done").length;

  return (
    <section className="hero">
      <div>
        <div className="hero-chip">GitHub Pages Ready</div>
        <h2>Build a real quant profile, week by week.</h2>
        <p>
          Month 1 is fully expanded with daily theory, examples, executed notebooks, interview drills,
          revision blocks, and project notebooks. The rest of the 24-week path is visible in the roadmap
          and ready for the same treatment.
        </p>
      </div>
      <div className="hero-stats">
        <StatCard label="Completed days" value={`${completedDays}/${totalDays}`} />
        <StatCard label="Weekday budget" value={data.weekly_time_budget["Mon-Fri"]} />
        <StatCard label="Weekend budget" value={`${data.weekly_time_budget.Sat} + ${data.weekly_time_budget.Sun}`} />
        <StatCard label="Month 1 detail" value={monthOneComplete ? "Ready" : "In progress"} />
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

function Overview({ data, roadmap, progress, setProgress }) {
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
          <h3>Month 1 Execution</h3>
          <button className="primary-button" onClick={() => navigate("/week/1")}>
            Start Week 1
          </button>
        </div>
        <p className="panel-copy">
          Month 1 is the current fully detailed build. Every day from Weeks 1-4 has theory, worked examples,
          practice, an executed notebook, and interview prep. Weekends are structured for revision and project work.
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
          Progress is stored in your browser with localStorage, so your completion state remains when you close and reopen the site on the same device and browser.
        </p>
      </section>

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
            <a className="secondary-button" href={withBase(week.weekly_plan_markdown_path)} target="_blank" rel="noreferrer">
              Weekly Markdown
            </a>
            {week.weekly_project_notebook_path ? (
              <a className="secondary-button" href={withBase(week.weekly_project_notebook_path)} target="_blank" rel="noreferrer">
                Project Notebook
              </a>
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
                    <a className="secondary-button compact" href={withBase(day.notebook_path)} target="_blank" rel="noreferrer">
                      Notebook
                    </a>
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

function DayPage({ roadmap, progress, setProgress }) {
  const { weekNumber, dayIndex } = useParams();
  const location = useLocation();
  const week = roadmap.find((item) => item.week === Number(weekNumber));
  const day = week?.daily_schedule.find((item) => item.day_index === Number(dayIndex));

  const key = week && day ? dayKey(week.week, day.day_index) : "";
  const saved = key ? progress.days?.[key] ?? { status: "not_started", confidence: 0, notes: "" } : null;
  const { content, status } = useMarkdown(day?.lesson_markdown_path);

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
    <div className="page-grid">
      <section className="panel lesson-side">
        <div className="panel-head">
          <div>
            <span className="eyebrow">{location.pathname.replace("/week/", "Week ").replace("/day/", " · Day ")}</span>
            <h3>{day.topic}</h3>
          </div>
          <StatusPill status={saved.status || "not_started"} />
        </div>

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
        </div>

        <div className="resource-list">
          {detailedDayAvailable ? (
            <>
              <a className="secondary-button" href={withBase(day.lesson_markdown_path)} target="_blank" rel="noreferrer">
                Open Lesson Markdown
              </a>
              <a className="secondary-button" href={withBase(day.lesson_pdf_path)} target="_blank" rel="noreferrer">
                Open Lesson PDF
              </a>
              <a className="secondary-button" href={withBase(day.notebook_path)} target="_blank" rel="noreferrer">
                Open Notebook
              </a>
            </>
          ) : (
            <span className="secondary-button disabled-button">Detailed daily lesson coming next phase</span>
          )}
          <a className="secondary-button" href={withBase(week.weekly_plan_pdf_path)} target="_blank" rel="noreferrer">
            Open Weekly Plan PDF
          </a>
          {week.weekly_project_notebook_path ? (
            <a className="secondary-button" href={withBase(week.weekly_project_notebook_path)} target="_blank" rel="noreferrer">
              Open Weekly Project
            </a>
          ) : null}
        </div>

        <div className="day-links">
          {week.daily_schedule.map((item) => (
            <Link key={item.day_index} to={`/week/${week.week}/day/${item.day_index}`} className={`day-jump ${item.day_index === day.day_index ? "active" : ""}`}>
              {item.day}
            </Link>
          ))}
        </div>
      </section>

      <section className="panel lesson-main">
        {!detailedDayAvailable ? (
          <div className="sub-panel">
            <h4>Detailed Daily Build Pending</h4>
            <p>
              The weekly plan for this week is already available, but the fully expanded daily lesson, executed notebook,
              and inline theory page have not been generated yet. Month 1 is the current fully detailed build.
            </p>
          </div>
        ) : null}
        {status === "loading" ? <p>Loading lesson content...</p> : null}
        {status === "error" ? <p>Could not load this lesson file.</p> : null}
        {status === "ready" ? (
          <div className="markdown-shell">
            <ReactMarkdown remarkPlugins={[remarkGfm]}>{content}</ReactMarkdown>
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

export default App;
