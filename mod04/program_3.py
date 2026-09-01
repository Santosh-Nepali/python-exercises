"""
module_4 program_3
Write a program that asks the user to enter numbers 
until they enter an empty string to quit. 
Finally, the program prints out the smallest and largest number from the numbers it received.

"""
largest=None        #assigning largest with none type data 
smallest=None       # Assigning smallest with none type data
while True:
    print(' ==== Quit(empty input) ==== ')  #print message within 
    num=input('Enter the number: ')
    if num=='':                     #checking condition for empty string input
        break                       # it will exit the loop if condition holds true
    num=float(num)                  # changing default string datatype into float for number comparision
    if largest is None or num>largest:   # checking condition for largest number from user data
        largest=num                      # assigning number into largest variable
    if smallest is None or num<smallest: # checking condition for smallest number from user data
        smallest=num                     # assigning number into smallest varible 

print(f'Largest  :::: {largest}')          # printing largest value from lists 
print(f'Smallest :::: {smallest}')        # printing smallest value from list of numbers