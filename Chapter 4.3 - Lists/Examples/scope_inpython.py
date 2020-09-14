grades = [100, 95, 93, 91, 90, 89, 87, 87, 85, 85, 84, 82]

sum_result = 0
count = 0

for grade in grades:
	sum_result += grade
	count += 1

print('grades:', grades)
print('average of grades:', sum_result / count)