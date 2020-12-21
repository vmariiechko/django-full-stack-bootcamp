# Basics
def my_func1(param1='default'):
	"""
	THIS IS THE DOCSTRING
	"""
	print("My first python function in this course!")
my_func1()


def my_func2(param2='default'):
	print("My first python function in this course! {}".format(param2))
my_func2()

# Return
def hello():
	return "hello"

result = hello()
print(result)

# Return type
def addNum(num1,num2):
	if type(num1) == type(num2) == type(10):
		return num1+num2
	else:
		return "Sorry, I need integers!"

result = addNum(2,3)
print(result)
print(type(result))

result = addNum("2","3")
print(result)
print(type(result))

result = addNum(2,"3")
print(result)
print(type(result))