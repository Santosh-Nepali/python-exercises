"""
game.py
Here Game class holds the game state such as location, score and inventory) and runs the main menu loop
"""

import random
from .user import UserManager
from .waste_item import WasteItem, waste_items_database
from .inventory import Inventory

class Game: # this is class for Game which is main control for waste sorting console game
    waste_collection_point="Collection Point"
    bin_locations=["Bio", "Paper", "Energy", "Plastic", "Mixed Waste"]
    
    def __init__(self):
        #self.user_manager=UserManager()
        #self.inventory=Inventory()
        self.score=0
        self.current_location=self.waste_collection_point
        self.all_locations=[self.current_location] + self.bin_locations



    #----------------------------
        # Menu Display method
    #----------------------------
    def show_menu(self):
        print('\n\t\t\t ******** MENU ******** ')
        print(f'\n\t\t (You are at: {self.current_location} | Score: {self.score})')
        print('TAKE || MOVE || DROP || LOPETA || INVENTORY || SCORE || USER-PROFILE || HELP ')
    
# checking the code
#x=Game()

print(x.all_locations)
     
    
