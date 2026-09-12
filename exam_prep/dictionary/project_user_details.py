
next_id=1
users_log=[]
#----------------------------
# User information function
#----------------------------
def command_signup():
    #fname=input('Enter your first name ')
    #lname=input('Enter your Last name ')
    global next_id
    name=input('Enter your name')
    # user_log={}

    while True:
        try:
            age=input('Enter your age ')
            age=int(age)
            break
        except ValueError:
            print(f' The value is not valid')
            continue
    #assigning each details.
        
    user={
        "user_id": next_id, 
        "name":name, 
        "age":age
        }
    users_log.append(user)
    
    print(f'User :: {name} added with USER_ID :: {next_id}')
        #append(fname, lname, age)}
    next_id+=1
  
    #return fname, lname, age
    
    
for i in range(3):    
    command_signup()
    print(f'{users_log}')