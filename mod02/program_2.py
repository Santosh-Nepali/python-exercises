"""
module_2 program_2

Write a program that asks the user for the radius of a circle and the prints out the area of the circle.

"""
#Importing math for using their functions
import math

# Input radius of the circle
radius=float(input('Enter radius of the cirlce :::: '))

#Assign value for pie
pi=3.14159

#Calculate are of the circle
area=pi*pow(radius,2)

#Print area of circle with two decimal point after dot
print(f'The area of circle having radius = {radius} is ::: {area:0.2f} ')