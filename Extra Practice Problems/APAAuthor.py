#APA citation style cites author names like this:
#
#  Last, F., Joyner, D., Burdell, G.
#
#Note the following:
#
# - Each individual name is listed as the last name, then a
#   comma, then the first initial, then a period.
# - The names are separated by commas, including the last
#   two.
# - There is no space or comma following the last period.
#
#Write a function called names_to_apa. names_to_apa should
#take as input one string, and return a reformatted string
#according to the style given above. You can assume that
#the input string will be of the following format:
#
#  First Last, David Joyner, and George Burdell
#
#You may assume the following:
#
# - There will be at least three names, with "and" before
#   the last name.
# - Each name will have exactly two words.
# - There will be commas between each pair of names.
# - The word 'and' will precede the last name.
# - The names will only be letters (no punctuation, special
#   characters, etc.), and first and last name will both be
#   capitalized.
#
#Hint: You can use the string replace() method to delete
#text from a string. For example, a_string.replace("hi", "")
#will delete all instances of "hi". There are multiple ways
#you might choose to use this.


#Write your function below!

def names_to_apa(input_string):
   
    lst = [name.strip() for name in input_string.replace('and', '').split(',')]
    # return ' '.join([name for full_name in input_string.replace('and', '').split(',') for name in full_name.split()])

    apa_citation = ''
    for name in lst:
        space = name.find(' ')
        apa_citation += name[space + 1:] + ', ' + name[0] + '., '
    return apa_citation.strip(', ')

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: Last, F., Joyner, D., & Burdell, G.
# print(names_to_apa("First Last, David Joyner, and George Burdell"))
print(names_to_apa("First Last, David Joyner, and George Burdell"))


