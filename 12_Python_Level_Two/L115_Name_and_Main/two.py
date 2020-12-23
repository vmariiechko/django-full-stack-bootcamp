import one
print("Top level two.py")

one.func()

if __name__ == '__main__':
	print("Two.py being run directly")
else:
	print("Two.py is being imported")