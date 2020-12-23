# First part:
# Reminder about scope
s = "GLOBAL VARIABLE"

def func1():
	return 1

print(func1())


# Passing global variable to func2
def func2(s):
	return s

print(func2(s))


# Using global variable in func3
def func3():
	return s

print(func3())


# Re-assigning global variable inside of func4
def func4():
	global s
	s = 50
	return s

print(func4())


# Print local and global variables
def func5():
	mylocal = 10
	print(locals())
	print(globals())

func5()

