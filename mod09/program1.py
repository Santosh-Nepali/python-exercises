"""
Module 9 program 1

Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters. 
The elevator has methods go_to_floor, floor_up and floor_down. 
A new elevator is always at the bottom floor. 
If you make elevator h for example the method call h.go_to_floor(5),
the method calls either the floor_up or floor_down methods as many times as it needs to get to the fifth floor.
The methods run the elevator one floor up or down and tell what floor the elevator is after each move. 
Test the class by creating an elevator in the main program, tell it to move to a floor of your choice and then back to the bottom floor.


"""
#class called Elevatpr with attribute bottom floor and top floor
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
                    
elevator =Elevator(0, 12)


while True:
    try:
        target_floor=int(input('Which floor would you like to go?[0 - 12] '))
        if target_floor==0:
            print(f'You are already on {elevator.current_floor}')
            break
        elif target_floor>0 and target_floor<=12:
            elevator.go_to_floor(target_floor)
            print(f'You have reached to {elevator.current_floor}')
            break
        else:
            print("Floor does not exist.")
        
    except ValueError:
        print('invalid input')  
    

        