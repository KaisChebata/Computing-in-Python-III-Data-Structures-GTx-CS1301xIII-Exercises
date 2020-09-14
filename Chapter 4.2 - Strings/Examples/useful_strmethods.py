mystring = 'this is MY test string!   '
print('mystring ->', mystring)
print('mystring.capitalize() ->', mystring.capitalize())
print('mystring.lower() ->', mystring.lower())
print('mystring.upper() ->', mystring.upper())
print('mystring.title() ->', mystring.title())
print('mystring.strip() ->', mystring.strip())
print('mystring.replace("MY", "YOUR") ->', mystring.replace('MY', 'YOUR'))
print('mylist = mystring.split() ....')
mylist = mystring.split()
print('mylist ->', mylist)
print('"-".join(mylist) ->', '-'.join(mylist))
print('mystring ->', mystring)

print('--------------------------------------------------------')
mystring_to_split = 'My-string-to-split'
print(mystring_to_split)
my_slipt_string = mystring_to_split.split('-')
print(my_slipt_string)
my_joind_string = '-'.join(my_slipt_string)
print(my_joind_string)

myString = "CS1301"
myString = myString.replace("CS", "computer science")
myString = myString.replace("1301", "101")
myString = myString.replace("e1", "e 1")
myString = myString.title()
print(myString == 'Computer Science 101')

print('-----------------------------------------------------------------')
def xyz_there(str):
	for index in range(len(str)):
		if str[index] != '.' and str[index + 1: index + 4] == 'xyz':
			return True
	if str[:3] == 'xyz':
		return True
	return False
	
str_test = 'abc.xyz' 
print(str_test.find('.'), '--', str_test.find('xyz'), str_test.find('.') < str_test.find('xyz'))
print(xyz_there('abc.xyz'))
print(xyz_there('abc.xxyz'), 'must be True')

print(range(len('abc.xxyz')))