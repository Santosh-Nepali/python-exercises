"""
Module_8 program4.py
Now we will program a car race.
The travelled distance of a new car is initialized as zero.
At the beginning of the main program, create a list that consists of 10 car objects created using a loop.
The maximum speed of each new car is a random value between 100 km/h and 200 km/h.
The registration numbers are created as follows: “ABC-1”, “ABC-2” and so on. Now the race begins.
One per every hour of the race, the following operations are performed:
   
     -The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h.
     This is done using the accelerate method.
     -Each car is made to drive for one hour. This is done with the drive method.
The race continues until one of the cars has advanced at least 10,000 kilometers.
Finally, the properties of each car are printed out formatted into a clear table.



"""
import random
class Car:
     def __init__(self, registration_no, max_speed):
          self.registration_no=registration_no
          self.max_speed=max_speed
          self.current_speed=0
          self.distance_travel=0
     
     def accelerate(self, change_on_speed):
          self.change_on_speed=change_on_speed
          self.current_speed=self.current_speed+change_on_speed
          if self.current_speed>self.max_speed:
               self.current_speed=self.max_speed
               #print(f'current speed:{self.current_speed}')
          if self.current_speed<0:
               self.current_speed=0
          
          #print(change_on_speed)
     def drive(self, hours):
       self.hours=hours
       self.distance_travel=self.distance_travel+self.hours*self.current_speed
     

#main program
car_object=[]

for count in range(10):
     registration_no="ABC-"
     registration_no+=str(count+1)
     max_speed=random.randint(100,200)
     #print(registration_no)
     #print(max_speed)
     
     name_object='car'
     name_object+=str(count)
     name_object=Car(registration_no, max_speed)
     car_object.append(name_object)

#for car in car_object:
 ##   print("******************************")
   #  print("Registration No. ::", car.registration_no)
    # print("Maximum Speed ::", car.max_speed,"km/h")
     #print("Current Speed ::", car.current_speed,"km/h")
     #rint("Distance Travelled ::", car.distance_travel,"km")

# Run the race, One hour at a time, until a car reaches 10000km 
hours=0
while True:
     for car in car_object:
          change_speed=random.uniform(-10, 15)
          # print(change_speed)
          car.accelerate(change_speed)
          car.drive(1)       
          hours+=1
     #checking if any car has reached at least 10000 km 
     if any(car.distance_travel>=10000 for car in car_object):
          break
          
print(f"\nRace finished after {hours} hours!\n")
print(f"{'Registration':<14}{'Max Speed':>4}{'Current Speed':>16}{'Distance':>14}")
print("-" * 56)  

for car in car_object:
     print(f"{car.registration_no:<14}" 
           f"{car.max_speed:>4} km/h"
           f"{car.current_speed:>11.1f} km/h"
           f"{car.distance_travel:>11.1f}km")
     
     
     