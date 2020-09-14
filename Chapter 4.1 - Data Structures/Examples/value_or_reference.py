# Introduce the main concept
#add one to an_integer

def add_one(an_integer):
	an_integer = an_integer + 1
	print("an_integer:", an_integer)

my_integer = 5
print('my_integer before add_one:', my_integer)
# call add_one on my_integer
add_one(my_integer)
print('my_integer after add_one:', my_integer)

print('---------------------------------------------')
print('Exercise 1')
# Exercise 1:

def square_integer(incoming_integer):
	# incoming_integer = incoming_integer ** 2
	incoming_integer **=2
	return incoming_integer

incoming_integer = 5
print('before calling square_integer, incoming_integer =', incoming_integer)
print('calling square_integer .....')
square_integer(incoming_integer)
print('after calling square_integer, incoming_integer =', incoming_integer)
print('------------------------------------------------------------')
print('at the begining my_integer = 5')
my_integer = 5
print('calling square_integer(my_integer) .......')
print('assign the return value from square_integer function to variable my_integer .......')
print('my_integer = square_integer(my_integer) .....')
my_integer = square_integer(my_integer)
print('my_integer = {} after calling square_integer function and assigning the result ....'.format(my_integer))

