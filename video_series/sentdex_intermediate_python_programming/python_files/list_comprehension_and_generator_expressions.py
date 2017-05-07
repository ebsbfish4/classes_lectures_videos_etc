#! usr/bin/python3

# Starting in python 3, range became a generator function. What this means is
# if you put for i in range(5), a list from 0 to 4 is not created and stored in
# memory. Fundamentally, list comprehension is faster than a generator, but it is
# going to use much more RAM than a generator.

# How do we build thest things? What is:

xyz = [i for i in range(5)]

# This will produce the same output as:

xyz = []
for i in range(5):
    xyz.append(i)


# The first is a list, second is a generator
xyz = [i for i in range(5)]
xyz = (i for i in range (5))
