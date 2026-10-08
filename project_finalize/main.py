"""
Organize the files in your project into separate modules and packages as needed. 
Describe the structure in the readme.md file. 
Continue following this instruction throughout the development of the entire project!
"""

# Entry point for the package eco_game which has to be executed at first.
#from eco_game.game import Game  # importing class Game from package_name.module_name i.e. eco_game.game
from eco_game import *

if __name__=='__main__':
    game=Game()
    game.execute()
    

