"""
Project 1. Starting the Programming Project Assignment
Create a separate folder project/ for the game inside the Python exercise project, and create a readme.md file inside it. Add the name of your game as the heading and your own name below it.
Create a program in the folder that asks for the player’s name and age, stores them in variables, and prints them to the console.

"""
def user_info():
    print('Name')
    fname=input('Enter your first name ')
    lname=input('Enter your Last name ')
    age=input('Enter your age ')
    
    print(f'Name :: {fname} {lname}')
    print(f'Age :: {age}')

user_info()