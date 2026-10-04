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


Project 4 - Organize the Structure and Introduce Objects
Note! You can also implement the game project without classes and objects, but in that case you cannot receive full points for the project. The object-oriented structure below is only a first model. For your own game, 
you can create exactly the classes and objects that are appropriate for it.

Organize the files in your project into separate modules and packages as needed. Describe the structure in the readme.md file. Continue following this instruction throughout the development of the entire project!
"""

# Entry point for the package eco_game which has to be executed at first.
from eco_game.game import Game  # importing class Game from package_name.module_name i.e. eco_game.game
if __name__=='__main__':
    game=Game()
    game.execute()

