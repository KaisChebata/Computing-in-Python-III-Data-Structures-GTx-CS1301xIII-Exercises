my_int_1 = 5
my_int_2 = my_int_1
my_int_1 = 7
print('integer variables assignment behavior ....')
print('my_int_1 = 5')
print('my_int_2 = my_int_1')
print('my_int_1 = 7')
print('now checking the values of my_int_1 and my_int_2:')
print('my_int_1 =', my_int_1)
print('my_int_2 =', my_int_2)
print('here first we set the value of my_int_1 to 5, then set the value of my_int_2 to my_int_1\'s value')
print('after we change the value of my_int_1 and set it to 7, we see that my_int_2 did not change ')
print('integer variables assignment acting the same as function with pass by value ....')
print('-------------------------------------------------------------------------------------------')

print('list variables assignment behavior .....')
print('my_list_1 = ["One", "Two", "Three"]')
my_list_1 = ["One", "Two", "Three"]
print('my_list_2 = my_list_1')
my_list_2 = my_list_1
print('my_list_1.append("Foure")')
my_list_1.append('Four')
print('my_list_1:', my_list_1)
print('my_list_2:', my_list_2)
print('if we modify a variable\'s value using a method (like my_List.append("An Item")),\
 then usually it mirrors the "assignment by reference" idea.')

print('------------------------------------------------------------------')
print('tests .....')
