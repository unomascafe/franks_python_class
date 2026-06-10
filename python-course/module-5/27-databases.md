# Lesson 27 — Databases with SQLite

## What You'll Learn
- Create and query a SQLite database with Python
- Use parameterized queries (safely)
- Connect a database to your Flask API

---

## Why SQLite?

SQLite is a file-based database — no server to install or configure. Your entire database is one `.db` file. Perfect for:
- Personal tools and scripts
- Small web apps
- Learning SQL and database patterns before moving to PostgreSQL or MySQL

---

## The sqlite3 Module

```python
import sqlite3

# Connect (creates the file if it doesn't exist)
conn = sqlite3.connect("myapp.db")
conn.row_factory = sqlite3.Row   # rows behave like dicts
cursor = conn.cursor()
```

---

## Creating Tables

```python
import sqlite3

conn = sqlite3.connect("tasks.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        title   TEXT NOT NULL,
        done    INTEGER DEFAULT 0,
        created TEXT DEFAULT (date('now'))
    )
""")
conn.commit()
```

---

## CRUD Operations

```python
# INSERT
cursor.execute(
    "INSERT INTO tasks (title) VALUES (?)",
    ("Buy more filament",)   # always use ? placeholders — never f-strings
)
conn.commit()
new_id = cursor.lastrowid

# SELECT
cursor.execute("SELECT * FROM tasks")
rows = cursor.fetchall()
for row in rows:
    print(dict(row))   # dict because of row_factory

# SELECT with filter
cursor.execute("SELECT * FROM tasks WHERE done = ?", (0,))
pending = cursor.fetchall()

# SELECT one
cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
task = cursor.fetchone()

# UPDATE
cursor.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
conn.commit()

# DELETE
cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
conn.commit()
```

**Always use `?` placeholders.** Never build SQL strings with f-strings or `+` — that's how SQL injection happens.

---

## A Database Helper Class

```python
import sqlite3
from pathlib import Path

class TaskDB:
    def __init__(self, db_path="tasks.db"):
        self.db_path = db_path
        self._init_db()
    
    def _connect(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def _init_db(self):
        with self._connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    done INTEGER DEFAULT 0,
                    created TEXT DEFAULT (date('now'))
                )
            """)
    
    def add(self, title):
        with self._connect() as conn:
            cursor = conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
            return cursor.lastrowid
    
    def get_all(self, done=None):
        with self._connect() as conn:
            if done is None:
                rows = conn.execute("SELECT * FROM tasks ORDER BY id").fetchall()
            else:
                rows = conn.execute(
                    "SELECT * FROM tasks WHERE done = ? ORDER BY id", (int(done),)
                ).fetchall()
            return [dict(r) for r in rows]
    
    def get(self, task_id):
        with self._connect() as conn:
            row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
            return dict(row) if row else None
    
    def mark_done(self, task_id):
        with self._connect() as conn:
            conn.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    
    def delete(self, task_id):
        with self._connect() as conn:
            conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))


# Usage
db = TaskDB()
db.add("Learn SQLite")
db.add("Build Flask app")
print(db.get_all())
db.mark_done(1)
print(db.get_all(done=False))
```

---

## Connecting to Flask

Replace the in-memory list from Lesson 26 with a real database:

```python
from flask import Flask, jsonify, request
from task_db import TaskDB

app = Flask(__name__)
db = TaskDB("tasks.db")

@app.route("/api/tasks", methods=["GET"])
def list_tasks():
    return jsonify(db.get_all())

@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "title required"}), 400
    task_id = db.add(data["title"])
    return jsonify(db.get(task_id)), 201
```

---

## Exercises

Create `db_demo.py` and a `task_db.py` module.

**Exercise 1:** Implement the full `TaskDB` class above. Add a `update_title(task_id, new_title)` method.

**Exercise 2:** Write a script that populates the database with 10 tasks, marks 3 of them done, then prints all pending tasks and a count of completed ones.

**Exercise 3:** Add a `search(query)` method to `TaskDB` that returns all tasks where the title contains the query string (case-insensitive). Use SQL `LIKE`.

**Exercise 4:** Wire `TaskDB` into your Flask API from Lesson 26, replacing the in-memory list. The app should survive restarts with data intact.

**Exercise 5 (stretch):** Add a second table `tags` and a `task_tags` join table. Implement methods to add tags to tasks and retrieve tasks by tag.

---

## Key Takeaway
SQLite = a database in a file, no setup required. Always use `?` placeholders. `row_factory = sqlite3.Row` makes rows behave like dicts. Wrap your DB logic in a class — it keeps Flask routes clean. When you outgrow SQLite, the patterns transfer directly to PostgreSQL with minimal changes.

**Next:** [Module 6 — AI & Machine Learning →](../module-6/28-ai-apis.md)
