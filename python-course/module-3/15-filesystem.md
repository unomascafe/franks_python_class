# Lesson 15 — File System Operations

## What You'll Learn
- Navigate the file system with `pathlib`
- List, create, move, copy, and delete files and folders
- Build paths that work on any OS

---

## pathlib — The Right Way

`pathlib.Path` is the modern, clean way to work with file paths. Forget string-based path manipulation.

```python
from pathlib import Path

# Build paths with /  (works on Windows, Mac, Linux)
home = Path.home()                     # C:\Users\Frank  or  /home/frank
docs = home / "Documents"
project = docs / "my-project" / "data.csv"

print(project)           # C:\Users\Frank\Documents\my-project\data.csv
print(project.name)      # data.csv
print(project.stem)      # data
print(project.suffix)    # .csv
print(project.parent)    # C:\Users\Frank\Documents\my-project
```

---

## Checking What Exists

```python
from pathlib import Path

p = Path("somefile.txt")

p.exists()       # True or False
p.is_file()      # True if it's a file
p.is_dir()       # True if it's a directory
```

---

## Listing Files

```python
from pathlib import Path

folder = Path(".")    # current directory

# All items in a folder
for item in folder.iterdir():
    print(item)

# Only files matching a pattern (glob)
for f in folder.glob("*.py"):
    print(f)

# Recursive — search all subdirectories
for f in folder.rglob("*.csv"):
    print(f)
```

---

## Reading and Writing via Path

```python
from pathlib import Path

p = Path("notes.txt")

# Read
content = p.read_text(encoding="utf-8")

# Write (overwrites)
p.write_text("Hello!\n", encoding="utf-8")
```

---

## Creating and Deleting

```python
from pathlib import Path

# Create a directory (and any missing parents)
Path("output/reports/2024").mkdir(parents=True, exist_ok=True)

# Delete a file
Path("old_file.txt").unlink(missing_ok=True)

# Delete an empty directory
Path("empty_folder").rmdir()

# Delete a directory and all its contents (careful!)
import shutil
shutil.rmtree("folder_to_delete")
```

---

## Copying and Moving

```python
import shutil
from pathlib import Path

# Copy a file
shutil.copy("source.txt", "destination.txt")

# Copy to a folder (keeps filename)
shutil.copy("report.pdf", Path("archive/"))

# Copy entire folder
shutil.copytree("src_folder", "dst_folder")

# Move / rename
shutil.move("old_name.txt", "new_name.txt")
Path("file.txt").rename("renamed.txt")
```

---

## os.path (the older way)

You'll see `os.path` in older code — worth knowing:

```python
import os

os.path.exists("file.txt")
os.path.join("folder", "subfolder", "file.txt")
os.path.basename("/path/to/file.txt")    # "file.txt"
os.path.dirname("/path/to/file.txt")     # "/path/to"
os.getcwd()                               # current working directory
os.listdir(".")                           # list directory
```

Prefer `pathlib` for new code — it's cleaner and more readable.

---

## Exercises

Create `filesystem.py`.

**Exercise 1:** Write a function `list_files(folder, extension=None)` that returns all files in a folder. If `extension` is provided (e.g., `".py"`), return only files with that extension.

**Exercise 2:** Write a function `organize_downloads(folder)` that looks at all files in a folder and moves them into subfolders by extension: `images/` for `.jpg/.png`, `docs/` for `.pdf/.docx`, `data/` for `.csv/.xlsx`, and `other/` for everything else. (Test it on a dummy folder you create.)

**Exercise 3:** Write a function `find_large_files(folder, min_size_mb=10)` that recursively finds all files over a given size and returns them as a sorted list of `(size_mb, path)` tuples.

**Exercise 4:** Write a script that takes a folder path and produces a summary: total number of files, total size in MB, and a breakdown of file counts by extension.

**Exercise 5 (stretch):** Write a backup function `backup(source_folder, backup_folder)` that copies the source folder to the backup location with a timestamp in the name: `backup_2024-01-15_09-32/`.

---

## Key Takeaway
Use `pathlib.Path` for all file system work — build paths with `/`, check existence with `.exists()`, list with `.glob()`. `shutil` handles copying, moving, and deleting folders. `parents=True, exist_ok=True` on `.mkdir()` saves you from checking first.

**Next:** [Lesson 16 — Running Shell Commands →](./16-shell.md)
