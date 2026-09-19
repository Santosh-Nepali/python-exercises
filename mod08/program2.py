"""
Module_8 program2.py

Extend the program by adding an accelerate method into the new class.
The method should receive the change of speed (km/h) as a parameter.
If the change is negative, the car reduces speed. 
The method must change the value of the speed property of the object. 
The speed of the car must stay below the set maximum and cannot be less than zero.
Extend the main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h.
Then print out the current speed of the car.
Finally, use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed.
The travelled distance does not have to be updated yet.
"""
# Creating class car with attributes and methods
class Car:
    def __init__(self, registration_no, max_speed): #constructor initializer
        self.registration_no=registration_no
        self.max_speed=max_speed
        self.current_speed=0
        self.travel_distance=0
        
    def accelerate(self,change_in_speed):
        self.change_in_speed=change_in_speed
        self.current_speed=self.current_speed+self.change_in_speed
        #print(self.current_speed)
        
        # Checking condition for current_speed must below max_spped
        if self.current_speed>self.max_speed:
            print("**** Alert!! you might get overspeed fine. ****\n Your's Current speed :: ",self.current_speed,"km/h")
            self.current_speed=self.max_speed
            #print("Good Job, You maintain the maximum speed i.e. ",self.current_speed,"km/h")
        
        # Checking condition for speed in negative or not. 
        if self.current_speed<0:
            self.current_speed=0
            #print("The speed cannot be negative value")
        
     
# Main program
# creating objects of the class .    
car=Car("ABC-123", 142)

# Diplaying current details of the car
print("Registration Number: ",car.registration_no)
print(" - Maximum Speed: ", car.max_speed)
print(" - Current Speed: ", car.current_speed)
print(" - Travelled Distance: ",car.travel_distance)

#Accelerating
car.accelerate(30)
print("The current Speed after accelerating +30 km/h :: ",car.current_speed,"km/h")
car.accelerate(70)
print("The current Speed after accelerating +70 km/h ::",car.current_speed,"km/h")
car.accelerate(50)
print("The current Speed after accelerating +50 km/h ::",car.current_speed,"km/h")

# Emergency brake

car.accelerate(-200)
print("The final speed after Applying Emergency brake :: ",car.current_speed,"km/h")

