# Lesson 11 — Reading & Writing Files

## What You'll Learn
- Open, read, and write text files
- Use the `with` statement
- Append to files
- Handle common file errors

---

## Opening Files

Use `open()` to work with files. Always use the `with` statement — it automatically closes the file when you're done, even if something crashes:

```python
with open("notes.txt", "r") as f:
    content = f.read()
print(content)
```

### File modes:
| Mode | Meaning |
|------|---------|
| `"r"` | Read (default) — file must exist |
| `"w"` | Write — creates file, overwrites if exists |
| `"a"` | Append — creates file, adds to end if exists |
| `"x"` | Create — fails if file already exists |

---

## Reading Files

```python
# Read entire file as one string
with open("data.txt", "r") as f:
    content = f.read()

# Read line by line (memory-efficient for large files)
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())   # .strip() removes the newline at the end

# Read all lines into a list
with open("data.txt", "r") as f:
    lines = f.readlines()
# lines = ["line 1\n", "line 2\n", "line 3\n"]
```

---

## Writing Files

```python
# Write (creates or overwrites)
with open("output.txt", "w") as f:
    f.write("Hello, file!\n")
    f.write("Second line.\n")

# Write a list of lines
lines = ["apple\n", "banana\n", "cherry\n"]
with open("fruits.txt", "w") as f:
    f.writelines(lines)

# Append (adds to existing content)
with open("log.txt", "a") as f:
    f.write("New log entry\n")
```

---

## File Paths

```python
# Relative paths (relative to where the script is run)
open("data.txt")
open("subfolder/data.txt")

# Absolute paths
open("C:/Users/Frank/Documents/data.txt")   # Windows
open("/home/frank/documents/data.txt")       # Linux/Mac

# Better: use pathlib (covered in Lesson 15)
from pathlib import Path
open(Path.home() / "Documents" / "data.txt")
```

---

## Encoding

Always specify encoding for text files to avoid surprises on different systems:

```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

`utf-8` handles basically everything. Use it by default.

---

## Exercises

Create `file_io.py`.

**Exercise 1:** Write a script that:
1. Creates a file called `tasks.txt` with 5 tasks (one per line)
2. Reads the file back and prints each line numbered (1. task one, 2. task two...)

**Exercise 2:** Write a function `count_lines(filename)` that returns the number of lines in a file. Handle the case where the file doesn't exist.

**Exercise 3:** Write a function `append_log(message, filename="app.log")` that appends a timestamped message to a log file. The format should be: `[2024-01-15 09:32:00] Your message here`. Run it a few times to verify it accumulates.

**Exercise 4:** Write a function `word_frequency(filename)` that reads a text file and returns a dictionary of word counts (lowercase, stripped of punctuation).

**Exercise 5 (stretch):** Write a simple note-taking script:
- If called with `python notes.py add "my note here"`, append the note to `notes.txt` with a timestamp
- If called with `python notes.py list`, print all notes
- Use `import sys; args = sys.argv[1:]` to read command-line arguments

---

## Key Takeaway
Always use `with open(...)` — it handles cleanup automatically. `"r"` reads, `"w"` writes (overwrites), `"a"` appends. Specify `encoding="utf-8"`. Strip newlines off lines when reading with `.strip()`.

**Next:** [Lesson 12 — CSV & JSON →](./12-csv-json.md)
