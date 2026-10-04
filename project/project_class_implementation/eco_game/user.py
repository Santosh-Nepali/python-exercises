"""
user.py
---------
"""
class User:
    def __init__(self, user_id, name, age):
        self.user_id=user_id
        self.name=name
        self.age=age
        
    def __str__(self):
        return f"User_ID :: {self.user_id} \n\t -- Name :: {self.name}"


class UserManager:
    """ information of all registered users and handling signup for new user"""
    minimum_age=12
    
    def __init__(self):
        self.users_logs=[]
        self.next_id=1
    
    def signup(self):
        """ asking for name and age and validating the age and also register the user if age is valid
        and also returns the new user object or None if the player is under the minimum age        
        """
        name=input("What is your name? ")
        
        while True:
            try:
                age=int(input("Enter your age :: "))
                break
            except ValueError:
                print("Value is not valid")
                continue
        
        # Removing users under 12 from the list
        if age<=self.minimum_age:
            print(f"{name} You are minor so you cannot continue the game.")
            return None
        user=User(self.next_id, name, age)
        self.users_logs.append(user)
        print(f'User :: {name} added with USER_ID :: {self.next_id}')
        self.next_id+=1
        return user
        
    def show_profiles(self):
        """ 
        printing profiles of each and every users one by one.
        
        """
        if not self.users_logs:
            print("Not registered users yet")
            return
        for user in self.users_logs:
            print(user)
  