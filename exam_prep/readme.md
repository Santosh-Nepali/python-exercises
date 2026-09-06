Here’s a **note-friendly summary** you can keep for revision.

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
