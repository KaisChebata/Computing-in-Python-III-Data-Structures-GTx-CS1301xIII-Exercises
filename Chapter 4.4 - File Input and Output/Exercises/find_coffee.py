#Write a function called "find_coffee" that expects a 
#filename as a parameter. The function should open the 
#given file and return True if the file contains the word 
#"coffee". Otherwise, the function should return False.
#
#Hint: look up the read() method if you want to do this
#more simply than you might do with readline().


#Write your function here!
txt = 'The function should open the given file and return True if the file contains the word \
"coffee"'

def find_coffee(file_name):
	# solution 1:

	# file_reader = open(file_name, 'r')
	# for item in file_reader.readlines():
	# 	if 'coffee' in item:
	# 		return True
	# file_reader.close()
	# return False

	# solution 2:
	file_reader = open(file_name, 'r')
	contents = file_reader.read()
	return 'coffee' in contents

#You can test your function with the provided files named 
#"coffeeful.txt" and "coffeeless.txt". With their original
#text, the lines below should print True, then False. You
#may also edit the files by selecting them in the drop
#down in the top left to try your code with different
#input.
# print(find_coffee("coffeeful.txt"))
# print(find_coffee("coffeeless.txt"))
print(find_coffee(r"Chapter 4.4 - File Input and Output\test.txt"))
