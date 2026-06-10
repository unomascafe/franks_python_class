# Lesson 05 — Lists

## What You'll Learn
- Create and modify lists
- Access items by index
- Loop over lists, sort them, slice them
- Understand when to use a list vs other types

---

## What's a List?

A list is an ordered collection of items. Items can be any type, and lists can hold mixed types (though usually they hold one type).

```python
tasks = ["buy filament", "run print job", "sand and prime"]
scores = [95, 87, 100, 72, 88]
mixed = ["Frank", 42, True, 3.14]
empty = []
```

---

## Accessing Items

Lists are zero-indexed — first item is at index `0`:

```python
items = ["a", "b", "c", "d"]
items[0]    # "a"
items[2]    # "c"
items[-1]   # "d"  (last item)
items[-2]   # "c"  (second to last)
```

Slicing works just like strings:
```python
items[1:3]   # ["b", "c"]
items[:2]    # ["a", "b"]
items[2:]    # ["c", "d"]
```

---

## Modifying Lists

```python
colors = ["red", "green", "blue"]

# Add items
colors.append("yellow")          # adds to end
colors.insert(1, "orange")       # inserts at index 1

# Remove items
colors.remove("green")           # removes by value
popped = colors.pop()            # removes and returns last item
popped = colors.pop(0)           # removes and returns item at index 0
del colors[1]                    # removes by index

# Update
colors[0] = "crimson"            # replace an item
```

---

## Useful List Operations

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

len(numbers)         # 8
sum(numbers)         # 31
min(numbers)         # 1
max(numbers)         # 9
numbers.count(1)     # 2  (how many times 1 appears)
numbers.index(5)     # 4  (index of first occurrence of 5)
4 in numbers         # True
10 in numbers        # False
```

Sorting:
```python
numbers.sort()              # sorts in place (modifies original)
numbers.sort(reverse=True)  # descending
sorted(numbers)             # returns a new sorted list, original unchanged
```

Reversing:
```python
numbers.reverse()           # in place
numbers[::-1]               # returns reversed copy
```

Combining:
```python
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b       # [1, 2, 3, 4, 5, 6]
a.extend(b)     # adds all of b to a in place
```

---

## Looping Over Lists

```python
tasks = ["research", "draft", "review", "publish"]

for task in tasks:
    print(task)
```

With index:
```python
for i, task in enumerate(tasks):
    print(f"{i + 1}. {task}")
```

Output:
```
1. research
2. draft
3. review
4. publish
```

---

## List Comprehensions

A compact way to build a list from another list:

```python
numbers = [1, 2, 3, 4, 5]

# Square every number
squares = [n ** 2 for n in numbers]
# [1, 4, 9, 16, 25]

# Only keep even numbers
evens = [n for n in numbers if n % 2 == 0]
# [2, 4]

# Both: square the evens
squared_evens = [n ** 2 for n in numbers if n % 2 == 0]
# [4, 16]
```

This is one of Python's most useful features. Learn to read it: **[expression for item in list if condition]**.

---

## Exercises

Create `lists.py`.

**Exercise 1:** Create a list of 5 video games you've played. Print the first one, the last one, and the list in alphabetical order.

**Exercise 2:** Start with `scores = [88, 72, 95, 61, 84, 90]`. Calculate and print: the average score, the highest score, the lowest score, and how many scores are above 80.

**Exercise 3:** Given `names = ["alice", "bob", "charlie", "dave", "eve"]`, use a list comprehension to create a new list with all names capitalized. Print both lists.

**Exercise 4:** Write code that takes a list of prices and returns a new list with a 10% discount applied to each price. Use a list comprehension.

**Exercise 5 (stretch):** Given a list of filenames:
```python
files = ["report.pdf", "image.png", "data.csv", "notes.txt", "photo.png", "budget.csv"]
```
Use a list comprehension to get only the `.csv` files. Then print how many there are.

---

## Key Takeaway
Lists are ordered and mutable (changeable). Zero-indexed. `.append()`, `.remove()`, `.pop()` are your most-used methods. List comprehensions are powerful once they click — practice reading them. Looping with `enumerate()` gives you index + value at the same time.

**Next:** [Lesson 06 — Dictionaries →](./06-dicts.md)
