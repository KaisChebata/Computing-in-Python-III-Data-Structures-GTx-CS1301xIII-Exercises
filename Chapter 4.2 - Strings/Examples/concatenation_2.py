my_string_1 = '12345\n'
my_string_2 = '67890'

print(my_string_1)
print(my_string_2)
print('In-Line Concatenation: ' + my_string_1 + my_string_2)

# Exercise 1:

test = 'Hello!'
test = '!' + test
print(test)
test = '?' + test + '?'
print(test)

# Exercise 2:
print('Exercise 2')

print('-----------------------------------------------------')
for i in range(1, 6):
	print_message = "Loop iteration #" + str(i) + " beginning now"
	print(print_message)

print('-----------------------------------------------------')
for i in range(1, 6):
	print_message = ' beginning now'
	print_message = str(i) + print_message
	print_message = "Loop iteration #" + print_message
	print(print_message)