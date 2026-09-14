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
