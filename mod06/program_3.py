"""
module_6 program_3

Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
Write a main program that asks for a volume in gallons from the user and converts the value to liters. 
The conversion must be done by using the function. Conversions continue until the user inputs a negative value.

"""
city_data=[]
total_city=5
# using for to input to the name of city
print('====== Recording Names of City =========')
for _ in range(total_city):
    city=input('Enter the Name of City ::: ')
    city_data.append(city)

# using for loop to display the name of the list 

print('====== Displaying Names of City =========')
for name_of_city in city_data:
    print(f'The name of the city is :::: {name_of_city}')