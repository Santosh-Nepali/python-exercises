"""
module_6 program_2

Modify the function above so that it gets the number of sides on the dice as a parameter. 
With the modified function you can for example roll a 21-sided role-playing dice. 
The difference to the last exercise is that the dice rolling in the main program continues until the program gets the maximum number on the dice,
which is asked from the user at the beginning.

"""

import random

# user defined function for rolling the dice
def rolling_dice(dice_sides):
    return(random.randint(1,dice_sides))

# This code check the validity of sides of a dice  i.e. integer only, not zero or negative sides 
while True:
    dice_sides=input('How many total sides of a dice? ') # asking from users the number of total sides a duce
    try:
        dice_sides=int(dice_sides)
        if dice_sides<=0:
            print('The sides of a dice needs to be greater than zero')
        else:
           break   
    except ValueError:
        print('Invalid value')
 
# here loops the user defined function with dice sides as parameter until rolled number is equal to dices sides      
while True:
    rolled_number=rolling_dice(dice_sides)
    print(f'{rolled_number}')
    if rolled_number==dice_sides:
        break