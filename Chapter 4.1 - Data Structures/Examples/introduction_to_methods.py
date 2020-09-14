# Methods in practice

my_numeric_string = '12345'
my_non_numeric_string = 'ABCDE'

# print true if my_numeric_string is digital
print('my_numeric_string.isdigit() print true if my_numeric_string is digital')
print('my_numeric_string.isdigit():', my_numeric_string.isdigit())

print('my_non_numeric_string.isdigit() print true if my_non_numeric_string is digital')
print('my_non_numeric_string.isdigit():', my_non_numeric_string.isdigit())

print('--------------------------------------------------------------')
print('writing equivalent syntax for isdigit method of string')

import string

def isdigit(in_string):
	for char in in_string:
		if not char in string.digits:
			return False
	return True

my_string = '52672'
print('check wether my_string is a digit string or not using our function "isdigit(in_string)" .....')
print('isdigit({}): {}'.format(my_string, isdigit(my_string)))
print('check wether my_string is a digit string or not using built-in string method\
 my_string.isdigit() .....')
print('{}.isdigit(): {}'.format(my_string, my_string.isdigit()))
