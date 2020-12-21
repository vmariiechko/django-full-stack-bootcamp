# Basics
'hello'
"hello"

" I'm a dog "

# Indexing
mystring = 'abcdefg'
print(mystring)
print(mystring[0])
print(mystring[-1])
print(mystring[3])

# Slicing
print(mystring[2:])
print(mystring[:3])
print(mystring[2:5])
print(mystring[:])	# the whole string 
print(mystring[::2])	# step
# mystring[0] = 'X'		# string indexing is immutable

# Basic Mehtods
x = mystring.upper()
print(x)
print(x.lower())
x = "hello world"
print(x.split())

# Print Formatting
x = "Insert another string here: {}".format("INSERT ME!")
print(x)

x = "Item One: {y} Item Two: {x}".format( x = "dog", y= "cat")
print(x)