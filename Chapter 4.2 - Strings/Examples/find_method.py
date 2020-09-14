mystring = 'ABCDE'
print('mystring.find("CDE") ->', mystring.find('CDE'))
print('mystring.find("CDE") ->', mystring.find('ACE'))

def check_in_string(check_string, search_string):
	if check_string.find(search_string) >= 0:
		print(search_string + ' was found!')
	else:
		print(search_string + ' was not found!')

print("check_in_string(mystring, 'BC') -> ")
check_in_string(mystring, 'BC')
print("check_in_string(mystring, 'GH') -> ")
check_in_string(mystring, 'GH')

mystring2 = 'ABCDEABCDEABCDE'
print('mystring2 ->', mystring2)
print('mystring2.find("CDE") ->', mystring2.find('CDE'))
print('mystring2.find("cde") ->', mystring2.find('cde'))

print('mystring2.find("CDE") ->', mystring2.find('CDE'))
print('mystring2.find("CDE", 5) ->', mystring2.find('CDE', 5))
print('mystring2.find("CDE", 13) ->', mystring2.find('CDE', 13))
print('mystring2.find("CDE", 4, 10) ->', mystring2.find('CDE', 4, 10))
print('mystring2.find("CDE", 3, 6) ->', mystring2.find('CDE', 3, 6))


mystring3 = 'ABCDEABCDEABCDEFGHIJFGHIJABCDEABCDEFGHIJ'
find_string = 'CDE'

current_location = mystring3.find(find_string)

while current_location >= 0:
	print(find_string, 'found at', current_location)
	current_location = mystring3.find(find_string, current_location + 1)

print('Count of', find_string, ':', mystring3.count(find_string))

str_test = 'ABCDEABCDEABCDE'

print(str_test.find('CDE', 3, 6))