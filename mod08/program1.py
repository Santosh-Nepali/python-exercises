"""
Write a Car class that has the following properties: registration number, 
maximum speed, current speed and travelled distance. 
Add a class initializer that sets the first two of the properties 
based on parameter values. 
The current speed and travelled distance of a new car must be 
automatically set to zero. 
Write a main program where you create a new car 
(registration number ABC-123, maximum speed 142 km/h).
Finally, print out all the properties of the new car.
"""
# Creating class car with attributes and methods
class Car:
    def __init__(self, registration_no='ETB-259', max_speed=60):
        self.registration_no=registration_no
        self.max_speed=max_speed
        self.current_speed=0
        self.travel_distance=0
        
    def drive(self):
       # print(f'Car registration :: {self.registration_no} \n - Maximum Speed :: {self.max_speed} km/h \n - Current_speed :: {self.current_speed} km/h \n - Distance travel :: {self.travel_distance} km\n')
        
        print("Car registration ::", self.registration_no, "\n - Maximum Speed ::", self.max_speed, "km/h \n - Current_speed ::", self.current_speed, "km/h \n - Distance travel ::", self.travel_distance, "km\n")

# creating objects of the class.
#for i in range(3):
 #   reg_number=input('Enter the registration number of the car[xxx-nnn]: ')
  #  max_speed=input('Enter the maximum speed[km/h]')
    
    car1=Car(ABC-123, 142)
    car1.drive()