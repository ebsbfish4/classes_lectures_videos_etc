#! python3

# Absolute value of any number = distance from 0

print(abs(-5) == 5)

# Help function possibly most underutilized

'''
How you can get info on time module. you can also type
help() from the terminal to get access to others.

import time
help(time)
'''

# Max and min

exList = [5,2,6,7,9,4]
print(max(exList) == 9)
print(min(exList) == 2)

print(round(5.666) == 6)

# Convert data types

intMe = '55'
intMe = int(intMe)
print(type(intMe) is int)

int2 = '55'
int2 = float(int2)
print(type(int2) is float)

strr = 77
strr = str(77)
print(type(strr) is str)
