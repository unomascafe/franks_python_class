# Lesson 12 — CSV & JSON

## What You'll Learn
- Read and write CSV files with the `csv` module
- Parse and generate JSON with the `json` module
- Understand when to use each format

---

## CSV Files

CSV (Comma-Separated Values) is the universal format for tabular data. Every row is a line; values are separated by commas.

```
name,age,city
Frank,42,Mesa
Alice,31,Phoenix
Bob,28,Tempe
```

### Reading CSV

```python
import csv

with open("people.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)   # reads each row as a dict
    for row in reader:
        print(row["name"], row["age"])
```

`DictReader` uses the first row as header keys — almost always what you want.

### Writing CSV

```python
import csv

people = [
    {"name": "Frank", "age": 42, "city": "Mesa"},
    {"name": "Alice", "age": 31, "city": "Phoenix"},
]

with open("output.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(people)
```

Note: Use `newline=""` when writing CSVs on Windows to prevent extra blank lines.

---

## JSON

JSON (JavaScript Object Notation) is the universal format for structured data and APIs. Python dicts and lists map directly to JSON objects and arrays.

```json
{
  "name": "Frank",
  "age": 42,
  "skills": ["Python", "Operations", "3D Printing"],
  "address": {
    "city": "Mesa",
    "state": "AZ"
  }
}
```

### Reading JSON

```python
import json

# From a file
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data["name"])       # "Frank"
print(data["skills"][0])  # "Python"

# From a string
json_string = '{"name": "Frank", "age": 42}'
data = json.loads(json_string)   # note: loads (with s for string)
```

### Writing JSON

```python
import json

data = {
    "name": "Frank",
    "scores": [95, 87, 100],
    "active": True
}

# To a file
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)   # indent=2 makes it readable

# To a string
json_string = json.dumps(data, indent=2)
print(json_string)
```

---

## When to Use Which

| Format | Use for |
|--------|---------|
| CSV | Tabular data, spreadsheets, rows × columns |
| JSON | Structured/nested data, API responses, config files |

If data fits in a spreadsheet → CSV. If it has nesting or structure → JSON.

---

## Exercises

Create `csv_json.py` and some sample data files.

**Exercise 1:** Create a CSV file with 5 employees (name, department, salary). Write a script that reads it and prints:
- All employees in "Operations"
- The average salary
- The highest-paid employee

**Exercise 2:** Download (or create) a JSON file with a list of 3D printing projects:
```json
[
  {"name": "Bracket v2", "material": "PLA", "hours": 3.5, "complete": true},
  {"name": "Phone Stand", "material": "PETG", "hours": 1.2, "complete": false}
]
```
Read the file and print only the incomplete projects.

**Exercise 3:** Write a function `csv_to_json(csv_file, json_file)` that converts a CSV file to a JSON array and saves it.

**Exercise 4:** Write a function `save_config(config_dict, filename)` and `load_config(filename)` that save/load a configuration dictionary as JSON. Add a default value so `load_config` returns `{}` if the file doesn't exist.

**Exercise 5 (stretch):** Write a script that reads a CSV of product orders, calculates the total revenue per product, and writes the summary back as a new CSV.

---

## Key Takeaway
`csv.DictReader` and `csv.DictWriter` are the standard for CSV. `json.load()`/`json.dump()` for files, `json.loads()`/`json.dumps()` for strings. JSON is the language of APIs — get comfortable with it now.

**Next:** [Lesson 13 — Installing & Using Libraries →](./13-libraries.md)
