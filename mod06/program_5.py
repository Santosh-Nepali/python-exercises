"""
module_6 program_5

Write a function that gets a list of integers as a parameter.
The function returns a second list that is otherwise 
the same as the original list except that all uneven numbers have been removed. 
For testing, write a main program where you create a list, call the function, 
and then print out both the original as well as the cut-down list.

"""
def even_list_segregator(numbers):
    list_without_even=[]
    for number in numbers:
        if number%2!=0:
            list_without_even.append(number)      
    return list_without_even

def get_values():
    numbers=[]
    n=int(input('How many numbers in the list ? '))
    if n>0:
        for i in range(n):
            value=int(input(f'Enter the {i+1} number:: '))
            numbers.append(value)
    else:
        print('The number of values must be greater than zero')
    return numbers


numbers=get_values()
if not numbers:
    print(' The list of numbers is empty. ')
else:
    print(f'The List of numbers before removing even {numbers}')
    print(f'The list after removing even numbers from the list ::: {even_list_segregator(numbers)}')
    


    

    