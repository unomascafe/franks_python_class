# Lesson 01 — Setup & Your First Script

## What You'll Learn
- Install Python and a code editor
- Run a Python script
- Understand the basic workflow

---

## Before We Start: What Are We Actually Doing?

Programming, at its core, is writing instructions in a text file and then asking a program to read that file and follow the instructions. That's it.

In our case, the instructions will be written in **Python** — a programming language designed to read more like English than most. The program that reads the instructions is called the **Python interpreter**. We're going to install the interpreter, write a tiny instruction file, and ask the interpreter to run it.

Before any of that works, we need two things on the computer:

1. **Python itself** — the interpreter that turns your code into something the machine can run.
2. **A code editor** — a text editor designed for writing code, with syntax highlighting, auto-complete, and a built-in terminal so you can run things without switching apps.

We'll set those up first, then run a one-line program to prove the whole pipeline works.

---

## Setup

### 1. Install Python

Go to [python.org/downloads](https://python.org/downloads) and grab the latest version (3.11 or newer). The site auto-detects your operating system, so the big download button should already be the right installer.

> **Windows users — important:** when the installer launches, the very first screen has a checkbox at the bottom that says **"Add Python to PATH"**. Check it. If you don't, your terminal won't know where to find Python later, and you'll get confusing "command not found" errors. (If you already installed without checking it, just re-run the installer and pick "Modify" — you can turn it on after the fact.)

Once it finishes, you need to confirm it actually worked. Open a terminal:

- **Windows:** open the Start menu, type "PowerShell", hit enter.
- **Mac:** open Spotlight (⌘+Space), type "Terminal", hit enter.

In that terminal window, type:

```
python --version
```

You should see something like `Python 3.12.1`. The exact number doesn't matter as long as it starts with `3.11` or higher. If you instead see "command not found" or "is not recognized," Python isn't on your PATH — re-run the installer and tick that box.

### 2. Install VS Code

Download from [code.visualstudio.com](https://code.visualstudio.com). VS Code is free, fast, and what most working developers use day-to-day. There are other editors (PyCharm, Sublime, Vim), but VS Code is the easiest place to start.

Once it's installed and open, look at the left edge of the window — there's a vertical bar of icons. Click the one that looks like four squares ("Extensions"), search for **"Python"** (the one from Microsoft), and click **Install**. This is what gives the editor its understanding of Python: autocomplete, error highlighting, the little play button to run scripts, all of that.

### 3. Create a project folder

Make a new folder somewhere on your computer — Documents, Desktop, wherever you'll remember it. Call it `python-practice`. This is where every script in this course will live, so you can find them later.

In VS Code, go to **File → Open Folder**, pick the folder you just made, and open it. The left sidebar will now show that folder's contents (empty for now).

---

## Your First Script

In VS Code, create a new file. Either click the "new file" icon in the sidebar or press **Ctrl+N** / **Cmd+N**. Name it `hello.py`. The `.py` extension is what tells everything — the editor, the interpreter, the operating system — that this is a Python file.

Type this single line into the file:

```python
print("Hello, world!")
```

Let's break that down before we run it. `print` is a **function** — a built-in command that Python already knows. The parentheses `()` are how you "call" the function (how you tell Python to actually do the thing). Inside the parentheses you pass the **argument**: the value you want the function to act on. In this case, the text `"Hello, world!"` — wrapped in quotes because it's a string of characters, not a number or a variable.

Save the file (**Ctrl+S** / **Cmd+S**). Now we need to run it.

Open a terminal **inside VS Code** — go to **View → Terminal**, or just press **Ctrl+`** (the backtick key, above Tab). A panel slides up at the bottom. This terminal is already pointed at your project folder, so you don't have to navigate anywhere.

Type:

```
python hello.py
```

This is you telling the Python interpreter: "Hey, read the file `hello.py` and do what it says." Hit enter, and you should see:

```
Hello, world!
```

That's it. You wrote code, you ran it, the computer did what you asked. The whole rest of this course is just expanding what you can put inside that script.

---

## How Python Works (the 60-second version)

Python is what's called an **interpreted** language. That means there's no separate "build" or "compile" step like you'd have in C++ or Java. You write your code, you save it, and the Python interpreter reads it directly — line by line, top to bottom — and executes each instruction as it goes.

This has a real consequence for how you'll work: the **edit → save → run** loop is fast. You change one line, save, hit the up-arrow in your terminal to recall the last command, run it again. Each iteration takes a few seconds. Don't try to write 50 lines and then run — write 2–3 lines, run, see what happens, write 2–3 more. Tight loops are how you learn.

When something goes wrong, Python will stop and print an **error message** (also called a *traceback*). These look scary at first, but they're trying to help you: they tell you which line broke and what kind of mistake it was. We'll get more comfortable reading them as we go.

---

## Exercises

**Exercise 1:** Modify `hello.py` to print your name instead of "world". Save and run it.

**Exercise 2:** Make the script print three separate lines — your name, your city, and one thing you want to build with Python. Each piece of text goes inside its own `print()` call, on its own line in the file. When you run the script, you should see three lines of output.

**Exercise 3:** Now intentionally break it. Remove the quotes from inside `print()` (so it reads `print(Hello, world!)`), save, and run. You'll get an error — read it carefully. What does Python think `Hello` is? Then put the quotes back. Getting comfortable reading errors is one of the most important skills you'll build in this course, so don't skip this one.

---

## Key Takeaway

Python runs `.py` files top to bottom. You write instructions in plain text, save with a `.py` extension, and run them with `python filename.py`. `print()` is the function that outputs text to the terminal — text goes inside quotes, inside the parentheses. When something breaks, **read the error** — it tells you exactly which line went wrong and what kind of mistake it was. That edit → save → run → read-the-output loop is the entire rhythm of programming.

**Next:** [Lesson 02 — Variables & Data Types →](./02-variables-and-types.md)
