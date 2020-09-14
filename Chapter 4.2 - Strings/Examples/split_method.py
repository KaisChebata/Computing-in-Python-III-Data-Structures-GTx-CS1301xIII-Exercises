mystring = 'This is my text. It has thirteen ' \
			'words. It also has three sentences.'

print('mystring ->', mystring)
print('spliting mystring based on spaces - mystring.split():')
print(mystring.split())
# print(len(mystring.split()))
print('spliting mystring based on "." - mystring.split("."):')
print(mystring.split('.'))
print('spliting mystring based on ". " - mystring.split(". "):')
print(mystring.split('. '))

names = input('Enter list of names separated by commas: ')
names_list = names.split(',')
print(names_list)