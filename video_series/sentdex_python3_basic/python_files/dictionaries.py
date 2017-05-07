#! python3

# Dictionaries are a lot like associated arrays in other languages. They are
# unsorted, so just because you put something into the dictionary in order has
# no effect.

# The main concept is that for each element of the dictionary you will have keys
# and values. These values can be of any type - including functions.

# You use curly braces to tell python that you are making a dictionary

exDict = {'Jack':[15, 'blonde'], 'Bob':[22,'brown'], 'Alice':[12,'black'], 'Kevin':[17, 'red']}

print(exDict['Jack'])

exDict['Tim'] = 14

print(exDict['Tim'])

exDict['Tim'] = 15

print(exDict['Tim'])

# To get rid of something you can do


del exDict['Tim']

print(exDict['Jack'][1])
