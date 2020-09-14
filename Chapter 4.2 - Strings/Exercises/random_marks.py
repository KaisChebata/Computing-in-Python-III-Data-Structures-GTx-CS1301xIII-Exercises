#Write a function called random_marks. random_marks should
#take three parameters, all integers. It should return a
#string.
#
#The first parameter represents how many apostrophes should
#be in the string. The second parameter represents how many
#quotation marks should be in the string. The third
#parameter represents how many apostrophe-quotation mark
#pairs should be in the string.
#
#For example, random_marks(3, 2, 3) would return this
#string: #'''""'"'"'"
#
#Note that there are three apostrophes, then two quotation
#marks, then three '" pairs.


#Add your function here!

# first solution:

def random_marks(apostrophes, quotations, apostros_quots_pair):
	return "'" * apostrophes + '"' * quotations + ''''"''' * apostros_quots_pair

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: '''""'"'"'"


# assert random_marks(3, 2, 3) == test_str

print('first solution using random_marks function')
print('random_marks(3, 2, 3) -> ', random_marks(3, 2, 3))

#-----------------------------------------------------------
# Second solution:

#First, we define the function. I've named my parameters to
#reflect how they'll be used:
def random_marks_v2(apostrophes, quotes, pairs):
    
    #Now, we want to build up our string. I'm going to do
    #this by creating substrings for each type of character.
    #First, we'll do this for quotation marks:
    
    quot_string = '"' * quotes
    
    #Next, well do this for apostrophes:
    
    apos_string = "'" * apostrophes
    
    #Notice that to include apostrophes, we had to start the
    #string with quotation marks. To include a quotation
    #mark, we had to declare the string with apostrophes.
    #
    #For the last part, we need both. For that, we'll need
    #to use triple-apostrophes:
    
    pair_string = ''''"''' * pairs
    
    #The first three and last three apostrophes declare
    #the string; the apostrophe and quote inside are the
    #actual contents.
    #
    #Now, we add them all together and return them:
    
    return apos_string + quot_string + pair_string

print('second solution using random_marks_v2 function')
print('random_marks_v2(3, 2, 3) -> ', random_marks_v2(3, 2, 3))
print('random_marks(3, 2, 3) == random_marks_v2(3, 2, 3) ==> ', 
	random_marks(3, 2, 3) == random_marks_v2(3, 2, 3))