import json

user = {
    "name": "Alex",
    "age": 25
}

with open("user.json", "w") as file:
    json.dump(user, file, indent=4)