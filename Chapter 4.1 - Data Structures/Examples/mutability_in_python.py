# add one to an integer

def add_one(an_integer):
	an_integer += 1
	print('an_integer:', an_integer)

print('immutable data types: Functions vs local assignments ......')
#create my_integer with value of 5 
my_integer = 5
print('my_integer before add_one:', my_integer)

#call add_one on my_integer
add_one(my_integer)

print('my_integer after add_one:', my_integer)

my_integer += 1
print('my_integer after increment:', my_integer)

print('-----------------------------------------------------------')

print('printing Memory address')

#creating my_int_1 with value of 5

my_int_1 = 5
# print the spot in memory which my_int_1 is pointing ....
print('my_int_1 =', my_int_1)
print('print the spot in memory which my_int_1 is pointing')
print('my_int_1\'s id:', id(my_int_1))

# changing the value of my_int_1 to 6 by creating another piece of memory for that
my_int_1 = 6
# print the spot in memory which my_int_1 is pointing ....
print('my_int_1 =', my_int_1)
print('print the spot in memory which my_int_1 is pointing')
print('my_int_1\'s id:', id(my_int_1))

print('--------------------------------------------------------')
print('dealing with mutable data types ........')

# creat a list 'my_list' 
my_list = ['One', 'Two', 'Three']
print('my_list:', my_list)
# print the spot in memory which my_list is pointing ....
print('print the spot in memory which my_list is pointing')
print('my_list\'s id:', id(my_list))

print('add an element to my_list my_list.append("Four")')
my_list.append('Four')
print('print the spot in memory which my_list is  pointing after adding a new element')
print('my_list\'s id:', id(my_list))

print('---------------------------------------------------------')
print('creating my_list = ["One", "Two", "Three"]')
my_list = ['One', 'Two', 'Three']

print('with an new assignment to my_list with a new value,\
 that will creat a new place in memory for my_list')
print('print the spot in memory which my_list is  pointing after adding a new element')
print('my_list\'s id:', id(my_list))
print('adding a new item to my_list ... my_list.append("Four")')
my_list.append('Four')
print('my_list\'s id after modfying the list in place is:', id(my_list))

print('set my_list variable to a new list: ')
print('my_list = ["Five", "Sex", "Seven"]')
my_list = ["Five", "Sex", "Seven"]
print('print the spot in memory which my_list is pointing after the new setting')
print('my_list\'s id after new setting to new values is:', id(my_list))

print('------------------------------------------------------------------------')
print('Testing if variables or object are sharing the same data in memory')
print('my_int_1 = 5, my_int_2 = 5')
my_int_1, my_int_2 = 5, 5
print('Testing (print True) if my_int_1 and my_int_2 pointing to the same spot in memory')
print('id(my_int_1) == id(my_int_2):', id(my_int_1) == id(my_int_2))

print('------------------------------------------------------------------------')
print('Testing mutable variables or object if they\'re sharing same spot memory')
my_list_1 = ['One', 'Two', 'Three']
my_list_2 = ['One', 'Two', 'Three']
print('id(my_list_1) == id(my_list_2):', id(my_list_1) == id(my_list_2))
print('the id(s) of my_list_1 and my_list_2 in memory are different because python create a new\
 spot of memory for variables when we set or make an assignment to them to values of mutable data types\
 even if the values on right hand side are the same, python well create a new place in memory, \
 but if the values on the right hand side were immutable then python will go \
 and check if that value is already exists somewhere in memory and if it is, point the new variable name\
 at the existing value')
print('add new item to the my_list_2 "my_list_2.append("Four")')
my_list_2.append('Four')
print('my_list_1:', my_list_1)
print('my_list_2:', my_list_2)
