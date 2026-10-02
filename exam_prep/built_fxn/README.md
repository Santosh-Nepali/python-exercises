Of course! Let's understand `__str__()` and `__repr__()` in Python from the very beginning, using simple language, real-life examples, and small pieces of code.

The most important thing to understand is that both `__str__()` and `__repr__()` convert an object into a string, but they are meant for different purposes.

- `__str__()` answers: "How should I show this object to a normal user?"

- `__repr__()` answers: "How should I describe this object so a programmer can understand exactly what it is?"

# 1. First, understand the problem

Imagine you have a `Student` object in Python.

Python

Run

```
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Alice", 20)

print(student1)
```

What do you think the output will be?

It will look something like this:

```
<__main__.Student object at 0x7f123456>
```

This output is not very helpful. It tells us that the object is a `Student`, but it doesn't tell us the student's name or age.

Wouldn't it be better if Python displayed something like this?

```
Alice is 20 years old
```

This is where `__str__()` and `__repr__()` come in. They let us decide how our objects should be represented as strings.

# 2. Understanding `__str__()`

`__str__()` is used when you want to display an object in a way that is easy for humans to read and understand.

For example:

Python

Run

```
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

student1 = Student("Alice", 20)

print(student1)
```

Output:

```
Alice is 20 years old
```

Let's understand what happened.

- We created a `Student` class.

- We created an object named `student1`.

- We defined `__str__()` to return a readable sentence.

- When we used `print(student1)`, Python automatically called `student1.__str__()`.

In other words, this:

Python

Run

```
print(student1)
```

is effectively equivalent to:

Python

Run

```
print(str(student1))
```

And `str(student1)` uses the `__str__()` method we defined.

Remember: `__str__()` is mainly for displaying information in a simple, readable way, just as you would explain the object to another person.

# 3. Understanding `__repr__()`

Now let's understand `__repr__()`.

`__repr__()` is used to provide a clear and detailed representation of an object, mainly for developers who are writing, debugging, or inspecting code.

Consider this example:

Python

Run

```
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student(name={self.name!r}, age={self.age!r})"

student1 = Student("Alice", 20)

print(repr(student1))
```

Output:

```
Student(name='Alice', age=20)
```

Why does it look different from `__str__()`?

Because `__repr__()` tries to show the object in a way that clearly reveals its type and the values stored inside it.

For example:

```
Alice is 20 years old
```

is a nice sentence for a person to read, but it doesn't clearly show how the data is structured.

On the other hand:

```
Student(name='Alice', age=20)
```

tells a developer:

- The object is a `Student`.

- Its `name` is `'Alice'`.

- Its `age` is `20`.

The `!r` inside the f-string calls `repr()` on the value. This helps show strings with quotes and makes their representations clearer.

Remember: `__repr__()` is mainly for developers. It should ideally provide an unambiguous representation and, where practical, one that can be used to recreate the object.

# 4. Let's compare both using the same class

This is the most important example for understanding the difference.

Python

Run

```
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def __repr__(self):
        return f"Student(name={self.name!r}, age={self.age!r})"


student1 = Student("Alice", 20)

print(str(student1))
print(repr(student1))
```

Output:

First line: `str(student1)`

Alice is 20 years old

Second line: `repr(student1)`

Student(name='Alice', age=20)

Both outputs describe the same object, but they present the information differently.

| `__str__()`             | `__repr__()`                                   |
| ----------------------- | ---------------------------------------------- |
| Alice is 20 years old   | Student(name='Alice', age=20)                  |
| Reads like a sentence   | Looks like a Python expression                 |
| Easy for a user to read | Easy for a developer to inspect                |
| Focuses on presentation | Focuses on identifying the object and its data |

Think of it this way:

Imagine you are introducing a student to someone.

- With `__str__()`, you say: "Alice is 20 years old."

- With `__repr__()`, you show a record: "Student(name='Alice', age=20)."

The information is similar, but the purpose is different.

# 5. Where does Python use them automatically?

This is where many beginners get confused. You don't always need to call these methods yourself. Python calls them automatically in certain situations.

Situation 1: Using `print()`

Python

Run

```
print(student1)
```

Python calls `__str__()` if it is defined.

Output:

```
Alice is 20 years old
```

Situation 2: Using `str()`

Python

Run

```
str(student1)
```

Python also calls `__str__()`.

Output:

```
'Alice is 20 years old'
```

The quotation marks above simply indicate that the returned value is a string; they aren't part of the actual returned value.

Situation 3: Using `repr()`

Python

Run

```
repr(student1)
```

Python calls `__repr__()`.

Output:

```
"Student(name='Alice', age=20)"
```

Again, the outer quotation marks indicate the result is a string.

Situation 4: Using a list

This is a particularly important difference.

Python

Run

```
students = [student1]

print(students)
```

Output:

```
[Student(name='Alice', age=20)]
```

Why didn't it print `Alice is 20 years old`?

Because when Python displays a list, it uses `__repr__()` to represent the objects inside it, rather than their `__str__()`.

A useful rule to remember

- `print(student1)` → `__str__()`

- `repr(student1)` → `__repr__()`

- `print([student1])` → `__repr__()` for the list element

- `print({"student": student1})` → `__repr__()` for the dictionary value

# 6. What if we define only one method?

You don't have to define both methods in every class.

Case 1: Only `__repr__()` is defined

Python

Run

```
class Student:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student({self.name!r})"


s = Student("Alice")

print(s)
print(repr(s))
```

Output:

```
Student('Alice')
Student('Alice')
```

Why are both outputs the same?

Because if `__str__()` is not defined, Python falls back to `__repr__()` when converting the object using `str()`.

Case 2: Only `__str__()` is defined

Python

Run

```
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student name is {self.name}"


s = Student("Alice")

print(s)
print(repr(s))
```

Output:

```
Student name is Alice
<__main__.Student object at 0x...>
```

The address will vary each time you run the program.

Here, `print(s)` works with your custom `__str__()`, but `repr(s)` uses Python's default representation because you haven't defined `__repr__()`.

The fallback works in only one direction:

`__str__()` missing

Falls back to `__repr__()`

`__repr__()` missing

Default object representation

# 7. Why does `__repr__()` use quotes around strings?

Look at this code:

Python

Run

```
name = "Alice"

print(str(name))
print(repr(name))
```

Output:

```
Alice
'Alice'
```

`str()` returns the string in a human-friendly form, while `repr()` returns a representation that makes it clear that the value is a string.

For example:

Python

Run

```
print(str("123"))
print(repr("123"))
```

Output:

```
123
'123'
```

The quotes in `repr()` help distinguish the string `"123"` from the integer `123`.

Python

Run

```
print(repr(123))
```

Output:

```
123
```

This distinction is useful when debugging, because a string containing digits and an integer are different data types.

# 8. A real-world example

Imagine you are creating a shopping application with a `Product` class.

![Laptop computor computer white background | Free Photo  - rawpixel](https://images.openai.com/static-rsc-4/SDyq3fnfQyNY-gD0hDGz6Z83rNDenYHxx11V_IYfk8d1b2wd4YVKfljmZoZFKLzJdQcb3rFBLnd-duajdLKl3fXFhR_SiAfdPfuEn5rEisEvleZyeX73JXMdjoPQ9UMPS5R6lzVULH-tzRREa05gn3ok-xp-l01YSO6R6OnXw1k?purpose=inline)

Python

Run

```
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} costs ${self.price}"

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price!r})"


product1 = Product("Laptop", 1200)

print(product1)
print(repr(product1))
```

Output:

```
Laptop costs $1200
Product(name='Laptop', price=1200)
```

In this example:

- `__str__()` is useful when showing product information to a customer.

- `__repr__()` is useful when a developer is inspecting the product object to understand its values.

One method focuses on the presentation of the product, while the other focuses on its representation in code.

# 9. Test your understanding

QUESTION 1 OF 3

What is the main purpose of `__str__()`?

To show a human-readable description

To recreate an object

To display the object's memory address

Correct!

`__str__()` is designed to produce a readable string for people.

QUESTION 2 OF 3

If a class defines only `__repr__()`, what happens when you call `print(obj)`?

It raises an error

It uses the default object representation

It uses `__repr__()` as a fallback

Correct!

Python falls back to `__repr__()` when `__str__()` is not defined.

QUESTION 3 OF 3

When you print a list containing a custom object, which method is used for the object's representation?

`__str__()`

`__repr__()`

Both are always called

Correct!

Lists use `repr()` for their elements, which calls each object's `__repr__()`.

Your score: 3 / 3

Try again

# 10. Final takeaway

Think of `__str__()` as a description and `__repr__()` as a detailed record.

`__str__()`

"Alice is 20 years old."

`__repr__()`

"Student(name='Alice', age=20)"

When you're creating your own Python classes, it is often useful to implement `__repr__()` first, then add `__str__()` if you need a more user-friendly display.

One final detail: `__repr__()` is ideally written so that it can recreate an object, but this is not mandatory. Its main goal is to give developers an informative, unambiguous representation.
