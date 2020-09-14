def add(numbers):
	sum = 0
	for i in range(len(numbers)):
		numbers[i] = -numbers[i]
		print('#{} iteration numbers[i] -> {}'.format(i,numbers[i]))
		sum -= numbers[i]
		print('#{} iteration sum -> {}'.format(i,sum))

	return sum, numbers

myList = [2, 4, 6, 8, 10]
print(add(myList))
print('------------------------------')
print(add(myList))
# print(add(myList))
# print(add(myList))

print('------------------------------------')

def add_v2(numbers):
	sum = 0
	for number in numbers:
		number = -number
		sum -= number
	return sum, numbers

myList_v2 = [2, 4, 6, 8, 10]
print(add_v2(myList_v2))
print(add_v2(myList_v2))

