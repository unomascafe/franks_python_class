# Lesson 01 — Setup & Your First Script

## What You'll Learn
- Install Python and a code editor
- Run a Python script
- Understand the basic workflow

---

## Setup

### 1. Install Python
Go to [python.org/downloads](https://python.org/downloads) and grab the latest version (3.11+).

**Windows:** During install, check the box that says **"Add Python to PATH"** — don't skip this.

Verify it worked by opening a terminal and typing:
```
python --version
```
You should see something like `Python 3.12.1`.

### 2. Install VS Code
Download from [code.visualstudio.com](https://code.visualstudio.com). Once installed, add the **Python extension** (search "Python" in the Extensions panel on the left).

### 3. Create a project folder
Make a folder somewhere on your computer called `python-practice`. Open it in VS Code (File → Open Folder).

---

## Your First Script

In VS Code, create a new file called `hello.py`. Type this in:

```python
print("Hello, world!")
```

Save it. Now run it — open the terminal in VS Code (View → Terminal) and type:
```
python hello.py
```

You should see:
```
Hello, world!
```

That's it. You just ran your first Python program.

---

## How Python Works (30-second version)

Python is an **interpreted** language — you write code in a `.py` file, and Python reads and runs it line by line, top to bottom. No compiling, no build steps. Write → Save → Run.

---

## Exercises

**Exercise 1:** Modify `hello.py` to print your name instead of "world".

**Exercise 2:** Make the script print three separate lines — your name, your city, and what you want to build with Python. Each `print()` call goes on its own line.

**Exercise 3:** What happens if you remove the quotes from inside `print()`? Try it, see the error, and read the error message. Getting comfortable reading errors is a core skill.

---

## Key Takeaway
Python runs `.py` files from top to bottom. `print()` outputs text to the terminal. When something breaks, read the error — it tells you exactly what went wrong and where.

**Next:** [Lesson 02 — Variables & Data Types →](./02-variables-and-types.md)
