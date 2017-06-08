# functions as objects, function annotations, lambda anonymous functions, 
# map, filter, reduce and a bunch of problems.

def mult_by_2(num):
	return num * 2

times_two = mult_by_2

print("4 * 2 =", times_two(4))

def do_math(func, num):
	return func(num)

print("8*2=", do_math(times_two, 8))

def get_func_mult_by_num(num):

	def mult_by(value):
		return num * value

	return mult_by

generated_func = get_func_mult_by_num(5)

print("5*10=", generated_func(10))

listOfFuncs = [times_two, generated_func]
print("5*9=", listOfFuncs[1](9))


'''
Practice Problem 1
'''

def is_odd(num):
	return (num%2==1)

def change_list(input, func):
	oddList = []
	for i in input:
		if func(i):
			oddList.append(i)
	return oddList

print(change_list([1,2,3,4,5,6,7],is_odd))

def random_func(name: str, age: int, weight: float) -> str:
	print("Name :", name)
	print("Age :", age)
	print("Weight :", weight)
	return "{} is {} years old and weighs {}".format(name, age, weight)

print(random_func("Derek", 41, 165.5))

# lambda is very similar to def, it instead just returns instead of assigning to a variable
#lambda arg1, arg2, .... : expression

sum = lambda x,y: x + y

# lambdas are used when you need a small function but you do not want to junk up your
# code with a whole bunch of functinon names

print("Sum :", sum(4,5)) 

can_vote = lambda age: True if age >= 18 else False

print("Can Vote:", can_vote(19))

powerList = [lambda x: x**2,
			lambda x: x**3,
			lambda x: x**4]

for func in powerList:
	print(func(4))

# You can also store lambdas inside of dictionaries

attack = {'quick': (lambda: print("Quick Attack")),
'power': (lambda: print("Power Attack")),
'miss': (lambda: print("Miss Attack"))			
}

attack['quick']()

import random

attackKey = random.choice(list(attack.keys()))

attack[attackKey]()

'''
Practice Problem 2
'''

def head_tails_100():
	results = []
	for i in range(100):
		results.append(random.choice(['H','T']))
	H = results.count('H')
	T = 100 - H
	return 'Heads : {}\nTails : {}'.format(H,T)

print(head_tails_100())

# map allows us to execute a function on each item in a list

oneto10 = range(1,11)

def dbl_num(num):
	return 2*num

print(list(map(dbl_num, oneto10)))

# You can also use lambda

print(list(map(lambda x: x*3, oneto10)))


aList = list(map(lambda x, y: x + y, [1,2,3], [4,5,6]))
print(aList)

# Filter selects items from a list based off of a function

print(list(filter(lambda x: x%2==0, range(1,100))))

'''
Practice Problem 3
'''

def random_9_mults():
	original_list = []
	for i in range(100):
		original_list.append(random.randrange(1,1001))
	div_by_nine_list = list(filter(lambda x: x%9 == 0, original_list))
	return div_by_nine_list

print(random_9_mults())

from functools import reduce

print(reduce((lambda x, y: x + y), range(1,6)))