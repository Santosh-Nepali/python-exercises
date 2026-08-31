"""
module_4 program_1
Write a program that converts inches to centimeters 
until the user inputs a negative value. Then the program ends.

"""
inches=float(input('Enter the value for inch'))
while inches>0:
    centimeter=inches*2.54
    print(f'{inches:0.2f} inches is equals to {centimeter:0.2f} centimeter')
    inches=float(input('Enter negative value to stop the program'))
print('programs ended')
