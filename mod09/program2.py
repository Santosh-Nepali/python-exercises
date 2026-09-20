"""
Module 9 program 2
Extend the previous program by creating a Building class.
The initializer parameters for the class are the numbers of the bottom and top floors and the number of elevators in the building.
When a building is created, the building creates the required number of elevators.
The list of elevators is stored as a property of the building.
Write a method called run_elevator that accepts the number of the elevator and the destination floor as its parameters.
In the main program, write the statements for creating a new building and running the elevators of the building.




"""

#class called Elevator with attribute bottom floor and top floor
class Elevator:
    def __init__(self, bottom_floor, top_floor): # constructor initializer which get object(self), bottom_floor and top_floor at attribute
        self.bottom_floor=bottom_floor
        self.top_floor=top_floor
        self.current_floor=self.bottom_floor
            
    def floor_up(self):
        self.current_floor+=1
        #print(f'Current floor :: {self.current_floor}')

    def floor_down(self):
        self.current_floor-=1
        #print(f'Current Floor :: {self.current_floor}')
        
    
    def go_to_floor(self,target_floor):
        self.target_floor=target_floor
        #while True:   
        while self.current_floor!=self.target_floor:
            if self.current_floor<self.target_floor:
                self.floor_up()
            else:
                self.floor_down()

#defining class Building with different attributes
class Building:
    def __init__(self, bottom_floor, top_floor, no_of_elevators):
        self.bottom_floor=bottom_floor
        self.top_floor=top_floor
        self.no_of_elevators=no_of_elevators
        
        self.elevators_collection=[]
        # here number of elevators looping and create objects with top floor and bottom floor
        for count in range(self.no_of_elevators):
            self.elevator=Elevator(self.bottom_floor, self.top_floor)
            self.elevators_collection.append(self.elevator)
            
    def run_elevator(self, target_elevator_no, target_floor):
        self.target_floor=target_floor
        self.target_elevator=target_elevator_no
        
        elevator=self.elevators_collection[self.target_elevator]
        elevator.go_to_floor(target_floor)
    
    
    
# Begining of main program
no_of_elevators=6
top_floor=12
bottom_floor=0

#objects of class Building with number of floors and number of elevators
building=Building(bottom_floor,top_floor,no_of_elevators) 


 
#accessing the objects of elevators 
for number, elevator in enumerate(building.elevators_collection):
    print(f'{number}  {elevator}')               

# Asking which elevators to use 
while True:
    try:
        target_elevator_no=int(input("which Elevator you want to use? [1-6]"))
        
        if target_elevator_no>=1 and target_elevator_no<=6:
            break
        
        else:
            print("Elevator does not exist.")
    
    except ValueError:
        print("Invalid input")
        
        
#asking target floor to reach    
while True:
    try:
        target_floor=int(input('Which floor would you like to go?[0 - 12] '))
 
        if target_floor>=0 and target_floor<=12:
            #elevator.go_to_floor(target_floor)
            #print(f'You have reached to {elevator.current_floor}')
            break
        else:
           print("Floor does not exist.")
        
    except ValueError:
       print('invalid input')  
    
# calling method of class Building and passing elevator number and floor number as attributes
building.run_elevator(target_elevator_no,target_floor)

#Displaying the result of reached floor using specific elevator
print(f'You have to reached to the floor {building.elevator.current_floor} using elevator {building.target_elevator} ')

        