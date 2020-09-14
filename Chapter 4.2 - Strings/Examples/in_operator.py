mystring = 'ABCDE'

print('mystring ->', mystring)

if 'BC' in mystring:
	print('BC was found!')

else:
	print('BC was not found')

if 'GH' in mystring:
	print('GH was found!')
else:
	print('GH was not found!')

def check_in_string(check_string, search_string):
	if search_string in check_string:
		print(search_string + ' was found!')
	else:
		print(search_string + ' was not found!')

def check_not_in_string(check_string, search_string):
	if search_string not in check_string:
		print(search_string + ' was not found!')
	else:
		print(search_string + ' was found!')

print('check_in_string(mysting, "AB") ->')
check_in_string(mystring, 'AB')
check_in_string(mystring, 'BC')
check_in_string(mystring, 'GH')

print('check_not_in_string("AB", mystring) ->')
check_not_in_string(mystring, 'AB')
check_not_in_string(mystring, 'DD')

print('------------------------------------------------')
test_String = "I like shorts!"
print('' in test_String)
print(test_String in "I like shorts! They're comfy and easy to wear!")