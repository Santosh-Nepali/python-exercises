"""
Module_8 program3.py

Again, extend the program by adding a new drive method that receives the number of hours as a parameter.
The method increases the travelled distance by how much the car has travelled in constant speed in the given time.
Example: The travelled distance of car object is 2000 km.
The current speed is 60 km/h. Method call car.drive(1.5) increases the travelled distance to 2090 km.


"""
class Car:
    def __init__(self, registration_no, max_speed): #constructor initializer
        self.registration_no=registration_no
        self.max_speed=max_speed
        self.current_speed=0
        self.travel_distance=0
        
    def accelerate(self,change_in_speed):  #method for calculate the current speed
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
    
    # logic for calculating the total distance travelled.
    def drive(self, hours):
        self.hours=hours
        self.travel_distance=self.travel_distance+hours*self.current_speed
# Main program
# creating objects of the class .    
car=Car("ABC-123", 142)

# Diplaying current details of the car
print("Registration Number: ",car.registration_no)
print(" - Maximum Speed: ", car.max_speed,"km/h")
print(" - Current Speed: ", car.current_speed,"km/h")
print(" - Travelled Distance: ",car.travel_distance,"km")

#Accelerating
car.accelerate(30)
print("The current Speed after accelerating +30 km/h :: ",car.current_speed,"km/h")
car.accelerate(70)
print("The current Speed after accelerating +70 km/h ::",car.current_speed,"km/h")
car.accelerate(50)
print("The current Speed after accelerating +50 km/h ::",car.current_speed,"km/h")
car.drive(4)

# Diplaying Details of car After driving for 4 hours with different accelerating speed
print("Registration Number: ",car.registration_no)
print(" - Maximum Speed: ", car.max_speed,"km/h")
print(" - Current Speed: ", car.current_speed,"km/h")
print(" - Travelled Distance: ",car.travel_distance,"km")

# Emergency brake

car.accelerate(-200)
print("The final speed after Applying Emergency brake :: ",car.current_speed,"km/h")
