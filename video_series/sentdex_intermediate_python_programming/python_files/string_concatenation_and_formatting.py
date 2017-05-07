#! usr/bin/python3
import time
import numpy as np
# random note, put spaces arounf equal sign except for function parameters
names = ['Jeff', 'Gary', 'Jill', 'Samantha']

# Depending on who you talk to, either could be correct or incorrect way
# of doing it. first one is more readable, second has slight performance edge.
######
##method1 = []
##method2 = []
##
##for i in range(0,10):
##    for name in names:
##        start = time.time()
##        print('Hello there, '+name)
##        finish = time.time()
##        method1.append(finish-start)
##    i += 1
##
##for i in range(0,10):
##    for name in names:
##        start = time.time()
##        print(' '.join(['Hello there', name]))
##        finish = time.time()
##        method2.append(finish-start)
##    i += 1
##
##
## 
##avg1 = sum(method1)/len(method1)
##avg2 = sum(method2)/len(method2)
##
##print(avg1)
##print(avg2)
######
# If you are concatenating more than two strings, you should probably use
# join because it will scale better (it uses less processing)
##print(', '.join(names))
######

##import os
##
##location_of_files = '/home/drew/sentdex_python3_basics/python_files'
##file_name = 'appending_files.py'

# It could be tempting to just solve this problem like this, but this is not
# the best way to do it.
##print(location_of_files + '/' + file_name)

##with open(os.path.join(location_of_files,file_name)) as f:
##    print(f.read())

######

who = 'Gary'
how_many = 12

# We want to say Gary bought 12 apples today!
## tempting to do something like this
# Better way is

print('{} bought {} apples today!'.format(who, how_many))

# Much more scalable!


