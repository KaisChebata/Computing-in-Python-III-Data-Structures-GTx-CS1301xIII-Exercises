#Write a function called fancy_find. fancy_find should have
#two parameters: search_within and search_for.
#
#fancy_find should check if search_for is found within the
#string search_within. If it is, it should print the message
#"[search_for] found at index [index]!", with [search_for]
#and [index] replaced by the value of search_for and the
#index at which it is found. If search_for is not found
#within search_within, it should print, "[search_for] was
#not found within [search_within]!", again with the values
#of search_for and search_within.
#
#For example:
#
#  fancy_find("ABCDEF", "DEF") -> "DEF found at index 3!"
#  fancy_find("ABCDEF", "GHI") -> "GHI was not found within ABCDEF!"


#Add your function here!

def fancy_find(search_within, search_for):
	# my solution:

	# if search_for in search_within:
	# 	index = search_within.find(search_for)
	# 	return search_for + ' found at index ' + str(index) + '!'
	# else:
	# 	return search_for + ' was not found within ' + search_within + '!'

	# course solution:

	index = search_within.find(search_for)

	if index >= 0:
		return search_for + " found at index " + str(index) + "!"
	else:
		return search_for + " was not found within " + search_within + "!"

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#DEF found at index 3!
#GHI was not found within ABCDEF!

print(fancy_find("ABCDEF", "DEF"))
print(fancy_find("ABCDEF", "GHI"))
