# Add item to a list

def add_item(a_list):
	a_list.append('New Item')
	print('a_list:', a_list)

print('passing by reference .....')
my_list = ['One', 'Two', 'Trhee']
print('my_list before add_item:', my_list)
print('calling add_item(my_list) .....')
add_item(my_list)
print('my_list after add_item:', my_list)

print('--------------------------------------------------------------')

print('example of dealing with string to clear the concept of pass by value on strings')
print('my_string = "kais"')
my_string = 'kais'
print('my_string after upper with print function print(my_string.upper()):', my_string.upper())
print('my_string after printing :', my_string)
print('to make changes to the variable "my_string" we would do the following .....')
print('my_string = "kais"')
print('my_string = my_string.upper()')
my_string = my_string.upper()
print('my_string after assigning the upper method result to the var itself ....', my_string)