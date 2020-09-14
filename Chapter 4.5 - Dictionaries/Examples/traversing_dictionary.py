mydictionary = {"sprockets" : 5, "widgets" : 11, "cogs" : 3, "gizmos" : 15,
                "gadgets" : 1}
print('search for any value less than 5, and order more from it')
for value in mydictionary.values():
    if value < 5:
        print('a value is less than 5, was found: {}'.format(value))

print('-----------------------------------------------------------')
print('search for any key that is value is less than 5, and order more from it')

for key in mydictionary.keys():
    if mydictionary[key] < 5:
        print(f'{key} is less than 5: {mydictionary[key]}')
print('-----------------------------------------------------------')
print('search for any (key,value) pair that is value is less than 5, and order more from it')

for key, value in mydictionary.items():
    if value < 5:
        print('{} is less than 5: {}'.format(key, value))

print('-----------------------------------------------------------')
