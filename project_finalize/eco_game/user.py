"""
user.py
---------
"""
import json
#-----------------------------------------------------
    # Defining the name of class as User 
#-----------------------------------------------------
class User:
    # Initializer for  class User
    def __init__(self, user_id, name, age, score=0):
        self.user_id=user_id
        self.name=name
        self.age=age
        self.score=score
        
    def __str__(self):
        return(
            f"User_ID :: {self.user_id}\n"
            f"\t -- Name :: {self.name}\n"
            f"\t -- Age :: {self.age}\n"
            f"\t -- Score :: {self.score}"
           )
        
    # here converting the user object into a dictionary for the Json
    def to_the_dictionary(self):
        
        return{
            "user_id":self.user_id,
            "name":self.name,
            "age": self.age,
            "score":self.score
            
        }

class UserManager:
    """ user details managemenent and handling login or signup """
    def __init__(self, filename="users.json"):
        self.filename=filename
        self.users_logs=[]
        self.next_id=1
        self.load_users()
    
    def load_users(self):
        # loading the users from the json file 
        try: 
            with open(self.filename, "r") as file:
                users_data=json.load(file)
        except FileNotFoundError:
            print("No users file found and starting with emply USER List.")
            return
        
        for data in users_data:
            user=User(
                data["user_id"],
                data["name"],
                data["age"],
                data.get("score",0) 
            )
            self.users_logs.append(user)
            
        
        # Creating unique id for each users
        if self.users_logs:
            highest_id=0
            for user in self.users_logs:
                if user.user_id>highest_id:
                    highest_id=user.user_id
                    
            self.next_id=highest_id+1
            
            
    def save_users(self):
        ## saving in to the json file 
        users_data=[]
        for user in self.users_logs:
            users_data.append(user.to_the_dictionary())
        
        with open(self.filename, "w") as file:
            json.dump(users_data, file, indent=4)
    

        
    def signup(self):
        """ 
        Registering new user
        """
        name=input("What is your name? ")
        
        while True:
            try:
                age=int(input("Enter your age :: "))
                break
            except ValueError:
                print("Value is not valid")
                continue
            
        user=User(self.next_id, name, age, score=0)
        self.users_logs.append(user)
        print(f'User :: {name} added with USER_ID :: {self.next_id}')
        self.next_id+=1
        self.save_users()
        return user
        
        
    def login(self):
        # Find the existing user using the name and ID:
        name=input("Enter your Name :: ")
        try:
            user_id=int(input("Enter your USER_ID :: "))
        except ValueError:
            print("Invalid USER_ID.")
            return None
        
        for user in self.users_logs:
            if user.user_id==user_id and user.name.lower()==name.lower():
                print("WelCome Back!")
                print(user)
                return user
        print("User Not Found")
        return None
    
    # This is main method where which in the beginning         
    def start_user(self):
    
        while True:
            answer=input("\n Are you already registered? (yes/no) ::").strip().lower()
            if answer in ("yes","y"):
                user=self.login()
                if user is not None:
                    return user
                print("Please try again or register as a new users.")
            elif answer in ("no","n"):
                return self.signup()
            
            else:
                print("Please Enter yes or no.")
                
