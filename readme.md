# Software 1 Python Exercises

A total of 6 points can be earned from the exercises associated with each module. The point value of one exercise is obtained by dividing the total points by the number of exercises. Exercises related to the project (marked separately) are assessed as part of the project. Points for these exercises can only be awarded for submissions made on time.

## 🚀 About Me

- **Name:** Santosh Nepali
- **University:** Metropolia University of Applied Science
- **Faculty:** Bachelor of Information Technology
- **Group:** TXL26S1-B
- **Student ID:** 2630920

## Module 1 (1 and 2. First Program and Setting Up Version Control)

##### I have completed exercises 1 and 2

##### 1. Install the development environment. Write a program that greets you using your own name. If your name were Viivi Virta, the program would print: Hello, Viivi Virta!

##### 2. Create a GitHub user account and make a repository for Python exercises. Configure your local project to use the repository as the remote repository for the exercise project. Make sure that you can retrieve, commit, and push the changes you have made (pull, commit, push).

🤔 Code

```javascript

# Assigning first name and Surname
first_name='Santosh'
last_name='Nepali'

# printing Full name with hello greetings
print(f'Hello, {first_name}  {last_name}!')

```

## Module 2 (Variables and interactive programs)

##### I have completed exercises 1, 2, 3, 4, 5 and 6

1. Write a program that asks your name and then greets you by your name: Examples:

- If you enter Viivi as your name, the program will greet you with Hello, Viivi!.
- If you enter Ahmed as your name, the program will greet you with Hello, Ahmed!.

🤔 Code

```javascript

# Asking first name surname from users
first_name=input('Enter your First Name>> ')
last_name=input('Enter your Surname>> ')

# Print message with Full name of user
print(f'Hello! {first_name} {last_name}')

```

2. Write a program that asks the user for the radius of a circle and the prints out the area of the circle.

🤔 Code

```javascript

import math
while True:
    # Input radius of the circle
    try:
        radius=float(input('Enter radius of the cirlce :::: '))
    except ValueError:
        print(f'Radius cannot be string value')
        #continue
    else:
        if(radius<=0):
            print(f'Radius cannot be {radius} value')
            continue

        pi=3.14159
        area=pi*pow(radius,2)
        break

#Print area of circle with two decimal point after dot
print(f'The area of circle having radius = {radius} is ::: {area:0.2f} ')

```

3. Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of the rectangle. The perimeter of a rectangle is the sum of the lengths of each four sides.

🤔 Code

```javascript

while True:
    try:
        length=float(input('Enter length of the rectangle ::: ')) # Input Length of the rectangle
        width=float(input('Enter width of the rectangle ::: ')) # Input width of the rectangle

    except ValueError:
        print('Either length or width is invalid data type')

    else:
        if length<=0 or width<=0:
            print(f'The length {length} or width {width} is invalid')
            print('Enter fresh value for length and width')
            continue

        perimeter=2*(length+width) #Calculate perimeter of the rectangle
        area=length*width #Calculate area of the rectangle
        break

#Print Perimeter and area of rectangle with two decimal point after dot
print(f'The perimeter of rectangle of length: {length} and width: {width} is ::: {perimeter:0.2f} ')
print(f'The area of rectangle of length: {length} and width: {width} is ::: {area:0.2f} ')
```

4. Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.

🤔 Code

```javascript
sum=0           # Initializing sum as zero for addition
product=1       # Initializing variable product as 1 for multiplication
count=3         #Number of values that user will be asked to enter
for i in range(count):  # loop exactly 'count' times
    while True:     # keeps looping until a valid number is entered for this iteration
        user_input=input('Enter a number :: ') # getting raw text input from the user
        try:
            number=int(user_input)  # Attempt to conter input string to an integer
        except ValueError:          # Runs only if int() failed or user input is not a number
            print('Please enter a valid number.')   # inform the user input is not valid number and repeat loop
        else:                                       # runs only when error is exeception is eliminated
            sum=sum+number                          # adding the user enter valid number
            product=product*number                  # multiplying user enter number
            break                                   # exit the while loop and enters into for loop for next number
print(f' The sum of numbers is : {sum}')            # prints the sum of numbers
print(f' The Product of numbers is : {product}')    # Prints the product of the numbers
print(f' The average of the number enter is : {sum/count:0.2f}')    # Prints the average of numbers


```

5. Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti). The program converts the input to full kilograms and grams and outputs the result to the user:

- One talent is 20 pounds.
- One pound is 32 lots.
- One lot is 13,3 grams.

🤔 Code

```javascript
lots_from_talents=20*32 #converting from talents to lots
lots_from_pounds=32     # converting pounds to lots
grams_per_lot=13.3  # defining grams per lot
while True:
    try:
        talent=float(input('Enter Talents: ')) # Asking talent value from user as string and converting into float type
        pound=float(input('Enter pounds : '))  # Asking pound value from user as string and converting into float type
        lot=float(input('enter lots '))       # Asking lots value from user as string and converting into float type
    except ValueError:
        print('One of the enter value is not numeric') # if the value is not numerice and through the error
        continue        # Continues the loop for next numeric value
    else:               # if user enter value is error free then jumps to this else
        if talent<=0 or pound<=0 or lot<=0:  #checking the values enter are non-negative or zero
            print('One the value enter zero or negative')  # displays message zero or negative number
            continue                                    # continues the while loop
        lots=(talent*lots_from_talents)+(pound*lots_from_pounds)+lot # Changes all the values to lots
        #print(f'Lots value is: {lots}')
        break       # breaks the while loop

# Changing the lots into grams
total_grams=lots*grams_per_lot # converting lots into grams
#print(total_grams)
kilogram=total_grams//1000 # Floor Division operator giving quotient value as kilogram
grams=total_grams%1000      # remainder operator giving remainder value as grams

print(f'Kilogram :::: {kilogram}')
print(f'Grams :::: {grams:0.2f}')

```

6. Write a program that draws two random combinations of numbers for a combination lock:

- a 3-digit code where each number is between 0 and 9.
- a 4-digit code where each number is between 1 and 6.

🤔 Code

```javascript

import random

digit3_code=''  #Assigning string to digit3_code variable
digit4_code=''  # Assigning string to digit4_code variable

for i in range(3): # looping three times which goes from 0,1,3
    digit3 = random.randint(0,9) # randomizing the digits between 0 and 9
    #print(f'{digit3}')
    digit3_code=digit3_code+str(digit3) # concatenation of digits
print(f'The 3-digits code is :::: {digit3_code}') #prints 3 digits code

for i in range(4):  # looping four times which runs throuh 0,1,2,3
    digit4=random.randint(1,6) #randomizing the digits between 1 and 6 inclusively
    #print(f'{digit4}')
    digit4_code=digit4_code+str(digit4) # concatination of digits changing tinto string
print(f'The 4-digits code is :::: {digit4_code}') # prints 4 digits code



```

#### Project 1. Starting the Programming Project Assignment

##### I have done

- Create a separate folder project/ for the game inside the Python exercise project, and create a readme.md file inside it. Add the name of your game as the heading and your own name below it.
- Create a program in the folder that asks for the player’s name and age, stores them in variables, and prints them to the console.

## Module 3 (Conditional Structures)

## Done

1. Write a program that asks a fisher the length of a zander in centimeters. If the zander does not fulfill the size limit, the program instructs to release the fish back into the lake and notifies the user of how many centimeters below the size limit the caught fish was. A zander must be 42 centimeters or longer to meet the size limit.

🤔 Code

```javascript



zander_size_limit=47 # variable setting the limit of fish size to catch

print("======= Hello Fisherman ======= ")  # display text

while True:   # looping until it holds true
    try:
        zander_size=float(input('Enter the lengthe of Zander you catch in centimeter >>> '))   # asking length of fish and converting into float datatype
        break                           #exit the loop

    except ValueError:                  #value error
        print('Value is not valid ')        #displays invalid
        continue                        # continue the loop

if zander_size<zander_size_limit:       #Checking the size of standar limit
    print('Sorry!! Fisherman Effort is appreciated') #display the message
    print(f'Release the fish back to lake as fish is {(zander_size_limit-zander_size)} cm below standard limit >=47 cm') #displays the message with size of fish short of standard limits
else:
    print(f'Congratulation Fisherman you catch {zander_size} cm fish from lake')   # displays the message with size of fish catch by fisherman


```

2. Write a program that asks the user to enter the cabin class of a cruise ship and then prints out a written description according to the list below. You must use an if/elif/else structure in your solution.
   LUX: upper-deck cabin with a balcony.
   A: above the car deck, equipped with a window.
   B: windowless cabin above the car deck.
   C: windowless cabin below the car deck.

If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class.

🤔 Code

```javascript


def display_menu():
    print('------------------------')
    print(' Cabin class :: LUX  ')
    print(' Cabin class :: A ')
    print(' Cabin class :: B  ')
    print(' Cabin class :: C ')
    print('------------------------')

def user_input():
    user_choose=input('Enter Cabin Class From the Menu ::: ')
    return user_choose


display_menu()    # calling display menu function
user_selection=user_input()   # calling user input function and assign to the variable
if user_selection.upper()=='LUX':
    print(f'You have choosen ::: {user_selection} class\n Features ::: Upper-Deck Cabin with a Balcony ' )
elif user_selection.upper()=='A':
    print(f'You have choosen ::: {user_selection} class\n Features ::: Above the Car Deck, equipped with a window  ' )
elif user_selection.upper()=='B':
    print(f'You have choosen ::: {user_selection} class\n Features ::: Windowless Cabin Above the  Car Deck  ' )
elif user_selection.upper()=='C':
    print(f'You have choosen ::: {user_selection} class\n Features ::: Windowless Cabin Below the  Car Deck ')
else:
    print(f'You have entered ::: {user_selection}  Cabin Class, which is Invalid')

```

3. Write a program that asks for the biological gender and hemoglobin value (g/l). The program the notifies the user if the hemoglobin value is low, normal or high.
   A normal hemoglobin value for adult females is between 117-155 g/l.
   A normal hemoglobin value for adult males is between 134-167 g/l.

🤔 Code

```javascript

def gender():       # user-defined function for gender input
    print('Female :::: F')
    print('Male :::: M')
    user_gender=input('Enter your Biological Gender')
    return user_gender      # returning single value

def hemoglobin(): # user defined function for hemoglobin input of users
    while True:
        user_hemoglobin=input('Enter your hemoglobin level in g/l ::')
        try:
            user_hemoglobin=int(user_hemoglobin)
            if user_hemoglobin<0:
                print(f'{user_hemoglobin} is not valid')
                continue
            break
        except ValueError:
            print('Invalid value')
            continue
    return user_hemoglobin # returning user's hemoglobin level

user_gender=gender()
user_hemoglobin=hemoglobin()

if user_gender.upper()=='F':

    if user_hemoglobin<117:
        print('You are Female Gender and Hemoglobin is low')
    elif user_hemoglobin>155:
        print('You are Female and Hemoglobin is high')
    else:
        print('You are Female and Hemoglobin is normal')

elif user_gender.upper()=='M':
    if user_hemoglobin<134:
        print('You are Male Gender and Hemoglobin is low')
    elif user_hemoglobin>167:
        print('You are Male and Hemoglobin is high')
    else:
        print('You are Male and Hemoglobin is normal')


```

4. Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year. A year is a leap year if it is divisible by four. However, years divisible by 100 are leap years only if they are also divisible by 400.

🤔 Code

```javascript

def year(): # user defined function year()

    while True:
        year_input=input('Enter a Year  ') # Ask for the enter the year

        try:
            year_input=int(year_input)
            if year_input<=0:           # checking for years not zero valur or negative
                print('Enter the positive value')
                continue                # if user enters negative or zero as input continue the loop
            break                       # if user enters valid year then break the loop leaving the rest of statement to be executed and exit
        except ValueError:
            print('Enter the whole number for the year')
            continue

    return year_input

year_input=year()  # calling user defined function

if (year_input%4==0 and year_input%100!=0) or (year_input%400==0):  # check condition for leap year or not
    print(f'{year_input} is a leap year.')  # true statements of the condition check
else:
    print(f'{year_input} is not a leap year.') # false statement of condition check


```

## Module 4 (While loops)

## Done

1. Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.

🤔 Code

```javascript

count=1
while (count<=1000):
    rem=count%3
    if(rem==0):
        print(f'The number {count} is divisible by 3')
    count=count+1

```

2. Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.

🤔 Code

```javascript

inches=float(input('Enter the value for inch'))
while inches>0:
    centimeter=inches*2.54
    print(f'{inches:0.2f} inches is equals to {centimeter:0.2f} centimeter')
    inches=float(input('Enter negative value to stop the program'))
print('programs ended')

```

3. Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program prints out the smallest and largest number from the numbers it received.

🤔 Code

```javascript

largest=None        # assigning largest with none type data
smallest=None       # Assigning smallest with none type data
while True:
    print(' ==== Quit(empty input) ==== ')  #print message within
    num=input('Enter the number: ')
    if num=='':   #checking condition for empty string input
        break      # it will exit the loop if condition holds true
    try:
        num=float(num)     # changing default string datatype into float for number comparision
        if largest is None or num>largest:   # checking condition for largest number from user data
            largest=num                      # assigning number into largest variable

        if smallest is None or num<smallest: # checking condition for smallest number from user data
            smallest=num                     # assigning number into smallest variable
    except ValueError:
        print(f'It is not numeric.')

print(f'Largest  :::: {largest:0.2f}')          # printing largest value from lists
print(f'Smallest :::: {smallest:0.2f}')        # printing smallest value from list of numbers
```

4. Write a game where the computer draws a random integer between 1 and 10. The user tries to guess the number until they guess the right number. After each guess the program prints out a text: Too high, Too low or Correct. Notice that the computer must not change the number between guesses.

🤔 Code

```javascript
import random
random_value=random.randint(1,10)
#print(f'{random_value}')
while True:
    user_guess=input('Guess the number from 1-10 ::: ')
    try:
        user_guess=int(user_guess)
        if user_guess>random_value:
            print('You have enter too high number')
            continue

        elif user_guess<random_value:
            print('You have enter too low number')
            continue
        else:
            print('Correct')
            break
    except ValueError:
        print('non numeric value')

```

5. Write a program that asks the user for a username and password. If either or both are incorrect, the program ask the user to enter the username and password again. This continues until the login information is correct or wrong credentials have been entered five times. If the information is correct, the program prints out Welcome. After five failed attempts the program prints out Access denied. The correct username is python and password rules.

🤔 Code

```javascript

max_attempt=5
correct_username='python'
correct_password='rules'
count=0

def get_user_credentials():
    #print('changes')
    username=input('Enter username ::: ')
    password=input('Enter password ::: ')
    return username, password

#for count in range(max_attempt):
while(count<max_attempt):
    print('================================================')
    print(f'{count+1} times out of {max_attempt} attempts')
    uname, pname=get_user_credentials()

    if uname.strip().lower()==correct_username and pname.strip()==correct_password:
        print('----Welcome----')
        break
    count=count+1
    print('================================================')
else:
    print('Access Denined')


```

6. implement an algorithm for calculating an approximation for the value of pi (π). Let’s assume that A is a unit circle. A unit circle has the radius of one and it is centered at the origin (0,0). Smallest possible square B is drawn around the unit circle so that circle A is completely inside the square. The corners of the square are now (-1,-1), (1, -1), (1, 1), and (-1, 1). If a large number of random points are scattered inside the square, the fraction of points that fall inside the circle A correlates with the fraction of the area of circle A compared to the area of square B: πr^2/4 = π\*1^2/4 = π/4. This can be used as a simple method for calculating an approximation of the value of pi: Let’s generate a large number of random points, such as one million, inside square B. Let N be the total number of random points. Each point inside the square is tested for whether it resides inside circle A. Let n be the total number of points that fall inside circle A. Now we have n/N≈π/4, and from that we get π≈4n/N. Write a program that asks the user how many random points to generate, and then calculates the approximate value of pi using the method explained above. At the end, the program prints out the approximation of pi to the user. (Notice that it is easy to test if a point falls inside circle A by testing if it fulfills the inequation x^2+y^2<1.).

🤔 Code

```javascript

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

```

## Module 5 (List structures and iterative loops (for))

## Progressing

1.Write a program that asks the user how many dice to roll.
The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.
🤔 Code

```javascript

import random  # importing random modules

def total_sum(sum):    # defining user defined function
    roll_value=random.randint(1,6)  #rolling dices and assigning the result to variable
    print(f' The values generated each roll :: {roll_value}') # printing each value generated by each roll
    sum+=roll_value # adding the value to sum
    return sum      # returning the total sum

#==========================================
# Main program where number of dices to roll asked and pass to function calling
#==========================================
sum=0   # initializing sum variable to zero
number_dice=int(input('How many dices to roll? '))  # asking from user number of dices to roll
for roll in range(number_dice):  # for loop to using the dices.
    sum=total_sum(sum)          #calling user defined function and assigning the result to sum
print(f'The sum of rolling {number_dice} dices is ::{sum}') #displaying total dices and their sum


```

2. Write a program that asks the user to enter numbers until they input an empty string to quit. At the end, the program prints out the five greatest numbers sorted in descending order. Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.

🤔 Code

```javascript

```

3.Write a program that asks the user for an integer and tells if the number is a prime number. Prime numbers are number that are only divisible by one or the number itself.
For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
On the other hand, 21 is not a prime number as it is divisible by 3 and 7.

🤔 Code

```javascript

```

4. Write a program that asks the user to enter the names of five cities one by on (use a for loop for reading the names) and stores them into a list structure. Finally, the program prints out the names of the cities one by one, one city per line, in the same order they were read as input. Use a for loop for asking the names and a for/in loop to iterate through the list.

🤔 Code

```javascript

```

## Acknowledgements

-[ How to write a Good readme](https://readme.so/editor)

## Debugging line of code for the variable

print(f"DEBUG: user_selection = {repr(variable_name)}")

## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)
