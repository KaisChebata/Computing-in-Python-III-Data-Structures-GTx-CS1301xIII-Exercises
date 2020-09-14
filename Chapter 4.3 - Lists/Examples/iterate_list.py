def average(lst):
	sum_result = 0
	for item in lst:
		sum_result += item
	return sum_result / len(lst)


myList1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
myList2 = [97, 87, 91, 83, 85, 91, 95, 99, 81, 85]

print('myList1:', myList1)
print('myList2:', myList2)
print('the average of myList1:', average(myList1))
print('the average of myList2:', average(myList2))
'\n'.join