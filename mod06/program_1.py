"""
module_6 program_1

Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters. 
Write a main program that rolls the dice until the result is 6. The main program should print out the result of each roll.

"""
import random

# User defined function without any parameters and reutnrs the result of rolled dice
def rolling_dice():
    return(random.randint(1,6))

while True:
    rolled_number=rolling_dice()
    print('The value is '+str(rolled_number)) 
    if rolled_number==6:
        break
       