# Inheritance
# Create an Aniaml class
class Animal():

	def __init__(self):
		print("Animal Initial Method")

	def who_am_i(self):
		print("Animal")

	def eat(self):
		print("Eating")

# Create a Dog class
class Dog(Animal):

	def __init__(self):
		# Animal.__init__(self)
		print("Dog Initial Method")

	def bark(self):
		print("WOOF")

mydog = Dog()
mydog.who_am_i()
mydog.eat()
mydog.bark()



# Special Methods
class Book():

	def __init__(self, title, author, pages):
		self.title = title
		self.author = author
		self.pages = pages

	def __str__(self):
		return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)

	def __len__(self):
		return self.pages

	def __del__(self):
		print("A book was deleted")

b = Book("Python", "Vadym", 250)
print(b)
print(len(b))
del b