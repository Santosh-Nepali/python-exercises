"""
module_6 program_1

Write a program that asks the user to enter names until he/she enters an empty string.
After each name is read the program either prints out New name or Existing name depending 
on whether the name was entered for the first time.
Finally, the program lists out the input names one by one, 
one below another in any order. 
Use the set data structure to store the names.

"""

name_collection=set()   #Defining the empty set, if set is not empty then we define the set as my_set={2,4,6,7}

while True:     # looping the program until empty space in enter
    name=input('Enter the name:')
    name=name.strip().upper()  # remove the space in left and right side of the word and converting in capital letter
    if name=='':    # if user enter value is empty then it exits the while loop
        break
    elif name in name_collection:  # represents each name of the collection set
        print(f'{name} is Existing name')
    else:
        print(f' {name} is new name and adding to the set')
        name_collection.add(name)

for name in name_collection:
    print(f'Name :::: {name}')
