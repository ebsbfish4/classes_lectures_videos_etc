#! usr/bin/python3

# zip function takes values from multiple iterables and combines them into one

x = [1, 2, 3, 4]
y = [7, 6, 2, 1]
z = ['a', 'b', 'c', 'd']

##for a,b,c in zip(x,y,z):
##    print(a,b,c)

# This produces a zip object, not a list or something
##print(zip(x,y,z))

# But of course you can iterate through and make it into a list
print(list(zip(x,y,z)))

# You can also convert to a dict if you only use two values
print(dict(zip(z,x)))

# Can also use list comprehension
[print(a,b,c) for a,b,c in zip(x,y,z)]

# It could be tempting to take previous line and do
for x,y in zip(x,y):
    print(x,y)

print(x) # will now only be 4.
# In list comprehension the variables are not stored, but in a regular for loop
# the variables are saved and can overwrite
