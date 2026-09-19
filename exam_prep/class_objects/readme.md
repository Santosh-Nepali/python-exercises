## Classes and Objects

In object-oriented programming (OOP), a class is a blueprint for creating objects, while an object is an instance of a class.

### 1. Class

A class defines the properties (data) and methods (functions) that its objects will have.

For example, a `Car` class can define a car's color, brand, and a method to drive.

### 2. Object

An object is a specific instance of a class. It has its own values for the properties defined by the class.

For example, a red Toyota car is an object of the `Car` class.

## Example in Python

Python

Run

```
# Define a class
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print("The car is driving")

# Create objects
car1 = Car("Toyota", "Red")
car2 = Car("BMW", "Blue")

# Access properties
print(car1.brand)  # Toyota
print(car2.color)  # Blue

# Call a method
car1.drive()
```

### How it works

Class

## Car

Blueprint

car1

brand = Toyota

color = Red

car2

brand = BMW

color = Blue

Both objects use the Car class

In short: A class is a template, and an object is a real instance created from that template.

## Concept of Memory allocation

# Memory Allocation Concept in Python OOP — Simple Example

Let's use your `Car` class to demonstrate this concretely, since you already understand it well.

## The core idea

When you create an object from a class, Python allocates a **separate block of memory** for that specific object's data — even if you create multiple objects from the exact same class. Each object gets its **own independent copy** of instance attributes (like `current_speed`), while the **class itself** (its methods, like `accelerate()`) is stored **once**, shared by all objects.

## Simple demonstration

```python
class Car:
    def __init__(self, registration_no, max_speed):
        self.registration_no = registration_no
        self.max_speed = max_speed
        self.current_speed = 0


car1 = Car("ABC-123", 142)
car2 = Car("XYZ-789", 120)

print(id(car1))   # e.g. 140234567891232
print(id(car2))   # e.g. 140234567891456  (a DIFFERENT address)

print(car1 is car2)   # False - two separate objects in memory
```

**What `id()` shows:** it returns the object's actual **memory address** (as a number). `car1` and `car2` have **completely different addresses**, proving Python allocated two separate, independent chunks of memory — one per object.

## Testing it live## What this proves

| Observation                                                     | What it tells us about memory                                                                                                 |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `car1` and `car2` have **different `id()` values**              | Each object occupies its own separate memory location                                                                         |
| Calling `car1.accelerate(30)` only changed `car1.current_speed` | Confirms `car1` and `car2` each hold their **own independent copy** of `current_speed` — changing one doesn't touch the other |
| Both started at `current_speed = 0`                             | Each object's `__init__` ran **separately** for each one, allocating fresh memory each time `Car(...)` was called             |

## Why this matters — the class vs. the object

This is a key distinction worth remembering:

- **The class `Car`** (the blueprint — the `__init__` and `accelerate` code itself) is defined **once**, and Python stores that code in memory only a single time, regardless of how many cars you create.
- **Each object** (`car1`, `car2`, `car3`, ...) gets its **own separate memory allocation** for its instance attributes (`registration_no`, `max_speed`, `current_speed`), created fresh every time you call `Car(...)`.

You can actually verify that the **method itself** is shared (not duplicated per object):

```python
print(car1.accelerate is Car.accelerate)   # True-ish concept (bound method wraps the same function)
print(Car.accelerate)                        # the same function object, regardless of car1 or car2
```

## A simple analogy

Think of the `Car` **class** as an architectural **blueprint** for a house — there's only **one blueprint** stored in a drawer. But every time you _build_ an actual house from that blueprint (`car1 = Car(...)`, `car2 = Car(...)`), you get a **brand-new, physically separate house**, sitting at its own separate address, with its own furniture (`current_speed`, `max_speed`) that doesn't affect any other house built from that same blueprint.

## Connecting this to a subtle bug this concept helps you avoid

This is actually _why_ the earlier `accelerate()` bug we found was purely about **missing print statements**, not a memory problem — `self.current_speed` really was correctly and safely updated in `car1`'s own private memory, completely independent of any other car object, exactly as this demonstration shows.
