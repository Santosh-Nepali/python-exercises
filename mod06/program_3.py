"""
module_6 program_3

Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
Write a main program that asks for a volume in gallons from the user and converts the value to liters. 
The conversion must be done by using the function. Conversions continue until the user inputs a negative value.

"""
def gallons_into_litres(gallon):
    return float(gallon)*3.78541
    
while True:
    try:
        gallon=input('Enter the gasoline in gallon ')
        if float(gallon)<0:
            print('Conversion Ends')
            break
        else:
            print(f' Gasoline = {gallon} gallons equals to {gallons_into_litres(gallon):0.2f} Litres')
    except ValueError:
        print('It is not a number.')   
