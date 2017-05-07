#! usr/bin/python3

# Enumerate will return the tuple containing the count along the way and the
# item itself you are iterating over.

# Basically, this is what enumerate does. Whenever you find yourself using
# something along the lines of for i in range(len(<something>)), you are probably
# doing it WRONG!
example = ['left', 'right', 'up', 'down']
for i in range(len(example)):
    print(i, example[i])

# Instead you should do this
for i,j in enumerate(example):
    print(i,j)

# You can use enumerate over a dictionary and other iterables

new_dict = dict(enumerate(example))



[print(i, j) for i, j in enumerate(new_dict)]
