"""
module_5 program_2
Write a program that asks the user to enter numbers until they input an empty string to quit. At the end, the program prints out the five greatest numbers sorted in descending order. 
Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.
"""

numbers_collection=[]
while True:
    number=input('Enter number')
    if number=='':
        break;
    else:
        number=int(number)
        numbers_collection.append(number)

print(f'The value in the list {numbers_collection}')
print(f' The sorted number in the list {numbers_collection.sort(reverse=True)}')
print(f'The value in the list {numbers_collection}')


