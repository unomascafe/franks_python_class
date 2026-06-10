# Lesson 22 — Visualizations

## What You'll Learn
- Create charts with `matplotlib` and `seaborn`
- Plot from Pandas DataFrames directly
- Save charts to files

---

## Install

```bash
pip install matplotlib seaborn
```

---

## matplotlib Basics

```python
import matplotlib.pyplot as plt

# Line chart
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 6, 3]
plt.plot(x, y)
plt.title("My Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# Save to file instead of showing
plt.savefig("chart.png", dpi=150, bbox_inches="tight")
plt.close()
```

---

## Common Chart Types

```python
import matplotlib.pyplot as plt
import numpy as np

# Bar chart
categories = ["Ops", "Eng", "Marketing"]
values = [90000, 108000, 80000]
plt.bar(categories, values, color="steelblue")
plt.title("Average Salary by Department")
plt.ylabel("Salary ($)")
plt.show()

# Histogram
data = np.random.normal(75, 10, 200)
plt.hist(data, bins=20, color="steelblue", edgecolor="white")
plt.title("Score Distribution")
plt.show()

# Scatter plot
x = np.random.rand(50)
y = x * 2 + np.random.rand(50) * 0.5
plt.scatter(x, y, alpha=0.6)
plt.title("Scatter Plot")
plt.show()

# Pie chart
labels = ["Ops", "Eng", "Marketing"]
sizes = [40, 45, 15]
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Headcount by Department")
plt.show()
```

---

## Plotting from Pandas

Pandas has built-in plotting that wraps matplotlib:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "dept": ["Ops", "Eng", "Marketing", "Ops", "Eng"],
    "salary": [90000, 105000, 78000, 85000, 112000],
    "years": [5, 3, 4, 7, 2]
})

# Bar chart from groupby
df.groupby("dept")["salary"].mean().plot(kind="bar", title="Avg Salary")
plt.tight_layout()
plt.show()

# Scatter from DataFrame columns
df.plot.scatter(x="years", y="salary", title="Salary vs Tenure")
plt.show()

# Histogram
df["salary"].plot.hist(bins=10, title="Salary Distribution")
plt.show()
```

---

## seaborn — Nicer Charts with Less Code

`seaborn` is built on top of matplotlib and makes statistical plots much easier:

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    "dept": ["Ops", "Eng", "Marketing", "Ops", "Eng", "Eng"],
    "salary": [90000, 105000, 78000, 85000, 112000, 98000],
})

# Box plot
sns.boxplot(data=df, x="dept", y="salary")
plt.title("Salary Distribution by Department")
plt.show()

# Bar chart with error bars
sns.barplot(data=df, x="dept", y="salary", errorbar="sd")
plt.show()

# Scatter with regression line
sns.regplot(data=df, x="years", y="salary")
plt.show()
```

---

## Exercises

Create `visualization.py`.

**Exercise 1:** Create a bar chart showing the average salary per department using a DataFrame you make up (at least 4 departments).

**Exercise 2:** Generate 1000 random numbers using `np.random.normal(mean=70, std=10)` and plot them as a histogram. Add vertical lines for the mean and ±1 standard deviation.

**Exercise 3:** Create a scatter plot of "years at company" vs "salary" with at least 15 data points. Color the points by department.

**Exercise 4:** Make a figure with 4 subplots (2×2 grid) — one bar chart, one line chart, one scatter, one histogram — all from the same employee dataset. Save it to `charts.png`.

**Exercise 5 (stretch):** Using real data (download a CSV from [Kaggle](https://kaggle.com) or use one you have), create 3 meaningful visualizations and save them to files. Write a short comment above each plot explaining what it shows.

---

## Key Takeaway
`plt.show()` displays, `plt.savefig()` saves. Pandas `.plot()` is fast for quick charts. Seaborn is better for statistical charts with less code. Always label axes and title your charts — unlabeled charts are meaningless to anyone but you.

**Next:** [Lesson 23 — Excel & Spreadsheets →](./23-excel.md)
