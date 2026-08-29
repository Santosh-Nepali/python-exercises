"""
module_3 program_1
Write a program that asks a fisher the length of a zander in centimeters. 
If the zander does not fulfill the size limit, the program instructs 
to release the fish back into the lake and notifies the user of 
how many centimeters below the size limit the caught fish was.
 A zander must be 42 centimeters or longer to meet the size limit.
"""

zander_size_limit=47 # variable setting the limit of fish size to catch

print("======= Hello Fisherman ======= ")  # display text

while True:   # looping until it holds true
    try:
        zander_size=float(input('Enter the lengthe of Zander you catch in centimeter >>> '))   # asking length of fish and converting into float datatype
        break                           #exit the loop 

    except ValueError:                  #value error  
        print('Value is valid ')        #displays valid 
        continue                        # continue the loop

if zander_size<zander_size_limit:       #Checking the size of standar limit
    print('Sorry!! Fisherman Effort is appreciated') #display the message
    print(f'Release the fish back to lake as fish is {(zander_size_limit-zander_size)} cm below standard limit >=47 cm') #displays the message with size of fish short of standard limits
else:
    print(f'Congratulation Fisherman you catch {zander_size} cm fish from lake')   # displays the message with size of fish catch by fisherman