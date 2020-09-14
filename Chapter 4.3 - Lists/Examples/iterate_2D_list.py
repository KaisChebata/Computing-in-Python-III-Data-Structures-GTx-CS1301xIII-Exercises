my2d_list = [[91, 95, 89, 92, 85],
			 [85, 87, 91, 81, 82],
			 [79, 75, 85, 83, 89],
			 [81, 89, 91, 91, 90],
			 [99, 91, 95, 89, 90]]

def two_dimension_average(two_d_list):
	result = []

	for student in two_d_list:
		summ = 0
		for grade in student:
			summ += grade
		result.append(summ /len(student))
	return result
print(two_dimension_average(my2d_list))
