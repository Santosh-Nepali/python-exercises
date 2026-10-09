import json
with open("user.json", "r") as file:
    user = json.load(file)
    
for data in user:
    print(user[data])

print(user)