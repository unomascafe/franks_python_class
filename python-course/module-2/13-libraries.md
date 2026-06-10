# Lesson 13 — Installing & Using Libraries

## What You'll Learn
- Install packages with `pip`
- Import and use modules
- Understand the Python ecosystem
- Set up a virtual environment

---

## The Python Ecosystem

Python's real power is its ecosystem. There are packages for almost everything:
- `requests` — HTTP calls
- `pandas` — data analysis
- `flask` — web apps
- `openai` — OpenAI API
- `beautifulsoup4` — web scraping
- `pillow` — image processing

Most Python projects use 5–20 external packages.

---

## pip — Package Manager

Install packages with `pip` in your terminal:

```bash
pip install requests
pip install pandas
pip install flask openai   # install multiple at once
pip install requests==2.31.0   # specific version
pip install --upgrade requests  # upgrade to latest
pip uninstall requests
pip list   # see installed packages
```

---

## Virtual Environments

A **virtual environment** is an isolated Python installation for one project. This prevents packages from different projects from conflicting with each other.

**Create and activate:**

```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Your terminal prompt will change to show (venv)
```

**Install packages while it's active:**
```bash
pip install requests pandas
```

**Deactivate:**
```bash
deactivate
```

Make a habit: one virtual environment per project.

---

## requirements.txt

`requirements.txt` lists your project's dependencies so others (or another machine) can install them all at once:

```bash
# Save current packages to requirements.txt
pip freeze > requirements.txt

# Install all packages from requirements.txt
pip install -r requirements.txt
```

A typical `requirements.txt`:
```
requests==2.31.0
pandas==2.1.0
flask==3.0.0
openai==1.3.5
```

---

## Importing Modules

Standard library (no install needed):
```python
import os
import json
import math
import datetime
from pathlib import Path
```

Third-party (installed via pip):
```python
import requests
import pandas as pd      # alias — standard convention
import numpy as np
```

Selective imports (only import what you need):
```python
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict, Counter
```

---

## Useful Standard Library Modules

You already have these — no install:

```python
import os           # OS operations, env variables
import sys          # Python runtime, command-line args
import json         # JSON encode/decode
import csv          # CSV files
import math         # math functions
import random       # random numbers
import datetime     # dates and times
import pathlib      # file paths
import re           # regular expressions
import collections  # Counter, defaultdict, etc.
import itertools    # advanced iteration tools
import functools    # higher-order functions
import logging      # proper logging
import subprocess   # run shell commands
import threading    # concurrent execution
import hashlib      # hashing
import base64       # encoding
import urllib       # URL utilities
```

---

## Exercises

**Exercise 1:** Create a new project folder, set up a virtual environment, and install `requests`. Write a script that makes a GET request to `https://httpbin.org/get` and prints the response JSON.

**Exercise 2:** Install `rich` (`pip install rich`) — a library for beautiful terminal output. Use it to print a table of your 5 favorite games with columns for name, genre, and rating.

**Exercise 3:** Create a `requirements.txt` for a project that needs `requests`, `pandas`, and `flask`. Pin each to its latest version (look them up on [pypi.org](https://pypi.org) or use `pip install` and check `pip list`).

**Exercise 4:** Use the `random` module (no install needed) to:
- Pick a random item from a list
- Generate a random integer between 1 and 100
- Shuffle a list in place

**Exercise 5 (stretch):** Use the `collections.Counter` class to count word frequencies in a string. Then use `most_common(5)` to get the top 5 words.

---

## Key Takeaway
`pip install` gets packages. Virtual environments keep projects clean. `import` brings them into your script. The standard library covers a ton — check it before reaching for a third-party package. `requirements.txt` is how you share dependencies.

**Next:** [Lesson 14 — Dates & Times →](./14-dates.md)
