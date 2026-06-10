# Lesson 03 — Strings

## What You'll Learn
- Manipulate and format strings
- Access parts of a string
- Use the most common string methods

---

## String Basics

Strings are text. They can be wrapped in single `'`, double `"`, or triple `"""` quotes:

```python
name = "Frank"
note = 'Single quotes work too'
multiline = """This string
spans multiple
lines."""
```

---

## String Concatenation

Join strings with `+`:

```python
first = "Frank"
last = "Taylor"
full_name = first + " " + last
print(full_name)   # Frank Taylor
```

---

## f-Strings (the right way to format strings)

f-strings let you embed variables directly in a string. Put `f` before the quote and use `{}` to insert values:

```python
name = "Frank"
city = "Mesa"
age = 42

print(f"My name is {name}, I live in {city}, and I'm {age} years old.")
# My name is Frank, I live in Mesa, and I'm 42 years old.
```

You can put any expression inside `{}`:
```python
price = 19.99
quantity = 3
print(f"Total: ${price * quantity:.2f}")   # Total: $59.97
```

The `:.2f` formats the number to 2 decimal places.

---

## String Indexing & Slicing

Strings are sequences — each character has a position (index), starting at 0:

```python
name = "Frank"
print(name[0])     # F
print(name[1])     # r
print(name[-1])    # k  (negative index counts from the end)
```

Slicing gets a chunk: `[start:end]` (end is not included):
```python
word = "Python"
print(word[0:3])   # Pyt
print(word[2:])    # thon  (to the end)
print(word[:4])    # Pyth  (from the start)
```

---

## Common String Methods

Methods are functions that belong to a string. Call them with a dot:

```python
text = "  Hello, World!  "

text.upper()          # "  HELLO, WORLD!  "
text.lower()          # "  hello, world!  "
text.strip()          # "Hello, World!"       (removes whitespace from edges)
text.replace("World", "Frank")   # "  Hello, Frank!  "
text.split(", ")      # ["  Hello", "World!  "]
```

Checking:
```python
email = "frank@example.com"
email.startswith("frank")   # True
email.endswith(".com")       # True
"@" in email                 # True
```

Finding and counting:
```python
sentence = "the cat sat on the mat"
sentence.find("cat")         # 4  (index where "cat" starts)
sentence.count("at")         # 3
```

Length:
```python
name = "Frank"
len(name)   # 5
```

---

## Exercises

Create `strings.py`.

**Exercise 1:** Given `username = "  FrankT  "`, write code that:
- Strips the whitespace
- Converts it to lowercase
- Prints the result

**Exercise 2:** Given `full_name = "Frank Taylor"`, print just the first name and just the last name using slicing (hint: use `split()`).

**Exercise 3:** Build a function that takes a person's first name, last name, and job title and prints a formatted introduction:
```
Hi, I'm Frank Taylor — Operations Manager.
```

**Exercise 4:** Given the string `"hello world"`, write code that capitalizes the first letter of each word (hint: look up the `.title()` method).

**Exercise 5 (stretch):** Write code that takes a filename like `"report_2024_q3.csv"` and prints just the base name without the extension (`"report_2024_q3"`). Don't hardcode the position — make it work for any filename.

---

## Key Takeaway
f-strings are your best friend for formatting. String methods (`.strip()`, `.split()`, `.replace()`, `.upper()`, etc.) do most of the heavy lifting. Indexing and slicing let you grab exactly the part you need.

**Next:** [Lesson 04 — Numbers & Math →](./04-numbers.md)
