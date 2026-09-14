class Car:
    created=0
    def __init__ (self, color, brand, year):
        self.color=color
        self.brand=brand
        self.year=year
        Car.created+=1
   
    def drive(self):
        print('The car is driving.')
car1=Car('Red','Toyota',2020) 
car2=Car('blue','Toyota',2022)
car3=Car('yellow', 'Nixon', 2026)
car4=car1
 
print(f'Brand: {car1.brand}\n\t-Color :: {car1.color} \n\t-Year :: {car1.year}')
print(f'Brand: {car4.brand}\n\t-Color :: {car4.color} \n\t-Year :: {car4.year}')
print(f'The number of objects created {Car.created}')
