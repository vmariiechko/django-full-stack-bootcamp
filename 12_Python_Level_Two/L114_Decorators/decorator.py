# Re-assigning function using decorator
def new_decorator(func):

	def wrap_func():
		print("Code here before executing func")
		func()
		print("func() has been called")

	return wrap_func

def first_func_needs_decorator():
	print("First function is in need of a decorator!")

first_func_needs_decorator = new_decorator(first_func_needs_decorator)

first_func_needs_decorator()


# Using '@' symbol
@new_decorator
def second_func_needs_decorator():
	print("Second function is in need of a decorator!")

second_func_needs_decorator()