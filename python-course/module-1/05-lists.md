# Lesson 05 — Lists

## What You'll Learn
- Create and modify lists
- Access items by index
- Loop over lists, sort them, slice them
- Understand when to use a list vs. other types

---

## Why Lists Matter

So far we've worked with one value at a time — a single string, a single number. But almost nothing in real programs is one value. You have a list of tasks, a list of users, a list of prices, a list of files in a folder. The moment you want to deal with *many of something*, you reach for a **list**.

A list is Python's most basic way of holding a group of values in a single variable, in a specific order. You can add to it, remove from it, sort it, search it, and loop over every item one at a time. Most programs you'll ever write will lean heavily on lists, so this lesson is worth slowing down for.

---

## Creating a List

You write a list as a comma-separated sequence of values inside **square brackets**:

```python
tasks = ["buy filament", "run print job", "sand and prime"]
scores = [95, 87, 100, 72, 88]
mixed = ["Frank", 42, True, 3.14]
empty = []
```

A few things to notice:

- The brackets `[ ]` are how Python knows "this is a list." Different from the parentheses `( )` we used for function calls.
- A list can hold **any type** of value — strings, numbers, booleans, even other lists. The `mixed` example proves it.
- In practice, lists usually hold values of one type — all tasks, all scores. Mixing types is legal but usually a sign you should use a different structure (we'll get to dictionaries next lesson).
- `empty = []` makes an empty list. You'll do this often — create an empty list, then add to it as your program runs.

---

## Accessing Items by Index

Each item in a list has a position, called its **index**. Python (like most programming languages) starts counting at zero, not one. This trips up almost every beginner, so it's worth saying out loud: **the first item is at index 0, not index 1.**

```python
items = ["a", "b", "c", "d"]
items[0]    # "a"   ← first item
items[1]    # "b"
items[2]    # "c"
items[3]    # "d"   ← last item (the list has 4 items, last index is 3)
```

You access an item by writing the list's name followed by square brackets containing the index.

Python also supports **negative indexing**, which counts backward from the end. `-1` means "the last item," `-2` means "second to last," and so on:

```python
items[-1]   # "d"  (last item)
items[-2]   # "c"  (second to last)
```

This is enormously useful. Instead of writing `items[len(items) - 1]` to get the last item, you just write `items[-1]`. You'll use this all the time.

---

## Slicing — Grabbing a Range

If you want more than one item — a chunk of the list — you use **slicing**, with the same `start:stop` syntax we saw with strings:

```python
items = ["a", "b", "c", "d"]
items[1:3]   # ["b", "c"]
items[:2]    # ["a", "b"]   (from the beginning)
items[2:]    # ["c", "d"]   (to the end)
```

One important quirk: the slice goes **up to but not including** the stop index. `items[1:3]` gives you indexes 1 and 2, but not 3. This is consistent with how `range()` and other Python features work, but it surprises everyone the first few times.

A slice always gives you back a **new list** — it doesn't modify the original.

---

## Modifying Lists

Unlike strings (which can't be changed once created), lists are **mutable** — you can add to them, remove from them, and change items in place after they're made.

```python
colors = ["red", "green", "blue"]

# Add items
colors.append("yellow")          # adds to the end
colors.insert(1, "orange")       # inserts at index 1, pushing others down

# Remove items
colors.remove("green")           # removes the first match by value
popped = colors.pop()            # removes AND returns the last item
popped = colors.pop(0)           # removes AND returns the item at index 0
del colors[1]                    # removes by index, no return value

# Update
colors[0] = "crimson"            # replaces the item at index 0
```

A few things worth understanding here:

- `.append()` is by far the most common. You'll use it in nearly every loop that builds up a list.
- `.pop()` is special because it both removes *and* hands you back the removed item. That's useful when you're processing items one at a time and want to consume them.
- `.remove()` removes by **value**, but `del` and `.pop()` work by **index**. Pick the right one for what you have.
- `.remove()` only removes the *first* match. If the value appears twice, only the first one goes.

A common beginner mistake: `colors.append(...)` modifies `colors` in place and returns `None`. So this is wrong:

```python
colors = colors.append("pink")   # ❌ colors is now None
```

Just call the method directly — don't assign the result back:

```python
colors.append("pink")            # ✅ colors now has "pink" at the end
```

---

## Useful List Operations

Python gives you a bunch of built-in functions and methods for the everyday things you'll want to do with lists:

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

len(numbers)         # 8     — how many items?
sum(numbers)         # 31    — total
min(numbers)         # 1     — smallest
max(numbers)         # 9     — largest
numbers.count(1)     # 2     — how many times does 1 appear?
numbers.index(5)     # 4     — what index is 5 at? (first occurrence)
4 in numbers         # True  — is 4 anywhere in the list?
10 in numbers        # False
```

The `in` operator is especially handy — it's the cleanest way to ask "does the list contain this?" without writing a loop.

### Sorting

```python
numbers.sort()              # sorts in place — modifies the original
numbers.sort(reverse=True)  # descending order
sorted(numbers)             # returns a new sorted list — original unchanged
```

There are two patterns here and they trip people up. `.sort()` is a **method on the list** that changes the list itself and gives back nothing. `sorted()` is a **function** that takes a list, leaves it alone, and gives you back a new sorted one. If you need the original to stay intact, use `sorted()`. If you just want it sorted and don't care about preserving the original, `.sort()` is slightly more efficient.

### Reversing

```python
numbers.reverse()           # in place
numbers[::-1]               # returns a reversed copy (slice with step -1)
```

The `[::-1]` syntax is a slice trick — same logic as `[start:stop:step]`, but with step set to `-1` it walks the list backward.

### Combining lists

```python
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b       # [1, 2, 3, 4, 5, 6] — creates a new list
a.extend(b)     # adds every item of b to the end of a — modifies a
```

`+` makes a new list. `.extend()` modifies the first list in place. Same end result, different memory behavior.

---

## Looping Over Lists

This is where lists really start to earn their keep. Most of the time you're not interested in one item — you want to do something with *every* item. A `for` loop reads each item from the list in order and runs a block of code for each one:

```python
tasks = ["research", "draft", "review", "publish"]

for task in tasks:
    print(task)
```

Read that out loud: "for each task in tasks, print the task." The variable name `task` is just a label — Python assigns the current item to it on each pass through the loop. You could call it `item` or `x`; `task` is just clearer.

Often you want to know the **index** of each item too, not just its value. That's what `enumerate()` is for:

```python
for i, task in enumerate(tasks):
    print(f"{i + 1}. {task}")
```

`enumerate()` wraps the list so each iteration gives you two values: the index and the item. (We add 1 here just to make the printed list 1-indexed for humans.) Output:

```
1. research
2. draft
3. review
4. publish
```

Anytime you find yourself writing a counter variable by hand alongside a loop, `enumerate()` is the cleaner answer.

---

## List Comprehensions

This is one of Python's most-loved features, and the first time you see one it looks like magic. Stick with it — once it clicks, you'll write them constantly.

A **list comprehension** is a compact way to build a new list from an existing one, all on a single line. The classic shape is:

```
[expression for item in list]
```

Read that as: "build a new list, where each entry is *expression*, by walking through every *item* in *list*." Examples:

```python
numbers = [1, 2, 3, 4, 5]

# Square every number
squares = [n ** 2 for n in numbers]
# [1, 4, 9, 16, 25]
```

That's the same as writing:

```python
squares = []
for n in numbers:
    squares.append(n ** 2)
```

The comprehension is shorter and, once you're used to reading them, clearer. You can also tack on a filter with `if`:

```python
# Only keep even numbers
evens = [n for n in numbers if n % 2 == 0]
# [2, 4]

# Both at once: square the evens
squared_evens = [n ** 2 for n in numbers if n % 2 == 0]
# [4, 16]
```

The full pattern is **`[expression for item in list if condition]`**. Read left to right, the expression on the far left is what you're collecting; the `for` part is what you're looping over; the optional `if` part is what you're filtering on.

Don't try to write nested or three-layer comprehensions until you're comfortable with the basics — they get unreadable fast. When a comprehension feels complicated, just write the loop the long way.

---

## Exercises

Create a file called `lists.py`.

**Exercise 1:** Make a list of 5 video games you've played. Print the first one, the last one (using negative indexing), and the list in alphabetical order (using `sorted()`).

**Exercise 2:** Start with `scores = [88, 72, 95, 61, 84, 90]`. Calculate and print: the average score (use `sum()` and `len()`), the highest, the lowest, and how many scores are above 80. For that last one, a list comprehension with `if` is the clean way.

**Exercise 3:** Given `names = ["alice", "bob", "charlie", "dave", "eve"]`, use a list comprehension to build a new list with every name capitalized (the `.capitalize()` string method capitalizes the first letter). Print both the original and the new list to confirm the original is unchanged.

**Exercise 4:** Write code that takes a list of prices and produces a new list with a 10% discount applied to each. Use a list comprehension. For example, `[100, 50, 200]` should become `[90.0, 45.0, 180.0]`.

**Exercise 5 (stretch):** Given a list of filenames:
```python
files = ["report.pdf", "image.png", "data.csv", "notes.txt", "photo.png", "budget.csv"]
```
Use a list comprehension to pick out only the `.csv` files. Then print how many there are. (Hint: the string method `.endswith(".csv")` is what you want for the `if` part.)

---

## Key Takeaway

Lists are **ordered** and **mutable** — items have a position and you can change them in place. Index from `0`; use negative indexes to count from the end. `.append()`, `.pop()`, and `.remove()` cover most of your add/remove needs — just remember they modify the list in place and don't return a new one. Use `in` to check membership. Loop with a plain `for item in list` when you only need the value, or `enumerate()` when you also need the index. List comprehensions look weird at first but become indispensable — they're how you write "take this list and turn it into a new one" without a full loop.

**Next:** [Lesson 06 — Dictionaries →](./06-dicts.md)
