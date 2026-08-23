"""
module_2 program_3

Write a program that asks the user for the length and width of a rectangle. 
The program then prints out the perimeter and area of the rectangle. 
The perimeter of a rectangle is the sum of the lengths of each four sides.

"""
while True:
    try:
        length=float(input('Enter length of the rectangle ::: ')) # Input Length of the rectangle
        width=float(input('Enter width of the rectangle ::: ')) # Input width of the rectangle
    
    except ValueError:
        print('Either length or width is invalid data type')
    
    else:
        if length<=0 or width<=0:
            print(f'The length {length} or width {width} is invalid')
            print('Enter fresh value for length and width')
            continue
            
        perimeter=2*(length+width) #Calculate perimeter of the rectangle
        area=length*width #Calculate area of the rectangle
        break

#Print Perimeter and area of rectangle with two decimal point after dot
print(f'The perimeter of rectangle of length: {length} and width: {width} is ::: {perimeter:0.2f} ')
print(f'The area of rectangle of length: {length} and width: {width} is ::: {area:0.2f} ')