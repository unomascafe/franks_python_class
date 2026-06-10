# Lesson 07 — Conditionals

## What You'll Learn
- Control what code runs based on conditions
- Use `if`, `elif`, `else`
- Understand comparison and logical operators
- Write clean conditional logic

---

## If / Elif / Else

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Below C")
```

Python reads top to bottom and stops at the first `True` condition. Only one branch runs.

**Indentation is not optional.** Python uses indentation (4 spaces) to define code blocks. If it's not indented, it's not part of the `if`.

---

## Comparison Operators

```python
x = 10
y = 5

x == y    # False  (equal to)
x != y    # True   (not equal to)
x > y     # True   (greater than)
x < y     # False  (less than)
x >= y    # True   (greater than or equal)
x <= y    # False  (less than or equal)
```

**`==` vs `=`**: One equal sign assigns a value. Two equal signs compare values. This is one of the most common beginner errors.

---

## Logical Operators

Combine conditions with `and`, `or`, `not`:

```python
age = 25
has_license = True

if age >= 16 and has_license:
    print("You can drive")

temperature = 95
is_raining = False

if temperature > 90 or is_raining:
    print("Stay inside")

is_admin = False
if not is_admin:
    print("Access denied")
```

---

## Checking Membership

```python
allowed_roles = ["admin", "editor", "moderator"]
role = "editor"

if role in allowed_roles:
    print("Access granted")

# Also works with strings
email = "frank@example.com"
if "@" in email and "." in email:
    print("Looks like a valid email")
```

---

## Truthy and Falsy

In Python, things aren't just `True` or `False` — most values have an implicit truth value:

**Falsy** (treated as `False`):
- `False`
- `0`, `0.0`
- `""` (empty string)
- `[]` (empty list)
- `{}` (empty dict)
- `None`

**Truthy**: everything else

```python
name = ""
if name:
    print(f"Hello, {name}")
else:
    print("No name provided")   # this runs

items = [1, 2, 3]
if items:
    print("List has items")     # this runs
```

This is idiomatic Python — you'll see it constantly.

---

## Inline Conditional (Ternary)

One-line version for simple cases:

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)   # "adult"
```

Only use this when it's genuinely simpler — don't nest them.

---

## Exercises

Create `conditionals.py`.

**Exercise 1:** Write a function `classify_temp(temp)` that returns:
- `"freezing"` if below 32
- `"cold"` if 32–59
- `"comfortable"` if 60–79
- `"hot"` if 80–99
- `"extreme"` if 100 or above

Test it with several values.

**Exercise 2:** Write a function `can_access(role, is_active)` that returns `True` only if the user's role is `"admin"` or `"editor"` AND their account is active.

**Exercise 3:** Given a list of products:
```python
products = [
    {"name": "Filament", "price": 22.99, "in_stock": True},
    {"name": "Print Bed", "price": 45.00, "in_stock": False},
    {"name": "Nozzle Kit", "price": 15.50, "in_stock": True},
    {"name": "Enclosure", "price": 189.99, "in_stock": True},
]
```
Print only the products that are in stock AND cost less than $50.

**Exercise 4:** Write a function `fizzbuzz(n)` that returns:
- `"FizzBuzz"` if `n` is divisible by both 3 and 5
- `"Fizz"` if only divisible by 3
- `"Buzz"` if only divisible by 5
- The number as a string otherwise

Print the result for every number from 1 to 20.

**Exercise 5 (stretch):** Write a function `password_strength(password)` that returns `"weak"`, `"medium"`, or `"strong"` based on rules you define (e.g., length, has numbers, has uppercase). Keep the logic readable.

---

## Key Takeaway
`if/elif/else` — only one branch runs, top to bottom. `==` compares, `=` assigns. Use `and`, `or`, `not` to combine conditions. Python's truthy/falsy values let you write clean checks like `if items:` instead of `if len(items) > 0:`.

**Next:** [Lesson 08 — Loops →](./08-loops.md)
