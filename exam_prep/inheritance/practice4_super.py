# Create the Animal class
class Animal:
	def __init__(self, name):
		self.name=name

	def speak(self):
		print(self.name)

class Dog(Animal):
	def __init__(self, name):
		super().__init__(name)
	def speak(self):
		super().speak()
d1=Dog("Rex")
d1.speak()
