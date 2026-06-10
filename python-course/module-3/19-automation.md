# Lesson 19 — Automation Scripts

## What You'll Learn
- Combine everything from Module 3 into real automation scripts
- Work with environment variables and `.env` files
- Schedule scripts to run automatically
- Structure scripts for reusability

---

## Environment Variables

Never hardcode API keys or passwords in your code. Use environment variables instead:

```python
import os

api_key = os.environ.get("OPENAI_API_KEY")
db_url = os.environ.get("DATABASE_URL", "sqlite:///default.db")  # with fallback
```

Set them in your terminal:
```bash
# Windows
set OPENAI_API_KEY=sk-abc123

# Mac/Linux
export OPENAI_API_KEY=sk-abc123
```

---

## .env Files

For development, keep variables in a `.env` file and load them with `python-dotenv`:

```bash
pip install python-dotenv
```

`.env` file:
```
OPENAI_API_KEY=sk-abc123
DATABASE_URL=sqlite:///myapp.db
DEBUG=true
```

```python
from dotenv import load_dotenv
import os

load_dotenv()   # loads .env into os.environ

api_key = os.environ.get("OPENAI_API_KEY")
```

**Always add `.env` to your `.gitignore`.** Never commit secrets.

---

## Script Structure

A well-structured automation script:

```python
"""
report_generator.py

Fetches sales data from the API and generates a daily CSV report.
Run daily: python report_generator.py
"""

import os
import csv
import requests
from datetime import date
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("SALES_API_KEY")
OUTPUT_DIR = Path("reports")


def fetch_sales(date_str):
    """Fetch sales data for a given date."""
    response = requests.get(
        "https://api.example.com/sales",
        headers={"Authorization": f"Bearer {API_KEY}"},
        params={"date": date_str},
        timeout=30
    )
    response.raise_for_status()
    return response.json()


def save_report(data, filename):
    """Save sales data to a CSV file."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    path = OUTPUT_DIR / filename
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"Saved: {path}")


def main():
    today = str(date.today())
    print(f"Generating report for {today}...")
    
    sales = fetch_sales(today)
    filename = f"sales_{today}.csv"
    save_report(sales, filename)
    
    print(f"Done. {len(sales)} records written.")


if __name__ == "__main__":
    main()
```

The `if __name__ == "__main__":` guard means `main()` only runs when the script is called directly — not when it's imported by another script.

---

## Scheduling

### Windows Task Scheduler
Run your script on a schedule via Windows Task Scheduler (search for it in Start):
1. Create a new Basic Task
2. Set the trigger (daily, weekly, etc.)
3. Action: Start a program → `python` → Add argument: `C:\path\to\script.py`

### cron (Mac/Linux)
Edit the crontab with `crontab -e`:
```
# Run every day at 8am
0 8 * * * /usr/bin/python3 /home/frank/scripts/report.py

# Run every hour
0 * * * * /usr/bin/python3 /home/frank/scripts/check.py
```

### Simple: just run it manually
For most automation, a script you run when needed beats scheduled tasks that fail silently.

---

## Logging

Use `logging` instead of `print` for scripts that run unattended:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()   # also print to terminal
    ]
)

logging.info("Script started")
logging.warning("Rate limit approaching")
logging.error("Failed to fetch data: %s", error_msg)
```

---

## Exercises

**Exercise 1:** Build a file watcher script: given a folder path, print a message whenever a new file appears in it. Use a loop with `time.sleep(2)` and track which files you've already seen.

**Exercise 2:** Build a "daily briefing" script that:
- Fetches the current weather for Mesa, AZ (use the Open-Meteo API from Lesson 17)
- Gets a random "word of the day" from [https://random-word-api.herokuapp.com/word](https://random-word-api.herokuapp.com/word)
- Prints a formatted morning briefing

**Exercise 3:** Create a `.env` file with a variable `MY_NAME=Frank`. Write a script that loads it and prints `"Good morning, Frank!"`. Make sure `.env` is in your `.gitignore`.

**Exercise 4 (stretch):** Build a URL health-checker: given a list of URLs, check each one every 60 seconds and log to a file whenever one returns a non-200 status or times out.

---

## Key Takeaway
Environment variables keep secrets out of code. `.env` + `python-dotenv` is the dev standard — never commit `.env`. Structure scripts with a `main()` function and `if __name__ == "__main__"`. Use `logging` instead of `print` for anything that runs unattended.

**Next:** [Module 4 — Data & Analysis →](../module-4/20-pandas-basics.md)
