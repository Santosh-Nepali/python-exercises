"""
module_4 program_4
Write a game where the computer draws a random integer between 1 and 10. 
The user tries to guess the number until they guess the right number.
After each guess the program prints out a text: Too high, Too low or Correct.
Notice that the computer must not change the number between guesses.
"""

import random
random_value=random.randint(1,10)
#print(f'{random_value}')
while True:
    user_guess=input('Guess the number from 1-10 ::: ')
    try:
        user_guess=int(user_guess)
        if user_guess>random_value:
            print('You have enter too high number')
            continue
        
        elif user_guess<random_value:
            print('You have enter too low number')
            continue
        else:
            print('Correct')
            break
    except ValueError:
        print('non numeric value')        
        