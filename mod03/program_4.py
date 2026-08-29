'''
Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year. 
A year is a leap year if it is divisible by four. 
However, years divisible by 100 are leap years only if they are also divisible by 400.

'''

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