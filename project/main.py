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

import random
#----------------------------
# Global Data
#----------------------------

users_log=[]
inventory=[]  # the list variable that TAKE adds to the INVENTORY prints
score=0
current_location="Collection Point"
bin_locations=["Bio", "Paper", "Energy", "Plastic", "Mixed Waste"]
all_locations=["Collection Point"]+bin_locations
waste_items_database=[
    {"name": "banana peel", "category": "Bio", "fact":"Bio waste like fruit peel can be composted or turned into biogas."},
    {"name": "apple core", "category": "Bio", "fact":"Food scraps deccompose naturally and idle for composting."},
    {"name": "used tea bag", "category": "Bio", "fact":"Tea bag without plastic linings break down easily as bio waste"},
    {"name": "newspaper", "category": "Paper", "fact":"Paper can be recycled up 5-7 times before its fibers become too short to reuse."},
    {"name": "cardboard box", "category": "Paper", "fact":"Clean, dry cardboard is one of the most recyclable materials available."},
    {"name": "newspaper", "category": "Paper", "fact":"Paper can be recycled up 5-7 times before its fibers become too short to reuse."},
    {"name": "notebook", "category": "Paper", "fact": "Paper recycling saves significant water and energy compared to making new paper."},
    {"name": "broken light bulb", "category": "Energy", "fact": "Some light bulbs need special recycling to recover energy or hazardous elements."},
    {"name": "old batteries", "category": "Energy",  "fact": "Batteries can be processed to recover metals and energy instead of polluting landfills."},
    {"name": "used cooking oil", "category": "Energy", "fact": "Used cooking oil can be converted into biodiesel, making it valuable energy waste."},
    {"name": "plastic bottle", "category": "Plastic", "fact": "A plastic bottle can take up to 450 years to decompose in a landfill."},
    {"name": "yogurt container", "category": "Plastic", "fact": "Most rigid plastic containers can be recycled if rinsed clean first."},
    {"name": "plastic bag", "category": "Plastic", "fact": "Thin plastic bags often need special drop-off points instead of regular recycling."},
    {"name": "broken ceramic mug", "category": "Mixed Waste", "fact": "Ceramics don't melt like glass, so they usually can't be recycled with regular glass."},
    {"name": "used tissue", "category": "Mixed Waste", "fact": "Used tissues count as general waste due to contamination."},
    {"name": "greasy pizza box", "category": "Mixed Waste", "fact": "Grease-soaked cardboard usually can't be recycled since the oil contaminates the fibers."},    
]
#next_id=1

#----------------------------
# Menu Display function
#----------------------------

def show_menu():
    print('\n\t\t\t ******** MENU ******** ')
    print(f'\n\t\t (You are at: {current_location} | Score: {score})')
    
    print('TAKE || MOVE || DROP || LOPETA || INVENTORY || SCORE || USER-PROFILE || HELP ')


#----------------------------
# User information function
#----------------------------
def command_signup():
    #fname=input('Enter your first name ')
    #lname=input('Enter your Last name ')
    next_id=1
    name=input('Enter your name :: ')
    # user_log={}

    while True:
        try:
            age=input('Enter your age :: ')
            age=int(age)
            break
        except ValueError:
            print(f' The value is not valid')
            continue
        
    #assigning each details.

    # Removing users under 12 from the list
    if age<=12:
        print(f'{name} You are minor so you cannot continue the game.')
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
    if not users_log:
        print("Not registered users yet.")
        return
    for user in users_log:
        print(f'User_id ::{user['user_id']}-- Name :: {user['name']}')

 
#----------------------------
# take command function
# only works at the Collection Point, Picks a random waste item annd it to the inventory list variable.
#----------------------------

def command_take():
    global current_location
    if current_location!='Collection Point':
        print('There is nothing to take here, Move to the Collection Point first. ')
        return
    item=random.choice(waste_items_database)
    inventory.append(item)
    print(f'You picked up : {item["name"]}')
    print('Carry it to the bin you think is correct, then use DROP. ')


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
    print(f'\n\n\t\t --------------- Welcome {current_user["name"]} ---------------')
    
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
