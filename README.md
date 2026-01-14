# Visualization Expense Tracker

Lightweight Streamlit app to track and visualize personal expenses with simple auto-categorization.

## Features
- Add expenses (date, description, category, amount).
- Auto-predicts a category from the description via `processor.py`.
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
1. Use Gemini API key for the categorizer LLM. `processor.py` 

2. Start the app:

```bash
streamlit run app.py
```

## Notes
- The app stores all entries in `expense.csv` in the project root. Back this up if needed.
- `processor.py` uses an LLM (via an OpenAI-style client) and falls back to `Other` on errors.
- A `container` folder is not required to run locally; it is created by deployment tooling.

---
Generated from repository files: `app.py`, `processor.py`, `requirements.txt`.
