class Item:
    created_object=0
    def __init__(self, name: str ,price: float , quantity=0):
        print(f'object created :: {Item.created_object+1}')
        # Run validataions to the received arguments 
        assert price>=0, f'Price {price} is not greater than Zero!'
        assert quantity>=0, f'Quantity {quantity} is not greater than Zero!'
        
        #Assign to self object
        self.name=name
        self.price=price 
        self.quantity=quantity
        Item.created_object+=1
        print('I am init methods') # when object is created of a class, python
                                   # creates __init__ methods automatically
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
item1=Item("phone", 200, 10) #creating an object of the class
#item1.name="Phone" # assigning value to the name
#item1.price=100   # assigning price value 
#item1.quantity=5   # assigning quantity 
#print(item1.calculate_total_price(item1.price, item1.quantity))  # calling the methods and assigning object itself, price and quantity as an arguments
item2=Item("Laptop",300,20) #creating an object of the class
#item2.name="laptop" # assigning value to the name
#item2.price=200   # assigning price value 
#item2.quantity=10   # assigning quantity 
#print(item2.calculate_total_price(item2.price, item2.quantity))  # calling the methods and assigning object itself, price and quantity as an arguments

print(f'\n Item :: {item1.name}\n\t- Price :: {item1.price} \n\t- Quantity :: {item1.quantity} \n\t- Total :: {item1.calculate_total_price()}')
print(f'\n Item :: {item2.name}\n\t- Price :: {item2.price} \n\t- Quantity :: {item2.quantity} \n\t- Total :: {item2.calculate_total_price()}')