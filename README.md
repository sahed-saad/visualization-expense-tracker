# Visualization Expense Tracker

> Lightweight Streamlit app to track and visualize personal expenses with simple auto-categorization.

## Features
- Add expenses (date, description, category, amount).
- Auto-predicts a category from the description via `processor.py` (LLM).
- Shows a table and category breakdown (bar and pie charts).

## Files
- `app.py` — Streamlit UI and charting logic.
- `processor.py` — Calls an LLM to auto-categorize descriptions.
- `expense.csv` — Local CSV datastore for transactions (created/updated by the app).
- `requirements.txt` — Python dependencies.
- `src/logo.svg` — Optional logo shown in the app header.

## Requirements
- Python 3.10+ (recommended)
- See `requirements.txt` and install with pip:

```bash
pip install -r requirements.txt
```

## Run locally
1. (Optional) Provide an API key for the categorizer LLM. `processor.py` expects a key named `GEMINI_KEY` in its current code; either:
   - Export `GEMINI_KEY` in your shell, or
   - Edit `processor.py` to load the key from `os.environ`/a secret manager.

2. Start the app:

```bash
streamlit run app.py
```

You can add the flags you used previously if needed:

```bash
streamlit run app.py --server.enableCORS false --server.enableXsrfProtection false
```

## Notes
- The app stores all entries in `expense.csv` in the project root. Back this up if needed.
- `processor.py` uses an LLM (via an OpenAI-style client) and falls back to `Other` on errors.
- A `container` folder is not required to run locally; it may be created by deployment/CI tooling.

## Next steps (optional)
- Replace the hard-coded API key in `processor.py` with `os.getenv('GEMINI_KEY')`.
- Add a .gitignore entry for `expense.csv` if you don't want data checked into git.

---
Generated from repository files: `app.py`, `processor.py`, `requirements.txt`.
