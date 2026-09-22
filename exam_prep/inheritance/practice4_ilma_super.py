# Create the Animal class
class Animal:
	def __init__(self, name):
		self.name=name

	def speak(self):
		print(self.name)

class Dog(Animal):
	def __init__(self, name):
		Animal.__init__(self, name)
	def speak(self):
		Animal.speak(self)
d1=Dog("Rex")
d1.speak()
