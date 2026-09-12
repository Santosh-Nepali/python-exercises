"""
Project 1. Starting the Programming Project Assignment
Create a separate folder project/ for the game inside the Python exercise project, and create a readme.md file inside it. Add the name of your game as the heading and your own name below it.
Create a program in the folder that asks for the player’s name and age, stores them in variables, and prints them to the console.


Project 2. Main Menu
Modify the game project program so that if the user enters an age under 12, the program informs them that they are a minor and shuts down.
Otherwise, the program greets the user, displays the main menu, and asks for commands until the user enters "lopeta".
Add a few fictional commands that each produce a different output in the console. After a command, always display the menu again. 

Project 3. Main Menu Functions and “Inventory”
Continue developing the game project: Create a separate function for each main menu function (at least three), 
which is executed when the user selects that function.
One function must ask the user for information (e.g. an item) that is added to a list variable.
Another function must print the contents of the list to the user.
The other functions can be designed and implemented freely.

"""

#----------------------------
# Menu Display function
#----------------------------
users_log=[]
#next_id=1

def show_menu():
    print('\n\t==== MENU ====')
    print('TAKE || MOVE || DROP || LOPETA || USER-PROFILE || HELP ')


#----------------------------
# User information function
#----------------------------
def command_signup():
    #fname=input('Enter your first name ')
    #lname=input('Enter your Last name ')
    next_id=1
    name=input('Enter your name')
    # user_log={}

    while True:
        try:
            age=input('Enter your age ')
            age=int(age)
            break
        except ValueError:
            print(f' The value is not valid')
            continue
        
    #assigning each details.

    # Removing users under 12 from the list
    if age<=12:
        print(f'{name} you are minor so you cannot continue the game.')
        return None
    else:
        user={
            "user_id": next_id, 
            "name":name, 
            "age":age
            }
        users_log.append(user)
        print(f'User :: {name} added with USER_ID :: {next_id}')
        next_id+=1
        return user
    

#----------------------------
# User Profile Function
#----------------------------
def command_profile():
    for user in users_log:
        print(f'User_id ::{user['user_id']}-- Name :: {user['name']}')
 
#----------------------------
# take command function
#----------------------------

def command_take():
    print('Take command')
    pass


#----------------------------
# move command function
#----------------------------
def command_move():
    print('Move command')
    pass

#----------------------------
# drop command function
#----------------------------
def command_drop():
    print('Drop command')
    pass


#----------------------------
# help command function
#----------------------------
def command_help():
    print('Help command')
    pass

#----------------------------
# MAIN GAME LOOP
#----------------------------
current_user=command_signup()
#print(f'{current_user}')
if current_user is None:
    print(f'Game Shutting Down')
else:
    print(f'\n========== Welcome {current_user["name"]} ==========')
    
    while True:
        show_menu()
        print('\n')
        command=input('Enter the command :::: ')
        
        if command.upper().strip()=='LOPETA':
            print('Thanks for playing game. Good Bye')
            break
        
        elif command.upper().strip()=='TAKE':
            command_take()
        
        elif command.upper().strip()=='MOVE':
            command_move()
        
        elif command.upper().strip()=='DROP':
            command_drop()
        
        elif command.upper().strip()=='HELP':
            command_help()
        elif command.upper().strip()=='USER-PROFILE':
            command_profile()
        else:
            print(f'{command} is not recognized') 
    
#print('==========================')
#print(f'Name :: {fname} {lname}')
#print(f'Age  :: {age} years old ')
#print('==========================')
