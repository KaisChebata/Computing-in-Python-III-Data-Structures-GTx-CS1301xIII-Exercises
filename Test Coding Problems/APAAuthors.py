#APA citation style cites author names like this:
#
#  Last, F., Joyner, D., & Burdell, G.
#
#Note the following:
#
# - Each individual name is listed as the last name, then a
#   comma, then the first initial, then a period.
# - The names are separated by commas, including the last
#   two.
# - There is also an ampersand and additional space before
#   the final name.
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


#Write your function below!

def names_to_apa(string_names):
    # solution 1
    # full_names_list = [name.strip() for name in string_names.replace('and', '&').split(',')]
    # apa_citation = ''
    # for name in full_names_list:
    #     if '&' not in name:
    #         space = name.find(' ')
    #         apa_citation += name[space + 1:] + ', ' + name[0] + '., '
    #     else:
    #         and_char = name.rfind('&')
    #         space = name.rfind(' ')
    #         apa_citation += name[and_char] +  ' ' + name[space + 1:] + ', ' + name[and_char + 2] + '.'
    # return apa_citation

    # solution 2
    list_names = string_names.split(",")
    apa_citation = ''

    for name in list_names:
        full_name = name.split()
        if full_name[0] != 'and':
            # apa_citation += full_name[1] + ', ' + full_name[0][0] + '., '
            apa_citation += full_name[1] + ", " + full_name[0][0] + "., "
        else:
            # apa_citation += '& ' + full_name[2] + ', ' + full_name[1][0] + '.'
            apa_citation += "& " + full_name[2] + ", " + full_name[1][0] + "."
    return apa_citation
    
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: Last, F., Joyner, D., & Burdell, G.
print(names_to_apa("First Last, David Joyner, and George Burdell"))
