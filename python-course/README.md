# Frank's Python Class

A practical, hands-on Python course built around what you actually want to do: automate things, build apps and tools, work with data, and build AI-powered projects.

**Format:** Each lesson has a short explanation, code examples, and one or more exercises. You write the code — that's the only way this sticks.

**Tools you'll need:**
- Python 3.11+ — [python.org/downloads](https://python.org/downloads)
- A code editor — [VS Code](https://code.visualstudio.com/) is recommended
- A terminal (Command Prompt, PowerShell, or the terminal inside VS Code)

---

## Course Map

### Module 1 — Python Foundations
*The core language. Everything else builds on this.*

| Lesson | Topic |
|--------|-------|
| [01](./module-1/01-setup.md) | Setup & Your First Script |
| [02](./module-1/02-variables-and-types.md) | Variables & Data Types |
| [03](./module-1/03-strings.md) | Strings |
| [04](./module-1/04-numbers.md) | Numbers & Math |
| [05](./module-1/05-lists.md) | Lists |
| [06](./module-1/06-dicts.md) | Dictionaries |
| [07](./module-1/07-conditionals.md) | Conditionals |
| [08](./module-1/08-loops.md) | Loops |
| [09](./module-1/09-functions.md) | Functions |
| [10](./module-1/10-errors.md) | Error Handling |

---

### Module 2 — Working with Files & Data
*Read, write, and move data around.*

| Lesson | Topic |
|--------|-------|
| [11](./module-2/11-file-io.md) | Reading & Writing Files |
| [12](./module-2/12-csv-json.md) | CSV & JSON |
| [13](./module-2/13-libraries.md) | Installing & Using Libraries |
| [14](./module-2/14-dates.md) | Dates & Times |

---

### Module 3 — Automation
*Make Python do repetitive things so you don't have to.*

| Lesson | Topic |
|--------|-------|
| [15](./module-3/15-filesystem.md) | File System Operations |
| [16](./module-3/16-shell.md) | Running Shell Commands |
| [17](./module-3/17-requests.md) | HTTP Requests & APIs |
| [18](./module-3/18-scraping.md) | Web Scraping |
| [19](./module-3/19-automation.md) | Putting It Together: Automation Scripts |

---

### Module 4 — Data & Analysis
*Work with data like a professional.*

| Lesson | Topic |
|--------|-------|
| [20](./module-4/20-pandas-basics.md) | Pandas: DataFrames |
| [21](./module-4/21-data-cleaning.md) | Cleaning & Transforming Data |
| [22](./module-4/22-visualization.md) | Visualizations |
| [23](./module-4/23-excel.md) | Excel & Spreadsheets |

---

### Module 5 — Building Apps & Tools
*Go from script to real software.*

| Lesson | Topic |
|--------|-------|
| [24](./module-5/24-cli-tools.md) | Command-Line Tools |
| [25](./module-5/25-flask.md) | Simple Web Apps with Flask |
| [26](./module-5/26-apis.md) | Building & Consuming APIs |
| [27](./module-5/27-databases.md) | Databases with SQLite |

---

### Module 6 — AI & Machine Learning
*Build on top of AI — and eventually understand what's under the hood.*

| Lesson | Topic |
|--------|-------|
| [28](./module-6/28-ai-apis.md) | Working with AI APIs |
| [29](./module-6/29-ai-tools.md) | Building AI-Powered Tools |
| [30](./module-6/30-ml-intro.md) | Intro to Machine Learning |

---

## Tracking Your Progress

The course includes a CLI tracker. Run it from the `python-course/` folder:

```bash
python tracker.py                        # show progress dashboard
python tracker.py done 5                 # mark lesson 5 complete
python tracker.py undone 5               # unmark it
python tracker.py note 5 "your note"    # attach a note to a lesson
python tracker.py next                   # show what's next
python tracker.py reset                  # clear all progress
```

Progress is stored in `progress.json`. **Commit and push after each session** to keep it synced across machines:

```bash
git add progress.json
git commit -m "Completed lesson X"
git push
```

---

## Working Across Machines

When you sit down on a new machine, always pull first:

```bash
git pull
```

Then pick up where you left off:

```bash
python tracker.py next
```

---

## How to Use This Course

1. Work through lessons in order — each one builds on the last.
2. **Actually do the exercises.** Reading code is not the same as writing it.
3. If an exercise feels too easy, do it anyway. If it feels impossible, re-read the lesson and try again before looking at the hint.
4. When you finish Module 1, you'll be able to write real programs. When you finish all 6, you'll be a capable Python developer.

Let's go.
