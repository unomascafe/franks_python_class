# Lesson 10 — Error Handling

## What You'll Learn
- Understand Python's exception system
- Catch and handle errors gracefully
- Raise your own exceptions
- Use `finally` for cleanup
- Read tracebacks

---

## What Are Exceptions?

When Python hits a problem it can't handle, it raises an **exception** and stops running. You've probably already seen a few:

```
ValueError: invalid literal for int() with base 10: 'hello'
TypeError: can only concatenate str (not "int") to str
FileNotFoundError: [Errno 2] No such file or directory: 'data.csv'
KeyError: 'username'
IndexError: list index out of range
ZeroDivisionError: division by zero
```

Unhandled exceptions crash your program. Error handling lets you catch them and decide what to do instead.

---

## try / except

```python
try:
    number = int("hello")   # this will fail
except ValueError:
    print("That's not a valid number.")
```

The code inside `try` runs. If it raises a `ValueError`, execution jumps to `except` — nothing crashes.

---

## Catching Multiple Exception Types

```python
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Can't divide by zero.")
        return None
    except TypeError:
        print("Both values must be numbers.")
        return None
```

Or catch multiple in one line:
```python
except (ZeroDivisionError, TypeError):
    print("Something went wrong with the math.")
```

---

## The Exception Object

Get details about what went wrong:

```python
try:
    value = int("oops")
except ValueError as e:
    print(f"Error: {e}")
    # Error: invalid literal for int() with base 10: 'oops'
```

---

## else and finally

`else` — runs only if no exception was raised:

```python
try:
    result = int("42")
except ValueError:
    print("Bad input")
else:
    print(f"Success: {result}")   # runs if no exception
```

`finally` — always runs, whether or not there was an exception. Use for cleanup:

```python
file = None
try:
    file = open("data.txt")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    if file:
        file.close()   # always close the file
```

---

## Raising Your Own Exceptions

Raise exceptions intentionally when inputs are invalid:

```python
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0 or age > 150:
        raise ValueError(f"Age {age} is not realistic")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"Invalid age: {e}")
```

---

## Reading Tracebacks

When your code crashes, Python shows a traceback. Read it **bottom up** — the last line tells you the error type and message, and the lines above show where it happened:

```
Traceback (most recent call last):
  File "main.py", line 15, in <module>
    result = process(data)
  File "main.py", line 8, in process
    return items[10]
IndexError: list index out of range
```

The error is `IndexError: list index out of range`. It happened on line 8, inside the `process` function, which was called from line 15. Start at the bottom, read the error, then look at the code on that line.

---

## Common Exceptions Cheat Sheet

| Exception | When it happens |
|-----------|----------------|
| `ValueError` | Right type, wrong value (`int("abc")`) |
| `TypeError` | Wrong type (`"a" + 1`) |
| `KeyError` | Dict key doesn't exist (`d["missing"]`) |
| `IndexError` | List index out of range |
| `FileNotFoundError` | File doesn't exist |
| `ZeroDivisionError` | Dividing by zero |
| `AttributeError` | Object doesn't have that attribute |
| `ImportError` | Module can't be found |

---

## Exercises

Create `errors.py`.

**Exercise 1:** Write a function `safe_int(value)` that tries to convert a value to an integer and returns `None` if it fails (instead of crashing).

**Exercise 2:** Write a function `get_dict_value(d, key, default=None)` that safely gets a value from a dictionary without crashing if the key doesn't exist. (Yes, `.get()` already does this — but write the try/except version for practice.)

**Exercise 3:** Write a function `load_config(filename)` that tries to open and read a file. If the file doesn't exist, print a warning and return an empty dictionary. If the file exists but contains invalid content, catch that too.

**Exercise 4:** Write a function `divide(a, b)` that:
- Raises `TypeError` if either argument isn't a number
- Raises `ValueError` if `b` is zero
- Returns `a / b` otherwise

Write tests that call it with bad inputs and catch the appropriate exceptions.

**Exercise 5 (stretch):** Write a function that reads a list of numbers from a string like `"10, 25, abc, 40, xyz, 15"`, converts each to an integer, skips any that aren't valid numbers (with a warning), and returns the valid ones as a list. Use `continue` inside a loop with a try/except.

---

## Module 1 Complete

You now know the core language. Here's what you can do:

- Store and manipulate data (variables, strings, numbers, lists, dicts)
- Control program flow (conditionals, loops)
- Organize logic into reusable functions
- Handle errors gracefully

That's enough to write real, useful programs. Everything in the remaining modules builds directly on this.

---

## Key Takeaway
Don't let your programs crash on bad input — catch exceptions with `try/except`. Only catch what you expect; let unexpected errors surface so you can fix them. Read tracebacks bottom-up. `finally` is for cleanup that must always happen.

**Next:** [Module 2 — Working with Files & Data →](../module-2/11-file-io.md)
