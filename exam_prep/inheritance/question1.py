### Python OOP — Inheritance Practice Questions
"""
1. Create an `Animal` class with a `speak()` method. Create a `Dog` class that inherits from `Animal` and overrides `speak()`.

2. Create a `Person` class with `name` and `age`. Create a `Student` class that inherits from `Person` and adds `student_id`.

3. Create a `Vehicle` class with `brand` and `speed`. Create a `Car` class that inherits from `Vehicle` and adds `model`.

4. Create an `Employee` class with `name` and `salary`. Create a `Manager` class that inherits from `Employee` and adds `department`.

5. Create a `Shape` class with an `area()` method. Create `Rectangle` and `Circle` classes that inherit from `Shape` and override the `area()` method.

6. Create a `BankAccount` class with `deposit()` and `withdraw()` methods. Create a `SavingsAccount` class that inherits from it and adds an `interest_rate`.

7. Create a `Person → Employee → Manager` multilevel inheritance structure. Each class should add its own attribute.

8. Create a `Vehicle` parent class and `Car` and `Bike` child classes. Give each child class its own version of a `start()` method.

9. Create an `Animal` class with `name` and `age`. Create `Dog` and `Cat` classes that inherit from it and have different `sound()` methods.

10. Create a `Product` class with `name` and `price`. Create an `ElectronicProduct` class that inherits from it and adds `warranty`.

11. Create a `UniversityMember` class. Create `Student` and `Professor` classes that inherit from it and have different `display_info()` methods.

12. Create a `Computer` class with `brand` and `ram`. Create a `Laptop` class that inherits from it and adds `battery`.

13. Create a `Book` class with `title` and `author`. Create a `TextBook` class that inherits from it and adds `subject`.

14. Create a `Person → Student → GraduateStudent` multilevel inheritance structure using `super()` in each constructor.

15. Create a `Company` class with `company_name`. Create `Employee` and `Customer` classes that inherit from it and add their own attributes.

16. Create an `Account` class with `balance`. Create `SavingsAccount` and `CurrentAccount` classes that inherit from it and implement different withdrawal rules.

17. Create a `Shape` parent class and `Rectangle`, `Triangle`, and `Circle` child classes. Each child should override an `area()` method.

18. Create a `Transport` class with a `move()` method. Create `Car`, `Train`, and `Airplane` classes that inherit from it and override `move()`.

19. Create a `GameCharacter` class with `name` and `health`. Create `Warrior` and `Wizard` classes that inherit from it and add their own attack methods.

20. Create a multilevel inheritance system: `Animal → Mammal → Dog`. Use `super()` to initialize attributes at every level.

"""
# question1
class Animal:
    def __init__(self, category, name):
        self.category=category
        self.name=name

    def speak(self):
        print(f"Method at Animal class")
        
class Dog(Animal):
    def __init__(self, cagetory, name):
        super().__init__(cagetory, name)
        
    def speak(self):
        super().speak()
        print("speak methods in class Dog")
        
d1=Dog("four legs","Joby")
d1.speak()

    