# Different types of errors:

# print('hello)
# SyntaxError: EOL while scanning string literal

# mylistthere = [1,2,3]
# print(mylist)
# NameError: name 'mylist' is not defined


# Handle errors

# f = open("simple.txt", 'r')
# f.write("Hello World")
# print("Hello World")
# print function won't be runned because io.UnsupportedOperation: not writable error happened

try:
	f = open("simple.txt", 'w')
	f.write("Hello World")
except IOError:
	print("1) Couldn't interact with a file!")
else:
	print("1) SUCСESS")
	f.close()

try:
	f = open("simple.txt", 'r')
	f.write("Hello World")
except IOError:
	print("2) Couldn't interact with a file!")
finally:
	print("2) Will be executed in any way")