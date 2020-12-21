# Filter function
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
	return num%2 == 0

evens = filter(even_bool,mylist)
print(evens)
print(list(evens))


lambda num: num%2 == 0

evens = filter(lambda num: num%2 == 0,mylist)
print(evens)
print(list(evens))


tweet = 'Go Sports! #Sports'
result = tweet.split('#')
print(result)

print('x' in [1,2,3])
print('x' in [1,2,3,'x'])