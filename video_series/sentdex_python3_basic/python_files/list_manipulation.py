#! python3

x = [3,6,5,9,1,1,1,44,6,2]

x.append(2)
print(x == [3,6,5,9,1,1,1,44,6,2,2])

x.insert(2,99)
print(x == [3,6,99,5,9,1,1,1,44,6,2,2])


x.remove(1) # This will remove the fist 1
print(x == [3,6,99,5,9,1,1,44,6,2,2])

x.remove(x[3]) # This will remove the third index, 5
print(x == [3,6,99,9,1,1,44,6,2,2])

print(x[2] == 99) # Accessing an index

print(x[3:6] == [9,1,1]) # Access a slice

print(x[-2] == 2) # You can index from the end

print(x.index(99) == 2) # How you find the index of a list item

print(x.count(1) == 2) # How many values of a type in a list

x.sort() # How you sort the elements of a list
print(x == [1, 1, 2, 2, 3, 6, 6, 9, 44, 99])

y = ['Bob','Janet','Kelly','Alex','Joe','Brad']
y.sort()
print(y == ['Alex', 'Bob', 'Brad', 'Janet', 'Joe', 'Kelly'])


