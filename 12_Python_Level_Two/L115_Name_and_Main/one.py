def func():
	print("func() in one.py")

print("Top level of one.py")

if __name__ == '__main__':
	print("one.py has been run directly")
else:
	print("one.py has been imported")