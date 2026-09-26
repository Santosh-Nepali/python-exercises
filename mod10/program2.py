"""
Module 10 program 2
Extend the previous program by creating a Building class.
The initializer parameters for the class are the numbers of the bottom and top floors and the number of elevators in the building.
When a building is created, the building creates the required number of elevators.
The list of elevators is stored as a property of the building.
Write a method called run_elevator that accepts the number of the elevator and the destination floor as its parameters.
In the main program, write the statements for creating a new building and running the elevators of the building.


"""

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = self.bottom_floor

    def floor_up(self):
        self.current_floor += 1

    def floor_down(self):
        self.current_floor -= 1

    def go_to_floor(self, target_floor):
        self.target_floor = target_floor
        while self.current_floor != self.target_floor:
            if self.current_floor < self.target_floor:
                self.floor_up()
            else:
                self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, no_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.no_of_elevators = no_of_elevators

        self.elevators_collection = []
        for count in range(self.no_of_elevators):
            new_elevator = Elevator(self.bottom_floor, self.top_floor)   # local variable, NOT self.elevator
            self.elevators_collection.append(new_elevator)

    def run_elevator(self, target_elevator_no, target_floor):
        self.target_floor = target_floor
        self.target_elevator = target_elevator_no

        elevator = self.elevators_collection[target_elevator_no - 1]   # -1 converts 1-based input to 0-based index
        elevator.go_to_floor(target_floor)
        self.last_elevator = elevator   # remember exactly which elevator we just moved
        return elevator

# Beginning of main program
no_of_elevators = 6
top_floor = 12
bottom_floor = 0

building = Building(bottom_floor, top_floor, no_of_elevators)

# Display elevators numbered 1-6, matching the prompt's expected range
#for number, elevator in enumerate(building.elevators_collection, start=1):
   # print(f'{number}  {elevator}')

while True:
    try:
        target_elevator_no = int(input("Which Elevator you want to use? [1-6] "))
        if target_elevator_no>=1 and target_elevator_no <= 6:
            break
        else:
            print("Elevator does not exist.")
    except ValueError:
        print("Invalid input")

while True:
    try:
        target_floor = int(input('Which floor would you like to go? [0-12] '))
        if target_floor>=0 and target_floor<= 12:
            break
        else:
            print("Floor does not exist.")
    except ValueError:
        print('Invalid input')

building.run_elevator(target_elevator_no, target_floor)

print(f'You have reached floor {building.last_elevator.current_floor} using elevator {target_elevator_no}')

