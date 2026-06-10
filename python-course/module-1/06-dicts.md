# Lesson 06 — Dictionaries

## What You'll Learn
- Create and use dictionaries (key-value pairs)
- Access, add, update, and delete entries
- Loop over dictionaries
- Nest dicts and use them with lists

---

## What's a Dictionary?

A dictionary stores data as **key-value pairs**. Think of it like a real dictionary: you look up a word (key) and get a definition (value).

```python
person = {
    "name": "Frank",
    "age": 42,
    "city": "Mesa",
    "is_admin": True
}
```

Keys are usually strings. Values can be anything.

---

## Accessing Values

```python
person = {"name": "Frank", "age": 42, "city": "Mesa"}

person["name"]            # "Frank"
person["age"]             # 42

# Safe access — returns None (or a default) if key doesn't exist
person.get("city")        # "Mesa"
person.get("phone")       # None
person.get("phone", "N/A")  # "N/A"
```

Use `.get()` when you're not sure a key exists — `dict["missing_key"]` will throw an error, `.get()` won't.

---

## Modifying Dictionaries

```python
config = {"host": "localhost", "port": 3000}

# Add or update (same syntax)
config["port"] = 8080          # update existing
config["debug"] = True         # add new key

# Delete
del config["debug"]
config.pop("port")             # removes and returns the value

# Check if key exists
"host" in config               # True
"password" in config           # False
```

---

## Looping Over Dictionaries

```python
user = {"name": "Frank", "role": "admin", "active": True}

# Keys only (default)
for key in user:
    print(key)

# Values only
for value in user.values():
    print(value)

# Keys and values (most common)
for key, value in user.items():
    print(f"{key}: {value}")
```

Output from `.items()`:
```
name: Frank
role: admin
active: True
```

---

## Useful Methods

```python
settings = {"theme": "dark", "lang": "en", "notifications": True}

settings.keys()      # dict_keys(['theme', 'lang', 'notifications'])
settings.values()    # dict_values(['dark', 'en', True])
settings.items()     # dict_items([('theme', 'dark'), ...])
len(settings)        # 3

# Merge two dicts (Python 3.9+)
defaults = {"lang": "en", "timezone": "UTC"}
overrides = {"lang": "es", "theme": "dark"}
merged = defaults | overrides
# {"lang": "es", "timezone": "UTC", "theme": "dark"}

# Or update in place
defaults.update(overrides)
```

---

## Nested Dictionaries

Dicts can contain dicts:

```python
users = {
    "frank": {
        "email": "frank@example.com",
        "role": "admin",
        "active": True
    },
    "alice": {
        "email": "alice@example.com",
        "role": "viewer",
        "active": False
    }
}

users["frank"]["email"]    # "frank@example.com"
users["alice"]["role"]     # "viewer"
```

---

## Lists of Dictionaries

This is extremely common — it's basically a table of data:

```python
employees = [
    {"name": "Frank", "dept": "Operations", "salary": 90000},
    {"name": "Alice", "dept": "Engineering", "salary": 105000},
    {"name": "Bob", "dept": "Operations", "salary": 85000},
]

# Print all names
for emp in employees:
    print(emp["name"])

# Find all Operations employees
ops = [e for e in employees if e["dept"] == "Operations"]
```

This pattern — lists of dicts — is how data from APIs, databases, and spreadsheets almost always arrives.

---

## Exercises

Create `dicts.py`.

**Exercise 1:** Create a dictionary for a 3D printing project: name, material, layer height (mm), estimated print time (hours), and whether it's complete. Print each key-value pair on its own line using `.items()`.

**Exercise 2:** Given this list of games:
```python
games = [
    {"title": "Baldur's Gate 3", "genre": "RPG", "hours_played": 120},
    {"title": "Starfield", "genre": "RPG", "hours_played": 40},
    {"title": "Deep Rock Galactic", "genre": "Shooter", "hours_played": 200},
    {"title": "Factorio", "genre": "Strategy", "hours_played": 350},
]
```
Write code to:
- Print the title and hours for every game
- Find the game with the most hours played
- Print all RPGs

**Exercise 3:** Write a function `word_count(text)` that takes a string and returns a dictionary where each key is a unique word and each value is how many times that word appears.
```python
word_count("the cat sat on the mat the cat")
# {"the": 3, "cat": 2, "sat": 1, "on": 1, "mat": 1}
```

**Exercise 4 (stretch):** Start with this config:
```python
defaults = {"debug": False, "port": 3000, "host": "localhost", "log_level": "info"}
overrides = {"port": 8080, "debug": True}
```
Merge them so overrides take priority, then print the final config sorted by key.

---

## Key Takeaway
Dictionaries are key-value stores — fast lookups, flexible structure. `.get()` is safer than `[]` when a key might not exist. Lists of dicts are the standard format for tabular data. Get comfortable with `.items()` for looping.

**Next:** [Lesson 07 — Conditionals →](./07-conditionals.md)
