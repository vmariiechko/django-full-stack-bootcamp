# Creating our own Dog  class
class Dog():
	
	def __init__(self, breed, name):
		self.breed = breed
		self.name = name

mydog = Dog(breed="Haski", name="Bony")
# print(mydog.breed)
# print(mydog.name)

otherdog = Dog("Rottweiler", 'Jacky')
# print(otherdog.breed)
# print(otherdog.name)


# Another class with methods
class Circle():

	pi = 3.14

	def __init__(self, radius=1):
		self.radius = radius

	def area(self):
		return self.radius**2 * Circle.pi

	def set_radius(self, new_r):
		self.radius = new_r


myc = Circle(3)
myc.set_radius(100)
print(myc.area())


