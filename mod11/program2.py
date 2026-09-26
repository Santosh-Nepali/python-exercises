
"""

Module 11 program 1

Extend the previously written Car class by adding two subclasses: ElectricCar and GasolineCar. 
Electric cars have the capacity of the battery in kilowatt-hours as their property. 
Gasoline cars have the volume of the tank in liters as their property. Write initializers for the subclasses.
For example, the initializer of electric cars receives the registration number, maximum speed and battery capacity as its parameter.
It calls the initializer of the base class to set the first two properties and then sets its capacity. 
Write a main program where you create one electric car (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l). Select speeds for both cars,
make them drive for three hours and print out the values of their kilometer counters.

"""

import random


class Car:
    def __init__(self, registration_no, max_speed):
        self.registration_no = registration_no
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_travel = 0

    def accelerate(self, change_on_speed):
        self.current_speed = self.current_speed + change_on_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.distance_travel = self.distance_travel + hours * self.current_speed


class ElectricCar(Car):
    def __init__(self, registration_no, max_speed, battery_capacity):
        super().__init__(registration_no, max_speed)   # sets registration_no and max_speed
        self.battery_capacity = battery_capacity         # the new, electric-specific property


class GasolineCar(Car):
    def __init__(self, registration_no, max_speed, tank_volume):
        super().__init__(registration_no, max_speed)   # sets registration_no and max_speed
        self.tank_volume = tank_volume                   # the new, gasoline-specific property


# ----------------------------
# Main program
# ----------------------------
electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.accelerate(100)
gasoline_car.accelerate(90)

electric_car.drive(3)
gasoline_car.drive(3)

print(f"Electric car {electric_car.registration_no}: {electric_car.distance_travel} km")
print(f"Gasoline car {gasoline_car.registration_no}: {gasoline_car.distance_travel} km")