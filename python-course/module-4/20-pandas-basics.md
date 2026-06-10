# Lesson 20 — Pandas: DataFrames

## What You'll Learn
- Load data into a DataFrame
- Inspect, select, and filter data
- Do basic aggregations

---

## Install

```bash
pip install pandas
```

---

## What's a DataFrame?

A DataFrame is a table — rows and columns, like a spreadsheet or SQL table. Pandas is the standard Python library for working with them.

```python
import pandas as pd

# Create from a list of dicts
data = [
    {"name": "Frank", "dept": "Operations", "salary": 90000},
    {"name": "Alice", "dept": "Engineering", "salary": 105000},
    {"name": "Bob", "dept": "Operations", "salary": 85000},
    {"name": "Carol", "dept": "Engineering", "salary": 112000},
    {"name": "Dave", "dept": "Marketing", "salary": 78000},
]
df = pd.DataFrame(data)
print(df)
```

```
    name         dept  salary
0  Frank   Operations   90000
1  Alice  Engineering  105000
2    Bob   Operations   85000
3  Carol  Engineering  112000
4   Dave    Marketing   78000
```

---

## Loading Data

```python
import pandas as pd

# From CSV
df = pd.read_csv("employees.csv")

# From Excel
df = pd.read_excel("report.xlsx", sheet_name="Sheet1")

# From JSON
df = pd.read_json("data.json")

# From a URL
df = pd.read_csv("https://example.com/data.csv")
```

---

## Inspecting DataFrames

```python
df.shape          # (rows, columns)
df.columns        # column names
df.dtypes         # data types of each column
df.head()         # first 5 rows
df.tail(3)        # last 3 rows
df.info()         # summary: shape, types, nulls
df.describe()     # stats: mean, std, min, max, etc.
```

---

## Selecting Data

```python
# Single column → Series
df["name"]
df["salary"]

# Multiple columns → DataFrame
df[["name", "salary"]]

# Row by index
df.iloc[0]        # first row
df.iloc[-1]       # last row
df.iloc[0:3]      # rows 0, 1, 2

# Row by label (if you've set an index)
df.loc[0]
```

---

## Filtering Rows

```python
# Boolean condition
df[df["salary"] > 90000]

# Multiple conditions
df[(df["dept"] == "Engineering") & (df["salary"] > 100000)]

# String matching
df[df["name"].str.startswith("A")]
df[df["dept"].isin(["Operations", "Engineering"])]

# Not null
df[df["manager"].notna()]
```

---

## Basic Aggregations

```python
df["salary"].mean()       # average
df["salary"].sum()        # total
df["salary"].max()        # highest
df["salary"].min()        # lowest
df["salary"].median()
df["salary"].count()      # non-null count

# Value counts — how many of each?
df["dept"].value_counts()

# Group by department
df.groupby("dept")["salary"].mean()
df.groupby("dept").agg({"salary": ["mean", "min", "max"], "name": "count"})
```

---

## Saving Data

```python
df.to_csv("output.csv", index=False)         # index=False skips row numbers
df.to_excel("output.xlsx", index=False)
df.to_json("output.json", orient="records")
```

---

## Exercises

Create `pandas_basics.py`. Download a CSV or create one to work with — or use this:

```python
import pandas as pd
import io

csv_data = """name,dept,salary,years
Frank,Operations,90000,5
Alice,Engineering,105000,3
Bob,Operations,85000,7
Carol,Engineering,112000,2
Dave,Marketing,78000,4
Eve,Engineering,98000,6
Frank2,Marketing,82000,1
"""
df = pd.read_csv(io.StringIO(csv_data))
```

**Exercise 1:** Print the shape, column names, and first 3 rows.

**Exercise 2:** Find all employees in Engineering. Print their names and salaries.

**Exercise 3:** What's the average salary by department? Which department pays the most on average?

**Exercise 4:** Add a new column `"bonus"` that is 10% of salary. Then add a `"total_comp"` column that is salary + bonus.

**Exercise 5:** Find employees who have been at the company more than 4 years AND earn less than $90,000. Print how many there are and list their names.

**Exercise 6 (stretch):** Group by department and compute: average salary, total headcount, and the name of the highest-paid employee in each department.

---

## Key Takeaway
`pd.read_csv()` loads data. `.head()`, `.info()`, `.describe()` tell you what you have. Filter with boolean conditions using `df[condition]`. Aggregate with `.mean()`, `.sum()`, `.groupby()`. Save with `.to_csv()`. The Pandas docs are excellent — search "pandas [what you want to do]" and you'll find it.

**Next:** [Lesson 21 — Cleaning & Transforming Data →](./21-data-cleaning.md)
