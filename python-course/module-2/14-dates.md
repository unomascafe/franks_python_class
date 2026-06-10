# Lesson 14 — Dates & Times

## What You'll Learn
- Work with dates and times using `datetime`
- Format and parse date strings
- Do date math (timedeltas)
- Get the current time and timestamps

---

## The datetime Module

Python's built-in `datetime` module handles dates and times. The main types:

| Type | What it represents |
|------|-------------------|
| `date` | Just a date (year, month, day) |
| `time` | Just a time (hour, minute, second) |
| `datetime` | Date + time combined |
| `timedelta` | A duration (difference between two datetimes) |

```python
from datetime import date, time, datetime, timedelta
```

---

## Getting the Current Date/Time

```python
from datetime import date, datetime

today = date.today()
print(today)           # 2024-01-15

now = datetime.now()
print(now)             # 2024-01-15 09:32:47.123456
```

---

## Creating Dates and Datetimes

```python
from datetime import date, datetime

birthday = date(1982, 6, 10)           # year, month, day
meeting = datetime(2024, 1, 15, 14, 30)  # year, month, day, hour, minute
```

---

## Formatting Dates (datetime → string)

Use `.strftime()` with format codes:

```python
from datetime import datetime

now = datetime.now()

now.strftime("%Y-%m-%d")           # "2024-01-15"
now.strftime("%B %d, %Y")          # "January 15, 2024"
now.strftime("%m/%d/%Y")           # "01/15/2024"
now.strftime("%Y-%m-%d %H:%M:%S")  # "2024-01-15 09:32:47"
now.strftime("%A, %B %d")          # "Monday, January 15"
```

Common format codes:
| Code | Meaning | Example |
|------|---------|---------|
| `%Y` | 4-digit year | 2024 |
| `%m` | Month (zero-padded) | 01 |
| `%B` | Full month name | January |
| `%d` | Day (zero-padded) | 15 |
| `%A` | Full weekday name | Monday |
| `%H` | Hour (24h) | 09 |
| `%M` | Minute | 32 |
| `%S` | Second | 47 |

---

## Parsing Dates (string → datetime)

Use `datetime.strptime()` — the format must match the string exactly:

```python
from datetime import datetime

date_str = "2024-01-15"
dt = datetime.strptime(date_str, "%Y-%m-%d")

date_str2 = "January 15, 2024"
dt2 = datetime.strptime(date_str2, "%B %d, %Y")
```

---

## Date Math with timedelta

```python
from datetime import date, timedelta

today = date.today()

tomorrow = today + timedelta(days=1)
last_week = today - timedelta(weeks=1)
in_90_days = today + timedelta(days=90)

# Difference between two dates
start = date(2024, 1, 1)
end = date(2024, 3, 15)
delta = end - start
print(delta.days)   # 74
```

---

## Comparing Dates

```python
from datetime import date

deadline = date(2024, 2, 1)
today = date.today()

if today > deadline:
    print("Past deadline!")
elif today == deadline:
    print("Due today!")
else:
    days_left = (deadline - today).days
    print(f"{days_left} days until deadline")
```

---

## Timestamps (Unix Time)

Unix timestamps are the number of seconds since Jan 1, 1970 — used in databases, APIs, and logs:

```python
from datetime import datetime

# Current timestamp
import time
ts = time.time()     # e.g., 1705312367.123

# Timestamp → datetime
dt = datetime.fromtimestamp(ts)

# datetime → timestamp
ts = datetime.now().timestamp()
```

---

## Exercises

Create `dates.py`.

**Exercise 1:** Print today's date in three formats: `2024-01-15`, `January 15, 2024`, and `Monday, Jan 15`.

**Exercise 2:** Write a function `days_until(target_date_str)` that takes a date string like `"2024-12-31"` and returns how many days until that date (negative if it's in the past).

**Exercise 3:** Given a list of log timestamps as strings (`"2024-01-15 09:32:47"`), parse them into datetime objects and find the most recent one.

**Exercise 4:** Write a function `age(birthdate_str)` that takes a birthdate like `"1982-06-10"` and returns the person's current age in years.

**Exercise 5 (stretch):** Write a function that takes a start date and end date and returns a list of all the dates in between (one per day). Then filter that list to only weekdays (Monday–Friday).

---

## Key Takeaway
`datetime.now()` and `date.today()` get the current time. `.strftime()` formats a datetime to a string. `strptime()` parses a string to a datetime — format must match exactly. `timedelta` does date math. Dates are comparable with `<`, `>`, `==`.

**Next:** [Module 3 — Automation →](../module-3/15-filesystem.md)
