class Cat:
    def __init__(self, name, color):
        self.name=name
        self.color=color
    
    def meow(self):
        print(f"{self.name} says: Meow")
    
      
    # for testing purpose, this code only runs when you execute this file indpendently
if __name__ == "__main__":
    cat = Cat("TestMisty", "black")
    cat.meow()