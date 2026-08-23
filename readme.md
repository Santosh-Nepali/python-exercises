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

```javascript

```

6. Write a program that draws two random combinations of numbers for a combination lock:

- a 3-digit code where each number is between 0 and 9.
- a 4-digit code where each number is between 1 and 6.

```javascript

```

#### Project 1. Starting the Programming Project Assignment

- Create a separate folder project/ for the game inside the Python exercise project, and create a readme.md file inside it. Add the name of your game as the heading and your own name below it.
- Create a program in the folder that asks for the player’s name and age, stores them in variables, and prints them to the console.

## Module 3

## Acknowledgements

-[ How to write a Good readme](https://readme.so/editor)

## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)
