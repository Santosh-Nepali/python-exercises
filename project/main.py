"""
Project 1. Starting the Programming Project Assignment
Create a separate folder project/ for the game inside the Python exercise project, and create a readme.md file inside it. Add the name of your game as the heading and your own name below it.
Create a program in the folder that asks for the player’s name and age, stores them in variables, and prints them to the console.


Project 2. Main Menu
Modify the game project program so that if the user enters an age under 12, the program informs them that they are a minor and shuts down.
Otherwise, the program greets the user, displays the main menu, and asks for commands until the user enters "lopeta".
Add a few fictional commands that each produce a different output in the console. After a command, always display the menu again. 

changes is made on the file 
changes 

"""

#----------------------------
# User information function
#----------------------------
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


#----------------------------
# Menu Display function
#----------------------------
def show_menu():
    print('==== MENU ====')
    print('TAKE || MOVE || DROP || HELP || LOPETA')

  


#----------------------------
# MAIN GAME LOOP
# MAIN GAME LOOP
# MAIN GAME LOOP
# MAIN GAME LOOP
#----------------------------
fname, lname, age=user_info()
if age < 12:
    print(F'{fname} {lname} you are a minor, so you cannot continue the game')
else:
    print(f'========== Welcome {fname} {lname} ==========')
#print('==========================')
#print(f'Name :: {fname} {lname}')
#print(f'Age  :: {age} years old ')
#print('==========================')
