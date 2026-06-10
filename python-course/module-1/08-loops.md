# Lesson 08 — Loops

## What You'll Learn
- Repeat code with `for` and `while` loops
- Control loops with `break`, `continue`, and `else`
- Use `range()` and `enumerate()`
- Know when to use each type

---

## For Loops

`for` loops iterate over a sequence — a list, string, range, dictionary, etc.

```python
# Loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop over a string (each character)
for char in "Python":
    print(char)

# Loop over a dictionary
config = {"host": "localhost", "port": 8080}
for key, value in config.items():
    print(f"{key} = {value}")
```

---

## range()

`range()` generates a sequence of numbers:

```python
range(5)          # 0, 1, 2, 3, 4
range(1, 6)       # 1, 2, 3, 4, 5
range(0, 10, 2)   # 0, 2, 4, 6, 8  (step of 2)
range(10, 0, -1)  # 10, 9, 8, ... 1  (counting down)
```

```python
for i in range(5):
    print(i)     # 0, 1, 2, 3, 4

for i in range(1, 6):
    print(i)     # 1, 2, 3, 4, 5
```

---

## enumerate()

Get the index AND value when looping:

```python
tasks = ["plan", "build", "test", "ship"]

for i, task in enumerate(tasks):
    print(f"{i + 1}. {task}")
```
```
1. plan
2. build
3. test
4. ship
```

---

## While Loops

`while` runs as long as a condition is `True`:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

Use `while` when you don't know ahead of time how many iterations you need:

```python
attempts = 0
max_attempts = 3
success = False

while attempts < max_attempts and not success:
    response = input("Enter password: ")
    if response == "secret":
        success = True
    else:
        attempts += 1
        print(f"Wrong. {max_attempts - attempts} attempts left.")
```

---

## break and continue

`break` — exit the loop immediately:
```python
numbers = [1, 5, 3, 8, 2, 9, 4]
for n in numbers:
    if n == 8:
        print("Found 8!")
        break       # stop looping
    print(n)
```

`continue` — skip the rest of the current iteration, continue to next:
```python
for i in range(10):
    if i % 2 == 0:
        continue    # skip even numbers
    print(i)        # prints 1, 3, 5, 7, 9
```

---

## Nested Loops

Loops inside loops. Each inner loop runs completely for each iteration of the outer loop:

```python
sizes = ["S", "M", "L"]
colors = ["red", "blue"]

for size in sizes:
    for color in colors:
        print(f"{size} {color}")
```
```
S red
S blue
M red
M blue
L red
L blue
```

Watch out — nested loops multiply iterations. Two loops of 1000 each = 1,000,000 iterations.

---

## Common Patterns

**Accumulating a total:**
```python
prices = [12.99, 5.50, 34.00, 7.25]
total = 0
for price in prices:
    total += price
print(f"Total: ${total:.2f}")
```

**Building a list inside a loop:**
```python
names = ["frank", "alice", "bob"]
capitalized = []
for name in names:
    capitalized.append(name.capitalize())
# Same as: capitalized = [n.capitalize() for n in names]
```

**Finding something:**
```python
users = [{"name": "Alice", "id": 1}, {"name": "Bob", "id": 2}]
target_id = 2
found = None
for user in users:
    if user["id"] == target_id:
        found = user
        break
```

---

## Exercises

Create `loops.py`.

**Exercise 1:** Print a multiplication table for numbers 1–5 (5x5 grid). Use nested loops.

**Exercise 2:** Given `scores = [85, 92, 78, 95, 61, 88, 73, 90]`, use a loop to count how many scores are above 80, and calculate their average separately from the below-80 scores.

**Exercise 3:** Write a loop that prints the first 10 numbers in the Fibonacci sequence: `1, 1, 2, 3, 5, 8, 13, 21, 34, 55`.

**Exercise 4:** Given a list of filenames, loop through and print only the ones that end in `.py`. Then print a count of how many `.py` files there are.
```python
files = ["main.py", "config.json", "utils.py", "README.md", "test.py", "data.csv"]
```

**Exercise 5 (stretch):** Write a while loop that simulates a simple number guessing game. Pick a secret number (hardcode it), then loop asking the user to guess. Tell them "too high" or "too low" each time, and stop when they get it. Count the attempts and print how many it took.

---

## Key Takeaway
`for` loops are for when you know what to iterate over. `while` loops are for when you're waiting for a condition to change. `break` exits, `continue` skips. `enumerate()` is your friend for index + value. Most loops can be replaced with list comprehensions — but not all, and readability wins.

**Next:** [Lesson 09 — Functions →](./09-functions.md)
