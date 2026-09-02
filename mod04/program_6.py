"""
module_4 program_6

Implement an algorithm for calculating an approximation for the value of pi (π). 
Let’s assume that A is a unit circle. A unit circle has the radius of one and it is centered at the origin (0,0).
Smallest possible square B is drawn around the unit circle so that circle A is completely inside the square. 
The corners of the square are now (-1,-1), (1, -1), (1, 1), and (-1, 1). 
If a large number of random points are scattered inside the square, 
the fraction of points that fall inside the circle 
A correlates with the fraction of the area of circle A compared to the area of square B: πr^2/4 = π*1^2/4 = π/4. 
This can be used as a simple method for calculating an approximation of the value of pi: 
Let’s generate a large number of random points, such as one million,
inside square B. Let N be the total number of random points. 
Each point inside the square is tested for whether it resides inside circle A. 
Let n be the total number of points that fall inside circle A. 
Now we have n/N≈π/4, and from that we get π≈4n/N.
Write a program that asks the user how many random points to generate, 
and then calculates the approximate value of pi using the method explained above. 
At the end, the program prints out the approximation of pi to the user. 
(Notice that it is easy to test if a point falls inside circle A by testing 
if it fulfills the inequation x^2+y^2<1.).


"""

import random
points_inside_circle=0 # initializing number of points falls inside the cicle to zero (n)
counter_loop= 0 # for the repeatation of loops
while True:
    get_random_point_generate=input('How many Random point to generate') # asking from user to generate total number of random point (N)
    try:
        get_random_point_generate=int(get_random_point_generate)   #checking for only interger value as input
        
        while(counter_loop<get_random_point_generate):          # looping upto total number of random points to generate
            x=random.uniform(-1,1)          #generate random of x axis from -1 to 1 
            y=random.uniform(-1,1)          # generate float point uniform for y axix from -1 to 1
            #print(f'x= {x} y={y}')
            z=x**2+y**2                     # using pythagorous theorem to find the distances 
            if z<1:                         # checking condition x**2+y**2<1 since radius is 1 and to check whether plotted value falls inside circle or not
                points_inside_circle+=1     # counting number of points inside the circle
                #print(f'Points indside the cicle {points_inside_circle}')
                #print(f'point inside the cicle{z}')
            counter_loop+=1             #looping counter
            #print(f'Points outside the circle {z}')
        break
    except ValueError:
        print('invalid data')
pi=float((4*points_inside_circle)/get_random_point_generate)  # calculating value of pi equating ration of area of cicle to square and area of circle to area of rectangle
print(f'The pi value is {pi:0.2f}')