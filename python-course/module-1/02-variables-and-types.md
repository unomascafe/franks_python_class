# Lesson 02 — Variables & Data Types

## What You'll Learn
- Store values in variables
- Understand Python's core data types
- Check what type something is

---

## Variables

A variable is a named container for a value. You create one with `=`:

```python
name = "Frank"
age = 42
height = 6.0
is_admin = True
```

Rules for variable names:
- Letters, numbers, underscores only (no spaces)
- Can't start with a number
- Case-sensitive: `name` and `Name` are different variables
- Convention: use `snake_case` (lowercase with underscores)

---

## Core Data Types

### str — Strings (text)
```python
name = "Frank"
city = 'Mesa'          # single or double quotes both work
greeting = "Hey there"
```

### int — Integers (whole numbers)
```python
age = 42
score = 1000
year = 2024
```

### float — Floating point (decimal numbers)
```python
height = 6.0
price = 19.99
ratio = 0.75
```

### bool — Boolean (True or False)
```python
is_logged_in = True
has_premium = False
```

### None — Nothing / empty
```python
result = None   # placeholder when you don't have a value yet
```

---

## Checking Types

Use `type()` to see what type a variable is:

```python
name = "Frank"
print(type(name))    # <class 'str'>

age = 42
print(type(age))     # <class 'int'>

score = 9.5
print(type(score))   # <class 'float'>
```

---

## Type Conversion

You can convert between types:

```python
age_text = "25"
age_number = int(age_text)      # "25" → 25
price = float("19.99")          # "19.99" → 19.99
as_text = str(42)               # 42 → "42"
```

This comes up constantly when reading data from files or user input — everything starts as text, and you convert it to what you need.

---

## Multiple Assignment

You can assign multiple variables in one line:

```python
x, y, z = 1, 2, 3
first, last = "Frank", "Taylor"
```

---

## Exercises

Create a file called `variables.py`.

**Exercise 1:** Create a variable for each of these: your name, your age, your city, and whether you've ever written code before (`True`/`False`). Print them all.

**Exercise 2:** Run this code and explain the output:
```python
a = "5"
b = 5
print(a == b)
print(type(a) == type(b))
```

**Exercise 3:** The user's age is stored as the string `"34"`. Convert it to an integer, add 10, and print the result.

**Exercise 4 (stretch):** What happens when you try `int("hello")`? Run it and read the error. What type of error is it?

---

## Key Takeaway
Variables store values. Python has a handful of core types: `str`, `int`, `float`, `bool`, `None`. Type matters — `"5"` and `5` are different things. Use `type()` when you're not sure what you've got.

**Next:** [Lesson 03 — Strings →](./03-strings.md)
