#!usr/bin/python3

# Timeit measures how long it takes for a certain snippet of code to run.
# So why would you want to use that over doing something like:

##start = time.time()
##total = time.time()- start

# Problem is, especially with smaller snippets of code, that operation is
# not as percise. If there is something else running it could impact the runtime.
# The timeit module will run the code many times (you specify) to give you a more
# accurate estimation of the time taken.

import timeit

##print(timeit.timeit('1+3', number=50000000))

##input_list = range(100)
##
##def div_by_five(num):
##    if num % 5 == 0:
##        return True
##    else:
##        return False
##
### Generator
##xyz = (i for i in input_list if div_by_five(i))
### List
##xyz = [i for i in input_list if div_by_five(i)]
        
##print(timeit.timeit('''
##input_list = range(100)
##
##def div_by_five(num):
##    if num % 5 == 0:
##        return True
##    else:
##        return False
##
### Generator
##xyz = (i for i in input_list if div_by_five(i))
##''', number = 5000))

##print(timeit.timeit('''
##input_list = range(100)
##
##def div_by_five(num):
##    if num % 5 == 0:
##        return True
##    else:
##        return False
##
### Generator
##xyz = [i for i in input_list if div_by_five(i)]
##''', number = 5000))

##print(timeit.timeit('''
##input_list = range(100)
##
##def div_by_five(num):
##    if num % 5 == 0:
##        return True
##    else:
##        return False
##
### Generator
##xyz = list((i for i in input_list if div_by_five(i)))
##''', number = 5000))

##print(timeit.timeit('1+3', number=50000000))

print(timeit.timeit('''
input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

# Generator
xyz = (i for i in input_list if div_by_five(i))
for i in xyz:
    x=i
''', number = 50000))
