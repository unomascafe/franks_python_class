# Lesson 24 — Command-Line Tools

## What You'll Learn
- Build proper CLI tools with `argparse`
- Accept arguments, flags, and subcommands
- Make scripts feel like real tools

---

## Install

`argparse` is in the standard library — no install needed.

---

## Why argparse?

You've already seen `sys.argv` for reading command-line arguments. `argparse` does the same thing but gives you:
- Automatic `--help` documentation
- Argument validation and type conversion
- Optional/required arguments
- Subcommands (like `git add`, `git commit`)

---

## Basic Usage

```python
# greet.py
import argparse

parser = argparse.ArgumentParser(description="Greet someone")
parser.add_argument("name", help="Name to greet")
args = parser.parse_args()

print(f"Hello, {args.name}!")
```

```bash
python greet.py Frank       # Hello, Frank!
python greet.py --help      # shows usage
```

---

## Optional Arguments and Flags

```python
import argparse

parser = argparse.ArgumentParser(description="Generate a report")

# Required positional argument
parser.add_argument("input_file", help="Input CSV file")

# Optional argument with default
parser.add_argument("--output", "-o", default="report.csv", help="Output file path")

# Flag (True/False)
parser.add_argument("--verbose", "-v", action="store_true", help="Show detailed output")

# Typed argument
parser.add_argument("--limit", type=int, default=100, help="Max rows to process")

# Choices
parser.add_argument("--format", choices=["csv", "json", "excel"], default="csv")

args = parser.parse_args()

print(f"Input: {args.input_file}")
print(f"Output: {args.output}")
print(f"Verbose: {args.verbose}")
print(f"Limit: {args.limit}")
```

```bash
python report.py data.csv
python report.py data.csv --output results.csv --verbose --limit 50
python report.py data.csv -o results.csv -v
```

---

## Subcommands

Model your tool after `git`, `docker`, or other CLIs with sub-commands:

```python
# task_manager.py
import argparse

def cmd_add(args):
    print(f"Adding task: {args.task}")

def cmd_list(args):
    print("Listing all tasks...")

def cmd_done(args):
    print(f"Marking task {args.id} as done")

parser = argparse.ArgumentParser(description="Task manager")
subparsers = parser.add_subparsers(dest="command")

# Add subcommand
add_parser = subparsers.add_parser("add", help="Add a task")
add_parser.add_argument("task", help="Task description")

# List subcommand
list_parser = subparsers.add_parser("list", help="List all tasks")

# Done subcommand
done_parser = subparsers.add_parser("done", help="Mark a task done")
done_parser.add_argument("id", type=int, help="Task ID")

args = parser.parse_args()

if args.command == "add":
    cmd_add(args)
elif args.command == "list":
    cmd_list(args)
elif args.command == "done":
    cmd_done(args)
else:
    parser.print_help()
```

```bash
python task_manager.py add "Buy more PLA filament"
python task_manager.py list
python task_manager.py done 3
```

---

## Making a Script Runnable

On Mac/Linux, add a shebang line and make it executable:
```python
#!/usr/bin/env python3
# ... rest of script
```
```bash
chmod +x my_tool.py
./my_tool.py
```

---

## Exercises

Create a file `cli_tool.py`.

**Exercise 1:** Build a CLI calculator: `python cli_tool.py 10 add 5` prints `15`. Support `add`, `subtract`, `multiply`, `divide`.

**Exercise 2:** Build a CLI file search tool: `python search.py folder --ext .py --name main` lists all files in the folder matching the criteria.

**Exercise 3:** Extend your note-taking script from Lesson 11 to use `argparse` properly, with subcommands: `add`, `list`, `delete <id>`, and `search <query>`.

**Exercise 4 (stretch):** Build a CLI tool that wraps the Open-Meteo weather API: `python weather.py --city "Mesa, AZ" --days 3` prints a 3-day forecast. Store the city-to-coordinates mapping in a dict.

---

## Key Takeaway
`argparse` makes scripts feel like real tools. Positional args are required. `--flags` are optional. `action="store_true"` for booleans. Subcommands model multi-function CLIs. The auto-generated `--help` is free.

**Next:** [Lesson 25 — Simple Web Apps with Flask →](./25-flask.md)
