#Create a function called tup_to_dict. tup_to_dict should take one
#parameter: a list of tuples. You can assume each tuple in
#the list has exactly two values.
#
#The function should return a dictionary where the first item
#in each tuple is the key, and the second item in each tuple
#is the corresponding value.
#
#For example:
# colors = [("turquoise", "#40E0D0"), ("red", "#990000")]
# tup_to_dict(colors) -> {"turquoise":"#40E0D0", "red":"#990000"}
#
#Hint: the previous exercise is very similar; this just turns
#it into a function! All our tuples will be color name-color
#value pairs.


#Write your function here!

def tup_to_dict(tuples_list):
    dictionary = {}
    # sol 1
    # for key, val in tuples_list:
    #     dictionary[key] = val
    # return dictionary

    # sol 2
    for a_tuple in tuples_list:
        dictionary[a_tuple[0]] = a_tuple[1]
    return dictionary
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:  {'Turquoise':'#40E0D0', 'Red':'#990000'}
#
#Don't worry if it prints those in the reverse order; that's
#still correct!
print(tup_to_dict([("Turquoise", "#40E0D0"), ("Red", "#990000")]))





