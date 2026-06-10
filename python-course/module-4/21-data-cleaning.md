# Lesson 21 — Cleaning & Transforming Data

## What You'll Learn
- Handle missing values
- Fix data types and formatting issues
- Rename, add, and transform columns
- Merge and reshape DataFrames

---

## Missing Values

Real data always has gaps. Pandas represents missing values as `NaN`.

```python
import pandas as pd
import numpy as np

df.isnull().sum()          # count nulls per column
df.isnull().any()          # True/False per column
df[df["salary"].isnull()]  # rows where salary is missing

# Drop rows with any nulls
df.dropna()

# Drop rows where specific columns are null
df.dropna(subset=["email", "salary"])

# Fill nulls with a value
df["salary"].fillna(0)
df["city"].fillna("Unknown")
df["salary"].fillna(df["salary"].mean())   # fill with mean
```

---

## Fixing Data Types

```python
# Check types
df.dtypes

# Convert
df["salary"] = df["salary"].astype(int)
df["date"] = pd.to_datetime(df["date"])
df["active"] = df["active"].astype(bool)

# Handle errors during conversion
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")  # bad values → NaN
```

---

## String Cleaning

```python
# Strip whitespace
df["name"] = df["name"].str.strip()

# Normalize case
df["email"] = df["email"].str.lower()
df["name"] = df["name"].str.title()

# Replace
df["dept"] = df["dept"].str.replace("Eng", "Engineering")

# Extract with regex
df["area_code"] = df["phone"].str.extract(r"\((\d{3})\)")
```

---

## Renaming and Reorganizing

```python
# Rename columns
df = df.rename(columns={"emp_name": "name", "dep": "dept"})

# Reorder columns
df = df[["name", "dept", "salary", "years"]]

# Drop columns
df = df.drop(columns=["internal_id", "temp_col"])

# Reset index (useful after filtering)
df = df.reset_index(drop=True)
```

---

## Adding and Transforming Columns

```python
# Simple math
df["bonus"] = df["salary"] * 0.10
df["total_comp"] = df["salary"] + df["bonus"]

# Apply a function to a column
df["name_upper"] = df["name"].apply(str.upper)

def classify_salary(sal):
    if sal < 80000:
        return "junior"
    elif sal < 100000:
        return "mid"
    else:
        return "senior"

df["level"] = df["salary"].apply(classify_salary)

# Conditional column with np.where
import numpy as np
df["high_earner"] = np.where(df["salary"] > 100000, True, False)
```

---

## Merging DataFrames

Like SQL JOINs:

```python
employees = pd.DataFrame([
    {"emp_id": 1, "name": "Frank", "dept_id": 10},
    {"emp_id": 2, "name": "Alice", "dept_id": 20},
])

departments = pd.DataFrame([
    {"dept_id": 10, "dept_name": "Operations"},
    {"dept_id": 20, "dept_name": "Engineering"},
])

# Inner join (only matching rows)
merged = employees.merge(departments, on="dept_id")

# Left join (all employees, even without a matching dept)
merged = employees.merge(departments, on="dept_id", how="left")
```

---

## Pivot Tables

Summarize data by two dimensions:

```python
pivot = df.pivot_table(
    values="salary",
    index="dept",
    columns="level",
    aggfunc="mean"
)
```

---

## Exercises

Create `data_cleaning.py`.

**Exercise 1:** Create a messy DataFrame:
```python
messy = pd.DataFrame([
    {"name": " frank ", "salary": "90,000", "dept": "ops", "email": "FRANK@EXAMPLE.COM"},
    {"name": "Alice",   "salary": "105000", "dept": "eng", "email": "alice@example.com"},
    {"name": " Bob  ",  "salary": None,      "dept": "ops", "email": "bob@example.com"},
    {"name": "Carol",   "salary": "bad",     "dept": "eng", "email": None},
])
```
Clean it: strip names, normalize emails to lowercase, fix the dept codes to full names, convert salary to numeric (replacing bad values with NaN), fill missing salaries with the column mean.

**Exercise 2:** Given two DataFrames — one with orders (`order_id`, `customer_id`, `amount`) and one with customers (`customer_id`, `name`, `city`) — merge them and find the total spending per customer city.

**Exercise 3:** Add a `"tenure_category"` column to an employee DataFrame: `"new"` (< 2 years), `"experienced"` (2–5 years), `"veteran"` (> 5 years). Use `.apply()`.

**Exercise 4 (stretch):** Load a real CSV file with messy data (or create one). Write a cleaning pipeline that runs each step in sequence and prints a summary of what changed (nulls removed, types fixed, etc.).

---

## Key Takeaway
Real data is always messy. `isnull()` finds gaps. `astype()` and `pd.to_numeric(errors="coerce")` fix types. `.str` accessor handles string operations. `.apply()` runs any function over a column. `merge()` joins DataFrames like SQL. Clean data before you analyze it — every time.

**Next:** [Lesson 22 — Visualizations →](./22-visualization.md)
