# args and kwargs help make your program more dynamic
# kwargs are keyword arguments and args are just arguments

blog_1 = 'I am so awesome.'
blog_2 = 'Cars are cool.'
blog_3 = 'Aww look at my cat!!!'

site_title = 'My Blog'


def blog_post(title, *args):
	print(title)
	for post in args:
		print(post)

# args lets you throw in an unlimited number of arguments

blog_post(site_title, blog_1,blog_2,blog_3)

# You can pass a regular arg to the funciton as well

def blog_post_2(title, **kwargs):
	print(title)
	for p_title, post in kwargs.items():
		print(p_title, post)

blog_post_2(site_title, blog_4 = 'I am so awesome.',
blog_5 = 'Cars are cool.',
blog_6 = 'Aww look at my cat!!!')

# You can have args and kwars

def blog_post_3(title, *args, **kwargs):
	print(title)
	for arg in args:
		print(arg)
	for p_title, post in kwargs.items():
		print(p_title, post)

blog_post_3(site_title, 1, 2, 3, blog_4 = 'I am so awesome.',
blog_5 = 'Cars are cool.',
blog_6 = 'Aww look at my cat!!!')

#

import matplotlib.pyplot as plt

def graph_operation(x, y):
	print('funciton that graphs {} and {}'.format(x, y))
	plt.plot(x, y)
	plt.show()

x1 = [1, 2, 3]
y1 = [2, 3, 1]

graph_operation(x1, y1)

#equivalently

graph_me = [x1,y1]
graph_operation(*graph_me)