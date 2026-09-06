"""
module_6 program_6

Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza in euros.
The function calculates and returns the unit price of the pizza per square meter. 
The main program asks the user to enter the diameter and price of two pizzas 
and tells the user which pizza provides better value for money (which of them has a lower unit price). 
You must use the function you wrote for calculating the unit prices.

"""
import math

#  user defined function  for unit price calculator
def unit_price_calculator(diameter_cm, price_pizza_euro):
    radius=diameter_cm/2
    area_m=(math.pi*radius**2)/10000
    return price_pizza_euro/area_m

# user-defined function of unit price per square meter
unit_price_per_sq_meter=[]
for i in range(2):
    diameter=float(input(f'Enter diameter of {i+1} pizza in cm::: '))
    price=float(input(f'Enter the price of {i+1} pizza in Euro:::  '))
    unit_price=unit_price_calculator(diameter, price)
    unit_price_per_sq_meter.append(unit_price)

for count, pizza_price in enumerate(unit_price_per_sq_meter):
    print(f'Price of Pizza {count+1} is {pizza_price:0.2f}')
    

if unit_price_per_sq_meter[0]<unit_price_per_sq_meter[1]:
    print('First Pizza has better value for money')
    
elif unit_price_per_sq_meter[0]>unit_price_per_sq_meter[1]:
    print('Second Pizza has better value for money')
    
else:
    print('Both Pizza has same value')
    






