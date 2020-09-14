# 1- make_pi problem:

# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

# make_pi() -> [3, 1, 4]

# sol 1:
def make_pi():
	pi = '3.141592653589793'
	return [int(char) for char in pi if char.isdigit()][:3]

# sol 2:
# def make_pi():
# 	pi = '3.141592653589793'
# 	array = []

# 	for i in pi:
# 		if i.isdigit() and len(array) < 3:
# 			array.append(int(i))
# 	return array

print('1- make_pi problem ......')
print(make_pi())
print('-------------------------------------------------')
# 2- common_end problem:
# Given 2 arrays of ints, a and b, 
# return True if they have the same first element or 
# they have the same last element. Both arrays will be length 1 or more.

# common_end([1, 2, 3], [7, 3]) -> True
# common_end([1, 2, 3], [7, 3, 2]) -> False
# common_end([1, 2, 3], [1, 3]) -> True
print('2- common_end problem ......')

def common_end(a, b):
	return a and b and (a[0] == b[0] or a[-1] == b[-1])

print('common_end([1, 2, 3], [7, 3]) ->', common_end([1, 2, 3], [7, 3]))
print('common_end([1, 2, 3], [7, 3, 2]) ->', common_end([1, 2, 3], [7, 3, 2]))
print('common_end([1, 2, 3], [1, 3]) ->', common_end([1, 2, 3], [1, 3]))
print('-------------------------------------------------')

# 3- sum problem:
# Given an array of ints length 3, return the sum of all the elements.

# sum3([1, 2, 3]) -> 6
# sum3([5, 11, 2]) -> 18
# sum3([7, 0, 0]) -> 7

def sum3(nums):
	return sum(nums)

print('3- sum problem ......')
print('sum3([1, 2, 3]) ->', sum3([1, 2, 3]))
print('sum3([5, 11, 2]) ->', sum3([5, 11, 2]))
print('sum3([7, 0, 0]) ->', sum3([7, 0, 0]))
print('-------------------------------------------------')

# 4- rotate_left3 problem:

# Given an array of ints length 3, 
# return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

# rotate_left3([1, 2, 3]) -> [2, 3, 1]
# rotate_left3([5, 11, 9]) -> [11, 9, 5]
# rotate_left3([7, 0, 0]) -> [0, 0, 7]

def rotate_left3(nums):
	return nums[-2:] + nums[:-2]

print('4- rotate_left3 problem ......')
print('rotate_left3([1, 2, 3]) ->', rotate_left3([1, 2, 3]))
print('rotate_left3([5, 11, 9]) ->', rotate_left3([5, 11, 9]))
print('rotate_left3([7, 0, 0]) ->', rotate_left3([7, 0, 0]))

print('-------------------------------------------------')


# 5- reverse3 problem:

# Given an array of ints length 3, 
# return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.

# reverse3([1, 2, 3]) -> [3, 2, 1]
# reverse3([5, 11, 9]) -> [9, 11, 5]
# reverse3([7, 0, 0]) -> [0, 0, 7]

def reverse3(nums):
	return nums[::-1]

print('5- reverse3 problem ......')
print('reverse3([1, 2, 3]) ->', reverse3([1, 2, 3]))
print('reverse3([5, 11, 9]) ->', reverse3([5, 11, 9]))
print('reverse3([7, 0, 0]) ->', reverse3([7, 0, 0]))

print('-------------------------------------------------')

#  6- max_end3 problem:

# Given an array of ints length 3, figure out which is larger, 
# the first or last element in the array, and set all the other elements to be that value. 
# Return the changed array.

# max_end3([1, 2, 3]) -> [3, 3, 3]
# max_end3([11, 5, 9]) -> [11, 11, 11]
# max_end3([2, 11, 3]) -> [3, 3, 3]

def max_end3(nums):
    # if nums[0] > nums[-1]:
    # 	for i in range(len(nums)):
    # 		nums[i] = nums[0]
    # for i in range(len(nums)):
    # 	nums[i] = nums[-1]
    return [nums[0] if nums[0] > nums[-1] else nums[-1] for i in range(len(nums))]

print('6- max_end3 problem ......')
print('max_end3([1, 2, 3]) ->', max_end3([1, 2, 3]))
print('max_end3([11, 5, 9]) ->', max_end3([11, 5, 9]))
print('max_end3([2, 11, 3]) ->', max_end3([2, 11, 3]))

print('-------------------------------------------------')
# 7- sum2 problem:

# Given an array of ints, return the sum of the first 2 elements in the array. 
# If the array length is less than 2, just sum up the elements that exist, 
# returning 0 if the array is length 0.

# sum2([1, 2, 3]) -> 3
# sum2([1, 1]) -> 2
# sum2([1, 1, 1, 1]) -> 2

def sum2(nums):
	return sum(nums[:2])

print('7- sum2 problem ......')
print('sum2([1, 2, 3]) ->', sum2([1, 2, 3]))
print('sum2([1, 1]) ->', sum2([1, 1]))
print('sum2([1, 1, 1, 1]) ->', sum2([1, 1, 1, 1]))
print('-------------------------------------------------')

# 8- middle_way problem:
# Given 2 int arrays, a and b, each length 3, 
# return a new array length 2 containing their middle elements.

def middle_way(a, b):
	return [a[len(a) // 2], b[len(b) // 2]]

print('8- middle_way problem ......')
print('middle_way([1, 2, 3], [4, 5, 6]) ->', middle_way([1, 2, 3], [4, 5, 6]))
print('middle_way([7, 7, 7], [3, 8, 0]) ->', middle_way([7, 7, 7], [3, 8, 0]))
print('middle_way([5, 2, 9], [1, 4, 5]) ->', middle_way([5, 2, 9], [1, 4, 5]))
print('-------------------------------------------------')

# 9- make_ends problem:

# Given an array of ints, 
# return a new array length 2 containing the first and last elements from the original array. 
# The original array will be length 1 or more.

def make_ends(nums):
	return [nums[0], nums[-1]]

print('9- make_ends problem ......')
print('make_ends([1, 2, 3]) ->', make_ends([1, 2, 3]))
print('make_ends([1, 2, 3, 4]) ->', make_ends([1, 2, 3, 4]))
print('make_ends([7, 4, 6, 2]) ->', make_ends([7, 4, 6, 2]))
print('-------------------------------------------------')


# 10- has23 problem:

# Given an int array length 2, return True if it contains a 2 or a 3.

# has23([2, 5]) -> True
# has23([4, 3]) -> True
# has23([4, 5]) -> False

def has23(nums):
	return 2 in nums or 3 in nums
print('10- has23 problem ......')
print('has23([2, 5]) ->', has23([2, 5]))
print('has23([4, 3]) ->', has23([4, 3]))
print('has23([4, 5]) ->', has23([4, 5]))
print('-------------------------------------------------')

# 11- count_evens problem:

# Return the number of even ints in the given array. 
# Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

def count_evens(nums):
	return len([i for i in nums if i % 2 == 0 ])
	# count = 0
	# for num in nums:
	# 	if num % 2 == 0:
	# 		count += 1
	# return count

print('11- count_evens problem ......')
print('count_evens([2, 1, 2, 3, 4]) ->', count_evens([2, 1, 2, 3, 4]))
print('count_evens([2, 2, 0]) ->', count_evens([2, 2, 0]))
print('count_evens([1, 3, 5]) ->', count_evens([1, 3, 5]))
print('-------------------------------------------------')

# 12- big_diff

# Given an array length 1 or more of ints, 
# return the difference between the largest and smallest values in the array. 
# Note: the built-in min(v1, v2) and max(v1, v2) functions 
# return the smaller or larger of two values.

# big_diff([10, 3, 5, 6]) -> 7
# big_diff([7, 2, 10, 9]) -> 8
# big_diff([2, 10, 7, 2]) -> 8

def big_diff(nums):
	return max(nums) - min(nums)
print('12- big_diff problem ......')
print('big_diff([10, 3, 5, 6]) ->', big_diff([10, 3, 5, 6]))
print('big_diff([7, 2, 10, 9]) ->', big_diff([7, 2, 10, 9]))
print('big_diff([2, 10, 7, 2]) ->', big_diff([2, 10, 7, 2]))
print('-------------------------------------------------')

# 13- centered_average problem:

# Return the "centered" average of an array of ints, 
# which we'll say is the mean average of the values, 
# except ignoring the largest and smallest values in the array. 
# If there are multiple copies of the smallest value, ignore just one copy, 
# and likewise for the largest value. 
# Use int division to produce the final average. 
# You may assume that the array is length 3 or more.

# centered_average([1, 2, 3, 4, 100]) -> 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) -> 5
# centered_average([-10, -4, -2, -4, -2, 0]) -> -3

def centered_average(nums):
	return (sum(nums) - max(nums) - min(nums)) // (len(nums) - 2)

print('13- centered_average problem ......')
print('centered_average([1, 2, 3, 4, 100])-> ',centered_average([1, 2, 3, 4, 100]))
print('centered_average([1, 1, 5, 5, 10, 8, 7]) ->', centered_average([1, 1, 5, 5, 10, 8, 7]))
print('centered_average([-10, -4, -2, -4, -2, 0]) ->', centered_average([-10, -4, -2, -4, -2, 0]))
print('-------------------------------------------------')

# 14- sum13 problem:

# Return the sum of the numbers in the array, 
# returning 0 for an empty array. 
# Except the number 13 is very unlucky, so it does not count 
# and numbers that come immediately after a 13 also do not count.

# sum13([1, 2, 2, 1]) -> 6
# sum13([1, 1]) -> 2
# sum13([1, 2, 2, 1, 13]) -> 6

def sum13(nums):
	total_sum = 0
	index = 0

	while index < len(nums):
		if nums[index] == 13:
			index += 2
		else:
			total_sum += nums[index]
			index += 1
	return total_sum
print('14- sum13 problem ......')
print('sum13([1, 2, 2, 1]) ->', sum13([1, 2, 2, 1]))
print('sum13([1, 1]) ->', sum13([1, 1]))
print('sum13([1, 2, 2, 1, 13]) ->', sum13([1, 2, 2, 1, 13]))
print('sum13([1, 2, 13, 2, 1, 13]) ->', sum13([1, 2, 13, 2, 1, 13]))
print('-------------------------------------------------')


# 15- sum67 problem:

# Return the sum of the numbers in the array, 
# except ignore sections of numbers starting with a 6 and extending to the next 7 
# (every 6 will be followed by at least one 7). Return 0 for no numbers.

# sum67([1, 2, 2]) -> 5
# sum67([1, 2, 2, 6, 99, 99, 7]) -> 5
# sum67([1, 1, 6, 7, 2]) -> 4
# sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]) -> 2
# sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]) -> 2
# sum67([2, 7, 6, 2, 6, 7, 2, 7]) -> 18

def sum67(nums):
	total_sum = 0
	skip_flag = False

	for number in nums:
		if number == 6:
			skip_flag = True
			continue
		if number == 7 and skip_flag == True:
			skip_flag = False
			continue
		if skip_flag == False:
			total_sum += number
	return total_sum

print('15- sum67 problem ......')
print('sum67([1, 2, 2]) ->', sum67([1, 2, 2]))
print('sum67([1, 2, 2, 6, 99, 99, 7]) ->', sum67([1, 2, 2, 6, 99, 99, 7]))
print('sum67([1, 1, 6, 7, 2]) ->', sum67([1, 1, 6, 7, 2]))
print('sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]) ->', sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]))
print('sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]) ->', sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]))
print('sum67([2, 7, 6, 2, 6, 7, 2, 7]) ->',sum67([2, 7, 6, 2, 6, 7, 2, 7]))
print('sum67([2, 7, 6, 2, 6, 2, 7]) ->', sum67([2, 7, 6, 2, 6, 2, 7]))
print('-------------------------------------------------')

#16- has22

# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

# has22([1, 2, 2]) → True
# has22([1, 2, 1, 2]) → False
# has22([2, 1, 2]) → False

def has22(nums):
	s = [str(i) for i in nums]
	return '22' in ''.join(s)

print('has22([1, 2, 2]) ->', has22([1, 2, 2]))
print('has22([1, 2, 1, 2]) ->', has22([1, 2, 1, 2]))
print('has22([2, 1, 2]) ->', has22([2, 1, 2]))