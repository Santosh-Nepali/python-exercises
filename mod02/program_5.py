"""
module_2 program_5

Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti). The program converts the input to full kilograms and grams and outputs the result to the user:
- One talent is 20 pounds.
- One pound is 32 lots.
- One lot is 13,3 grams.

"""
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

