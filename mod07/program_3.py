"""
module_7 program_3

Write a program for fetching and storing airport data. The program asks the user if they want to enter a new airport, fetch the information of an existing airport or quit. 
If the user chooses to enter a new airport, the program asks the user to enter the ICAO code and name of the airport. If the user chooses to fetch airport information instead, 
the program asks for the ICAO code of the airport and prints out the corresponding name. If the user chooses to quit, 
the program execution ends. The user can choose a new option as many times they want until they choose to quit. 
(The ICAO code is an identifier that is unique to each airport.
For example, the ICAO code of Helsinki-Vantaa Airport is EFHK. 
You can easily find the ICAO codes of different airports online.)
"""

def menu():
    print('....................................')
    print('|  Add  | :: Register New Airport')
    print('....................................')
    print('| Fetch | :: Access Airport Details')
    print('....................................')
    print('| Quit  | :: To exit the program')
    print('....................................')
    select =input('Choose One of the MENU from Above :::: ')
    return select

def add_airport(airport_details):
    icao=input('Enter ICAO code of the Airport::: ').upper().strip()
    if icao in airport_details:
        print(f'{icao} belongs to {airport_details[icao]} already.')
        confirm=input('Do you want to Overwrite the Airport details? (y/n)').lower().strip()
        if confirm!='y':
            print('Cancelled. No change made.')
            return
    name=input('What is the Name of Airport? ').strip()
    airport_details[icao]=name
        
    for icao in airport_details:
        print(f'{icao} ::: {airport_details[icao]}')
    return

def fetch_airport(airport_details):
    icao=input('Do you know ICAO code of the Airport?::: ').upper().strip()
    if icao in airport_details:
        print(f'{icao} belongs to {airport_details[icao]}')
    else:
        print(f'{icao} code is not found')
    return 
    

airport_details={
    'AGAF' : 'Afutara Airport',
    'AYPY' : 'Jacksons International Airport',
    'EFHK' : 'Helsinki-Vantaa airport',
    'EGLL' : 'London Heathrow Airport',
    'KJFK' : 'John F. Kennedy international Airport',
    'LFPG' : 'Charles De Gaulle Airport(France)',
    'YSSY' : 'Sydney Kingsford Airport',
    'RJTT' : 'Tokyo Haneda Airport(Japan)'
    
}    
while True:
        user_choice=menu()
        if user_choice.upper() =='ADD':
            add_airport(airport_details)
        elif user_choice.upper()=='FETCH':
            fetch_airport(airport_details)
        elif user_choice.upper()=='QUIT':
            print('Thank you for visiting')
            break
        else:
            print('Invalid Choice')
            