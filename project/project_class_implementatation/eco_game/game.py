"""
game.py
-------
Here Game class holds the game state such as location, score and inventory) 
and runs the main menu loop
"""

import random
from user import UserManager
from waste_item import WasteItem, waste_items_database
from inventory import Inventory

# Defining class Game ::: # this is class for Game 
# which is main control for waste sorting console game 
class Game: 
    waste_collection_point="Collection Point"
    bin_locations=["Bio", "Paper", "Energy", "Plastic", "Mixed Waste"]
    
    def __init__(self):
        self.user_manager=UserManager()
        self.inventory=Inventory()
        self.score=0
        self.current_location=self.waste_collection_point
        self.all_locations=[self.current_location] + self.bin_locations



    #----------------------------
       # Menu Display Method
    #----------------------------
    def show_menu(self):
        print('\n\t\t\t ******** MENU ******** ')
        print(f'\n\t\t (You are at: {self.current_location} | Score: {self.score})')
        print('TAKE || MOVE || DROP || LOPETA || INVENTORY || SCORE || USER-PROFILE || HELP ')
    


    #------------------------------------------------------------------
      # command_inventory methods to prints the items of inventory list 
    #-------------------------------------------------------------------
    def command_inventory(self):
        self.inventory.show()
        
     
    #----------------------------
        # User Profile Function
    #----------------------------
    
    def command_profile(self):
        self.user_manager.show_profiles()
    
    #--------------------------------------------------------------------
        # take command function
        # only works at the Collection Point, 
        # Picks a random waste item and it to the inventory list variable.
    #---------------------------------------------------------------------
    
    def command_take(self):
        if self.current_location!=self.waste_collection_point:
            print("There is nothing to take, First Move to Collection Point first. ")
            return
        item=random.choice(waste_items_database)
        self.inventory.add_item(item)
        print(f"Item Picked::: {item}")
        print("Want to pick more? Yes: Use Command Take Again NO: Use command DROP and Select bins ")
#checking the code
#x=Game()

#print(x.all_locations)
#print(x.show_menu)
#print(x.inventory)
     
    
