"""
module_2 program_3

Write a program that asks the user for the length and width of a rectangle. 
The program then prints out the perimeter and area of the rectangle. 
The perimeter of a rectangle is the sum of the lengths of each four sides.

"""

# Input Length and width of the rectangle
length=input('Enter length of the rectangle ::: ')
width=input('Enter width of the rectangle ::: ')
#print(type(length))
#print(type(width))

# Changing value into numeric value 
length_numeric=float(length)
width_numeric=float(width)
# print(type(length_numeric))
# print(type(width_numeric))
#Calculate perimeter of the rectangle
perimeter=2*(length_numeric+width_numeric)

#Calculate area of the rectangle
area=length_numeric*width_numeric

#Print Perimeter and area of rectangle with two decimal point after dot
print(f'The perimeter of rectangle of length: {length} and width: {width} is ::: {perimeter:0.2f} ')
print(f'The area of rectangle of length: {length} and width: {width} is ::: {area:0.2f} ')