"""
module_5 program_3
Write a program that asks the user for an integer and tells if the number is a prime number. 
Prime numbers are number that are only divisible by one or the number itself.
For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
On the other hand, 21 is not a prime number as it is divisible by 3 and 7.

"""

prime_counter=0
num=input("Enter the number ::: ")
try:
    num=int(num)
    if num<=1:
        print(f'{num} is less or equal to 1')
    else:
        for count in range(1, num+1):
            if(num%count)==0:
                prime_counter+=1
            
        if prime_counter==2:
            print(f'{num} is a prime number.')
        else:
            print(f'{num} is not a prime number.')
                
except ValueError:
    print(f'{num} is not integer value.')
                
                
                

