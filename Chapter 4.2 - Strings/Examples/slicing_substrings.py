my_string = 'ABCDE'
my_substring = ''

for char in my_string:
	my_substring += char
print(my_substring)

my_substring = ''

for index in range(0, 3):
	my_substring += my_string[index]
print('first three characters:', my_substring)

print('Slicing string with slice operator ":"')

start = 0
end = 3

print("my_string[start:end] = my_string[0:3] will return first three characters")
print("my_string[start:end]:", my_string[start:end])
print('------------------------------------------------------------')
print('my_string[0:3] ->', my_string[0:3])
print('my_string[1:4] ->', my_string[1:4])
print('------------------------------------------------------------')
print('my_string[:3] ->', my_string[:3])
print('my_string[3:] ->', my_string[3:])
print('my_string[3:10] ->', my_string[3:10])
print('------------------------------------------------------------')
test_str = "Hello, world!"
print('test_str:', test_str)
print('test_str[1:9] ->', test_str[1:9])
print('test_str[1:9:2] -> {} - comparing to my sol: el,w -> {}'
	.format(test_str[1:9:2], test_str[1:9:2] == 'el,w'))
print('test_str[::3] -> {} - comparing to my sol: Hl r! -> {}'
	.format(test_str[::3], test_str[::3] == 'Hl r!'))
