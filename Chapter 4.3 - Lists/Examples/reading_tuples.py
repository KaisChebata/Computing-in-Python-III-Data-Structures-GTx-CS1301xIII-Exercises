mystring = 'Hello World!'
myfloat = 49.98
myinteger = 33
mycharacter = 'K'
myinteger2 = -1
mytuple = (mystring, myinteger, myfloat, mycharacter, myinteger2)

print('mytuple[0] ->', mytuple[0])
print('mytuple[1] ->',mytuple[1])
print('mytuple[2] ->', mytuple[2])
print('mytuple[3] ->', mytuple[3])

print('mytuple ->', mytuple)
print('-------------------------------------')
print('mytuple[3:] ->', mytuple[3:])
print('mytuple[2:] ->', mytuple[:2])
print('mytuple[1:3] ->', mytuple[1:3])
print('mytuple[-3:] ->', mytuple[-3:])
print('mytuple[:-3] ->', mytuple[:-3])
print('-----------------------------------------')
print('unpacking element from a tuple ....')
print('(my_new_string, my_new_integer, my_new_float, my_new_char, my_new_integer2) = mytuple')
(my_new_string, my_new_integer, my_new_float, my_new_char, my_new_integer2) = mytuple
print('my_new_string:', my_new_string)
print('my_new_integer:', my_new_integer)
print('my_new_float:', my_new_float)
print('my_new_char:', my_new_char)
print('my_new_integer2:', my_new_integer2)