"""
module_7 program_1

Write a program that asks the user for a number of a month and 
then prints out the corresponding season (spring, summer, autumn, winter).
Save the seasons as strings into a tuple in your program. 
We can define each season to last three months, 
December being the first month of winter.
"""
seasons=('Spring', 'Summer', 'Autumn', 'Winter') # Tuple storing seasons list
months={ 
 "1" : "January",
 "2" : "February",
 "3" : "March",
 "4" : "April",
 "5" : "May",
 "6" : "June",
 "7" : "July",
 "8" : "August",
 "9" : "September",
 "10" : "October",
 "11" : "November",
 "12" : "December"
} # dictionary storing  key values for 12 months 

print("***** Season Identifying System (based on month) *****")
month=input("Enter the month( 1 = January, 2 = February ...... 12 = December ) ::: ")
if month in months:
    name_of_month=months[month]
    print(f'{month}')
    if month=='12' or month=='1' or month=='2':
        print(f'The month ::: {name_of_month} belongs ::: {seasons[3]} ')
    elif month=='3' or month=='4' or month=='5':
        print(f'The month ::: {name_of_month} belongs ::: {seasons[0]} ')
    elif month=='9' or month=='10' or month=='11':
        print(f'The month ::: {name_of_month} belongs ::: {seasons[2]} ')
    else:
        print(f'The month ::: {name_of_month} belongs ::: {seasons[1]}' )
else:
    print(f'user entered data {month} is not valid')

#for season in seasons:
#    print(f'{season}')
'''
for key, value in months.items():
    if key=='12' or key=='1' or key=='2':
        print(f'The month ::: {value} belongs ::: {seasons[3]} ')
        break
    elif key=='3' or key=='4' or key=='5':
        print(f' The month ::: {value} belongs ::: {seasons[0]} ')
        break
    elif key=='6' or key=='7' or key=='8':
        print(f' The month ::: {value} belongs ::: {seasons[1]} ')
        break
    elif key=='9' or key=='10' or key=='11':
        print(f' The month ::: {value} belongs ::: {seasons[2]} ')
        break
    #print(f'{key}: {value}')
      
if month==1 or month==12 or month==2:
    print(f' The month {month} is ')
    '''
