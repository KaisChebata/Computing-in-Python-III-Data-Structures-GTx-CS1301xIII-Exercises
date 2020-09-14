#Write a function called "load_file" that accepts one 
#parameter: a filename. The function should open the
#file and return the contents.#
#
# - If the contents of the file can be interpreted as
#   an integer, return the contents as an integer.
# - Otherwise, if the contents of the file can be
#   interpreted as a float, return the contents as a
#   float.
# - Otherwise, return the contents of the file as a
#   string.
#
#You may assume that the file has only one line.
#
#Hints:
#
# - Don't forget to close the file when you're done!
# - Remember, anything you read from a file is
#   initially interpreted as a string.

"""
test cases:
! $urWXG)eC`/8.E
-83.871326
-4206
n.ZFrX9Lm9YWoApVfzI
8625
27.2607556
138
16.9827538
8o X'V0ah!s B
-61.03936
n.ZFrX9Lm9YWoApVfzI
"""
#Write your function here!

def load_file(file_name):
	# sloution 1:
	# file_reader = open(file_name, 'r')
	# content = file_reader.read().strip()

	# for converter in (int, float, str):
	# 	try:
	# 		return converter(content)
	# 	except Exception as e:
	# 		pass
	# 	finally:
	# 		file_reader.close()

	# course solution #1:
	file_reader = open(file_name, 'r')

	content = file_reader.readline()

	try:
		#Now, we want to try to convert it to an integer.
        #If contents can be read as an integer, this line
        #will work, and the function is over*. If this
        #line doesn't work, an error will arise.
		return int(content)

	except Exception as e:

        #If we reach this point, an error arose. So, the
        #contents can't be read as an integer. Now let's
        #try to read them as a float:

		try:
			#If this line works, then contents was a float
            #and the function is over*. If not, it will
            #generate an error.

			return float(content)

		except Exception as e:
			#If we reach here, then we encountered an
            #error converting contents to both an int and
            #a float. So, there's nothing left to do but
            #just return the original contents of the file
            #as a string, then the function is over*.

			return content
			#See those asterisks where I wrote 'over'? That's
    		#because this is a great demonstration of when we might
    		#use a finally block. The contents of a finally block
    		#after a try-except block will always run no matter what
    		#happened inside the try-except blocks. So, since we
    		#always need to close the file, we can do that in a
    		#finally block:
	finally:
		file_reader.close()

	


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 123, followed by <class 'int'>.
# contents = load_file("LoadFromFileInput.txt")
# print(contents)
# print(type(contents))
cntent = load_file(r'Chapter 4.4 - File Input and Output\WriteFileOutput.txt')
print(cntent)
print(type(cntent))



