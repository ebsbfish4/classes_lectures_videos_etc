#! python3

import statistics

example_list = [4,6,2,3,8,6,5,2,1,8,9,3,4,7,3,99]
x = statistics.mean(example_list)
y = statistics.median(example_list)
z = statistics.stdev(example_list)
a = statistics.variance(example_list)
print(x,y,z)
