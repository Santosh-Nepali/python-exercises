
"""

The core idea

When you create an object from a class, 
Python allocates a separate block of memory for that specific object's data — 
even if you create multiple objects from the exact same class. Each object gets its own independent copy of instance attributes

What id() shows: it returns the object's actual memory address (as a number). 
car1 and car2 have completely different addresses, 
proving Python allocated two separate, independent chunks of memory — one per object.

"""


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