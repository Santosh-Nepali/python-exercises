"""
module_6 program_4

Write a function that gets a list of integers as a parameter.
The function returns the sum of all the numbers in the list. 
For testing, write a main program where you create a list, call the function,
and print out the value it returned.

"""
def addition(numbers):
    sum=0
    for i in range(len(numbers)):
        sum =sum+numbers[i]
    return(sum)    
    #return sum(numbers)

numbers=[4, 6, 8, 90, 45, 31, -1]
sum=addition(numbers)
print(f' The sum of {numbers} is :: {sum}')
