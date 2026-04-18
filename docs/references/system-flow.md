# System Flow

1. Open the roadmap and select the current week.
2. Read the weekly PDF and daily markdown lessons.
3. Work through the weekly notebook and daily coding task.
4. Update progress in the Streamlit dashboard.
5. Save weak spots into the error log with a scheduled review date.
6. Complete the weekly review every Sunday.
7. Complete the monthly assessment after every capstone week.
8. Use the admissions and interview tracks in parallel so technical growth becomes application evidence.

Persistence model:

- The app writes to `data/progress.db`.
- Closing the browser or stopping Streamlit does not erase progress.
- Reopening the app restores saved progress, reviews, and error logs from SQLite.
