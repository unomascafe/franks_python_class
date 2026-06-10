# Lesson 16 — Running Shell Commands

## What You'll Learn
- Run shell commands from Python with `subprocess`
- Capture output and handle errors
- Know when to use shell commands vs pure Python

---

## subprocess.run()

The modern way to run shell commands:

```python
import subprocess

# Run a command
result = subprocess.run(["python", "--version"])

# Capture the output
result = subprocess.run(
    ["git", "status"],
    capture_output=True,
    text=True
)

print(result.stdout)    # the command's output
print(result.stderr)    # any error output
print(result.returncode)  # 0 = success, anything else = error
```

Key parameters:
| Parameter | What it does |
|-----------|-------------|
| `capture_output=True` | Capture stdout and stderr |
| `text=True` | Return strings instead of bytes |
| `check=True` | Raise an exception if the command fails |
| `cwd="path"` | Run the command from a specific directory |
| `timeout=30` | Fail if it takes longer than 30 seconds |

---

## Checking for Errors

```python
import subprocess

try:
    result = subprocess.run(
        ["git", "push"],
        capture_output=True,
        text=True,
        check=True   # raises CalledProcessError if returncode != 0
    )
    print("Push successful")
except subprocess.CalledProcessError as e:
    print(f"Command failed: {e.stderr}")
```

---

## Running Shell Strings

Sometimes you want to run a full shell string (with pipes, etc.):

```python
import subprocess

# On Windows
result = subprocess.run("dir /b", shell=True, capture_output=True, text=True)

# On Mac/Linux
result = subprocess.run("ls -la | grep .py", shell=True, capture_output=True, text=True)

print(result.stdout)
```

Avoid `shell=True` when you can — it's a security risk if any part of the command comes from user input. Use the list form instead.

---

## Practical Examples

**Run a Python script:**
```python
subprocess.run(["python", "process_data.py", "--input", "data.csv"], check=True)
```

**Open a file with the default app:**
```python
import os
os.startfile("report.pdf")          # Windows
subprocess.run(["open", "report.pdf"])   # Mac
subprocess.run(["xdg-open", "report.pdf"])  # Linux
```

**Get git log:**
```python
result = subprocess.run(
    ["git", "log", "--oneline", "-10"],
    capture_output=True, text=True, check=True
)
for line in result.stdout.strip().split("\n"):
    print(line)
```

---

## When to Use subprocess vs Pure Python

| Task | Use |
|------|-----|
| File operations | `pathlib` / `shutil` |
| HTTP requests | `requests` library |
| Running another script | `subprocess` |
| Git operations | `subprocess` (or `gitpython`) |
| System info | `subprocess` or `psutil` |
| Anything with a CLI tool | `subprocess` |

---

## Exercises

Create `shell.py`.

**Exercise 1:** Write a function `run_cmd(command_list)` that runs a command, captures output, and returns `(success, stdout, stderr)`. Test it with `["python", "--version"]` and `["git", "status"]`.

**Exercise 2:** Write a function `git_log(n=10)` that returns the last `n` git commits as a list of strings (one per commit). Handle the case where the folder isn't a git repo.

**Exercise 3:** Write a script that runs `pip list` and parses the output into a list of `(package_name, version)` tuples. Print them sorted by package name.

**Exercise 4 (stretch):** Write a function `run_python_script(script_path, *args)` that runs any `.py` file as a subprocess, captures its output, and returns it as a string. Add a timeout of 30 seconds.

---

## Key Takeaway
`subprocess.run()` with `capture_output=True, text=True` is the standard pattern. Use `check=True` to get automatic error raising. Prefer the list form over `shell=True`. For file and HTTP work, use dedicated Python libraries — `subprocess` is for things that genuinely need a shell command.

**Next:** [Lesson 17 — HTTP Requests & APIs →](./17-requests.md)
