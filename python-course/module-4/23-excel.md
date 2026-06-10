# Lesson 23 — Excel & Spreadsheets

## What You'll Learn
- Read and write Excel files with `openpyxl` and Pandas
- Work with multiple sheets
- Apply formatting, formulas, and charts to Excel output

---

## Install

```bash
pip install openpyxl xlrd
```

Pandas uses `openpyxl` for `.xlsx` files under the hood — you need it installed even if you only use Pandas.

---

## Reading Excel with Pandas

```python
import pandas as pd

# Single sheet
df = pd.read_excel("report.xlsx")

# Specific sheet
df = pd.read_excel("report.xlsx", sheet_name="Sales")

# All sheets → dict of DataFrames
sheets = pd.read_excel("report.xlsx", sheet_name=None)
for name, df in sheets.items():
    print(f"{name}: {df.shape}")
```

---

## Writing Excel with Pandas

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["Frank", "Alice", "Bob"],
    "Salary": [90000, 105000, 85000],
})

# Single sheet
df.to_excel("output.xlsx", index=False)

# Multiple sheets
with pd.ExcelWriter("output.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Employees", index=False)
    summary_df.to_excel(writer, sheet_name="Summary", index=False)
```

---

## openpyxl — Direct Control

When you need formatting, formulas, or precise control:

```python
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

# Create new workbook
wb = Workbook()
ws = wb.active
ws.title = "Report"

# Write data
ws["A1"] = "Name"
ws["B1"] = "Salary"
ws.append(["Frank", 90000])
ws.append(["Alice", 105000])

# Formatting
ws["A1"].font = Font(bold=True, size=12)
ws["B1"].font = Font(bold=True, size=12)
ws["A1"].fill = PatternFill(fill_type="solid", fgColor="4472C4")

# Column width
ws.column_dimensions["A"].width = 20
ws.column_dimensions["B"].width = 15

# Formula
ws["B4"] = "=SUM(B2:B3)"

wb.save("formatted_report.xlsx")
```

---

## Loading and Modifying Existing Files

```python
from openpyxl import load_workbook

wb = load_workbook("existing.xlsx")
ws = wb["Sheet1"]

# Read a cell
value = ws["A1"].value
value = ws.cell(row=1, column=1).value

# Iterate rows
for row in ws.iter_rows(min_row=2, values_only=True):
    print(row)   # tuple of values

# Modify and save
ws["C1"] = "New Column"
wb.save("updated.xlsx")
```

---

## Exercises

Create `excel_demo.py`.

**Exercise 1:** Create an Excel workbook with two sheets: `"Employees"` (name, dept, salary) and `"Summary"` (average salary per dept). Use `pd.ExcelWriter`.

**Exercise 2:** Open an existing Excel file (create one, or use any you have), read it with Pandas, do some analysis (sort, filter, aggregate), and write the results to a new sheet in the same file.

**Exercise 3:** Use `openpyxl` to create a formatted expense report:
- Header row with bold text and a colored background
- Data rows alternating light gray and white
- A `SUM` formula at the bottom of the amount column
- Auto-sized columns

**Exercise 4 (stretch):** Write a function `excel_diff(file1, file2, sheet)` that reads the same sheet from two Excel files and prints which rows are different (use Pandas `merge` with `indicator=True`).

---

## Key Takeaway
Pandas handles reading and writing Excel for data work. `openpyxl` gives you direct control when you need formatting, formulas, or sheet manipulation. Use `pd.ExcelWriter` for multi-sheet output. `load_workbook` for modifying existing files.

**Next:** [Module 5 — Building Apps & Tools →](../module-5/24-cli-tools.md)
