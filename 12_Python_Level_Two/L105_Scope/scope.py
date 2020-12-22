# Test
x = 10

def my_func():
	x = 50
	return x

print(x)
print(my_func())
my_func()
print(x)

# LEVELS:

# Local
lambda x: x**3

# Enclosing function locals and Globals
name = "Global Scope!"

def greet():
	name = "Jimmy"

	def hello():
		print('hello '+name)

	hello()

greet()

# Built-in
# len = 10	# Don't do this!

# Another examples:
y = 30

def func1(y):
	print("y:",y)
	y = 200
	print("local y:",y)

func1(y)
print(y)

# Accessing to global
z = 75

def func2():
	global z
	z = 125

print('Before func2 call, z:',z)
func2()
print('After func2 call, z:',z)