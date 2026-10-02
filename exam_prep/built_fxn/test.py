class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} costs ${self.price}"

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price!r})"


product1 = Product("Laptop", 1200)

print(product1)
print(repr(product1))