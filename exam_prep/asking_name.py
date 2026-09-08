player_name=()
while True:
    name=input('Enter your name :: ')
    if name=='':
        break
    else:
        player_name = player_name + (name, )

# accessing the tuples
for name in player_name:
    print(f'Name of Player: {name}')
    