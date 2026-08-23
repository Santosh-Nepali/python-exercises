"""
module_2 program_2

Write a program that asks the user for the radius of a circle and the prints out the area of the circle.

"""
#Importing math for using their functions
import math
while True:
    # Input radius of the circle
    try:
        radius=float(input('Enter radius of the cirlce :::: '))
    except ValueError:
        print(f'Radius cannot be string value')
        #continue
    else:
        if(radius<=0):
            print(f'Radius cannot be {radius} value')
            continue
    
        pi=3.14159
        area=pi*pow(radius,2)
        break

#Print area of circle with two decimal point after dot
print(f'The area of circle having radius = {radius} is ::: {area:0.2f} ')
