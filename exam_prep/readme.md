Here’s a **note-friendly summary** you can keep for revision.

```javascript

print(f'{iter(numbers_collection)}')
num_iterator=iter(numbers_collection)
print(f'{next(num_iterator)}')
print(f'{next(num_iterator)}')
print(f'{next(num_iterator)}')
print(f'{next(num_iterator)}')
print(f'{next(num_iterator)}')
print(f'{next(num_iterator)}')
print(f'{next(num_iterator)}')
print(f'{next(num_iterator)}')

pythons 'for' loop command iterates over an object using the iterator protocol.
iterators are objects used to iterate over an iterable and implement iterator protocols.
A for loops calls iter() on an iterable to create an iterator object.
The iterator object is responsible for returning each item to the loop.
A for loop calls next() on the iterator object to fetch each item.
The next() function raises an StopIteration exception when there is nothing left in the iterator object.

In Python, everything is an object.

Simple rule:

Need each value → for number in numbers
Need a specific position → numbers[index]
Need both index and value → enumerate(numbers)

```

# Python Lists — Iterating and Removing Items

## 1. Accessing items in a list

A `for` loop can access each value:

```python
numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)
```

Output:

```text
10
20
30
40
```

To access an item using its position (index):

```python
numbers[0]  # 10
numbers[1]  # 20
```

Indexes start from **0**.

---

## 2. `pop()` vs `remove()`

### `pop()`

`pop()` removes an item using its **index** and returns the removed value.

```python
numbers = [10, 20, 30]

x = numbers.pop(1)

print(x)        # 20
print(numbers)  # [10, 30]
```

Without an index:

```python
numbers.pop()
```

removes the **last item**.

### `remove()`

`remove()` removes an item using its **value**.

```python
numbers = [10, 20, 30]

numbers.remove(20)

print(numbers)  # [10, 30]
```

**Remember:**

```text
pop(index)     → remove by position
remove(value)  → remove by value
```

---

## 3. Checking whether a list is empty

The preferred Python way:

```python
if not numbers:
    print("List is empty")
```

To check if it contains values:

```python
if numbers:
    print("List is not empty")
```

You can also use:

```python
if len(numbers) == 0:
    print("List is empty")
```

But `if not numbers:` is simpler and more Pythonic.

---

## 4. The danger of modifying a list while iterating

Avoid:

```python
for number in numbers:
    numbers.remove(number)
```

The problem is that `remove()` changes the list while the `for` loop is moving through it.

Example:

```python
numbers = [2, 4, 6, 8]
```

After removing `2`:

```text
Before:  [2, 4, 6, 8]
           ↑

Remove 2

After:   [4, 6, 8]
```

The remaining elements shift to the left.

The loop continues forward, so it can **skip elements**.

### Key rule

> **Don't add or remove items from a list while directly iterating over that same list.**

---

## 5. Using `.copy()` when you need to remove items

If you specifically need to use `remove()`, iterate over a copy:

```python
for number in numbers.copy():
    if number % 2 == 0:
        numbers.remove(number)
```

There are now two lists:

```text
numbers        → original list (being changed)
numbers.copy() → copy (being iterated over)
```

The loop is safe because the list being iterated over doesn't change.

---

## 6. Better approach: create a new list

Instead of removing items while iterating, you can create another list:

```python
result = []

for number in numbers:
    if number % 2 != 0:
        result.append(number)
```

For:

```python
numbers = [1, 2, 3, 4, 5, 6]
```

the result is:

```python
[1, 3, 5]
```

The original list isn't modified during iteration.

---

## 7. List comprehension

The same idea can be written more compactly:

```python
result = [number for number in numbers if number % 2 != 0]
```

This creates a new list containing only odd numbers.

---

## Important concepts to remember

```text
for x in list
    → access each item

list[index]
    → access item by position

pop(index)
    → remove by index and return the item

remove(value)
    → remove by value

if not list
    → list is empty

if list
    → list is not empty

list.copy()
    → create a separate copy

Don't modify a list while directly iterating over it.
```

## Tuples

If you have an **empty tuple**, you cannot add values to it using `append()` because tuples are immutable.

```python
my_tuple = ()
```

### If you want to collect values from the user

Use a **list first**, then convert it to a tuple:

```python
values = []

for i in range(3):
    value = input("Enter a value: ")
    values.append(value)

my_tuple = tuple(values)

print(my_tuple)
```

For example:

```text
Enter a value: Apple
Enter a value: Banana
Enter a value: Orange

('Apple', 'Banana', 'Orange')
```

### You can also create a new tuple each time

```python
my_tuple = ()

value = input("Enter a value: ")
my_tuple = my_tuple + (value,)

print(my_tuple)
```

Notice the comma here:

```python
(value,)
```

The comma is important because `(value)` is just parentheses, not a tuple.

**Best practice:** If you're repeatedly adding user input, use a **list**, then convert it to a tuple when you're finished.

Here's a second, more challenging set — heavier on code-tracing and edge cases, which is what tends to trip people up on exams.

NOTE:
Here's a second, more challenging set — heavier on code-tracing and edge cases, which is what tends to trip people up on exams.

# Software 1: Python Programming — Study Notes (Topics 1–8)

Source: Metropolia sw1-python course material

---

## Topic 1: Getting Started with Programming

**Operating System (OS)**

- Software that mediates between user, programs, and hardware (Windows, macOS, Linux).
- Source code → compiled/interpreted → machine-language executable → run by OS on hardware.

**File System**

- Hierarchical: root → folders → subfolders → files.
- **Absolute path**: starts from root (`C:\Users\...` or `/home/...`).
- **Relative path**: relative to the program's current location (`./data/file1.txt`).
- Avoid spaces/special characters in filenames; use letters, numbers, `_`, `-`.
- Filenames are case-sensitive on many systems (`file1.txt` ≠ `File1.txt`).
- Python source code files use `.py` extension.

**Dev Tools**

- **Plain text** files (code, notes, CSV) vs **binary files** (PDF, images, video).
- **Compiler**: translates source → machine code ahead of time.
- **Interpreter**: translates & runs code on the fly (Python uses this).
- **IDE**: editor + tools (autocomplete, debugging, syntax highlighting) combined.
- AI assistants (Copilot, Claude Code, Cursor) help but must be used critically — course exams require writing code unaided.

**Version Control (intro)**

- Solves the "final_final2_v3" file-naming problem by tracking all changes systematically.
- Used in Google Docs, Wikipedia, Dropbox, and essential in software teams.

---

## Topic 2: Version Control (Git)

- **Version control system**: tracks changes (what/why/when/who), enables parallel development, collaboration, comparing/restoring versions, backup, code quality.
- **Commit**: a save point. **Branch**: a timeline of commits (default: `main`).
- **Repository**: folder storing all versions/branches/metadata.
- **Merge**: joining branches together. **Conflict**: occurs when merged branches changed the same content — must be resolved manually.
- **Checkout**: switches the active branch, replacing working files with that branch's version.

**Git specifics**

- Git = distributed VCS (each dev has full history locally); created by Linus Torvalds (2005).
- **Three states/areas**:
  1. **Working directory** — where you edit files.
  2. **Staging area** — files staged for the next commit (`git add`).
  3. **Repository** (`.git/` folder) — all committed history.
- Core workflow:
  1. Edit files in working directory.
  2. `git add <file>` or `git add .` → staging area.
  3. `git commit -m "message"` → saves to repository.
  4. `git status` — check state anytime.
- Branching: `git branch <name>`, `git checkout <name>` (or `git checkout -b <name>` to create+switch), `git merge <name>` to merge into current branch.
- Other commands: `git log` (history), `git diff` (compare changes), `git reset` (undo staging/changes — use carefully).
- `.git/` folder = all version control data; deleting it destroys history.
- `.gitignore` — lists files/folders Git should NOT track (e.g., `.venv/`, `__pycache__/`, IDE settings, secrets, large binaries). `*` = wildcard.

---

## Topic 3: Variables and Interactive Programs

**Printing**

- `print("text")` — outputs text, auto-adds a newline after each call.
- Strings can use `'single'` or `"double"` quotes — use the other type inside if needed.
- `\n` = newline character inside a string.

**Input & Variables**

- `input("prompt")` — always returns a **string**, waits for Enter key.
- Assignment: `variable = expression` (variable name left, value/expression right).
- Variable names: letters, digits, underscores; cannot start with a digit or contain spaces.
- Steps of assignment: (1) evaluate right-hand side, (2) create/reuse variable, (3) store value (overwriting old value if any).
- Variable values can change any time during execution.

**Types**

- Python determines type automatically — no declarations needed.
- Basic (primitive) types: **string**, **number** (int, float, complex), **boolean** (`True`/`False`).
- Other structures: list, tuple, dictionary, object references.
- Complex numbers use `j` for the imaginary part (not `i`), e.g. `-4 + 2j`.
- Underscores can group digits in large integers: `12_456_123_180`.
- Convert types: `int()`, `float()`, `str()`.
- String concatenation uses `+` (all parts must be strings).

**Output formatting (f-strings)**

- `f"...{expression:format_code}..."`
- Format code examples:
  - `.5f` → float, 5 decimals
  - `10.2f` → float, 2 decimals, field width 10
  - `<20s` → string, left-aligned, width 20
  - `8d` → integer, field width 8
- Needs `import math` to use `math.pi`, `math.e`, etc.

---

## Topic 4: Conditional Statement (if)

**Syntax**

```
if condition:
    block executed if true
elif other_condition:
    block executed if that's true
else:
    block executed if none matched
```

- Indentation (4 spaces / one Tab) is **mandatory** in Python — defines code blocks.
- `elif` = "else if"; only one matching branch runs, checked top to bottom.
- An `else` binds to the nearest `if`/`elif` at the same indentation level.

**Comparison operators**: `>`, `<`, `>=`, `<=`, `==` (equal), `!=` (not equal).

- Chaining allowed: `170 <= height < 180`.
- Comparisons also work on strings (alphabetical order).
- `==` compares values; `=` assigns — common source of bugs.

**Logical operators**: `and`, `or`, `not`.

- Precedence: `not` → `and` → `or` (parentheses override).
- **Short-circuit evaluation**: Python stops evaluating a logical expression as soon as the result is determined (e.g., in `a or b`, if `a` is True, `b` is never evaluated).

---

## Topic 5: Loop Structure (while)

- Python has two loop types: **while** (initial-condition) and **for** (iterative).
- Syntax:

```
while condition:
    block to repeat
```

- Condition checked **before** each iteration; loop ends once it's false.
- Must update the loop variable inside the loop, or you get an **infinite loop** (a common bug — force-stop with Ctrl+C in terminal / trash icon in VS Code).

**Patterns**

- Fixed repetitions: counter variable incremented each round, compared to a target.
- User-controlled: loop `while command != "stop":`.
- Randomized: e.g. rolling dice with `import random; random.randint(1,6)`.

**Nested loops**: a loop inside another loop; inner loop completes fully for every outer iteration (e.g., multiplication tables).

**break**: immediately exits the loop, skipping the condition check. Overuse can create "spaghetti code" — prefer well-designed conditions when possible.

**while/else**: `else` block runs only if the loop ends normally (condition became false) — **not** if exited via `break`.

**Infinite loop**: occurs when the condition never becomes false (e.g., forgetting to increment the loop variable).

---

## Topic 6: Lists and For Loops

**Lists**

- Ordered, mutable collection: `names = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]`.
- Indexing starts at **0**. Negative indices count from the end (`-1` = last item).
- Slicing: `names[1:3]` → items from index 1 up to (not including) index 3.
- `names[2:]` → from index 2 to the end. `len(names)` → number of items.
- Out-of-range index → `IndexError: list index out of range`.

**Common list operations**
| Operation | Meaning |
|---|---|
| `append(x)` | add item to end |
| `remove(x)` | remove first occurrence of x |
| `insert(i, x)` | insert x at index i |
| `extend(other_list)` | append all items from another list |
| `index(x)` | get index of first occurrence of x |
| `x in list` | membership test |
| `sort()` | sort items in place |

**for loop**

```
for item in list:
    do something with item
```

- Iterates through each element in order ("iteration").

**range()**

- `range(1,4)` → 1, 2, 3 (end excluded)
- `range(5,0,-1)` → 5, 4, 3, 2, 1 (custom step)
- `range(10,21,2)` → 10, 12, ..., 20
- One argument: `range(n)` → 0 to n-1.

---

## Topic 7: Functions

**Definition & call**

```
def function_name(parameters):
    statements
    return value   # optional
```

- Function must be **defined before** it's called (main program typically last in file).
- Naming: lowercase, words separated by underscores.
- Calling transfers execution to the function; execution resumes after the call once the function returns.

**Parameters & arguments**

- Parameters = variables in the function definition; arguments = values passed at the call.
- Multiple parameters separated by commas, matched by position.
- **Keyword arguments**: `greet(times=2, greeting="Hey")` — order doesn't matter.
- **Default values**: `def greet(greeting="Hello", times=1):`.
- **Variable-length args**: `def sum(*numbers):` — collects extra args into a tuple/list-like structure.

**Variable scope**

- Variables created inside a function = **local** (invisible outside).
- Variables created outside functions = **global** (visible everywhere, including inside functions, for reading).
- Assigning to a variable inside a function makes it local by default, even if a global variable shares the same name — the global is untouched.

**Return values**

- `return value` sends a result back to the caller; must be captured/used, e.g. `result = my_function(...)`.

**Lists as parameters**

- Lists (and other mutable structures) are passed **by reference** (memory address), not copied.
- Changes made to a list inside a function (e.g., `.append()`, `.clear()`) affect the original list outside the function too — unlike simple types (numbers, strings), which are copied by value.

---

## Topic 8: Tuple, Set, and Dictionary

**Tuple**

- Ordered, like a list, but **immutable** (cannot add/remove/change items after creation).
- Created with parentheses: `days = ("Mon", "Tue", "Wed")` — parentheses often optional: `fruits = "Orange", "Banana", "Apple"`.
- Indexed like a list (`days[0]`), starting at 0.
- **Unpacking**: `(a, b, c) = fruits` assigns each element to a variable.
- **Return multiple values**: a function can `return first, second` — Python packs them into a tuple automatically; caller can unpack: `x, y = my_func()`.

**Set**

- Unordered, **no duplicate items** allowed, **not indexable**.
- Create: `games = {"Monopoly", "Chess"}`. Empty set **must** use `set()` — `{}` creates an empty dictionary instead.
- Operations: `add(x)`, `remove(x)`; adding a duplicate is silently ignored.
- Iterate with `for x in my_set:` — order is unspecified/arbitrary.

**Dictionary**

- Stores **key–value pairs**: `numbers = {"Viivi": "050-1234567", "Ahmed": "040-1112223"}`.
- Access/set a value: `dictionary[key]` / `dictionary[key] = value`.
- Check key existence: `if key in dictionary:`.
- Since Python 3.7, dictionaries preserve insertion order.
- Iterating `for k in dictionary:` gives you the **keys**.

**Nested data structures**

- Common pattern: a **list of dictionaries** (e.g., list of car records), useful for JSON-like/tabular data.
- Access pattern: `list[index]["key"]`, e.g. `cars[0]["make"]`.
- Loop through: `for car in cars: print(car["make"], car["year"])`.

---

## Quick Reference: Operators

| Category   | Operators               |
| ---------- | ----------------------- |
| Arithmetic | `+  -  *  /  %  //  **` |
| Comparison | `>  <  >=  <=  ==  !=`  |
| Logical    | `and  or  not`          |

70%
Score
14
Correct
6
Incorrect
How many times does 'Hi' get printed? finished_rounds = 0 while finished_rounds < 3: print("Hi") finished_rounds = finished_rounds + 1
Correct
You answered 3 times.

What happens when this program runs and the user enters exactly 5? money = float(input("Enter amount: ")) if money > 5: print("You can buy a latte.")
Correct
You answered Nothing is printed.

names = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"] print(names[-1]) print(names[0:2]) What is printed (two lines)?
Correct
You answered Mary ['Viivi', 'Ahmed'].

age = 23 if age >= 65: print("Retired") elif age >= 18: print("Working-age") elif age >= 7: print("In school") else: print("Small child") What is printed?
Incorrect
You answered "Working-age" then "In school", the correct answer was Only "Working-age".

i = 1 while i <= 2: j = 1 while j <= 3: print(i, j) j += 1 i += 1 How many total lines does this program print?
Correct
You answered 6.

numbers = [1, 2, 3, 4, 5] total = 0 index = 0 while total < 6: total += numbers[index] index += 1 What is the value of total when the loop ends?
Incorrect
You answered 3, the correct answer was 6.

count = 5 def increment(): count = count + 1 print(count) increment() What happens when this code runs?
Correct
You answered It raises an error (UnboundLocalError).

def squares(a, b): return a**2, b**2 result = squares(2, 3) print(result) What is printed?
Correct
You answered (4, 9).

point = (1, 2) point[0] = 10 What happens?
Correct
You answered It raises a TypeError because tuples are immutable.

def empty_bag(items): items.clear() backpack = ["Water bottle", "Map"] empty_bag(backpack) print(backpack) What is printed?
Correct
You answered [].

games = {"Chess", "Monopoly"} games.add("Chess") print(len(games)) What is printed?
Incorrect
You answered An error occurs, the correct answer was 2.

numbers = {"Viivi": "050-1234567"} print(numbers["Mary"]) What happens?
Incorrect
You answered It prints an empty string, the correct answer was It raises a KeyError.

for x in range(2, 10, 3): print(x) What values are printed?
Incorrect
You answered 3, 6, 9, the correct answer was 2, 5, 8.

commands = ["A", "STOP", "B"] for c in commands: if c == "STOP": break print(c) else: print("Done") What is printed? (Note: for loops also support else, same rule as while/else)
Correct
You answered A.

What is the result of: "apple" < "banana" ?
Correct
You answered True.

def greet(greeting, times): for i in range(times): print(f"{greeting} {i+1}. time") greet(times=2, greeting="Hey") What is printed?
Correct
You answered "Hey 1. time" then "Hey 2. time".

cars = [ {"make": "Toyota", "model": "Corolla"}, {"make": "Ford", "model": "Focus"} ] print(cars[1]["model"]) What is printed?
Correct
You answered "Focus".

score = 5 print("Score: " + score) What happens?
Correct
You answered A TypeError occurs.

def total(\*nums): result = 0 for n in nums: result += n return result print(total(10, 20, 30)) What is printed?
Incorrect
You answered It raises an error because too many arguments were passed, the correct answer was 60.

age = 20 if age < 13: print("Child") elif 15 <= age < 18: print("Teen") else: print("Adult") What is printed?
Correct
You answered "Adult".

#### Difference between list, set, tuples and dictionary

# Python Data Structures — Lists, Tuples, Sets, and Dictionaries

A quick-reference comparison of Python's four core built-in collection types.

## Comparison Table

| Feature                                        | List                                                                      | Tuple                                                                   | Set                                         | Dictionary                                                |
| ---------------------------------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------- | --------------------------------------------------------- |
| Syntax                                         | `[1, 2, 3]`                                                               | `(1, 2, 3)`                                                             | `{1, 2, 3}`                                 | `{"a": 1, "b": 2}`                                        |
| Ordered?                                       | Yes (maintains insertion order)                                           | Yes (maintains insertion order)                                         | No (no guaranteed order)                    | Yes (maintains insertion order, since Python 3.7+)        |
| Mutable? (can change after creation)           | Yes                                                                       | No                                                                      | Yes                                         | Yes (values can change; keys are fixed once set)          |
| Allows duplicate values?                       | Yes                                                                       | Yes                                                                     | No (automatically removes duplicates)       | Keys: No — Values: Yes                                    |
| Indexed access? (`obj[0]`)                     | Yes, by position                                                          | Yes, by position                                                        | No (sets aren't indexed at all)             | Yes, but by key, not position                             |
| Access syntax                                  | `my_list[0]`                                                              | `my_tuple[0]`                                                           | Cannot index; use `in` to check membership  | `my_dict["key"]`                                          |
| Add an item                                    | `.append(x)`                                                              | Not possible (immutable)                                                | `.add(x)`                                   | `my_dict["new_key"] = value`                              |
| Remove an item                                 | `.remove(x)` or `.pop()`                                                  | Not possible (immutable)                                                | `.remove(x)` or `.discard(x)`               | `.pop("key")` or `del my_dict["key"]`                     |
| Typical use case                               | An ordered collection you'll modify (e.g. a shopping list, player scores) | A fixed collection that shouldn't change (e.g. coordinates, RGB values) | Fast membership checks, removing duplicates | Key-value lookups (e.g. a name to phone number directory) |
| Can contain mixed data types?                  | Yes                                                                       | Yes                                                                     | Yes (elements must be hashable)             | Yes (keys must be hashable, values can be anything)       |
| Can be used as a dictionary key?               | No (lists are unhashable)                                                 | Yes (if all its elements are also hashable)                             | No (sets are unhashable)                    | No (dictionaries are unhashable)                          |
| Performance for membership checks (`x in obj`) | Slow — O(n), checks each item one by one                                  | Slow — O(n), same as list                                               | Fast — O(1) on average, uses hashing        | Fast — O(1) on average for keys, uses hashing             |
| Iterable?                                      | Yes                                                                       | Yes                                                                     | Yes                                         | Yes (iterates over keys by default)                       |

## Quick code examples side-by-side

```python
# List - ordered, mutable, allows duplicates
my_list = [1, 2, 2, 3]
my_list.append(4)
print(my_list)   # [1, 2, 2, 3, 4]

# Tuple - ordered, immutable, allows duplicates
my_tuple = (1, 2, 2, 3)
# my_tuple.append(4)  # would raise AttributeError

# Set - unordered, mutable, NO duplicates
my_set = {1, 2, 2, 3}
print(my_set)   # {1, 2, 3}  <- duplicate automatically removed

# Dictionary - ordered (3.7+), mutable, unique keys
my_dict = {"a": 1, "b": 2}
my_dict["c"] = 3
print(my_dict)   # {'a': 1, 'b': 2, 'c': 3}
```

## When to use which — a simple decision guide

| If you need...                                                                         | Use        |
| -------------------------------------------------------------------------------------- | ---------- |
| An ordered collection you'll change often (add/remove/edit items)                      | List       |
| A fixed collection that should never change (e.g. function return values, coordinates) | Tuple      |
| To automatically eliminate duplicates, or do fast "is X in this collection?" checks    | Set        |
| To look values up by a meaningful label/key instead of position                        | Dictionary |
