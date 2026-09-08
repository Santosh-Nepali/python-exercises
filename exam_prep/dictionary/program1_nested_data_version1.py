
# Create a list named 'cars'
cars = [
    # First car (dictionary)
    {
        "make": "Toyota",
        "model": "Corolla",
        "year": 2018
    },
    # Second car (dictionary)
    {
        "make": "Ford",
        "model": "Focus",
        "year": 2020
    },
    # Third car (dictionary)
    {
        "make": "VW",
        "model": "ID.3",
        "year": 2023
    }
]

for car in cars:
    print('********************')
    for key, value in car.items():
        print(f'{key} ::: {value}')
        
'''
for i in range(len(cars)):
    print('--------------------')
    for  key, value in cars[i].items():
        print(f'{key} ::: {value}')
'''
# here items() is the function which returns key a values of the dictonary