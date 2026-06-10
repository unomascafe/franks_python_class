# Lesson 09 — Functions

## What You'll Learn
- Write reusable functions
- Work with parameters, defaults, and return values
- Understand scope
- Use *args and **kwargs

---

## Why Functions?

Functions let you name a block of code and reuse it. Without them, you'd copy-paste constantly and maintain 10 versions of the same logic.

---

## Defining and Calling

```python
def greet():
    print("Hello, world!")

greet()   # call it
greet()   # call it again
```

---

## Parameters and Arguments

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Frank")    # Hello, Frank!
greet("Alice")    # Hello, Alice!
```

Multiple parameters:
```python
def greet(name, title):
    print(f"Hello, {title} {name}!")

greet("Taylor", "Mr.")
```

---

## Return Values

Functions can send a value back to whoever called them:

```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)     # 7
```

`return` ends the function immediately. A function without a `return` statement returns `None`.

Return multiple values (Python returns them as a tuple):
```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 8, 5, 2])
print(low, high)   # 1 8
```

---

## Default Parameters

Give a parameter a default value so it's optional:

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Frank")              # Hello, Frank!
greet("Frank", "Hey")       # Hey, Frank!
```

Parameters with defaults must come **after** required parameters.

---

## Keyword Arguments

Call a function using parameter names:

```python
def create_user(name, role, active=True):
    return {"name": name, "role": role, "active": active}

# Positional (order matters)
create_user("Frank", "admin")

# Keyword (order doesn't matter)
create_user(role="admin", name="Frank")
create_user("Frank", role="viewer", active=False)
```

---

## Scope

Variables inside a function are **local** — they only exist inside that function:

```python
def do_thing():
    x = 10       # local variable
    print(x)

do_thing()
print(x)   # NameError: x is not defined
```

Variables defined outside functions are **global** and can be read inside functions, but don't modify them from inside unless you have a good reason:

```python
MAX_RETRIES = 3   # global constant (fine to read inside functions)

def attempt():
    for i in range(MAX_RETRIES):
        print(f"Attempt {i + 1}")
```

---

## *args and **kwargs

Accept a variable number of positional arguments with `*args`:

```python
def total(*numbers):
    return sum(numbers)

total(1, 2, 3)        # 6
total(10, 20, 30, 40) # 100
```

Accept a variable number of keyword arguments with `**kwargs`:

```python
def build_query(**filters):
    for key, value in filters.items():
        print(f"{key} = {value}")

build_query(status="active", role="admin", dept="ops")
```

---

## Docstrings

Document what your function does:

```python
def calculate_discount(price, discount_percent):
    """
    Apply a percentage discount to a price.
    
    Args:
        price: Original price (float)
        discount_percent: Discount as a percentage (e.g., 10 for 10%)
    
    Returns:
        Discounted price (float)
    """
    return price * (1 - discount_percent / 100)
```

Get into the habit of writing docstrings — your future self will thank you.

---

## Exercises

Create `functions.py`.

**Exercise 1:** Write a function `celsius_to_fahrenheit(c)` and a function `fahrenheit_to_celsius(f)`. Test both with several values.

**Exercise 2:** Write a function `summarize_list(numbers)` that returns a dictionary with:
- `min`, `max`, `sum`, `average`, and `count`

Test it with `[10, 25, 8, 42, 17, 31]`.

**Exercise 3:** Write a function `format_currency(amount, symbol="$", decimals=2)` that formats a number as currency. The symbol and decimals should have defaults but be overridable.
```python
format_currency(1999.5)             # "$1999.50"
format_currency(1999.5, "€")        # "€1999.50"
format_currency(1999.5, decimals=0) # "$2000"
```

**Exercise 4:** Write a function `filter_and_sort(items, key, reverse=False)` that takes a list of dicts, a key to sort by, and an optional reverse flag. It should return the list sorted by that key.
```python
products = [
    {"name": "Nozzle", "price": 12.00},
    {"name": "Filament", "price": 22.99},
    {"name": "Enclosure", "price": 189.99},
    {"name": "Print Bed", "price": 45.00},
]
filter_and_sort(products, "price")              # cheap to expensive
filter_and_sort(products, "price", reverse=True) # expensive to cheap
filter_and_sort(products, "name")               # alphabetical
```

**Exercise 5 (stretch):** Write a function `flatten(nested_list)` that takes a list of lists and returns a single flat list.
```python
flatten([[1, 2], [3, 4], [5]])   # [1, 2, 3, 4, 5]
```
Then write a version that handles multiple levels of nesting.

---

## Key Takeaway
Functions are the building block of all real programs. Define with `def`, return values with `return`, document with docstrings. Defaults make functions flexible. Scope keeps variables contained. Once you're comfortable writing functions, you're writing real software.

**Next:** [Lesson 10 — Error Handling →](./10-errors.md)
