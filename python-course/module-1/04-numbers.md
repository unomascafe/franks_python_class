# Lesson 04 — Numbers & Math

## What You'll Learn
- Work with integers and floats
- Use Python's math operators
- Round, format, and work with the `math` module

---

## Arithmetic Operators

```python
a = 10
b = 3

a + b    # 13  (addition)
a - b    # 7   (subtraction)
a * b    # 30  (multiplication)
a / b    # 3.3333...  (division — always returns float)
a // b   # 3   (floor division — rounds down to int)
a % b    # 1   (modulo — remainder)
a ** b   # 1000  (exponentiation — 10 to the power of 3)
```

`//` and `%` are more useful than they look:
- `//` is handy for dividing things into groups
- `%` is great for checking if a number is even/odd, or cycling through values

```python
# Is a number even?
number = 42
print(number % 2 == 0)   # True

# What page am I on if I'm at item 37, showing 10 per page?
print(37 // 10 + 1)      # 4
```

---

## Order of Operations

Standard math rules apply (PEMDAS). Use parentheses to be explicit:

```python
result = 2 + 3 * 4       # 14  (multiplication first)
result = (2 + 3) * 4     # 20  (addition first)
```

---

## Updating Variables

```python
count = 0
count = count + 1   # count is now 1
count += 1          # shorthand — same thing
count -= 5
count *= 2
count //= 3
```

---

## Rounding & Formatting

```python
price = 19.9999

round(price)          # 20
round(price, 2)       # 20.0
round(price, 1)       # 20.0

# Format as string with 2 decimal places
f"{price:.2f}"        # "20.00"
f"{1000000:,}"        # "1,000,000"  (comma separator)
f"{0.456:.1%}"        # "45.6%"  (as percentage)
```

---

## The math Module

Python's built-in `math` module covers most math operations you'll need:

```python
import math

math.sqrt(16)         # 4.0
math.ceil(4.1)        # 5  (round up)
math.floor(4.9)       # 4  (round down)
math.abs(-5)          # 5  (absolute value — also works as just abs(-5))
math.pi               # 3.14159...
math.pow(2, 10)       # 1024.0
```

---

## Integer vs Float

Division always returns a float:
```python
10 / 2     # 5.0 (float, not 5)
10 // 2    # 5   (int)
```

If you mix an int and a float in a calculation, you get a float back:
```python
3 + 1.0    # 4.0
```

---

## Exercises

Create `numbers.py`.

**Exercise 1:** You're buying gear for a 3D print project. Items cost $12.50, $8.75, and $34.00. Calculate the total, the tax (8.5%), and the grand total. Print each value formatted to 2 decimal places.

**Exercise 2:** Write code that takes a number of minutes (e.g., `137`) and prints it as hours and minutes: `"2 hours, 17 minutes"`. Use `//` and `%`.

**Exercise 3:** A game scores experience points. The player earns 350 XP per level. If they have 2,740 XP total, what level are they on, and how much XP until the next level? Print both.

**Exercise 4:** Write code that checks if a given year is a leap year. A year is a leap year if it's divisible by 4, EXCEPT century years (divisible by 100), which must also be divisible by 400.
- Test with: 2024 (yes), 1900 (no), 2000 (yes), 2023 (no)

---

## Key Takeaway
`/` always gives a float. `//` and `%` are underrated. f-strings with format specs (`.2f`, `,`, `%`) handle most number formatting. Import `math` when you need something beyond the basics.

**Next:** [Lesson 05 — Lists →](./05-lists.md)
