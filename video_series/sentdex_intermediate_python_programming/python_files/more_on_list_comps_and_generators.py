#! usr/bin/python3

input_list = [5,6,2,10,15,20,5,2,1,3]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

##xyz = (i for i in input_list if div_by_five(i))

##for i in xyz:
##    print(i)
##print(xyz)

##xyz = [i for i in input_list if div_by_five(i)]
##print(xyz)

# You can do for loops within for loops on one line
##[[print(i,ii) for ii in range(5)] for i in range(5)]
# is equivalent to

##for i in range(5):
##    for ii in range(5):
##        print(i, ii)


xyz = ([[i,ii] for ii in range(5)] for i in range(5))
print(xyz)
print([i for i in xyz])

for i in xyz:
    for ii in i:
        print(ii)

# The saying goes, "With big list comprehension you will run out of
# memory and with big generators you will run out of time."

