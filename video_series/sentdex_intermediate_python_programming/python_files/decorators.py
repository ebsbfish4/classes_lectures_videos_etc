# There are certain things that you can use decorators with
# that wrap a function with certain code

from functools import wraps

def add_wrapping_with_style(style):
	def add_wraping(item):
		@wraps(item)
		def wrapped_item():
			return 'a wrapped up box of {}'.format(str(item()))
		return wrapped_item
	return add_wraping



def new_gpu():
	return 'a new Tesla P100 GPU'

@add_wrapping_with_style('beautifully')
def new_bicycle():
	return 'a new bicycle'

print(new_gpu())
print(new_bicycle())