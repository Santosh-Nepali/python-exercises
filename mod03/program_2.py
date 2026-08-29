"""
module_3 program_2
Write a program that asks the user to enter the cabin class of a cruise ship and 
then prints out a written description according to the list below. 
You must use an if/elif/else structure in your solution. 
LUX: upper-deck cabin with a balcony. 
A: above the car deck, equipped with a window. 
B: windowless cabin above the car deck. 
C: windowless cabin below the car deck.
If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class

"""
def display_menu():
    print('------------------------')
    print(' Cabin class :: LUX  ')
    print(' Cabin class :: A ')
    print(' Cabin class :: B  ')
    print(' Cabin class :: C ')
    print('------------------------')

def user_input():
    user_choose=input('Enter Cabin Class From the Menu ::: ')
    return user_choose


display_menu()    # calling display menu function
user_selection=user_input()   # calling user input function and assign to the variable
#print(user_selection)
if user_selection.upper()=='LUX':
    print(f'You have choosen ::: {user_selection} class\n Features ::: Upper-Deck Cabin with a Balcony ' )
elif user_selection.upper()=='A':
    print(f'You have choosen ::: {user_selection} class\n Features ::: Above the Car Deck, equipped with a window  ' )
elif user_selection.upper()=='B':
    print(f'You have choosen ::: {user_selection} class\n Features ::: Windowless Cabin Above the  Car Deck  ' )
elif user_selection.upper()=='C':
    print(f'You have choosen ::: {user_selection} class\n Features ::: Windowless Cabin Below the  Car Deck ')
else:
    print(f'You have entered ::: {user_selection}  Cabin Class, which is Invalid')

    

