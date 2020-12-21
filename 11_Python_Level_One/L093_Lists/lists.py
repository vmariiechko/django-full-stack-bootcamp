# Initialize
mylist = [1,2,3]
mylist = ['sadfjkflakd',12,1,2,3,4,True,'fasd',[1,2,3]]
print(mylist)
print(len(mylist))

# Indexing
mylist = ['a','b','c','d','e']
print(mylist[1])
print(mylist[:3])

# List is immutable
print('Before re-assignment:')
print(mylist)
mylist[0] = "New Item"
print("After re-assignment:")
print(mylist)

# Methods
mylist.append("Another Item")
mylist.append([1,2,3,4])
listtwo = ['x','y','z']
mylist.extend(listtwo)
print(mylist)

item = mylist.pop()
print(mylist)
print(item)

item = mylist.pop(0)
print(mylist)
print(item)

mylist.reverse()
print(mylist)

mylist = [1,2,4,5,6,73,2,2,1,3,4,5,6]
mylist.sort()
print(mylist)

# Nested list
mylist = [1,2, ['x','y','z']]
print(mylist[2])
print(mylist[2][1])

# List Comprehension
matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_row = [row[0] for row in matrix]
print(first_row)