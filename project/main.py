"""
Project 1. Starting the Programming Project Assignment
Create a separate folder project/ for the game inside the Python exercise project, and create a readme.md file inside it. Add the name of your game as the heading and your own name below it.
Create a program in the folder that asks for the player’s name and age, stores them in variables, and prints them to the console.


Project 2. Main Menu
Modify the game project program so that if the user enters an age under 12, the program informs them that they are a minor and shuts down.
Otherwise, the program greets the user, displays the main menu, and asks for commands until the user enters "lopeta".
Add a few fictional commands that each produce a different output in the console. After a command, always display the menu again.ss

"""
def user_info():
    fname=input('Enter your first name ')
    lname=input('Enter your Last name ')

    while True:
        try:
            age=input('Enter your age ')
            age=int(age)
            break
        except ValueError:
            print(f' The value is not valid')
            continue
    return fname, lname, age
  
fname, lname, age=user_info()

print('==========================')
print(f'Name :: {fname} {lname}')
print(f'Age  :: {age} years old ')
print('==========================')
