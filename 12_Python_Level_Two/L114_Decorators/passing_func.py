# Second part

# Assign funcion to variable
def hello(name="Vadym"):
	return "Hello " + name

print(hello())

mygreet = hello

print(mygreet())


# Nested function
def hello(name="Vadym"):
	print("The hello() function has been run!")

	def greet():
		return "This string is inside greet()"

	def welcome():
		return "This string is inside welcome!"

	print(greet())
	print(welcome())
	print("End of hello()")

hello()


# Return nested function
def hello(name="Vadym"):
	print("The hello() function has been run!")

	def greet():
		return "This string is inside greet()"

	def welcome():
		return "This string is inside welcome!"

	if name == "Vadym":
		return greet
	else:
		return welcome

func = hello()

print(func())


# Function as a parameter
def hello():
	return "Vadym!"

def other(func):
	print("Hello ", end='')
	print(func())
	print(func)
	
other(hello)
