"""
module_4 program_5
Write a program that asks the user for a username and password. 
If either or both are incorrect, the program ask the user to enter the username and password again. 
This continues until the login information is correct or wrong credentials have been entered five times. 
If the information is correct, the program prints out Welcome. 
After five failed attempts the program prints out Access denied. 
The correct username is python and password rules.
"""
max_attempt=5       
correct_username='python'  
correct_password='rules'

def get_user_credentials():
    #print('changes')
    username=input('Enter username ::: ')
    password=input('Enter password ::: ')
    return username, password

for count in range(max_attempt):
    print(f'{count+1} times out of {max_attempt} attempts')
    uname, pname=get_user_credentials()
    if uname.strip()==correct_username and pname.strip()==correct_password:
        print('----Welcome----')
        break
else:
    print('Access Denined')
