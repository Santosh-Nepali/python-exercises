"""
module_4 program_1
Write a program that uses a while loop to print out 
all numbers divisible by three in the range of 1-1000.

"""

count=1
while (count<=1000):
    rem=count%3
    if(rem==0):
        print(f'The number {count} is divisible by 3')
    count=count+1