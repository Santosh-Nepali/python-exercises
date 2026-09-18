class Item:
    def calculate_total_price(self,x, y):
        return x*y
item1=Item() #creating an object of the class
item1.name="Phone" # assigning value to the name
item1.price=100   # assigning price value 
item1.quantity=5   # assigning quantity 
print(item1.calculate_total_price(item1.price, item1.quantity))  # calling the methods and assigning object itself, price and quantity as an arguments

item2=Item() #creating an object of the class
item2.name="laptop" # assigning value to the name
item2.price=200   # assigning price value 
item2.quantity=10   # assigning quantity 
print(item2.calculate_total_price(item2.price, item2.quantity))  # calling the methods and assigning object itself, price and quantity as an arguments

    
    
    