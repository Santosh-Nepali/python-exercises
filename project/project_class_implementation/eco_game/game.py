"""
game.py
-------
Here Game class holds the game state such as location, score and inventory) 
and runs the main menu loop
"""

import random
from .user import UserManager, User
from .waste_item import WasteItem, waste_items
from .inventory import Inventory

#-----------------------------------------------------
    # Defining class Game ::: # this is class for Game 
    # which is main control for waste sorting console game 
#-----------------------------------------------------

class Game: 
    waste_collection_point="Collection Point"
    bin_locations=["Bio", "Paper", "Energy", "Plastic", "Mixed Waste"]
    
    # class Game magic initializer
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
        print('\n\t\t\t 🌷🌷🌷🌷🌷🌷🌷 MENU 🌷🌷🌷🌷🌷🌷🌷  ')
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
        item=random.choice(waste_items)
        #print(item)
        self.inventory.add_item(item)
        print(f"Item Picked::: {item.name}")
        print("Want to pick more? Yes: Use Command Take Again NO: Use command DROP and Select bins ")

    #-----------------------------------------------------------------------
        # move command function
        # moves the players between the collection point and the five bins
    #-----------------------------------------------------------------------
    
    def command_move(self):
        print(f"Available Locations: {', '.join(self.all_locations)}")
        destination=input("Where do you want to move? :::: ").strip()
        
        matched=None
        for location in self.all_locations:
            if location.upper()==destination.upper():
                    matched=location
                    break
        if matched:
            self.current_location=matched
            print(f"You move to {self.current_location}.")
        else:
            print(f"{destination} is not a valid location.")
    
    #-------------------------------------------------------------------------
        # drop command method
        # Sort a carried item into into the bin 
        # the player is currently standing in 
        # Correct bin : +1 point .. Wrong bin : -1 point with an explanation
    #--------------------------------------------------------------------------
    def command_drop(self):
        # Checking the inventory list is empty or not 
        if not self.inventory:
            print("You have nothing to drop.")
            return
        
        # Checking game player is in bin location or not  
        if self.current_location not in self.bin_locations:
            print("This is not a sorting bin, Move to Proper Bin first ")
            return
        
        # displaying the inventory list 
        print(f"Your Inventory : {', '.join(self.inventory.names())}")
        
        # checking the item input by player if in the inventory list or not 
        item_name=input("Which item do you want to drop in the Bin? ::::: ").strip()
        matching_item=self.inventory.find_by_name(item_name)
        if matching_item is None:
            print(f"You are not carrying {item_name}.")
            return
        
        # checking the condtion for correct sorting by players 
        # if correcting sorting in to the bin locations awarding the player +1 and 
        # Incorrecting sorting of items penalize by -1 
        if matching_item.category==self.current_location:
            self.score+=1
            print(f"Correct !! +1 points. (score: {self.score})")
        else:
            self.score-=1
            print(f"Wrong Bin !! -1 point. (Score: {self.score})")
            print(f"Correct Bin: {matching_item.category}")
            print(f"Reason :{matching_item.fact}")
        
        # After dropping the waste into bin location, 
        # inventory is updated after removing the item  
        self.inventory.remove_item(matching_item)
    
    #----------------------------
        # score command method
    #----------------------------
    def command_score(self):
        print(f"Your score is : {self.score}")
        
    
    #----------------------------
        # help command method
    #----------------------------
    def command_help(self):
        #print("\n=================================================================================================================================")
        try:
            with open("eco_game/instruction.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("File not found.")
        
        #print("=====================================================================================================================================")
    
    #----------------------------
        # MAIN GAME LOOP
    #----------------------------
    def execute(self):
        
        try:
            with open("eco_game/intro.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("File not found.")
                
        self.current_user=self.user_manager.signup()
        
        if self.current_user is None:
            print("Game is Shutting Down.")
        else:
            print(f"\n\n\t\t --------------- Welcome {self.current_user.name} ---------------")
        
            while True:
                self.show_menu()
                print("\n")
                command=input("Enter the Command ::::: ")
                if command.upper().strip()=="LOPETA":
                    print("Thanks for playing the game. Good Bye")
                    break
                elif command.upper().strip()=="INVENTORY":
                    self.command_inventory()
                elif command.upper().strip()=="TAKE":
                    self.command_take()
                elif command.upper().strip()=="MOVE":
                    self.command_move()
                elif command.upper().strip()=="DROP":
                    self.command_drop()
                elif command.upper().strip()=="SCORE":
                    self.command_score()
                elif command.upper().strip()=="HELP":
                    self.command_help()
                elif command.upper().strip()=="USER-PROFILE":
                    self.command_profile()
                else:
                    print(f"{command} is not recognized")
                
    