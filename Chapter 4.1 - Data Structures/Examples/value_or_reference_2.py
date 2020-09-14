# add an exclamation mark to a_string

def add_exc(a_string):
	a_string += '!'
	print('a_string:', a_string)

my_string = 'Hello, World'
print('my_string befor add_exc:', my_string)
add_exc(my_string)
print('my_string after add_exc:', my_string)