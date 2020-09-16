#Write a function called find_range. find_range should take
#as input a string representing a filename. The file
#corresponding to that filename will be a list of integers,
#one integer per line. find_range should return a tuple
#containing the smallest and largest numbers in the file
#(the smallest first, then the largest).
#
#For example, in the dropdown in the top left you'll find a
#file named FindRangeInput.txt. The smallest number in that
#file is 2, and the largest is 37. So, if you called
#find_range("FindRangeInput.txt"), the function would return
#(2, 37), a tuple with two integers.
#
#You may assume that all lines in the file will contain a
#positive integer (greater than 0). There may be duplicates.
#
#Hint: Remember, if you loop through all the lines in a file
#then you have to close and reopen the file to read it again,
#or by use file.seek(0) to start from the top. However, you
#can do this problem without having to read the file twice.


#Write your function here!

def find_range(file_name):
    range_reader = open(file_name, 'r')
    lst = [int(num.strip()) for num in range_reader.readlines()]
    range_reader.close()
    return (min(lst), max(lst)) 
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: (2, 37)
print(find_range(r"Extra Practice Problems\\FindRangeInput.txt"))
