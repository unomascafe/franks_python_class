"""
tracker.py — Frank's Python Class progress tracker

Usage:
  python tracker.py              # show progress dashboard
  python tracker.py done 5       # mark lesson 5 complete
  python tracker.py undone 5     # unmark lesson 5
  python tracker.py note 5 "finished the stretch exercise too"
  python tracker.py next         # show next lesson to work on
  python tracker.py reset        # clear all progress (asks for confirmation)
"""

import json
import sys
from datetime import date
from pathlib import Path

# ── Course definition ────────────────────────────────────────────────────────

LESSONS = {
    1:  ("Module 1", "Setup & Your First Script"),
    2:  ("Module 1", "Variables & Data Types"),
    3:  ("Module 1", "Strings"),
    4:  ("Module 1", "Numbers & Math"),
    5:  ("Module 1", "Lists"),
    6:  ("Module 1", "Dictionaries"),
    7:  ("Module 1", "Conditionals"),
    8:  ("Module 1", "Loops"),
    9:  ("Module 1", "Functions"),
    10: ("Module 1", "Error Handling"),
    11: ("Module 2", "Reading & Writing Files"),
    12: ("Module 2", "CSV & JSON"),
    13: ("Module 2", "Installing & Using Libraries"),
    14: ("Module 2", "Dates & Times"),
    15: ("Module 3", "File System Operations"),
    16: ("Module 3", "Running Shell Commands"),
    17: ("Module 3", "HTTP Requests & APIs"),
    18: ("Module 3", "Web Scraping"),
    19: ("Module 3", "Automation Scripts"),
    20: ("Module 4", "Pandas: DataFrames"),
    21: ("Module 4", "Cleaning & Transforming Data"),
    22: ("Module 4", "Visualizations"),
    23: ("Module 4", "Excel & Spreadsheets"),
    24: ("Module 5", "Command-Line Tools"),
    25: ("Module 5", "Simple Web Apps with Flask"),
    26: ("Module 5", "Building & Consuming APIs"),
    27: ("Module 5", "Databases with SQLite"),
    28: ("Module 6", "Working with AI APIs"),
    29: ("Module 6", "Building AI-Powered Tools"),
    30: ("Module 6", "Intro to Machine Learning"),
}

MODULES = {
    "Module 1": "Python Foundations",
    "Module 2": "Working with Files & Data",
    "Module 3": "Automation",
    "Module 4": "Data & Analysis",
    "Module 5": "Building Apps & Tools",
    "Module 6": "AI & Machine Learning",
}

PROGRESS_FILE = Path(__file__).parent / "progress.json"

# ── Progress I/O ─────────────────────────────────────────────────────────────

def load_progress():
    if not PROGRESS_FILE.exists():
        return {"completed": [], "notes": {}, "started": None, "last_updated": None}
    with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    # Ensure all expected keys exist (handles older progress files)
    data.setdefault("completed", [])
    data.setdefault("notes", {})
    data.setdefault("started", None)
    data.setdefault("last_updated", None)
    return data


def save_progress(data):
    data["last_updated"] = str(date.today())
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# ── Display helpers ──────────────────────────────────────────────────────────

def bar(completed, total, width=20):
    filled = int(width * completed / total) if total else 0
    return "█" * filled + "░" * (width - filled)


def print_dashboard():
    data = load_progress()
    completed = set(data["completed"])
    total = len(LESSONS)
    done = len(completed)
    pct = int(100 * done / total)

    print()
    print("  ┌─────────────────────────────────────────┐")
    print("  │       Frank's Python Class Progress      │")
    print("  └─────────────────────────────────────────┘")
    print()
    print(f"  Overall  [{bar(done, total)}]  {done}/{total} lessons  ({pct}%)")
    if data["started"]:
        print(f"  Started: {data['started']}   Last updated: {data['last_updated'] or 'never'}")
    print()

    current_module = None
    for num, (module, title) in LESSONS.items():
        if module != current_module:
            current_module = module
            mod_lessons = [n for n, (m, _) in LESSONS.items() if m == module]
            mod_done = len([n for n in mod_lessons if n in completed])
            mod_total = len(mod_lessons)
            print(f"  {module}: {MODULES[module]}")
            print(f"  [{bar(mod_done, mod_total, width=12)}] {mod_done}/{mod_total}")

        status = "✓" if num in completed else "○"
        note = f"  ← {data['notes'][str(num)]}" if str(num) in data["notes"] else ""
        print(f"    {status}  {num:02d}. {title}{note}")

    print()

    # Show next lesson
    next_lesson = next((n for n in sorted(LESSONS) if n not in completed), None)
    if next_lesson:
        _, title = LESSONS[next_lesson]
        print(f"  ▶  Next up: Lesson {next_lesson:02d} — {title}")
    else:
        print("  🎉  Course complete! You did it.")
    print()


# ── Commands ─────────────────────────────────────────────────────────────────

def cmd_done(lesson_num):
    if lesson_num not in LESSONS:
        print(f"  ✗  Lesson {lesson_num} doesn't exist (valid: 1–{len(LESSONS)})")
        return
    data = load_progress()
    if lesson_num in data["completed"]:
        print(f"  Lesson {lesson_num} is already marked done.")
        return
    if data["started"] is None:
        data["started"] = str(date.today())
    data["completed"].append(lesson_num)
    data["completed"].sort()
    save_progress(data)
    _, title = LESSONS[lesson_num]
    print(f"  ✓  Lesson {lesson_num:02d}: {title} — marked complete.")
    remaining = len(LESSONS) - len(data["completed"])
    if remaining == 0:
        print("  🎉  That's the whole course! Nicely done.")
    else:
        print(f"     {remaining} lessons to go.")


def cmd_undone(lesson_num):
    if lesson_num not in LESSONS:
        print(f"  ✗  Lesson {lesson_num} doesn't exist.")
        return
    data = load_progress()
    if lesson_num not in data["completed"]:
        print(f"  Lesson {lesson_num} wasn't marked done.")
        return
    data["completed"].remove(lesson_num)
    save_progress(data)
    _, title = LESSONS[lesson_num]
    print(f"  ○  Lesson {lesson_num:02d}: {title} — unmarked.")


def cmd_note(lesson_num, note_text):
    if lesson_num not in LESSONS:
        print(f"  ✗  Lesson {lesson_num} doesn't exist.")
        return
    data = load_progress()
    data["notes"][str(lesson_num)] = note_text
    save_progress(data)
    print(f"  📝  Note saved for Lesson {lesson_num:02d}.")


def cmd_next():
    data = load_progress()
    completed = set(data["completed"])
    next_lesson = next((n for n in sorted(LESSONS) if n not in completed), None)
    if next_lesson is None:
        print("  🎉  You've completed everything!")
    else:
        module, title = LESSONS[next_lesson]
        print(f"\n  ▶  Next up: Lesson {next_lesson:02d} — {title} ({module})\n")


def cmd_reset():
    confirm = input("  Reset ALL progress? This can't be undone. Type 'yes' to confirm: ")
    if confirm.strip().lower() == "yes":
        save_progress({"completed": [], "notes": {}, "started": None, "last_updated": None})
        print("  Progress reset.")
    else:
        print("  Cancelled.")


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]

    if not args:
        print_dashboard()
        return

    command = args[0].lower()

    if command == "done":
        if len(args) < 2:
            print("  Usage: python tracker.py done <lesson_number>")
            return
        try:
            cmd_done(int(args[1]))
        except ValueError:
            print(f"  ✗  '{args[1]}' isn't a valid lesson number.")

    elif command == "undone":
        if len(args) < 2:
            print("  Usage: python tracker.py undone <lesson_number>")
            return
        try:
            cmd_undone(int(args[1]))
        except ValueError:
            print(f"  ✗  '{args[1]}' isn't a valid lesson number.")

    elif command == "note":
        if len(args) < 3:
            print('  Usage: python tracker.py note <lesson_number> "your note here"')
            return
        try:
            cmd_note(int(args[1]), " ".join(args[2:]))
        except ValueError:
            print(f"  ✗  '{args[1]}' isn't a valid lesson number.")

    elif command == "next":
        cmd_next()

    elif command == "reset":
        cmd_reset()

    else:
        print(f"  ✗  Unknown command: '{command}'")
        print("  Commands: done, undone, note, next, reset")
        print("  Run 'python tracker.py' with no arguments for the dashboard.")


if __name__ == "__main__":
    main()
