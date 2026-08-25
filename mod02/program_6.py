"""
Write a program that draws two random combinations of numbers for a combination lock:
- a 3-digit code where each number is between 0 and 9.
- a 4-digit code where each number is between 1 and 6.
"""
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

    

