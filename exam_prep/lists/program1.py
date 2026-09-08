def inventory(items):
    print("Items inside your backpack:")
    for item in items:
        print(f' - {item}')
    
    items.clear()
    return
    
backpack=["bottle", "Map", "Compass", "Chewing"]
inventory(backpack)
backpack.append("Engergy Drinks")
inventory(backpack)

'''
What happened here? When a list is given as a parameter, 
it is passed to the function differently compared to basic type variables.

The value of a basic-type variable is copied 
from the argument in the function call to a parameter value.
In case of a list, the list contents are not copied.
Only the memory address of the list is passed on to the function. 
The memory address is where the list is stored in main memory.

In this case the memory address of the global backpack variable 
is stored as the value of the items variable. 
Now both the backpack and items variables point to the same list 
in computer memory. 
The function changes the contents of the list stored
in the items variable with the list method clear that clears the list. 
As there is only one shared list, the change also applies to 
the global backpack variable.
Therefore, changes to a list that has been received as a parameter
also apply to the list that was used in the function call.
'''
