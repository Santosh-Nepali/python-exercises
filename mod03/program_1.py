"""
module_3 program_1
Write a program that asks a fisher the length of a zander in centimeters. 
If the zander does not fulfill the size limit, the program instructs 
to release the fish back into the lake and notifies the user of 
how many centimeters below the size limit the caught fish was.
 A zander must be 42 centimeters or longer to meet the size limit.
"""

zander_size_limit=47 # variable setting the limit of fish size to catch

print("======= Hello Fisherman ======= ")
while True:
    try:
        zander_size=float(input('Enter the lengthe of Zander you catch in centimeter >>> '))
        break
    except ValueError:
        print('Value is valid ')
        continue

if zander_size<zander_size_limit:       
    print('Sorry!! Fisherman Effort is appreciated')
    print(f'Release the fish back to lake as fish is {(zander_size_limit-zander_size)} cm below standard limit >=47 cm')
else:
    print(f'Congratulation Fisherman you catch {zander_size} cm fish from lake')