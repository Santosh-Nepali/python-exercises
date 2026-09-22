"""
Test your understanding of class properties by completing a small coding challenge.

Instructions
Inside the editor, complete the following steps:
Create a class Student with an __init__ that takes name and grade, and stores them as properties
Create an object s1 with name "Anna" and grade "A"
Print the grade of s1
Change the grade of s1 to "B"
Print the updated grade

"""
class Student:
    x="properties of class"
    def __init__(self, name, grade):
        self.name=name
        self.grade=grade
    
    def print_info(self):
        print(f" Name : {self.name} & Grade : {self.grade}")

s1=Student("Anna", "A")
print(f'Your grade is {s1.grade}')
s1.print_info()
s1.grade="B"
print(f"Your changed grade is : {s1.grade}")
s1.print_info()
print(f"{Student.x}")

