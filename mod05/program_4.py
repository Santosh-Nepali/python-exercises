"""
module_5 program_4

Write a program that asks the user to enter the names of five cities one by on (use a for loop for reading the names) 
and stores them into a list structure. Finally, the program prints out the names of the cities one by one,
one city per line, in the same order they were read as input.
Use a for loop for asking the names and a for/in loop to iterate through the list.

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