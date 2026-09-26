"""
Module_10 program4.py

This exercise continues the previous car race exercise from the last exercise set. 
Write a Race class that has the following properties: name, distance in kilometers and a list of cars participating in the race. 
The class has an initializer that receives the name, kilometers, and car list as parameters and sets their values to the corresponding properties in the class. 
The class has the following methods:
     - hour_passes, which performs the operations done once per hour in the original exercise: generates a random change of speed for each car and calls their drive method.
     - print_status, which prints out the current information of each car as a clear, formatted table.
     - race_finished, which returns True if any of the cars has reached the finish line, meaning that they have driven the entire distance of the race.

Write a main program that creates an 8000-kilometer race called Grand Demolition Derby. 
The new race is given a list of ten cars similarly to the earlier exercise. 
The main program simulates the progressing of the race by calling the hour_passes in a loop, after which it uses the race_finished method 
to check if the race has finished. The current status is printed out using the print_status method every ten hours and then once more at the end of the race.




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

class Race:
     def __init__(self, name, distance, car_list):
          self.name=name
          self.distance=distance
          self.car_list=car_list
     
     def hour_passes(self):
          for car in self.car_list:
               change_speed=random.uniform(-10, 15)
               car.accelerate(change_speed)
               car.drive(1)
     
     def print_status(self):
          print(f"{'Registration':<14}{'Max Speed':>12}{'Current Speed':>16}{'Distance':>14}")
          print("-" * 56)
          for car in self.car_list:
               print(f"{car.registration_no:<14}"
                     f"{car.max_speed:>9} km/h"
                    f"{car.current_speed:>13.1f} km/h"
                    f"{car.distance_travel:>11.1f} km")
     
     def race_finished(self):
          return any(car.distance_travel>=self.distance for car in self.car_list)
     

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
race=Race("Grand Demolition Derby", 8000, car_object)

#for car in car_object:
 ##   print("******************************")
   #  print("Registration No. ::", car.registration_no)
    # print("Maximum Speed ::", car.max_speed,"km/h")
     #print("Current Speed ::", car.current_speed,"km/h")
     #rint("Distance Travelled ::", car.distance_travel,"km")

# Run the race, One hour at a time, until a car reaches 10000km 
hours = 0
while True:
    race.hour_passes()   # generate a random change of speed for each car and calls their drive method. 
    hours += 1

    if hours % 10 == 0:       #print out every ten hours
        race.print_status()

    if race.race_finished():
        break

print(f"\nRace finished after {hours} hours!")  # then once more ate the end the race 
race.print_status()     