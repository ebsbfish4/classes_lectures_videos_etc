#! python3

# While loop and for loop are completely interchangeable. He prefers the for loop
# because sometimes you can condense the code more easily.

example_list = [1,5,6,1,6,7,8,9,345,53,5]

# for each_number creates a new variable in memory
for each_number in example_list:
    print(each_number)

# if this line is indented then you will see the string for each number printed
# currently it will print after the entire list has been printed
print('continue program')


'''
A difference between range in python 3 and 2.7 is that if you called something
like range(1,100000000000000)in python 2.7 then it will generate a list with all
those numbers, which could very easily max out your RAM and crash your program.
Python 3 will go through the range of numbers without doing that.
'''
# This will print 1-10. Range is a python function that does not need to be imported
for x in range(1,11):
    print (x)
