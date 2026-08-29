'''
Write a program that asks for the biological gender and hemoglobin value (g/l). 
The program the notifies the user if the hemoglobin value is low, normal or high.
A normal hemoglobin value for adult females is between 117-155 g/l.
A normal hemoglobin value for adult males is between 134-167 g/l.

'''

def gender():       # user-defined function for gender input
    print('Female :::: F')
    print('Male :::: M')
    user_gender=input('Enter your Biological Gender')
    return user_gender      # returning single value 

def hemoglobin(): # user defined function for hemoglobin input of users
    while True:
        try: 
            user_hemoglobin=int(input('Enter your Hemoglobin Level in g/l'))
            break
        except ValueError:
            print('Invalid value')
            continue
    return user_hemoglobin # returning user's hemoglobin level

user_gender=gender()
user_hemoglobin=hemoglobin()

if user_gender.upper()=='F':

    if user_hemoglobin<117:
        print('You are Female Gender and Hemoglobin is low')
    elif user_hemoglobin>155:
        print('You are Female and Hemoglobin is high')
    else:
        print('You are Female and Hemoglobin is normal')

elif user_gender.upper()=='M':
    if user_hemoglobin<134:
        print('You are Male Gender and Hemoglobin is low')
    elif user_hemoglobin>167:
        print('You are Male and Hemoglobin is high')
    else:
        print('You are Male and Hemoglobin is normal')