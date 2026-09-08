def sum(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print("Sum is", sum(1, 2, 3))

'''
Variable-length argument lists. A varying number of arguments can be provided from one function call to another. 
The function can process the received values as a list:
'''
