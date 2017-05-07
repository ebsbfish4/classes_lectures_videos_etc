# The first of these will not give you as much informaiton as the 
# full traceback in the secnond, stuff like that line etc.

'''
try:
	a+b
except Exception as e:
	print(str(e))

a + b
'''

# It is unwise to save errors to variables, because if you have an exception
# in the exception it would create a loop. So just slice the tuple like this
import sys
import logging

def error_handling():
	print('{}. {}, line: {}'.format(sys.exc_info()[0],
										sys.exc_info()[1],
										sys.exc_info()[2].tb_lineno))

try:
	a + b
except Exception as e:
	logging.error(error_handling())
