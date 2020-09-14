#Write a function called sum_lists. sum_lists should take
#one parameter, which will be a list of lists of integers.
#sum_lists should return the sum of adding every number from
#every list.
#
#For example:
#
# list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# sum_list(list_of_lists) -> 67


#Add your code here!

def sum_lists(lst_of_lst):
	# return sum(sum(x) for x in lst)
	sum_result = 0
	for a_list in lst_of_lst:
		for item in a_list:
			sum_result += item
	return sum_result
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 78
list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(sum_lists(list_of_lists))
# print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))


