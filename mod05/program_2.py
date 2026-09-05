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


'''
print(f'{iter(numbers_collection)}')  
num_iterator=iter(numbers_collection)
print(f'{next(num_iterator)}')
print(f'{next(num_iterator)}')
print(f'{next(num_iterator)}')
print(f'{next(num_iterator)}')
print(f'{next(num_iterator)}')
print(f'{next(num_iterator)}')
print(f'{next(num_iterator)}')
print(f'{next(num_iterator)}')

pythons 'for' loop command iterates over an object using the iterator protocol.
iterators are objects used to iterate over an iterable and implement iterator protocols.
A for loops calls iter() on an iterable to create an iterator object.
The iterator object is responsible for returning each item to the loop.
A for loop calls next() on the iterator object to fetch each item. 
The next() function raises an StopIteration exception when there is nothing left in the iterator object.

In Python, everything is an object. 
'''
print('test')