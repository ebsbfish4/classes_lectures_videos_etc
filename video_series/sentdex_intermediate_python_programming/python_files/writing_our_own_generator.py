#! usr/bin/python3

# remember the difference between
##[i for i in range(5)]#list
##(i for i in range(5))#generator

##def simple_gen():
##    yield 'Oh'
##    yield 'hello'
##    yield 'there'
##
##for i in simple_gen():
##    print(i)

# Let's consider an example where a generator will be better than a for
# loop or even list comprehension. Let's say you are trying to figure
# out the write combination.

CORRECT_COMBO = (3,6,1)

# with a for loop, you might try something like this, but even after
# it has found the combo it will keep iterating through. Break will not
# work, it will only break the current c3 loop. You could create a variable
# and check everytime if found, then break.
##for c1 in range(10):
##    for c2 in range(10):
##        for c3 in range(10):
##            if (c1, c2, c3) == CORRECT_COMBO:
##                print('Found the combo: {}'.format((c1, c2, c3)))
##            print(c1,c2,c3)


# Here we can break out with only a single break! Prettier code
def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)

for (c1, c2, c3) in combo_gen():
    print(c1,c2,c3)
    if (c1,c2,c3) == CORRECT_COMBO:
        print('Found the combo: {}'.format((c1, c2, c3)))
        break
