"""
module_2 program_4

Write a program that asks the user for three integer numbers. 
The program prints out the sum, product, and average of the numbers.

"""

 # Asking three integer numbers from user
#number_1=int(input('Enter First number'))
#number_2=int(input('Enter Second number'))
#number_3=int(input('Enter Third number'))

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
            #continue                                # return back to while loop
        else:                                       # runs only when error is exeception is eliminated
            sum=sum+number                          # adding the user enter valid number
            product=product*number                  # multiplying user enter number
            break                                   # exit the while loop and enters into for loop for next number
print(f' The sum of numbers is : {sum}')            # prints the sum of numbers 
print(f' The Product of numbers is : {product}')    # Prints the product of the numbers
print(f' The average of the number enter is : {sum/count:0.2f}')    # Prints the average of numbers