class Customer:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
    
    def customer_places_order(self, order):
        print(self.fname, self.lname, "places the order and its order id ", order.order_id)

class Restaurant:
    def __init__(self, name):
        self.name=name
        
    def prepare_order(self, order):
        print(self.name, "is preparing order", order.order_id)

class Order:
    def __init__(self, order_id):
        self.order_id=order_id  
    
customer1=Customer("John", "Chamling")
resturant1=Restaurant("PizzaHut")
order1=Order(101)

customer1.customer_places_order(order1)

resturant1.prepare_order(order1)

